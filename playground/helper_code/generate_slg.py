import pandas as pd
import numpy as np

def isNaN(num):
    return num != num

def generate_slg_data():

    statcast_2016 = pd.read_csv("statcast_data/statcast2016.csv")
    statcast_2017 = pd.read_csv("statcast_data/statcast2017.csv")
    statcast_2018 = pd.read_csv("statcast_data/statcast2018.csv")
    names_data = pd.read_csv("statcast_data/names_mlbam.csv")

    statcast_data = pd.concat([statcast_2016, statcast_2017, statcast_2018], ignore_index=True)

    # SLG = (1B + 2Bx2 + 3Bx3 + HRx4)/AB
    # events: single, double, triple, home_run
    slg_dict = {}
    mlbam_dict = {}
    for index, row in names_data.iterrows():
        slg_dict[row['mlbam']] = {'name': row['name'], 'single': 0, 'double': 0, 'tiple': 0, 'hr': 0, 'e_single': 0, 'e_double': 0, 'e_triple': 0, 'e_hr': 0, 'l_single': 0, 'l_double': 0, 'l_triple': 0, 'l_hr': 0, 'AB': 0, 'e_AB': 0, 'l_AB': 0}
        mlbam_dict[row['mlbam']] = row['name']

    for index, row in statcast_data.iterrows():
        if(row['batter'] in mlbam_dict):

            #print(row['events'], type(row['events']))

            # Late game innings (9 and 8)
            if(row['inning']>=8):

                if(row['events']=="single"):
                    slg_dict[row['batter']]['single'] += 1
                    slg_dict[row['batter']]['l_single'] += 1

                elif(row['events']=="double"):
                    slg_dict[row['batter']]['double'] += 1
                    slg_dict[row['batter']]['l_double'] += 1

                elif(row['events']=="tiple"):
                    slg_dict[row['batter']]['triple'] += 1
                    slg_dict[row['batter']]['l_triple'] += 1

                elif(row['events']=="home_run"):
                    slg_dict[row['batter']]['hr'] += 1
                    slg_dict[row['batter']]['l_hr'] += 1

                if(not isNaN(row['events'])):
                    slg_dict[row['batter']]['l_AB'] += 1
                    slg_dict[row['batter']]['AB'] += 1

            # Early game innings (1-7)
            elif(row['inning']<=8):

                if(row['events']=="single"):
                    slg_dict[row['batter']]['single'] += 1
                    slg_dict[row['batter']]['e_single'] += 1

                elif(row['events']=="double"):
                    slg_dict[row['batter']]['double'] += 1
                    slg_dict[row['batter']]['e_double'] += 1

                elif(row['events']=="tiple"):
                    slg_dict[row['batter']]['triple'] += 1
                    slg_dict[row['batter']]['e_triple'] += 1

                elif(row['events']=="home_run"):
                    slg_dict[row['batter']]['hr'] += 1
                    slg_dict[row['batter']]['e_hr'] += 1

                if(not isNaN(row['events'])):
                    slg_dict[row['batter']]['e_AB'] += 1
                    slg_dict[row['batter']]['AB'] += 1


    df = pd.DataFrame.from_dict(slg_dict, orient='index')
    df.reset_index(level=0, inplace=True)
    df.rename(index=str, columns={"index": "mlbam"}, inplace=True)
    print(df)
    df.to_csv(r'/Users/blaisepage/Documents/CUBoulder/Sabermetrics/all_slg_data.csv')


generate_slg_data()
