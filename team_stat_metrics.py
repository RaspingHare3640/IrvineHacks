import pandas as pd
csv_path = 'all_team_stats.csv'

data = pd.read_csv(csv_path)


# LOWER SCORES ARE BETTER FOR ALL THE METRICS!!!

# Perimeter offense: Generating free throws, midrange effectiveness, and 3-point shooting
# 3P% Rank, FTA Rank, PFD Rank

perimeter_offense_dict = {}

for i in range(30):
    # avg is ~46.5
    perimeter_offense_metric = int(data['FG3_PCT_RANK'][i]) + int(data['FTA_RANK'][i]) + int(data['PFD_RANK'][i])
    perimeter_offense_dict[f'{data['TEAM_NAME'][i]}'] = perimeter_offense_metric

# Interior offense: Getting to the paint frequently, finishing inside consistently, and crashing offensive glass.

# OR Rank, BLKA Rank

interior_offense_dict = {}

for i in range(30):
    # avg is ~31
    interior_offense_metric = int(data['OREB_RANK'][i]) #+ int(data['BLKA_RANK'][i])
    interior_offense_dict[f'{data['TEAM_NAME'][i]}'] = interior_offense_metric
        
# Control: Not just how well a team moves the basketball but also how well a team protects it
# AST Rank, TOV Rank

control_dict = {}

for i in range(30):
    # avg is ~31
    control_metric = int(data['AST_RANK'][i]) + int(data['TOV_RANK'][i])
    control_dict[f'{data['TEAM_NAME'][i]}'] = control_metric
    
# Perimeter defense: Defending without fouling, being able to contest midrange shots, and preventing 3s

# PF Rank, STL Rank

perimeter_defense_dict = {}

for i in range(30):
    # avg is ~31
    perimeter_defense_metric = int(data['PF_RANK'][i]) + int(data['STL_RANK'][i])
    perimeter_defense_dict[f'{data['TEAM_NAME'][i]}'] = perimeter_defense_metric
    
# Interior defense: Paint scoring prevention, rim protection, defensive rebounding

# DR Rank, BLK Rank

interior_defense_dict = {}

for i in range(30):
    # avg is ~31
    interior_defense_metric = int(data['DREB_RANK'][i]) + int(data['BLK_RANK'][i])
    interior_defense_dict[f'{data['TEAM_NAME'][i]}'] = interior_defense_metric
  
# “Intangibles”: Fast-break scoring differential and free-throw percentage

# FT% Rank, FG% Rank, REB Rank, PLUS MINUS Rank

intangibles_dict = {}

for i in range(30):
    # avg is ~62
    intangibles_metric = int(data['FT_PCT_RANK'][i]) + int(data['FG_PCT_RANK'][i]) + int(data['REB_RANK'][i]) + int(data['PLUS_MINUS_RANK'][i])
    intangibles_dict[f'{data['TEAM_NAME'][i]}'] = intangibles_metric

# print('PERIMETER OFFENSE\n', perimeter_offense_dict, '\nPERIMETER DEFENSE\n', perimeter_defense_dict, '\nINTERIOUS OFFENSE\n', interior_offense_dict, '\nINTERIOR DEFENSE\n', interior_defense_dict, '\nCONTROL\n',control_dict, '\nINTANGIBLES\n', intangibles_dict)