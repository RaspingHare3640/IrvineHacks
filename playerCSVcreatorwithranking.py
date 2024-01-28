import pandas as pd
import time
from nba_api.stats.static import players
from nba_api.stats.endpoints import leaguedashplayerstats

# Get all players
active_player_dict = players.get_active_players()

# Initialize an empty DataFrame to store all player stats
all_player_stats = []
# Iterate over all players
for player in active_player_dict:
    # Get player's id
    player_id = player['id']

    # Get player's career stats
    player_career = leaguedashplayerstats.LeagueDashPlayerStats(player_id)

    # Convert to DataFrame
    data = player_career.get_data_frames()[0]
    # Append DataFrame to list
    all_player_stats.append(data)
    time.sleep(15)

# Concatenate all DataFrames in the list
all_player_stats_df = pd.concat(all_player_stats, ignore_index=True)

# Save DataFrame to a CSV file
all_player_stats_df.to_csv('all_player_stats.csv', index=False)