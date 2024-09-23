# NRL WPA AND EPA CALCULATION

## Project description:


The project aims to create two key predictive models: Win Probability Added (WPA) and Expected Points Added (EPA). These metrics, commonly used in sports analytics, will be calculated for each team and player during NRL matches. WPA evaluates how individual game actions, such as scoring or conceding penalties, shift a team's probability of winning. EPA, on the other hand, measures how specific actions contribute to scoring potential, helping teams optimize high-leverage plays. 
 
This project offers real-world benefits by providing actionable insights for NRL teams. Calculating WPA/EPA helps teams to refine offensive strategies, identifying when quick ball movement leads to scoring opportunities, and allow real-time decision-making based on key game actions.EPA quantifies individual contributions to scoring, and WPA highlights critical moments that influence win probability, helping teams improve performance. These metrics offer deeper game insights for fans, enriching the viewing experience with data-driven analysis of pivotal plays. 

While WPA and EPA have been successfully applied in various sports such as American Football, a low amount of research has been conducted on expected points in the NRL. By modelling WPA and EPA for rugby league, we aim to build upon existing research and introduce a new analytical perspective to the sport. Relevant work can be found in the following sources: 

https://www.rugbyleagueeyetest.com/2022/02/07/explainer-eye-test-expected-points-etxp-for-the-nrl/  

https://www.sfu.ca/~tswartz/papers/nrl.pdf  

Additionally, a very insightful podcast on optimising rugby performance is the one below with Rugby Legend Sam Tomkins: 

https://www.youtube.com/watch?v=xt6FuKarlEc  

 

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

### 5. Modelling
Organize the data for modelling, split into training/testing sets, and use logistic regression to calculate WPA and EPA. Analyse the results to identify impactful plays. 


## Data description: 
The dataset consists of approximately 4.6 million observations (rows), with each row representing a unique event or game state during an NRL match. These events could include possessions, tackles, passes, scoring attempts, and turnovers. 

Each observation captures essential details such as the match ID, sequence ID, possession times, player actions, and physical attributes of players, among other metrics. The dataset covers every match from 2020 to 2023, ensuring a robust amount of data for building predictive models. 

 

#### Number of observations: 

Each observation (row) will represent a game state at a given moment, typically captured when an event (e.g., score change, possession switch) occurs in the match. The number of observations will depend on the number of matches and the number of events in each match. 

The data product will consist of approximately 10,000 observations, each representing a unique event from NRL matches. Each row will include time-stamped data on specific plays, capturing ball movement dynamics and player attributes during key events (e.g., score changes, possession switches). 

#### Features: 

Match ID: Identifies the specific match. 

Sequence ID: Ensures events are in chronological order. 

Team A ID / Team B ID: Identifies the competing teams. 

Win/Loss column 


#### This will also include WPA Features of: 

Score Difference: Calculated as Team A Score - Team B Score. 

Time Remaining: Total minutes remaining derived from Elapsed Minutes, Elapsed Secs, and Half. 

 

#### This will also include EPA Features of: 

Event Name: Type of event (e.g., tackle, try, pass). 

Possession Time: Total and opponent's possession time. 

Physical Coordinates: XmPhysical and YmPhysical for field position. 

Score Tracking: Current and opponent's scores. 

Elapsed Game Time: Includes Elapsed Minutes, Elapsed Seconds, and Half. 

Field Position: Normalized XmPhysical and YmPhysical based on field zones. 

Game Context: Score differential and game clock information. 


#### The Target variables of this project are the WPA and EPA. 



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
