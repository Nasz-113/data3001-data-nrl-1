import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',200)
pd.set_option('display.max_rows',200)

# Load the data from 2020-2023 Event Data.csv and Players.csv
nrlData20_23 = pd.read_csv('D:/NRL Data/OneDrive_2023-09-05/UNSW Data/2020-2023 Event Data.csv')
playersdf = pd.read_csv('D:/NRL Data/OneDrive_2023-09-05/UNSW Data/Players.csv')

# Remove unwanted columns
nrlData20_23 = nrlData20_23[[ #'Anonymize 1PlayerId', 
'Away Score', 
# 'Captain',
#  'ChannelPhysical', 'ChannelPlayer', 'ChannelPossession', 
# 'Club Id', 'Club Name', 
'Deidentified Away Club Id', 
'Deidentified Away Club Name', 
'Deidentified Club Home Id', 
'Deidentified Club Home Name', 'DistanceMs', 'DurationSecs', 
# 'ElapsedMillisecs', 
'ElapsedMins', 'ElapsedSecs', 'EventCode', 
'EventName',
#  'GameMins', 'GameSecs', 
'Half', 'Home Score', 
'InPossessionClub Id', 'InPossessionPlayerId', 
# 'MatchId', 
# 'MatchMinute', 'OfficialId', 'Opposition Id','OppPossessionSecs', 'OppScore',
'Player Id', 'Points', 
# 'PositionId', 'PossessionSecs', 
#'Qualifier1', 'Qualifier1Name', 'Qualifier2', 'Qualifier2Name', 'Qualifier3', 'Qualifier3Name', 'Qualifier4', 'Qualifier4Name', 'Qualifier5', 'Qualifier5Name', 'Qualifier6', 'Qualifier6Name', 'Qualifier7', 'Qualifier7Name', 'Qualifier8', 'Qualifier8Name', 
# 'RoundId', 'RunOn','Score', 
# 'SeasonId', 
# 'SectionPhysical', 'SectionPlayer', 'SectionPossession', 'SeqNumber', 
# 'SeriesId', 
'Set', 'Tackle', 
# 'TeamAId', 
'TeamAPossessionSecs', 
# 'TeamBId', 
'TeamBPossessionSecs', 'TotalPossessionSecs', 'WeatherConditionName', 'XmPhysical', 
# 'XmPlayer', 'XmPossession', 
'YmPhysical', 
# 'YmPlayer', 'YmPossession', 'ZonePhysical', 'ZonePlayer', 'ZonePossession'
]].copy()



# Standardizing column names
nrlData20_23.rename(columns={'Player Id': 'PlayerId', 'Deidentified Away Club Name': 'AwayClubName', 'Deidentified Away Club Id': 'AwayClubId', 'Away Score': 'AwayScore', 'Deidentified Club Home Id': 'HomeClubId', 'Deidentified Club Home Name': 'HomeClubName', 'Home Score': 'HomeScore', 'InPossessionClub Id': 'InPossessionClubId', 'TeamAPossessionSecs': 'HomeClubPossessionSecs', 'TeamBPossessionSecs': 'AwayClubPossessionSecs'}, inplace=True)

# Adds a 'InPossessionClubName' column
nrlData20_23['InPossessionClubName'] = np.where(
    nrlData20_23['InPossessionClubId'] == nrlData20_23['HomeClubId'], 
    nrlData20_23['HomeClubName'], 
    np.where(nrlData20_23['InPossessionClubId'] == nrlData20_23['AwayClubId'], 
             nrlData20_23['AwayClubName'], 
             np.nan)  # If neither matches, assign NaN
)

# Merge 'PlayerName','PlayerPositionName','PlayerHeightCms','PlayerWeightKgs' from playersdf

nrlData20_23 = pd.merge(nrlData20_23, playersdf[['PlayerId', 'PlayerName','PlayerPositionName','PlayerHeightCms','PlayerWeightKgs']], on='PlayerId', how='left')

# Perform a second merge for 'InPossessionPlayerId' with suffixes to avoid name conflict
nrlData20_23 = pd.merge(
    nrlData20_23,
    playersdf[['PlayerId', 'PlayerName']],
    left_on='InPossessionPlayerId',
    right_on='PlayerId',
    how='left',
    suffixes=('', '_InPossession')  # Adds suffix to the second 'PlayerName' column
)

# Rename 'PlayerName_InPossession' to 'InPossessionPlayerName'
nrlData20_23.rename(columns={'PlayerName_InPossession': 'InPossessionPlayerName'}, inplace=True)

# Drop unwanted columns
nrlData20_23.drop(columns=['PlayerId_InPossession','InPossessionPlayerId','PlayerId', 'AwayClubId', 'HomeClubId','InPossessionClubId'], inplace=True)

# Impute missing values in 'Points' with 0
nrlData20_23['Points'] = nrlData20_23['Points'].fillna(0)

# Impute missing values in 'DurationSecs' with 0
nrlData20_23['DurationSecs'] = nrlData20_23['DurationSecs'].fillna(0)

# Information regarding the nrlData20_23
print("Shape:\n",nrlData20_23.shape)

# Unique values
print("Unique values in columns:\n",nrlData20_23.nunique())

# N/A Values
print(nrlData20_23.isnull().sum())
print((nrlData20_23.isnull().sum()/(len(nrlData20_23)))*100)

# FEATURE ENGINEERING

# Create ScoreDifference as 1 when the home club is in possession and 0 when the away club is in possession
nrlData20_23['HomeAwayIndicator'] = np.where(nrlData20_23['InPossessionClubName'] == nrlData20_23['HomeClubName'], 1, 0)

# Create ScoreDifference as HomeScore - AwayScore
nrlData20_23['ScoreDifference'] = nrlData20_23['HomeScore'] - nrlData20_23['AwayScore']

# Create TimeRemaining
nrlData20_23['TimeRemaining'] = nrlData20_23.apply(
    lambda row: 40 - (row['ElapsedMins'] + row['ElapsedSecs'] / 60) if row['Half'] == 1 
                else 80 - (row['ElapsedMins'] + row['ElapsedSecs'] / 60),
    axis=1
)


















# events_with_points = nrlData20_23[nrlData20_23['DurationSecs'].notna()]
# print(events_with_points[['EventName','DurationSecs']])

# event_codes = [
#     'PBFD', 'PBFS', 'PBHD', 'PBHS', 
#     'PBID', 'PBIS', 'PBND', 'PBNS', 
#     'PBSD', 'PBSS'
# ]

# # Filter the DataFrame for the specified EventCodes
# filtered_events = nrlData20_23[(nrlData20_23['EventCode'].isin(event_codes) & (nrlData20_23['DurationSecs'].isna()))]

# # Print the relevant columns
# print(filtered_events[['EventCode', 'EventName', 'ElapsedMins', 'ElapsedSecs']])

# print("DUPLICATED NRL20-23\n") # To inspect how many duplicated values
# print(nrlData20_23.duplicated().sum())
# print("DUPLICATED PLAYERS\n") # To inspect how many duplicated values
# print(playersdf.duplicated().sum())

# events_with_points = nrlData20_23[nrlData20_23['InPossessionPlayerId'].notna()]
# print(events_with_points[['Player Id','InPossessionPlayerId','EventName']])
# print(nrlData20_23.isnull().sum())