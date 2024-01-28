from sklearn.metrics.pairwise import cosine_similarity
from nba_api.stats.static import players
import pandas as pd
import numpy as np

def load_prep_data(datapath:str):
    '''
    load and prep the data
    '''
    data = pd.read_csv(datapath)
    data = data.sort_values(by=['SEASON_ID', 'TEAM_ID'])
    return data

def get_player_ids(data, targetseason, player_id):
    # calculate similiarity between players per season
    # Get unique years
    # return 10 most similar players to player_id in the given season
    unique_seasons = data['SEASON_ID'].unique()

    # Initialize a dictionary to store cosine similarity matrices for each season
    cosine_sim_by_season = {}

    # Loop over each unique season
    for season in unique_seasons:
        # Subset the data for the current year
        data_season = data[data['SEASON_ID'] == targetseason]
        
        # Identify players with multiple entries in the season
        player_counts = data_season['PLAYER_ID'].value_counts()
        multiple_teams_players = player_counts[player_counts > 1].index

        # For players with multiple entries, keep only the 'TOT' row
        data_season = data_season[(~data_season['PLAYER_ID'].isin(multiple_teams_players)) | (data_season['TEAM_ABBREVIATION'] == 'TOT')]

        # Reset the index
        data_season = data_season.reset_index(drop=True)
        
        # Compute the cosine similarity matrix for the current season
        cosine_sim_by_season[season] = cosine_similarity(data_season.iloc[:, 6:])
    # Get the cosine similarity matrix for the season of interest
    cosine_sim_season = cosine_sim_by_season[season]

    # Find the index of the player of interest in the data for the season of interest
    player_index = np.where(data[(data['SEASON_ID'] == targetseason) & (data['PLAYER_ID'] == player_id)].index)[0][0]

    # Get the top 10 similar players for the player of interest 
    similar_players = cosine_sim_season[player_index].argsort()[-10:]
    '''
    get the player IDs from a given season
    '''
    # Get the data for the season of interest
    data_season = data[data['SEASON_ID'] == season]

    # Identify players with multiple entries in the season
    player_counts = data_season['PLAYER_ID'].value_counts()
    multiple_teams_players = player_counts[player_counts > 1].index

    # For players with multiple entries, keep only the 'TOT' row
    data_season = data_season[(~data_season['PLAYER_ID'].isin(multiple_teams_players)) | (data_season['TEAM_ABBREVIATION'] == 'TOT')]

    # Reset the index
    data_season = data_season.reset_index(drop=True)

    # Get the player IDs of the similar players
    similar_player_ids = data_season.iloc[similar_players]['PLAYER_ID']
    return similar_player_ids


if __name__ == '__main__':
    data = load_prep_data('all_player_stats.csv')
    ids = get_player_ids(data, '2023-24', 2544)
    print(ids)