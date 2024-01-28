from scipy.spatial.distance import pdist, squareform
from nba_api.stats.static import players
import pandas as pd

def load_prep_data(datapath: str):
    '''
    Load and prep the data
    '''
    data = pd.read_csv(datapath)
    data = data.sort_values(by=['SEASON_ID', 'TEAM_ID'])
    
    # Calculate 'PTS/GP' column
    data['PTS/GP'] = data['PTS'] / data['GP']
    
    # Remove 'PTS' and 'GP' columns
    data = data.drop(['PTS', 'GP'], axis=1)
    
    return data

def get_player_ids(data: pd.DataFrame, targetseason: str, player_id: int):
    ''' 
    Calculate similiarity between players per season
    Get unique years
    Return 10 most similar players to player_id in the given season
    '''
    
    unique_seasons = data['SEASON_ID'].unique()

    # Initialize a dictionary to store cosine similarity matrices for each season
    euclidean_dist_by_season = {}

    # Loop over each unique season
    for season in unique_seasons:
        # Subset the data for the current year
        data_season = data[data['SEASON_ID'] == season]
        
        # Identify players with multiple entries in the season
        player_counts = data_season['PLAYER_ID'].value_counts()
        multiple_teams_players = player_counts[player_counts > 1].index

        # For players with multiple entries, keep only the 'TOT' row
        data_season = data_season[(~data_season['PLAYER_ID'].isin(multiple_teams_players)) | (data_season['TEAM_ABBREVIATION'] == 'TOT')]

        # Reset the index
        data_season = data_season.reset_index(drop=True)
        
        # Compute the Euclidean distance matrix for the current season
        euclidean_dist_by_season[season] = squareform(pdist(data_season.iloc[:, 5:]))
    # Get the cosine similarity matrix for the season of interest
    euclidean_dist_by_season = euclidean_dist_by_season[targetseason]

    # Find the index of the player of interest in the data for the season of interest
    player_index = data_season[data_season['PLAYER_ID'] == player_id].index[0]

    # Get the top 10 similar players for the player of interest 
    similar_players = euclidean_dist_by_season[player_index].argsort()[:10]
    '''
    Get the player IDs from a given season
    '''
    # Get the data for the season of interest
    data_season = data[data['SEASON_ID'] == targetseason]

    # Identify players with multiple entries in the season
    player_counts = data_season['PLAYER_ID'].value_counts()
    multiple_teams_players = player_counts[player_counts > 1].index

    # For players with multiple entries, keep only the 'TOT' row
    data_season = data_season[(~data_season['PLAYER_ID'].isin(multiple_teams_players)) | (data_season['TEAM_ABBREVIATION'] == 'TOT')]

    # Reset the index
    data_season = data_season.reset_index(drop=True)

    # Get the player IDs of the similar players
    similar_player_ids = data_season.iloc[similar_players]['PLAYER_ID'].tolist()
    similar_player_ids.append(player_id)
    return similar_player_ids

def get_names(player_ids: list):
    '''
    Get the names of the players
    '''
    # Initialize an empty dictionary
    player_names = {}

    # Get the names of the similar players
    for id in player_ids:
        player = players.find_player_by_id(id)
        player_names[id] = player['full_name']
    
    return player_names

def get_id(name: str):
    '''
    Get the ID of the player
    '''
    # Get the ID of the player
    player = players.find_players_by_full_name(name)
    player_id = player[0]['id']
    
    return player_id

if __name__ == '__main__':
    data = load_prep_data('all_player_stats.csv')
    ids = get_player_ids(data, '2023-24', get_id("LeBron James"))
    names = get_names(ids)
    id_name_dict = {id: names[id] for id in ids}
    print(id_name_dict)
