import pandas as pd
import numpy as np


slg_data = pd.read_csv("statcast_data/all_slg_data.csv")

print(slg_data)
final_slg = {}

for index, row in slg_data.iterrows():
    final_slg[row['name']] = {}

# SLG = (1B + 2Bx2 + 3Bx3 + HRx4)/AB
for index, row in slg_data.iterrows():
    if(row['AB']!=0):
        final_slg[row['name']]['SLG'] = ((row['single']) + (row['double'])*2 + (row['tiple'])*3 + (row['hr'])*4)/((row['AB']))
    else:
        final_slg[row['name']]['SLG'] = 0
    if(row['l_AB']!=0):
        final_slg[row['name']]['LGS'] = ((row['l_single']) + (row['l_double'])*2 + (row['l_triple'])*3 + (row['l_hr'])*4)/((row['l_AB']))
    else:
        final_slg[row['name']]['LGS'] = 0
    if(row['e_AB']!=0):
        final_slg[row['name']]['EGS'] = ((row['e_single']) + (row['e_double'])*2 + (row['e_triple'])*3 + (row['e_hr'])*4)/((row['e_AB']))
    else:
        final_slg[row['name']]['EGS'] = 0
    final_slg[row['name']]['SLG_GAIN'] = final_slg[row['name']]['LGS'] - final_slg[row['name']]['EGS']


df = pd.DataFrame.from_dict(final_slg, orient='index')
df.reset_index(level=0, inplace=True)
df.rename(index=str, columns={"index": "name"}, inplace=True)
print(df)
df.to_csv(r'/Users/blaisepage/Documents/CUBoulder/Sabermetrics/final_slg_data.csv')
