import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from category_encoders import TargetEncoder
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
pd.set_option('display.max_columns',2000)
pd.set_option('display.max_rows',2000)

# Load the data from 2021 Event Data.csv, Players.csv, and 2021 Matches.csv
nrl21 = pd.read_csv("D:/NRL Data/OneDrive_2023-09-05/UNSW Data/2021 Event Data.csv")
playersdf = pd.read_csv('D:/NRL Data/OneDrive_2023-09-05/UNSW Data/Players.csv')
matchdf = pd.read_csv('D:/NRL Data/OneDrive_2023-09-05/UNSW Data/2021 Matches.csv')


nrl21 = nrl21.sort_values(by=['MatchId', 'Half', 'SeqNumber'], ascending=[True, True,True])

nrl21 = nrl21[[
    'MatchId','SeqNumber', 
    # 'SeasonId', 'SeriesId', 'RoundId', 'VenueId','WeatherConditionId', 
    'ClubId', 'OppositionId', 'PlayerId', 
    # 'Jumper',
    # 'PositionId', 
    # 'RunOn', 'Captain', 
       'Half', 'ElapsedMins', 'ElapsedSecs',
    #    'ElapsedMillisecs', 'GameMins', 'GameSecs', 
       'InPossessionClubId', 'InPossessionPlayerId', 
       'Set', 'Tackle', 'EventCode', 'EventName',  
    #    'Qualifier1Name', 'Qualifier1', 'Qualifier2Name', 'Qualifier2',
    #    'Qualifier3Name', 'Qualifier3', 'Qualifier4Name', 'Qualifier4',
    #    'Qualifier5Name', 'Qualifier5', 'Qualifier6Name', 'Qualifier6',
    #    'Qualifier7Name', 'Qualifier7', 'Qualifier8Name', 'Qualifier8',
       'DurationSecs', 'DistanceMs', 'Points', 'Score', 'OppScore',
       'XmPhysical', 'YmPhysical', 
    #    'ZonePhysical', 'ChannelPhysical',
    #    'SectionPhysical', 'XmPlayer', 'YmPlayer', 'ZonePlayer',
    #    'ChannelPlayer', 'SectionPlayer', 'XmPossession', 'YmPossession', 'ZonePossession', 'ChannelPossession', 'SectionPossession',
       'PossessionSecs', 'OppPossessionSecs', 'TotalPossessionSecs',
    #    'OfficialId', 
    #    '0_20_ElapsedSecs', '20_Half_ElapsedSecs',
    #    'Half_20_ElapsedSecs', '20_Try_ElapsedSecs'
]]

# Information regarding the nrlData20_23
print("Info:\n",nrl21.info())
print("Shape:\n",nrl21.shape)

# Unique values
print("Unique values in columns:\n",nrl21.nunique())

# N/A Values
print(nrl21.isnull().sum())
print((nrl21.isnull().sum()/(len(nrl21)))*100)

# Impute missing values with the next available value (backward fill)
clubid_filled = nrl21.groupby('MatchId')['ClubId'].apply(lambda x: x.bfill().ffill()).reset_index(drop=True)
oppid_filled = nrl21.groupby('MatchId')['OppositionId'].apply(lambda x: x.bfill().ffill()).reset_index(drop=True)
nrl21['ClubId'] = clubid_filled
nrl21['OppositionId'] = oppid_filled
nrl21['InPossessionClubId'] = nrl21['InPossessionClubId'].bfill()
nrl21['InPossessionPlayerId'] = nrl21['InPossessionPlayerId'].bfill()
nrl21['Score'] = nrl21.groupby('MatchId')['Score'].transform(lambda x: x.bfill())
nrl21['OppScore'] = nrl21.groupby('MatchId')['OppScore'].transform(lambda x: x.bfill())
nrl21['Score'] = nrl21.groupby('MatchId')['Score'].transform(lambda x: x.ffill())
nrl21['OppScore'] = nrl21.groupby('MatchId')['OppScore'].transform(lambda x: x.ffill())

