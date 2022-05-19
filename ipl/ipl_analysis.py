import pandas as pd

df=pd.read_excel("/Users/gopalkatariya/Documents/MLAI/ETS/All_IPL_Match_Scores_Easy.xlsx")
df.head()

bat_first_run_rate =  df['Bat_First_Run_Rate'].head(9)
bat_second_run_rate =  df['Bat_Second_Run_Rate'].head(9)
balls_remaining =  df.Balls_Remaining
firstBatting = df['Winning_Team'] == 'FirstBatting'

venue = df['Venue'].head(9)

print(balls_remaining)