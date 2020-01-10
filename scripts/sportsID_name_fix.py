import numpy as np
import pandas as pd

sports_df = pd.read_csv('/Users/jacobtryba/DSI/assignments/capstone1/data/fixed_betfair_dataset.csv')

sports_names = {1: 'Soccer', 2: 'Tennis', 3: 'Golf', 4: 'Cricket', 5: 'Rugby Union', 
     6: 'Boxing', 8: 'Motor Sport', 10: 'Special Bets', 11: 'Cycling', 1477: 'Rugby League',
     3503: 'Darts', 3988: 'Athletics', 4339: 'Greyhound Racing', 6231: 'Financial Bets', 6422: 'Snooker',
     6423: 'American Football', 7511: 'Baseball', 7522: 'Basketball', 7524: 'Ice Hockey', 61420: 'Australian Rules',
     468328: 'Handball', 998917: 'Volleyball', 2152880: 'Gaelic Games', 26420387: 'UFC'
    }

sports_df.SPORTS_ID = sports_df.SPORTS_ID.replace(sports_names)
sports_df = sports_df.to_csv (r'/Users/jacobtryba/DSI/assignments/capstone1/data/sports_df_named.csv', index = None, header=True)