# Impute missing values with the value from 'InPossessionPlayerId'
nrl21['PlayerId'] = nrl21['PlayerId'].fillna(nrl21['InPossessionPlayerId'])

# Impute missing value in 'EventName'
nrl21['EventName'] = nrl21['EventName'].fillna("Field goal (2 pt)- OK")

# Impute missing values with 0
nrl21['Points'] = nrl21['Points'].fillna(0)
nrl21['DurationSecs'] = nrl21['DurationSecs'].fillna(0)
nrl21['DistanceMs'] = nrl21['DistanceMs'].fillna(0)
nrl21['PossessionSecs'] = nrl21['PossessionSecs'].fillna(0)
nrl21['OppPossessionSecs'] = nrl21['OppPossessionSecs'].fillna(0)
nrl21['TotalPossessionSecs'] = nrl21['TotalPossessionSecs'].fillna(0)

# Define the columns to convert
columns_to_convert = [
    'ClubId', 'OppositionId', 
    'PlayerId', 'InPossessionClubId', 'InPossessionPlayerId', 'Score', 'Points', 'OppScore', ]
nrl21[columns_to_convert] = nrl21[columns_to_convert].astype('int64')

# Drop duplicates from playersdf to avoid unnecessary expansion during merges
clubdf = playersdf.drop_duplicates(subset=['PlayerClubId'], keep='first')

# Merge ClubName, OppositionName, and InPossessionClubName in a single step
nrl21 = pd.merge(nrl21, clubdf[['PlayerClubId', 'PlayerClubName']], left_on='ClubId', right_on='PlayerClubId', how='left')
nrl21 = pd.merge(nrl21, clubdf[['PlayerClubId', 'PlayerClubName']], left_on='OppositionId', right_on='PlayerClubId', how='left', suffixes=('', '_Opposition'))
nrl21 = pd.merge(nrl21, clubdf[['PlayerClubId', 'PlayerClubName']], left_on='InPossessionClubId', right_on='PlayerClubId', how='left', suffixes=('', '_InPossession'))

# Merge PlayerName and PlayerPositionName for PlayerId and InPossessionPlayerId
nrl21 = pd.merge(nrl21, playersdf[['PlayerId', 'PlayerName', 'PlayerPositionName']], on='PlayerId', how='left')
nrl21 = pd.merge(nrl21, playersdf[['PlayerId', 'PlayerName', 'PlayerPositionName']], left_on='InPossessionPlayerId', right_on='PlayerId', how='left', suffixes=('', '_InPossession'))

# Merge WeatherConditionName, TeamAName, and TeamBName for MatchId
nrl21 = pd.merge(nrl21, matchdf[['MatchId', 'WeatherConditionName', 'TeamAName', 'TeamBName']], on='MatchId', how='left', suffixes=('', '_InPossession'))

# Rename the merged columns
nrl21.rename(columns={
    'PlayerName_InPossession': 'InPossessionPlayerName',
    'PlayerPositionName_InPossession': 'InPossessionPlayerPosition',
    'PlayerClubName_InPossession': 'InPossessionClubName',
    'PlayerClubName_Opposition': 'OppositionName',
    'PlayerClubName': 'ClubName',
    'TeamAName': 'HomeClubName',
    'TeamBName': 'AwayClubName'
}, inplace=True)

# Drop unnecessary columns after the merges
nrl21.drop(columns=['PlayerClubId_InPossession','PlayerClubId_Opposition','PlayerId_InPossession', 'InPossessionPlayerId', 'PlayerId', 'OppositionId', 'ClubId', 'InPossessionClubId', 'PlayerClubId'], inplace=True)

