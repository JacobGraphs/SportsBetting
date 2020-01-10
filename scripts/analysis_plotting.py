import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sports_df = pd.read_csv('/Users/jacobtryba/DSI/assignments/capstone1/data/sports_df_named.csv')

by_sport_event = sports_df.groupby(['SPORTS_ID', 'FULL_DESCRIPTION',
                                     'EVENT', 'SELECTION', 'WIN_FLAG',
                                      'ODDS', 'LATEST_TAKEN']).agg(
                                          {'VOLUME_MATCHED' : 'sum', 'NUMBER_BETS': 'sum'}).reset_index()


# Creates individual dataframes for each sport #
football_american = by_sport_event.query('SPORTS_ID == "American Football"').reset_index()
aussie = by_sport_event.query('SPORTS_ID == "Australian Rules"').reset_index()
baseball = by_sport_event.query('SPORTS_ID == "Baseball"').reset_index()
basketball = by_sport_event.query('SPORTS_ID == "Basketball"').reset_index()
boxing = by_sport_event.query('SPORTS_ID == "Boxing"').reset_index()
cricket = by_sport_event.query('SPORTS_ID == "Cricket"').reset_index()
cycling = by_sport_event.query('SPORTS_ID == "Cycling"').reset_index()
financial = by_sport_event.query('SPORTS_ID == "Financial Bets"').reset_index()
gaelic = by_sport_event.query('SPORTS_ID == "Gaelic Games"').reset_index()
golf = by_sport_event.query('SPORTS_ID == "Golf"').reset_index()
greyhound = by_sport_event.query('SPORTS_ID == "Greyhound Racing"').reset_index()
handball = by_sport_event.query('SPORTS_ID == "Handball"').reset_index()
hockey = by_sport_event.query('SPORTS_ID == "Ice Hockey"')
motor = by_sport_event.query('SPORTS_ID == "Motor Sport"').reset_index()
rugby_league = by_sport_event.query('SPORTS_ID == "Rugby League"').reset_index()
rugby_union = by_sport_event.query('SPORTS_ID == "Rugby Union"').reset_index()
snooker = by_sport_event.query('SPORTS_ID == "Snooker"').reset_index()
soccer = by_sport_event.query('SPORTS_ID == "Soccer"').reset_index()
special = by_sport_event.query('SPORTS_ID == "Special Bets"').reset_index()
tennis = by_sport_event.query('SPORTS_ID == "Tennis"').reset_index()
ufc = by_sport_event.query('SPORTS_ID == "UFC"').reset_index()
volleyball = by_sport_event.query('SPORTS_ID == "Volleyball"').reset_index()

# Finds the Revenue per Sport #
football_american_revenue = football_american['VOLUME_MATCHED'].sum()
aussie_revenue = aussie['VOLUME_MATCHED'].sum()
baseball_revenue = baseball['VOLUME_MATCHED'].sum()
basketball_revenue = basketball['VOLUME_MATCHED'].sum()
boxing_revenue = boxing['VOLUME_MATCHED'].sum()
cricket_revenue = cricket['VOLUME_MATCHED'].sum()
cycling_revenue = cycling['VOLUME_MATCHED'].sum()
financial_revenue = financial['VOLUME_MATCHED'].sum()
gaelic_revenue = gaelic['VOLUME_MATCHED'].sum()
golf_revenue = golf['VOLUME_MATCHED'].sum()
greyhound_revenue = greyhound['VOLUME_MATCHED'].sum()
handball_revenue = handball['VOLUME_MATCHED'].sum()
hockey_revenue = hockey['VOLUME_MATCHED'].sum()
motor_revenue = motor['VOLUME_MATCHED'].sum()
rugby_league_revenue = rugby_league['VOLUME_MATCHED'].sum()
rugby_union_revenue = rugby_union['VOLUME_MATCHED'].sum()
snooker_revenue = snooker['VOLUME_MATCHED'].sum()
soccer_revenue = soccer['VOLUME_MATCHED'].sum()
tennis_revenue = tennis['VOLUME_MATCHED'].sum()
ufc_revenue = ufc['VOLUME_MATCHED'].sum()
volleyball_revenue = volleyball['VOLUME_MATCHED'].sum()

