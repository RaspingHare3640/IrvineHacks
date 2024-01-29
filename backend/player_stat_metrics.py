from nba_api.stats.static import players
import pandas as pd
import numpy as np
import simPlayers as sp
import team_stat_metrics as tsm

def mean_stats(data: pd.DataFrame):
    # Group the data by player ID and calculate the mean of each stat
    num_data = data
    num_data = num_data.drop(['SEASON_ID','TEAM_ID','TEAM_ABBREVIATION','PLAYER_AGE'], axis=1)
    average_stats = num_data.groupby('PLAYER_ID').mean()
    # Reset the index to make 'PLAYER_ID' a column again
    average_stats.reset_index(inplace=True)
    return average_stats

def rank(data: pd.DataFrame, stat: str):
    # Rank the players by a given stat
    data = data.sort_values(by=[stat], ascending=False)
    # Reset the index
    data = data.reset_index(drop=True)
    # Add a column for the rank of each player
    data[stat + 'RANK'] = data.index + 1
    return data

def calculate_rank(data: pd.DataFrame, stats: list):
    # Create a new column that is the sum of 2 stats
    data[stats[0] + stats[1]] = data[stats[0]] + data[stats[1]]
    # Rank the players by the sum of 'FTP' and 'TF3P'
    data = rank(data, stats[0]+stats[1])
    return data


# Load and prep the data
data = sp.load_prep_data('all_player_stats.csv')
# Get the mean stats for each player
average = mean_stats(data)

perimeter_offense_stats = ['FG3_PCT', 'FTA']

perimeter_offense_rank = calculate_rank(average, perimeter_offense_stats)

perimeter_offense_player_dict = dict()

for i in range(524):
    perimeter_offense_player_metric = perimeter_offense_rank['FG3_PCTFTARANK'][i]
    perimeter_offense_player_dict[perimeter_offense_rank['PLAYER_ID'][i]] = perimeter_offense_player_metric

# # Interior offense: Getting to the paint frequently, finishing inside consistently, and crashing offensive glass.

# OR Rank, BLKA Rank

interior_offense_dict = {}

interior_offense_stats = ['OREB', 'OREB']

interior_offense_rank = calculate_rank(average, interior_offense_stats)

interior_offense_player_dict = dict()

for i in range(524):
    interior_offense_player_metric = interior_offense_rank['OREBOREBRANK'][i]
    interior_offense_player_dict[interior_offense_rank['PLAYER_ID'][i]] = interior_offense_player_metric


# # Control: Not just how well a team moves the basketball but also how well a team protects it
# # AST Rank, TOV Rank


control_stats = ['AST', 'TOV']

control_rank = calculate_rank(average, control_stats)

control_player_dict = dict()

for i in range(524):
    # avg is ~31
    control_metric = int(control_rank['ASTTOVRANK'][i])
    control_player_dict[f'{control_rank['PLAYER_ID'][i]}'] = control_metric

# # Perimeter defense: Defending without fouling, being able to contest midrange shots, and preventing 3s

# # PF Rank, STL Rank

perimeter_defense_stats = ['PF', 'STL']

perimeter_defense_rank = calculate_rank(average, perimeter_defense_stats)

perimeter_defense_player_dict = dict()

for i in range(524):
    # avg is ~31
    perimeter_defense_metric = int(perimeter_defense_rank['PFSTLRANK'][i])
    perimeter_defense_player_dict[f'{perimeter_defense_rank['PLAYER_ID'][i]}'] = perimeter_defense_metric

# # Interior defense: Paint scoring prevention, rim protection, defensive rebounding

# # DR Rank, BLK Rank

interior_defense_stats = ['DREB', 'BLK']

interior_defense_rank = calculate_rank(average, interior_defense_stats)

interior_defense_player_dict = dict()

for i in range(524):
    # avg is ~31
    interior_defense_metric = int(interior_defense_rank['DREBBLKRANK'][i])
    interior_defense_player_dict[f'{interior_defense_rank['PLAYER_ID'][i]}'] = interior_defense_metric

# # “Intangibles”: Fast-break scoring differential and free-throw percentage

# # FT% Rank, FG% Rank, REB Rank, PLUS MINUS Rank

