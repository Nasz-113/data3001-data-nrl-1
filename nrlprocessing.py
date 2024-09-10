import pandas as pd
# nrlData20_23 = pd.read_csv('D:\\NRL Data\\OneDrive_2023-09-05\\UNSW Data\\2020-2023 Event Data.csv')
nrlData21 = pd.read_csv('D:\\NRL Data\\OneDrive_2023-09-05\\UNSW Data\\2021 Event Data.csv')
# print(nrlData21)
# print(nrlData21.head())
# print(nrlData20_23.head())
# col23 = list(nrlData20_23.columns)
col21 = list(nrlData21.columns)

# print(f'col23: {col23}')
# print(f'col21: {col21}')
# print(f'columns 55 and 57: {col[55]} {col[57]}')

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
ptbEvent = ['PBFD','PBFS','PBHD','PBHS','PBID','PBIS','PBND','PBNS','PBSD','PBSS']
nrlData21PTB = nrlData21[nrlData21["EventCode"].isin(ptbEvent)]
nrlData21PTB.to_csv('ptb.csv', index=False, header=True)

print(nrlData21PTB.isnull().sum().to_string())