sports_revenue = {'Aussie':aussie_revenue,
                  'Baseball': baseball_revenue,
                  'Basketball': basketball_revenue,
                  'Boxing': boxing_revenue,
                  'Cricket': cricket_revenue,
                  'Cycling': cycling_revenue,
                  'Financial': financial_revenue,
                  'Football': football_american_revenue,
                  'Gaelic': gaelic_revenue,
                  'Golf': golf_revenue,
                  'Greyhound': greyhound_revenue,
                  'Handball': handball_revenue,
                  'Hockey': hockey_revenue,
                  'Motor': motor_revenue,
                  'Rugby_league': rugby_league_revenue,
                  'Rugby_union': rugby_union_revenue,
                  'Snooker': snooker_revenue,
                  'Soccer': soccer_revenue,
                  'Tennis': tennis_revenue,
                  'UFC': ufc_revenue,
                  'Volleyball': volleyball_revenue}

high_revenue = 100000000
low_revenue = 1000000

sports_revenue_low = {k:v for (k,v) in sports_revenue.items() if v < low_revenue}
sports_revenue_mid = {k:v for (k,v) in sports_revenue.items() if v >= low_revenue and v <= high_revenue}
sports_revenue_high = {k:v for (k,v) in sports_revenue.items() if v > high_revenue}

# Finds the Cost per Sport as Defined by Player Win #

by_sport_event_costs = by_sport_event.query('WIN_FLAG == 1').reset_index()
    # Creates Dataframes with Cost Column Where Players Win #
by_sport_event_costs['COSTS'] = by_sport_event_costs['ODDS'] * by_sport_event_costs['VOLUME_MATCHED']
football_american_costs = by_sport_event_costs.query('SPORTS_ID == "American Football"').reset_index()
aussie_costs = by_sport_event_costs.query('SPORTS_ID == "Australian Rules"').reset_index()
baseball_costs = by_sport_event_costs.query('SPORTS_ID == "Baseball"').reset_index()
basketball_costs = by_sport_event_costs.query('SPORTS_ID == "Basketball"').reset_index()
boxing_costs = by_sport_event_costs.query('SPORTS_ID == "Boxing"').reset_index()
cricket_costs = by_sport_event_costs.query('SPORTS_ID == "Cricket"').reset_index()
cycling_costs = by_sport_event_costs.query('SPORTS_ID == "Cycling"').reset_index()
financial_costs = by_sport_event_costs.query('SPORTS_ID == "Financial Bets"').reset_index()
gaelic_costs = by_sport_event_costs.query('SPORTS_ID == "Gaelic Games"').reset_index()
golf_costs = by_sport_event_costs.query('SPORTS_ID == "Golf"').reset_index()
greyhound_costs = by_sport_event_costs.query('SPORTS_ID == "Greyhound Racing"').reset_index()
handball_costs = by_sport_event_costs.query('SPORTS_ID == "Handball"').reset_index()
hockey_costs = by_sport_event_costs.query('SPORTS_ID == "Ice Hockey"').reset_index()
motor_costs = by_sport_event_costs.query('SPORTS_ID == "Motor Sport"').reset_index()
rugby_league_costs = by_sport_event_costs.query('SPORTS_ID == "Rugby League"').reset_index()
rugby_union_costs = by_sport_event_costs.query('SPORTS_ID == "Rugby Union"').reset_index()
snooker_costs = by_sport_event_costs.query('SPORTS_ID == "Snooker"').reset_index()
soccer_costs = by_sport_event_costs.query('SPORTS_ID == "Soccer"').reset_index()
special_costs = by_sport_event_costs.query('SPORTS_ID == "Special Bets"').reset_index()
tennis_costs = by_sport_event_costs.query('SPORTS_ID == "Tennis"').reset_index()
ufc_costs = by_sport_event_costs.query('SPORTS_ID == "UFC"').reset_index()
volleyball_costs = by_sport_event_costs.query('SPORTS_ID == "Volleyball"').reset_index()