# Create HomeScore, AwayScore, HomePossessionSecs, OppPossessionSecs
nrl21['HomeScore'] = np.where(
    nrl21['HomeClubName'] == nrl21['ClubName'], 
    nrl21['Score'],
    np.where(nrl21['HomeClubName'] == nrl21['OppositionName'], 
             nrl21['OppScore'],0))
nrl21['AwayScore'] = np.where(
    nrl21['AwayClubName'] == nrl21['ClubName'], 
    nrl21['Score'],
    np.where(nrl21['AwayClubName'] == nrl21['OppositionName'], 
             nrl21['OppScore'],0))
nrl21['HomePossessionSecs'] = np.where(
    nrl21['HomeClubName'] == nrl21['ClubName'], 
    nrl21['PossessionSecs'],
    np.where(nrl21['HomeClubName'] == nrl21['OppositionName'], 
             nrl21['OppPossessionSecs'],0))
nrl21['AwayPossessionSecs'] = np.where(
    nrl21['AwayClubName'] == nrl21['ClubName'], 
    nrl21['PossessionSecs'],
    np.where(nrl21['AwayClubName'] == nrl21['OppositionName'], 
             nrl21['OppPossessionSecs'],0))

# Drop unwanted columns
nrl21.drop(columns=['ClubName', 'OppositionName', 
                    'Score', 'OppScore', 
                    'PossessionSecs', 'OppPossessionSecs'], inplace=True)

# Create a 'Win' column
final_scores = nrl21.groupby('MatchId').agg({
    'HomeScore': 'last', 
    'AwayScore': 'last'
}).reset_index()
final_scores.rename(columns={'HomeScore': 'HomeScore_Final', 'AwayScore': 'AwayScore_Final'}, inplace=True)
nrl21 = nrl21.merge(final_scores, on='MatchId', how='left')
nrl21['Win'] = np.where(
    (nrl21['HomeScore_Final'] > nrl21['AwayScore_Final']) & (nrl21['InPossessionClubName'] == nrl21['HomeClubName']), 1, 0
)
nrl21['Win'] = np.where(
    (nrl21['AwayScore_Final'] > nrl21['HomeScore_Final']) & (nrl21['InPossessionClubName'] == nrl21['AwayClubName']), 1, nrl21['Win']
)
nrl21['Win'] = np.where(
    (nrl21['HomeScore_Final'] == nrl21['AwayScore_Final']), 0.5, nrl21['Win']
)
nrl21.drop(columns=['HomeScore_Final', 'AwayScore_Final'], inplace=True)

# EXPLORATORY DATA ANALYSIS

# Identify categorical and numerical columns
cat_cols = nrl21.select_dtypes(include=['object']).columns
num_cols = nrl21.select_dtypes(include=np.number).columns.tolist()

print("Categorical:\n", cat_cols)
print("Nominal:\n", num_cols)

# Univariate Data Analysis
# for col in cat_cols:
#     plt.figure(figsize=(12, 6))
#     sns.countplot(data=nrl21, x=col)
#     plt.title(f'Count of {col}')
#     plt.xticks(rotation=45)
#     plt.show()

nrl21[num_cols].describe()

# for col in num_cols:
#     plt.figure(figsize=(12, 6))
#     sns.histplot(nrl21[col], bins=30, kde=True)
#     plt.title(f'Distribution of {col}')
#     plt.show()

#     plt.figure(figsize=(12, 6))
#     sns.boxplot(x=nrl21[col])
#     plt.title(f'Box plot of {col}')
#     plt.show()

# Print rows where Half is equal to 4
half_4_data = nrl21[nrl21['Half'] == 4]
print(half_4_data)
nrl21.drop(columns=['DurationSecs', 'DistanceMs'], inplace=True)

# Bivariate Data Analysis

# Identify categorical and numerical columns after adjustments
cat_cols = nrl21.select_dtypes(include=['object']).columns
num_cols = nrl21.select_dtypes(include=np.number).columns.tolist()

