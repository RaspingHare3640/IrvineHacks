from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity
from nba_api.stats.static import players
import pandas as pd

#load the data
data = pd.read_csv('all_player_stats.csv')
data = data.sort_values(by=['SEASON_ID', 'TEAM_ID'])

# calculate similiarity between players per year
# Get unique years
unique_seasons = data['SEASON_ID'].unique()

# Initialize a dictionary to store cosine similarity matrices for each year
cosine_sim_by_season = {}

# Loop over each unique year
for year in unique_seasons:
    # Subset the data for the current year
    data_year = data[data['SEASON_ID'] == year]
    
    # Compute the cosine similarity matrix for the current year
    cosine_sim_by_season[year] = cosine_similarity(data_year.iloc[:, 6:])

# cosine_sim_by_season is a dict where the keys are seasons and the values are cosine similarity matrices for that season


# Get the cosine similarity matrix for the season of interest
cosine_sim_season = cosine_sim_by_season['2020-21']
# Get the top 10 similar players for the player of interest
player_id = 2544 
similar_players = cosine_sim_season[player_id].argsort()[-10:]

print(similar_players)

# Create and train the model
#model = LinearRegression()
#model.fit(features_train, target_train)

# Make predictions
#predictions = model.predict(features_test)

# Evaluate the model
#mse = mean_squared_error(target_test, predictions)
#print(f'Mean Squared Error: {mse}')