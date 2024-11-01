#!/usr/bin/env python

import matplotlib as plt
import pandas as pd
import numpy as np

## filtering out Posession variables-locational data normalized wrt to the club in possesion-**Posession
#csv_path = 'path_to_"2021 Event Data.csv" from "UNSW 2021 Event Data.zip" '
csv_path = 'your_path_to_2021 Event Data.csv'

def Possession_filter(csv_path):
    df = pd.read_csv(csv_path, low_memory=False)
    possession_col = [
        #match identifying columns
        'MatchId', 'ClubId', 'OppositionId', 
        #Time related data
        'SeqNumber', 'Half', 'ElapsedMins', 'ElapsedSecs','PossessionSecs', 'OppPossessionSecs', 'TotalPossessionSecs',
        #Event data
        'EventCode', 'EventName', 'Set', 'Tackle',
        #possession club/player id
        'InPossessionClubId', 'InPossessionPlayerId',
        #score
        'Score', 'OppScore', 
        #field position data(normalized)
        'XmPhysical', 'YmPhysical', 'XmPossession', 'YmPossession',
        #extra? possession related data
        'ZonePhysical', 'ChannelPhysical', 'SectionPhysical', 'ZonePhysical', 'ChannelPhysical', 'SectionPhysical'
    ]
    df_possession = df[possession_col]
    df_possession = df_possession.dropna()
    return df_possession
df_possession = Possession_filter(csv_path)

#filtered = Possession_filter(csv_path)
#filtered.to_csv(csv_path, index=False)
def get_overall_possession_with_features(df_possession):
    # Group by MatchId and InPossessionClubId - each team, each match
    overall_possession = df_possession.groupby(['MatchId', 'InPossessionClubId']).agg(
        TotalPossessionTime=('PossessionSecs', 'sum'),
        TotalOpponentPossessionTime=('OppPossessionSecs', 'sum'),
        AverageFieldPositionX=('XmPhysical', 'mean'),
        AverageFieldPositionY=('YmPhysical', 'mean'),
        AverageScore=('Score', 'mean'),
        AverageOppScore=('OppScore', 'mean'),
        PossessionCount=('PossessionSecs', 'count')
    ).reset_index()

    
    #feature 1. posseiontime_diff
    overall_possession['PossessionTime_Diff'] = overall_possession['TotalPossessionTime'] - overall_possession['TotalOpponentPossessionTime']
    
    #feature 2. posseiiontime_field position: total posssssion time * avg filed position gives the effect of controlling the ball in strategic field positions.
    overall_possession['PossessionTime_FieldPosition'] = overall_possession['TotalPossessionTime'] * overall_possession['AverageFieldPositionX']
    
    # Match and club IDs as integers, measured figures as floats
    overall_possession['MatchId'] = overall_possession['MatchId'].astype(int)
    overall_possession['InPossessionClubId'] = overall_possession['InPossessionClubId'].astype(int)
    
    float_cols = ['TotalPossessionTime', 'TotalOpponentPossessionTime', 'AverageFieldPositionX', 
                  'AverageFieldPositionY', 'AverageScore', 'AverageOppScore', 'PossessionCount', 
                  'PossessionTime_Diff', 'PossessionTime_FieldPosition']
    overall_possession[float_cols] = overall_possession[float_cols].astype(float)
    
    return overall_possession

df_possession = Possession_filter(csv_path)
df_overall_possession = get_overall_possession_with_features(df_possession)

def get_players_possession(df_possession): 
    # Group by MatchId, InPossessionClubId, and InPossessionPlayerId-each player
    players_possession = df_possession.groupby(['MatchId', 'InPossessionClubId', 'InPossessionPlayerId']).agg(
        TotalPossessionTime=('PossessionSecs', 'sum'),
        TotalOpponentPossessionTime=('OppPossessionSecs', 'sum'),
        AverageFieldPositionX=('XmPhysical', 'mean'),
        AverageFieldPositionY=('YmPhysical', 'mean'),
        AverageScore=('Score', 'mean'),
        AverageOppScore=('OppScore', 'mean'),
        PossessionCount=('PossessionSecs', 'count')
    ).reset_index()
    players_possession['MatchId'] = players_possession['MatchId'].astype(int)
    players_possession['InPossessionClubId'] = players_possession['InPossessionClubId'].astype(int)
    players_possession['InPossessionPlayerId'] = players_possession['InPossessionPlayerId'].astype(int)

                                                                                        

    float_cols = ['TotalPossessionTime', 'TotalOpponentPossessionTime', 'AverageFieldPositionX', 'AverageFieldPositionY', 'AverageScore', 'AverageOppScore', 'PossessionCount']
    players_possession[float_cols] = players_possession[float_cols].astype(float)
    players_possession = players_possession.sort_values(by='InPossessionPlayerId') #sort by playerID

    return players_possession

df_players_possession = get_players_possession(df_possession)

#possession indicator 0 or 1
df_possession['PossessionIndicator'] = df_possession['InPossessionClubId'].apply(lambda x: 1 if pd.notna(x) else 0)
Possession_Indicator = df_possession['PossessionIndicator']

#possession Time segmentation
# Detect changes in possession
df_possession['PreviousPossessionClubId'] = df_possession['InPossessionClubId'].shift(1)
df_possession['PossessionSwitched'] = df_possession['InPossessionClubId'] != df_possession['PreviousPossessionClubId']

# Create possession segments by detecting when possession switches
df_possession['PossessionPhaseStart'] = df_possession['PossessionSwitched'].apply(lambda x: 1 if x else 0).cumsum()

# possession duration = ending - starting time 
df_possession['PossessionStartSecs'] = df_possession.groupby('PossessionPhaseStart')['ElapsedMins'].transform('first') * 60 + df_possession.groupby('PossessionPhaseStart')['ElapsedSecs'].transform('first')
df_possession['PossessionEndSecs'] = df_possession.groupby('PossessionPhaseStart')['ElapsedMins'].transform('last') * 60 + df_possession.groupby('PossessionPhaseStart')['ElapsedSecs'].transform('last')
df_possession['PossessionDuration'] = df_possession['PossessionEndSecs'] - df_possession['PossessionStartSecs']

Possession_duration = df_possession['PossessionDuration']

