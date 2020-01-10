

### International Sports Gambling
A Look at Sports Betting Action From UK-Based Gambling House, "BetFair"

*Capstone 1 Project for Galvanize Data Science Immersive, Week 4*
*by Jacob Tryba*


**Table of Contents**
1. Background
2. The Data
3. Visualization




#### Background
In the world of sports gambling, there are several players. There are US-based platforms within states who have voted for legal action. There are troves of bookies taking action in groupchats. There are off-shore networks that cater to the world. States that have fully voted and created an operating opportunity for gambling houses include:
  - Delaware
  - New Jersey
  - Rhode Island
  - New York
  - Indiana
  - Mississippi
  - New Mexico
  - West Virginia
  - Iowa
  - Nevada
  - Pennsylvania
  - Arkansas
  - Oregon
  
 Six additional states have passed legislation and the opportunity for large corporate gambling is now in place. While this EDA studies a sample of data coming from an international gambling house, it is clear that sports betting has cleared through the US over the last few elections. Nevada is not the only economy.
What does the betting breakdown look like in an international market? American Football is the most gambled sport in the US, but internationally, which sports have the most action?

#### The Data
##### Brief Introduction
Sports Betting House, BetFair, claims to be the largest online betting exchange. They are based out of West London, UK and Clonskeagh, Dublin. For their highroller customers, those with total dollars gambled or total losses exceeding an arbitrary amount, there is access to betting data. The data collected consists of information on sport, event, the kind of bet placed, the selection of that bet, the odds by which that bet is met, the volume of the action, and the number of bets for the first week of September, 2014. Some extraneous information was gathered from outside sources.

##### Explanation of Data's Structure
  https://www.kaggle.com/zygmunt/betfair-sports   
  
The data starts as a CSV file on kaggle. Columns utilized are as follows:
- SPORTS_ID : an integer representing a series of sports
- FULL_DESCRIPTION : a string describing a full event 
                    
                    (ie Internationals/International Friendly/Fixtures 04 September / Slovakia v Malta)
- EVENT : a string describing the type of bet
                    
                    (ie Moneyline, the concept of choosing one team will win vs its competitor)
- SELECTION : a string describing the choice
                    
                    (ie Texas to win by any amount)
- ODDS : an integer representing the multiplier amount paid out to a player in the event of a win

                    (ie 1.2)
- VOLUME_MATCHED : a float representing the total amount of action BetFair took

                    (ie 2422340)
- WIN_FLAG : an integer of 1 or 0 representing a casino win or player win

##### Manipulation Methodology
1. First step was to apply a data fix provided by a secondary viewer of the original set. Applying their function recreated the csv so pandas could then read it in as a dataframe. This script is dataset_fix.py
2. Second step was to replace the integer for SPORTS_ID with a string describing the actual sport. This script is sportsID_name_fix.py.
3. Third step was to create my analysis. I grouped the data by sport, event, bet type, bet option, odds, win flag, and summed up total volume and number of bets for each. I also grouped by sport and got the average bet.

#### Visualization
##### Sample Cleaned Data
![Image description](https://github.com/JacobGraphs/SportsBetting/blob/master/images/sample.png)
##### Data Organized by Top Average Bet
![Image description](https://github.com/JacobGraphs/SportsBetting/blob/master/images/sports_averagebet.png)
##### Total Volume Gambled by Sport: Low, Mid, High
![Image description](https://github.com/JacobGraphs/SportsBetting/blob/master/images/revenues.png)
##### Return in % of Bet Volume Paid Out and Total Profit/Loss by Sport: All
![Image description](https://github.com/JacobGraphs/SportsBetting/blob/master/images/all.png)
##### Return in % of Bet Volume Paid Out and Total Profit by Sport: Low, Mid
![Image description](https://github.com/JacobGraphs/SportsBetting/blob/master/images/low_mid_gain.png)
##### Return in % of Bet Volume Paid Out and Total Loss by Sport: Low, Mid
![Image description](https://github.com/JacobGraphs/SportsBetting/blob/master/images/low_mid_loss.png)