intangibles_stats = ['REB', 'FG_PCT']

intangibles_rank = calculate_rank(average, intangibles_stats)


intangibles_player_dict = dict()

for i in range(524):
    # avg is ~31
    intangibles_metric = int(intangibles_rank['REBFG_PCTRANK'][i])
    intangibles_player_dict[f'{intangibles_rank['PLAYER_ID'][i]}'] = intangibles_metric



team_trade_index_dict = tsm.get_tradable_index_dict_of_teams()

top_player_dict = dict()

for team in team_trade_index_dict:
    index = team_trade_index_dict[team]
    if index == 0:
        # print(perimeter_offense_player_dict)
        player_id = int(f'{perimeter_offense_rank['PLAYER_ID'][0]}')
    elif index == 1:
        player_id = int(f'{interior_offense_rank['PLAYER_ID'][0]}')
    elif index == 2:
        player_id = f'{control_rank['PLAYER_ID'][0]}'
    elif index == 3:
        player_id = f'{perimeter_defense_rank['PLAYER_ID'][0]}'
    elif index == 4:
        player_id = f'{interior_defense_rank['PLAYER_ID'][0]}'
    else:
        player_id = f'{intangibles_rank['PLAYER_ID'][0]}'
    top_player_dict[team] = player_id


def get_top_player_dict():
    return top_player_dict


    
# LOWER SCORES ARE BETTER FOR ALL THE METRICS!!!

# Perimeter offense: Generating free throws, midrange effectiveness, and 3-point shooting
# 3P% Rank, FTA Rank, PFD Rank

# csv_path = 'all_team_stats.csv'

# data = pd.read_csv(csv_path)

# perimeter_offense_dict = {}

# for i in range(30):
#     perimeter_offense_metric = int(data['FG3_PCT_RANK'][i]) + int(data['FTA_RANK'][i]) + int(data['PFD_RANK'][i])
#     perimeter_offense_dict[f'{data['TEAM_NAME'][i]}'] = perimeter_offense_metric

# # Interior offense: Getting to the paint frequently, finishing inside consistently, and crashing offensive glass.

# # OR Rank, BLKA Rank

# interior_offense_dict = {}

# for i in range(30):
#     # avg is ~31
#     interior_offense_metric = int(data['OREB_RANK'][i]) #+ int(data['BLKA_RANK'][i])
#     interior_offense_dict[f'{data['TEAM_NAME'][i]}'] = interior_offense_metric
        
# # Control: Not just how well a team moves the basketball but also how well a team protects it
# # AST Rank, TOV Rank

# control_dict = {}

# for i in range(30):
#     # avg is ~31
#     control_metric = int(data['AST_RANK'][i]) + int(data['TOV_RANK'][i])
#     control_dict[f'{data['TEAM_NAME'][i]}'] = control_metric
    
# # Perimeter defense: Defending without fouling, being able to contest midrange shots, and preventing 3s

# # PF Rank, STL Rank

# perimeter_defense_dict = {}

# for i in range(30):
#     # avg is ~31
#     perimeter_defense_metric = int(data['PF_RANK'][i]) + int(data['STL_RANK'][i])
#     perimeter_defense_dict[f'{data['TEAM_NAME'][i]}'] = perimeter_defense_metric
    
# # Interior defense: Paint scoring prevention, rim protection, defensive rebounding

# # DR Rank, BLK Rank

# interior_defense_dict = {}

# for i in range(30):
#     # avg is ~31
#     interior_defense_metric = int(data['DREB_RANK'][i]) + int(data['BLK_RANK'][i])
#     interior_defense_dict[f'{data['TEAM_NAME'][i]}'] = interior_defense_metric
  
# # “Intangibles”: Fast-break scoring differential and free-throw percentage

# # FT% Rank, FG% Rank, REB Rank, PLUS MINUS Rank

# intangibles_dict = {}

# for i in range(30):
#     # avg is ~62
#     intangibles_metric = int(data['FT_PCT_RANK'][i]) + int(data['FG_PCT_RANK'][i]) + int(data['REB_RANK'][i]) + int(data['PLUS_MINUS_RANK'][i])
#     intangibles_dict[f'{data['TEAM_NAME'][i]}'] = intangibles_metric