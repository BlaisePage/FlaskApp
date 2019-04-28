import pandas as pd
import numpy as np

names_data = pd.read_csv("statcast_data/names_mlbam.csv")

names = []
for index, row in names_data.iterrows():
    names.append(row['name'])

print(names)
