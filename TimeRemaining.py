import pandas as pd
df = pd.read_csv('2020-2023 Event Data.csv', low_memory = False)
df['TimeRemaining'] = df.apply(
    lambda row: 40 - (row['ElapsedMins'] + row['ElapsedSecs'] / 60) if row['Half'] == 1 
                else 80 - (row['ElapsedMins'] + row['ElapsedSecs'] / 60),
    axis=1
)