football_american_costs_complete = football_american_costs['COSTS'].sum()
aussie_costs_complete = aussie_costs['COSTS'].sum()
baseball_costs_complete = baseball_costs['COSTS'].sum()
basketball_costs_complete = basketball_costs['COSTS'].sum()
boxing_costs_complete = boxing_costs['COSTS'].sum()
cricket_costs_complete = cricket_costs['COSTS'].sum()
cycling_costs_complete = cycling_costs['COSTS'].sum()
financial_costs_complete = financial_costs['COSTS'].sum()
gaelic_costs_complete = gaelic_costs['COSTS'].sum()
golf_costs_complete = golf_costs['COSTS'].sum()
greyhound_costs_complete = greyhound_costs['COSTS'].sum()
handball_costs_complete = handball_costs['COSTS'].sum()
hockey_costs_complete = hockey_costs['COSTS'].sum()
motor_costs_complete = motor_costs['COSTS'].sum()
rugby_league_costs_complete = rugby_league_costs['COSTS'].sum()
rugby_union_costs_complete = rugby_union_costs['COSTS'].sum()
snooker_costs_complete = snooker_costs['COSTS'].sum()
soccer_costs_complete = soccer_costs['COSTS'].sum()
special_costs_complete = special_costs['COSTS'].sum()
tennis_costs_complete = tennis_costs['COSTS'].sum()
ufc_costs_complete = ufc_costs['COSTS'].sum()
volleyball_costs_complete = volleyball_costs['COSTS'].sum()

sports_costs = {'Football': football_american_costs_complete,
                  'Aussie':aussie_costs_complete,
                  'Baseball': baseball_costs_complete,
                  'Basketball': basketball_costs_complete,
                  'Boxing': boxing_costs_complete,
                  'Cricket': cricket_costs_complete,
                  'Cycling': cycling_costs_complete,
                  'Financial': financial_costs_complete,
                  'Gaelic': gaelic_costs_complete,
                  'Golf': golf_costs_complete,
                  'Greyhound': greyhound_costs_complete,
                  'Handball': handball_costs_complete,
                  'Hockey': hockey_costs_complete,
                  'Motor': motor_costs_complete,
                  'Rugby_league': rugby_league_costs_complete,
                  'Rugby_union': rugby_union_costs_complete,
                  'Snooker': snooker_costs_complete,
                  'Soccer': soccer_costs_complete,
                  'Tennis': tennis_costs_complete,
                  'UFC': ufc_costs_complete,
                  'Volleyball': volleyball_costs_complete}

# These dictionaries are structured according to the high, mid, low revenue list #
sports_costs_high = {'Cricket': cricket_costs_complete,
                        'Soccer': soccer_costs_complete,
                        'Tennis': tennis_costs_complete}

sports_costs_mid = {'Baseball': baseball_costs_complete,
                    'Motor': motor_costs_complete,
                    'Rugby_union': rugby_union_costs_complete,
                    'Volleyball': volleyball_costs_complete,
                    'Aussie': aussie_costs_complete,
                    'Rugby_league': rugby_league_costs_complete,
                    'Football': football_american_costs_complete,
                    'Golf': golf_costs_complete,
                    'Greyhound': greyhound_costs_complete,
                    'Basketball':basketball_costs_complete}

sports_costs_low = {'Handball': handball_costs_complete,
                    'UFC': ufc_costs_complete,
                    'Financial': financial_costs_complete,
                    'Hockey': hockey_costs_complete,
                    'Gaelic': gaelic_costs_complete,
                    'Boxing': boxing_costs_complete,
                    'Snooker': snooker_costs_complete,
                    'Cycling': cycling_costs_complete}