# sns.countplot(data=nrl21, x='InPossessionClubName', hue='Win')
# plt.title('InPossessionClub vs Win')
# plt.xticks(rotation=45)
# plt.show()
# sns.countplot(data=nrl21, x='PlayerPositionName', hue='Win')
# plt.title('PlayerPositionNam vs Win')
# plt.xticks(rotation=45)
# plt.show()

# for col in ['TotalPossessionSecs', 'XmPhysical', 'YmPhysical']:
#     plt.figure(figsize=(12, 6))
#     sns.boxplot(data=nrl21, x='Win', y=col)
#     plt.title(f'{col} vs Win')
#     plt.show()

# Multivariate Data Analysis

# Calculate the correlation matrix
correlation_matrix = nrl21[num_cols].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title('Correlation Heatmap')
plt.show()

sns.pairplot(nrl21, hue='Win', vars=num_cols)
plt.show()

# FEATURE ENGINEERING

# Create ScoreDifference as 1 when the home club is in possession and 0 when the away club is in possession
nrl21['HomeAwayIndicator'] = np.where(nrl21['InPossessionClubName'] == nrl21['HomeClubName'], 1, 0)

# Create ScoreDifference as HomeScore - AwayScore
nrl21['ScoreDifference'] = nrl21['HomeScore'] - nrl21['AwayScore']

# Create TimeRemaining
nrl21['TimeRemaining'] = nrl21.apply(
    lambda row: 40 - (row['ElapsedMins'] + row['ElapsedSecs'] / 60) if row['Half'] == 1 
                else 80 - (row['ElapsedMins'] + row['ElapsedSecs'] / 60),
    axis=1
)

# Create TryIndicator: 1 if the event is a try, 0 otherwise.
nrl21['TryIndicator'] = np.where(nrl21['EventCode'].isin(['TRY', 'PTRY']), 1, 0)

# Create ConversionIndicator: 1 if the event is a conversion, 0 otherwise.
nrl21['ConversionIndicator'] = np.where(nrl21['EventCode'].isin(['CVOK']), 1, 0)

# Create PenaltyIndicator: 1 if the event is a penalty, 0 otherwise.
nrl21['PenaltyIndicator'] = np.where(nrl21['EventCode'].isin(['PGOK']), 1, 0)

# Create FieldGoalIndicator: 1 if the event is a Field Goal, 0 otherwise.
nrl21['FieldGoalIndicator'] = np.where(nrl21['EventCode'].isin(['FGOK']), 1, 0)

# Create ConsecutiveEvent for each team
nrl21 = nrl21.sort_values(by=['MatchId', 'Half', 'SeqNumber'])
nrl21['PossessionChange'] = (nrl21['InPossessionClubName'] != nrl21['InPossessionClubName'].shift(1)).astype(int)
nrl21['Group'] = nrl21.groupby('MatchId')['PossessionChange'].cumsum()
nrl21['ConsecutiveEvent'] = nrl21.groupby(['MatchId', 'Group']).cumcount() + 1

# Drop the temporary columns
nrl21.drop(columns=['PossessionChange', 'Group'], inplace=True)

# Create a new column 'XmPhysical_Binned' to hold the binned values
bins = [-25,-1, 25, 50, 75, 100, 125]
labels = ['(-25)-(-1)','0-25', '26-50', '51-75', '76-100', '101-125']
nrl21['XmPhysical_Binned'] = pd.cut(nrl21['XmPhysical'], bins=bins, labels=labels, right=True)

# # Ensure there are no zero values in DurationSecs to avoid division errors
# nrl21['DurationSecs'] = nrl21['DurationSecs'].replace(0, np.nan)

# # Calculate BallSpeed as DistanceMs divided by DurationSecs
# nrl21['BallSpeed'] = nrl21['DistanceMs'] / nrl21['DurationSecs']

