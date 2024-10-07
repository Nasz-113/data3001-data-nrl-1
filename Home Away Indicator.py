import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# HomeAwayIndicator: 1 if the team in possession is playing at home, 0 otherwise. (nas)
# Field position: Distance from goalposts can be calculated using XmPhysical and YmPhysical coordinates to enhance WPA/EPA. (nas)

nrlData20_23 = pd.read_csv('D:/NRL Data/OneDrive_2023-09-05/UNSW Data/2020-2023 Event Data.csv')
playersdf = pd.read_csv('D:/NRL Data/OneDrive_2023-09-05/UNSW Data/Players.csv')

# in_possession_not_na=nrlData20_23[nrlData20_23['InPossessionClub Id'].notna()]
# print(in_possession_not_na[['InPossessionClub Id']])

nrlData20_23['HomeAwayIndicator'] = np.where(nrlData20_23['InPossessionClub Id'] == nrlData20_23['Deidentified Club Home Id'], 1, 0)

print(nrlData20_23[['InPossessionClub Id', 'Deidentified Club Home Id', 'Deidentified Away Club Id', 'HomeAwayIndicator']].head())
