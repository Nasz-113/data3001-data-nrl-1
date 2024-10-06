import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
    df_possession = df_possession.dropna() #2-1 Null handling
    return df_possession


    