# # Handle any potential NaN values that arise from zero division
# nrl21['BallSpeed'].fillna(0, inplace=True)
# nrl21['DurationSecs'].fillna(0, inplace=True)

# # Check the results
# print(nrl21[['DistanceMs', 'DurationSecs', 'BallSpeed']].head(10))


# CATEGORICAL VARIABLE

nrl21.drop(columns=['EventName'], inplace=True)

# Handling High Cardinality Features

# Frequency Encoding for high cardinality features
high_cardinality_cols = ['EventCode', 'PlayerName', 'InPossessionPlayerName']
# Apply frequency encoding
for col in high_cardinality_cols:
    nrl21[col + '_FreqEnc'] = nrl21[col].map(nrl21[col].value_counts())
# # Group Rare Categories into "Other"
# threshold = 0.01 * len(nrl21)  # Define a threshold for grouping rare categories (1% of the data)
# for col in high_cardinality_cols:
#     freq = nrl21[col].value_counts()
#     rare_labels = freq[freq < threshold].index  # Identify rare categories
#     nrl21[col] = nrl21[col].apply(lambda x: 'Other' if x in rare_labels else x)
# Apply Target Encoding using sklearn's TargetEncoder
# Target column assumed to be 'Win'
te = TargetEncoder(cols=high_cardinality_cols)
# Perform target encoding on the selected columns
nrl21_encoded = te.fit_transform(nrl21, nrl21['Win'])  # Apply on training data
# Drop original high cardinality columns after encoding if not needed
nrl21_encoded.drop(columns=high_cardinality_cols, inplace=True)

# Define the order for ordinal encoding
position_order = ['Rain', 'Showers', 'Fine']
ordinal_columns = ['WeatherConditionName']

# Initialize the ordinal encoder
ordinal_encoder = OrdinalEncoder(categories=[position_order] * len(ordinal_columns))

# Apply ordinal encoding
nrl21_encoded[ordinal_columns] = ordinal_encoder.fit_transform(nrl21_encoded[ordinal_columns])

# print("Data after Ordinal Encoding:")
# print(nrl21_encoded[ordinal_columns])

# Initialize the OneHotEncoder
onehot_encoder = OneHotEncoder(sparse_output=False, drop='first')  # drop='first' to avoid dummy variable trap

# Fit and transform the desired columns
onehot_encoded = onehot_encoder.fit_transform(nrl21_encoded[['InPossessionClubName', 'PlayerPositionName', 'InPossessionPlayerPosition', 'HomeClubName', 'AwayClubName']])

# Create a DataFrame for the one-hot encoded data
onehot_df = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names_out(['InPossessionClubName', 'PlayerPositionName', 'InPossessionPlayerPosition', 'HomeClubName', 'AwayClubName']))

# Concatenate with the original DataFrame
nrl21_encoded = pd.concat([nrl21_encoded.reset_index(drop=True), onehot_df.reset_index(drop=True)], axis=1)

# Drop the original categorical columns
nrl21_encoded.drop(columns=['InPossessionClubName', 'PlayerPositionName', 'InPossessionPlayerPosition', 'HomeClubName', 'AwayClubName'], inplace=True)

# print("Data after One-Hot Encoding with OneHotEncoder:")
# print(nrl21_encoded.head())

# # Identify categorical and numerical columns
# cat_cols = nrl21_encoded.select_dtypes(include=['object']).columns
# num_cols = nrl21_encoded.select_dtypes(include=np.number).columns.tolist()

# # Print categorical variables and their unique counts
# print("Categorical Variables and their unique counts:")
# for col in cat_cols:
#     print(f"{col}: {nrl21_encoded[col].nunique()} unique values")

# # Print numerical variables and their unique counts
# print("\nNumerical Variables and their unique counts:")
# for col in num_cols:
#     print(f"{col}: {nrl21_encoded[col].nunique()} unique values")

# nrl21_encoded.to_csv('testingdata.csv', index=False)