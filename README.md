# NRL WPA AND EPA CALCULATION

## Project description:
For each round of the league and every draw on each team, NRL provides in-depth analysis on detailed breakdowns of team performances and match draws, and continues evolving the sport by enhancing team strategies by proving its dedication to analytic views on the sport. Therefore, this in-depth data will be used in this project to address two critical objectives in sports analytics.
This project aims to develop a model to calculate Win Probability Added (WPA) for each team and Expected Points Added (EPA) for each player during a game. By evaluating key actions and their impact on outcomes, the model will provide metrics to assess how each play affects a team's likelihood of winning or scoring. WPA quantifies how individual actions, such as scoring or penalties, influence win probability, while EPA predicts the scoring impact of specific plays, helping teams optimize strategies in critical moments.
WPA and EPA are both a very interesting analysis that is widely used in multiple sports such as xG in Football or even WPA and EPA in American Football. Although some similar analysis has been done, it is still not widely used in the NRL. Therefore, we are focusing on modeling both WPA and EPA in each NRL game from 2020-2023 to show the significance of the analysis for the NRL, teams, players, and also the viewers. 

Some previous works that are related to WPA and EPA are in these links:
https://www.rugbyleagueeyetest.com/2022/02/07/explainer-eye-test-expected-points-etxp-for-the-nrl/ 
https://www.sfu.ca/~tswartz/papers/nrl.pdf 


## Sources:

The primary source of data is the official 2020-2023 NRL database. This database includes comprehensive information on matches, players, teams, events, and venues, with each row representing a single event. Key variables include MatchId, SeqNumber, and identifiers for Season, Series, Round, Venue, Club, Opposition, and Player. Time variables track the half of the game's elapsed time since kickoff, the number of times on the game clock in the current half, and the local kickoff time of the match.
Events are further detailed by PossessingClubId, PossessingPlayerId, and information on the specific event such as Set number, Tackle number, and EventCode with its corresponding EventName. The file also includes data for points scored, current match score, and opposition score at the time of the event. Locational data includes both physical and normalized coordinates (relative to the player or team in possession) across the rugby field, broken down into Xm/YmPhysical, Zone, Channel, and Section coordinates. Additional time-based variables track total possession seconds for both teams, offering insights into ball control during the match.

## Workflow: 
### 1. Data Collection
The Events.csv and Players.csv files contain information about matches, players, teams, and events, with each row representing a specific event. Key data points include match identifiers, timestamps, player positions, physical attributes (height, weight, age), and event types (e.g., passes, tackles).

### 2. Data Cleaning
Null handling: removing the rows of data with null values
Standardizing data format
Removing outliers

### 3. Feature Engineering
Create Field Position, Game Clock, Score Differential, and Possession variable
Calculate WPA: Post-play Win Probability - Pre-play Win Probability
Calculate EPA: Expected Points After Event - Expected Points Before Event
Create a binary variable for Win/Loss. 1 for win and 0 for loss
Create State variables (snapshots of the game state for chosen significant events, such as tries, ruck infringements, and tackles)

### 4. Data Validation
Perform exploratory data analysis (EDA) which are univariate analysis using histogram and box plot, bivariate analysis using barplot, pairplot and scatterplot, and multivariate analysis using heatmap. Also, perform normalization of the columns, log transformations/box cox transformation for skewed data and Kalman Filter for Time Series Data

### Data description: 
The data product will consist of approximately 10,000 observations, each representing a unique event from NRL matches. Each row will include time-stamped data on specific plays, capturing ball movement dynamics and player attributes during key events (e.g., score changes, possession switches).

Match ID: Identifies the specific match.
Sequence ID: Ensures events are in chronological order.
Team A ID / Team B ID: Identifies the competing teams.
Win/Loss column

This will also include WPA Features of:
Score Difference: Calculated as Team A Score - Team B Score.
Time Remaining: Total minutes remaining derived from Elapsed Minutes, Elapsed Seconds, and Half.

This will also include EPA Features of:
Event Name: Type of event (e.g., tackle, try, pass).
Possession Time: Total and opponent's possession time.
Physical Coordinates: XmPhysical and YmPhysical for field position.
Score Tracking: Current and opponent's scores.
Elapsed Game Time: Includes Elapsed Minutes, Elapsed Seconds, and Half.
Field Position: Normalized XmPhysical and YmPhysical based on field zones.
Game Context: Score differential and game clock information.
The Target variables of this project are the WPA and EPA.

## Project status:
We have completed the readme draft file and data collection and will continue with data cleaning as our next step. As mentioned before, we will remove null data, standardize the data format, and remove outliers, before proceeding into the next step.
The timeline and progress of our project can be found [here](https://github.com/Nasz-113/data3001-data-nrl-1/blob/20b659f92d8469e82df94c839294b4e151d3da17/weeklyTasks.csv)

## Usage: 
The dataset aims to calculate Win Probability Added (WPA) for each team and Expected Points Added (EPA) for each player during NRL games. This analysis will help assess how individual actions impact the likelihood of winning or scoring.

## Contacts:
Ahmad Nasiruddin (z5442313@ad.unsw.edu.au)
Belinda Wang (z5445872@ad.unsw.edu.au)
Hye Jun Jee (z5428730@ad.unsw.edu.au)
Lavan Indrajit (z5313058@ad.unsw.edu.au)

## Contributors: 
Ahmad Nasiruddin, Belinda Wang,, Hye Jun Jee, Lavan Indrajit.
If you are interested in contributing to the WPA and EPA analysis for NRL, You can share Your Insights, Provide Feedback, or Spread the Word: For any inquiries or to express your interest, please contact any of the team members listed above. We gratefully appreciate any support or contributions to our project
