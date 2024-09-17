import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',200)

nrlData20_23 = pd.read_csv('D:/NRL Data/OneDrive_2023-09-05/UNSW Data/2020-2023 Event Data.csv')
playersdf = pd.read_csv('D:/NRL Data/OneDrive_2023-09-05/UNSW Data/Players.csv')
# print(nrlData20_23.head())

# print("DUPLICATED NRL20-23\n") # To inspect how many duplicated values
# print(nrlData20_23.duplicated().sum())
# print("DUPLICATED PLAYERS\n") # To inspect how many duplicated values
# print(playersdf.duplicated().sum())

nrlData20_23 = nrlData20_23[[ #'Anonymize 1PlayerId', 
'Away Score', 'Captain', 'ChannelPhysical', 'ChannelPlayer', 'ChannelPossession', 
# 'Club Id', 
'Club Name', 
# 'Deidentified Away Club Id', 
'Deidentified Away Club Name', 
# 'Deidentified Club Home Id', 
'Deidentified Club Home Name', 'DistanceMs', 'DurationSecs', 'ElapsedMillisecs', 
# 'ElapsedMins', 'ElapsedSecs', 'EventCode', 
'EventName', 'GameMins', 'GameSecs', 'Half', 'Home Score', 'InPossessionClub Id', 'InPossessionPlayerId', 
# 'MatchId', 
'MatchMinute', 'OfficialId', 'Opposition Id', 'OppPossessionSecs', 'OppScore', 'Player Id', 
'Points', 
# 'PositionId', 
'PossessionSecs', 'Qualifier1', 'Qualifier1Name', 'Qualifier2', 'Qualifier2Name', 'Qualifier3', 
'Qualifier3Name', 'Qualifier4', 'Qualifier4Name', 'Qualifier5', 'Qualifier5Name', 'Qualifier6', 'Qualifier6Name', 'Qualifier7', 
'Qualifier7Name', 'Qualifier8', 'Qualifier8Name', 
'RoundId', 'RunOn', 'Score', 
# 'SeasonId', 
'SectionPhysical', 'SectionPlayer', 'SectionPossession', 'SeqNumber', 
# 'SeriesId', 
'Set', 'Tackle', 
# 'TeamAId', 
'TeamAPossessionSecs', 
# 'TeamBId', 
'TeamBPossessionSecs', 'TotalPossessionSecs', 'WeatherConditionName', 'XmPhysical', 'XmPlayer', 'XmPossession', 'YmPhysical', 'YmPlayer', 'YmPossession', 'ZonePhysical', 'ZonePlayer', 'ZonePossession']].copy()
# col23 = list(nrlData20_23.columns)
# print(col23)
nrlData20_23.rename(columns={'Player Id': 'PlayerId'}, inplace=True)
merged_nrl20_23 = pd.merge(nrlData20_23, playersdf[['PlayerId', 'PlayerName','PlayerPositionName','PlayerHeightCms','PlayerWeightKgs']], on='PlayerId', how='left')
# Perform a second merge for 'InPossessionPlayerId' with suffixes to avoid name conflict
merged_nrl20_23 = pd.merge(
    merged_nrl20_23,
    playersdf[['PlayerId', 'PlayerName']],
    left_on='InPossessionPlayerId',
    right_on='PlayerId',
    how='left',
    suffixes=('', '_InPossession')  # Adds suffix to the second 'PlayerName' column
)
# Rename 'PlayerName_InPossession' to 'InPossessionPlayerName'
merged_nrl20_23.rename(columns={'PlayerName_InPossession': 'InPossessionPlayerName'}, inplace=True)
# Drop the extra 'PlayerId' column from the second merge (optional)
merged_nrl20_23.drop(columns=['PlayerId_InPossession','InPossessionPlayerId','PlayerId'], inplace=True)
# print(merged_nrl20_23.head(5))
# print(merged_nrl20_23.columns)

# print(f'col23: {col23}')
# print(f'col21: {col21}')
# print(f'columns 55 and 57: {col[55]} {col[57]}')

# nrlData20_23PTB = nrlData20_23[nrlData20_23["EventCode"].isin(ptbEvent)]
# print(nrlData20_23.shape)
# print(nrlData20_23.isnull().sum().to_string())

merged_nrl20_23 = merged_nrl20_23[~merged_nrl20_23['Club Name'].isna()].copy()
print(merged_nrl20_23.shape)
print(merged_nrl20_23.isnull().sum().to_string())
# print(merged_nrl20_23.head())
# merged_nrl20_23.to_csv('merged.csv', index=False, header=True)


# PTB Event Data

# PBFD	PTB by opp - fast
# PBFS	PTB - fast
# PBHD	PTB by opp - handed over
# PBHS	PTB - hands over
# PBID	PTB by opp - interrupted
# PBIS	PTB - interrupted
# PBND	PTB by opp - neutral
# PBNS	PTB - neutral
# PBSD	PTB by opp - slow
# PBSS	PTB - slow

# ptbEvent = ['PBFD','PBFS','PBHD','PBHS','PBID','PBIS','PBND','PBNS','PBSD','PBSS']