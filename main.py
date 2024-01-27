from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity
from nba_api.stats.static import players
import pandas as pd

#load the data
data = pd.read_csv('all_player_stats.csv')
data = data.sort_values(by=['SEASON_ID', 'TEAM_ID'])

# filter columns
# Compute the cosine similarity matrix
# Select only the columns after the first 6 for the cosine similarity calculation
cosine_sim = cosine_similarity(data.iloc[1:, 6:])

# Get the top 10 similar players for each player
top_10_similar = cosine_sim.argsort()[:, -10:]

# Now, for a given player, you can recommend other players to trade based on their similarity
player_id = 2544  # replace with the id of the player you're interested in
similar_players = top_10_similar[player_id]
print(similar_players)
print(data.iloc[similar_players])
# Create and train the model
#model = LinearRegression()
#model.fit(features_train, target_train)

# Make predictions
#predictions = model.predict(features_test)

# Evaluate the model
#mse = mean_squared_error(target_test, predictions)
#print(f'Mean Squared Error: {mse}')