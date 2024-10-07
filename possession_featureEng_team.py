#!/usr/bin/env python

import matplotlib as plt
import pandas as pd
import numpy as np
'''
df_possession.to_csv('/path_to/possession_data_with_features.csv', index=False)
df_overall_possession.to_csv('/path_to/team_possession_data.csv', index=False)
df_players_possession.to_csv('/path_to/player_possession_data.csv', index=False)
'''

csv_path2 = 'df_overall_possession.csv' # per team
pt_possession = pd.read_csv(csv_path2, low_memory=False)

pt_possession['PossessionIndicator'] = pt_possession['InPossessionClubId'].apply(lambda x: 1 if pd.notna(x) else 0)
#possession indicator
Possession_Indicator = pt_possession['PossessionIndicator']  

