from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from nba_api.stats.static import players
import pandas as pd

#load the data
data = pd.read_csv('all_player_stats.csv')
data = data.sort_values(by=['TEAM_ID', 'SEASON_ID'])
