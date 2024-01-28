import pandas as pd
import time
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguedashteamstats

#get teams
team_dict = teams.get_teams()

#initialize empty dataframelist
all_team_stats = []

#iterate over all teams
for team in team_dict:
    #get team id
    team_id = team['id']

    #get team stats for this year
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id, season='2023-24')

    #convert to dataframe
    data = team_stats.get_data_frames()[0]

    #append dataframe to list
    all_team_stats.append(data)
    time.sleep(15)

#concatenate all dataframes in the list
all_team_stats_df = pd.concat(all_team_stats, ignore_index=True)

#convert to csv
all_team_stats_df.to_csv('all_team_stats.csv', index=False)