# produce roi by sport in positive and negative dictionaries
def roi_calculator(revenue, costs):
    roi_positive = {}
    roi_negative = {}
    for sport in revenue:
        if (revenue[sport] - costs[sport]) > 0:
            roi_positive[sport] = ((revenue[sport] - costs[sport])/costs[sport])
        else:
            roi_negative[sport] = ((revenue[sport] - costs[sport])/costs[sport])
    return roi_positive, roi_negative

# produce roi in dollars by sport in positive and negative dictionaries
def roi_calculator_dollars(revenue, costs):
    roi_dollars_positive = {}
    roi_dollars_negative = {}
    for sport in revenue:
        if (revenue[sport] - costs[sport]) > 0:
            roi_dollars_positive[sport] = (revenue[sport] - costs[sport])
        else: roi_dollars_negative[sport] = (revenue[sport] - costs[sport])
    return roi_dollars_positive, roi_dollars_negative

sports_roi_dict_posi,sports_roi_dict_neg  = roi_calculator(sports_revenue, sports_costs)
sports_roi_dollars_dict_posi, sports_roi_dollars_dict_neg = roi_calculator_dollars(sports_revenue, sports_costs)

high_sports_roi_dict_posi, high_sports_roi_dict_neg  = roi_calculator(sports_revenue_high, sports_costs_high)
high_sports_roi_dollars_dict_posi, high_sports_roi_dollars_dict_neg = roi_calculator_dollars(sports_revenue_high, sports_costs_high)

mid_sports_roi_dict_posi, mid_sports_roi_dict_neg  = roi_calculator(sports_revenue_mid, sports_costs_mid)
mid_sports_roi_dollars_dict_posi, mid_sports_roi_dollars_dict_neg = roi_calculator_dollars(sports_revenue_mid, sports_costs_mid)

low_sports_roi_dict_posi, low_sports_roi_dict_neg  = roi_calculator(sports_revenue_low, sports_costs_low)
low_sports_roi_dollars_dict_posi, low_sports_roi_dollars_dict_neg = roi_calculator_dollars(sports_revenue_low, sports_costs_low)


# Generates Revenue Figures #

fig, ax = plt.subplots(1, 3, figsize = (20,6))

ax[0].bar(list(sports_revenue_low.keys()), sports_revenue_low.values(), color = 'yg')
ax[0].set_title('Total Gambled by Sport - Low')
ax[0].ticklabel_format(axis = 'y', useOffset=False, style='plain')
ax[0].tick_params(axis='x', labelrotation=90)

ax[1].bar(list(sports_revenue_mid.keys()), sports_revenue_mid.values(), color = 'gy')
ax[1].set_title('Total Gambled by Sport - Mid')
ax[1].ticklabel_format(axis = 'y', useOffset=False, style='plain')
ax[1].tick_params(axis='x', labelrotation=90)

ax[2].bar(list(sports_revenue_high.keys()), sports_revenue_high.values(), color = 'yg')
ax[2].set_title('Total Gambled by Sport - High')
ax[2].ticklabel_format(axis = 'y', useOffset=False, style='plain')
ax[2].tick_params(axis='x', labelrotation=90)

revenues_fig = fig.savefig('/Users/jacobtryba/DSI/assignments/capstone1/images/revenues.png', bbox_inches='tight')


# Generates Full Revenue minus Costs Figures #
fig, ax = plt.subplots(4,1, figsize = (20,15))
ax[0].bar(list(sports_roi_dict_posi.keys()), sports_roi_dict_posi.values(), color = 'yg')
ax[0].set_title('Positive ROI by Sport')
ax[0].ticklabel_format(axis = 'y', useOffset=False, style='plain')

ax[1].bar(list(sports_roi_dollars_dict_posi.keys()), sports_roi_dollars_dict_posi.values(), color = 'yg')
ax[1].set_title('Positive ROI by Sport')
ax[1].ticklabel_format(axis = 'y', useOffset=False, style='plain')

