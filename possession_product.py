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
def get_overall_possession(df_possession):
    # Group by MatchId and ClubId-each team, each match
    overall_possession = df_possession.groupby(['MatchId', 'InPossessionClubId']).agg(
        TotalPossessionTime=('PossessionSecs', 'sum'),
        TotalOpponentPossessionTime=('OppPossessionSecs', 'sum'),
        AverageFieldPositionX=('XmPhysical', 'mean'),
        AverageFieldPositionY=('YmPhysical', 'mean'),
        AverageScore=('Score', 'mean'),
        AverageOppScore=('OppScore', 'mean'),
        PossessionCount=('PossessionSecs', 'count')
    ).reset_index()
    #Match, club IDs int, while measured figures float
    overall_possession['MatchId'] = overall_possession['MatchId'].astype(int)
    overall_possession['InPossessionClubId'] = overall_possession['InPossessionClubId'].astype(int)

    float_cols = ['TotalPossessionTime', 'TotalOpponentPossessionTime', 'AverageFieldPositionX', 'AverageFieldPositionY', 'AverageScore', 'AverageOppScore', 'PossessionCount']
    overall_possession[float_cols] = overall_possession[float_cols].astype(float)

    return overall_possession

df_overall_possession = get_overall_possession(df_possession)

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
