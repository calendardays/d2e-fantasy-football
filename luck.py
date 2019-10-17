import json
import numpy as np

class DataError(Exception):
    def __init__(self, message):
        self.message = message

with open('d2e-fantasy.json') as f:
    data = json.load(f)
    
    for season in data:
        print(f'{season} Season'
              f'\n___________'
              )
            
        print(f'\tTeam & '
              f'\tRank & '
              f'\tStrength of Schedule % & '
              f'\tOpponent Heat Index % & '
              )
              
        random_team = list(data[season].keys())[0]
        n_weeks = len(data[season][random_team]['Schedule'])
              
        pts_for = np.array([data[season][team]['Pts For'] for team in data[season]])
        pts_for_avg = pts_for.mean()
        pts_for_avg_per_game = pts_for_avg / n_weeks
              
        for team in data[season]:
            n_games = len(data[season][team]['Schedule'])
            if n_games != n_weeks:
                raise DataError(f'{team} played {n_games} in {n_weeks} in {season}')
                
            rank = data[season][team]['Rank']
                
            pts_against = data[season][team]['Pts Against']
            pts_against_per_game = pts_against / n_weeks
            strength_of_schedule = pts_against_per_game / pts_for_avg_per_game
            strength_of_schedule_pct = 100 * (strength_of_schedule - 1)
            
            expected_opponent_pts = np.array([data[season][opponent]['Pts For'] for opponent in data[season][team]['Schedule']])
            expected_opponent_pts_avg = expected_opponent_pts.mean()
            opponent_heat_index = pts_against / expected_opponent_pts_avg
            opponent_heat_index_pct = 100 * (opponent_heat_index - 1)
            
            print(f'\t{team} & '
                  f'\t{rank} & '
                  f'\t{strength_of_schedule_pct} & '
                  f'\t{opponent_heat_index_pct} & '
                  )
                  