ax[2].bar(list(sports_roi_dict_neg.keys()), sports_roi_dict_neg.values(), color = 'ry')
ax[2].set_title('Negative ROI by Sport')
ax[2].ticklabel_format(axis = 'y', useOffset=False, style='plain')

ax[3].bar(list(sports_roi_dollars_dict_neg.keys()), sports_roi_dollars_dict_neg.values(), color = 'ry')
ax[3].set_title('Negative ROI by Sport')
ax[3].ticklabel_format(axis = 'y', useOffset=False, style='plain')
all_rev_costs = fig.savefig('/Users/jacobtryba/DSI/assignments/capstone1/images/all.png', bbox_inches='tight')

# sorts the dictionaries for plotting #
low_sports_roi_dict_posi = {k: v for k, v in sorted(low_sports_roi_dict_posi.items(), key=lambda item: item[1])}
low_sports_roi_dollars_dict_posi = {k: v for k, v in sorted(low_sports_roi_dollars_dict_posi.items(), key=lambda item: item[1])}

mid_sports_roi_dict_posi = {k: v for k, v in sorted(mid_sports_roi_dict_posi.items(), key=lambda item: item[1])}
mid_sports_roi_dollars_dict_posi = {k: v for k, v in sorted(mid_sports_roi_dollars_dict_posi.items(), key=lambda item: item[1])}

# Generates Positive ROI Sports Low and Mid #
fig, ax = plt.subplots(4,1, figsize = (20,15))
ax[0].bar(list(low_sports_roi_dict_posi.keys()), low_sports_roi_dict_posi.values(), color = 'yg')
ax[0].set_title('Positive ROI by Sport - Low')
ax[0].ticklabel_format(axis = 'y', useOffset=False, style='plain')

ax[1].bar(list(low_sports_roi_dollars_dict_posi.keys()), low_sports_roi_dollars_dict_posi.values(), color = 'yg')
ax[1].set_title('Positive ROI by Sport - Low')
ax[1].ticklabel_format(axis = 'y', useOffset=False, style='plain')

ax[2].bar(list(mid_sports_roi_dict_posi.keys()), mid_sports_roi_dict_posi.values(), color = 'yg')
ax[2].set_title('Positive ROI by Sport - Mid')
ax[2].ticklabel_format(axis = 'y', useOffset=False, style='plain')

ax[3].bar(list(mid_sports_roi_dollars_dict_posi.keys()), mid_sports_roi_dollars_dict_posi.values(), color = 'yg')
ax[3].set_title('Positive ROI by Sport - Mid')
ax[3].ticklabel_format(axis = 'y', useOffset=False, style='plain')

low_mid_gain = fig.savefig('/Users/jacobtryba/DSI/assignments/capstone1/images/low_mid_gain.png', bbox_inches='tight') 
# sorting the dictionaries for plotting #
mid_sports_roi_dict_neg = {k: v for k, v in sorted(mid_sports_roi_dict_neg.items(), key=lambda item: item[1])}
mid_sports_roi_dollars_dict_neg = {k: v for k, v in sorted(mid_sports_roi_dollars_dict_neg.items(), key=lambda item: item[1])}

# Generates Negative ROI Sports Low and Mid

fig, ax = plt.subplots(2, 1, figsize = (20,6))

ax[0].bar(list(mid_sports_roi_dict_neg.keys()), mid_sports_roi_dict_neg.values(), color = 'ry')
ax[0].set_title('Negative ROI by Sport - Mid')
ax[0].ticklabel_format(axis = 'y', useOffset=False, style='plain')

ax[1].bar(list(mid_sports_roi_dollars_dict_neg.keys()), mid_sports_roi_dollars_dict_neg.values(), color = 'ry')
ax[1].set_title('Dollars Lost by Sport - Mid')
ax[1].ticklabel_format(axis = 'y', useOffset=False, style='plain')

low_mid_loss = fig.savefig('/Users/jacobtryba/DSI/assignments/capstone1/images/low_mid_loss.png', bbox_inches='tight')