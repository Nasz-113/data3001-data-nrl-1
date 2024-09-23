DRAFT ReadMe File


Project description:

This project focuses on analysing two key predictive models: Win Probability Added (WPA) and Expected Points Added (EPA). These metrics, commonly used in sports analytics, will be calculated for each team and player during NRL matches. WPA evaluates how individual game actions, such as scoring or conceding penalties, shift a team's probability of winning. EPA, on the other hand, measures how specific actions contribute to scoring potential, helping teams optimize high-leverage plays. 

Significance:

This project offers real-world benefits by providing actionable insights for NRL teams. Understanding the effect of events and calculating WPA/EPA helps teams to refine offensive strategies, identifying what tends to lead to scoring opportunities, and allow real-time decision-making based on key game actions.

EPA quantifies individual contributions to scoring, and WPA highlights critical moments that influence win probability, helping teams improve performance. These metrics offer deeper game insights for fans, enriching the viewing experience with data-driven analysis of pivotal plays.

Relevance to Previous Work:

While WPA and EPA have been successfully applied in various sports such as American Football, a low amount of research has been conducted on expected points in the NRL. By modelling WPA and EPA for rugby league, we aim to build upon existing research and introduce a new analytical perspective to the sport. Relevant work can be found in the following sources:
https://www.rugbyleagueeyetest.com/2022/02/07/explainer-eye-test-expected-points-etxp-for-the-nrl/ 
https://www.sfu.ca/~tswartz/papers/nrl.pdf 

Additionally, a very insightful podcast on optimising rugby performance is the one below with Rugby Legend Sam Tomkins:
https://www.youtube.com/watch?v=xt6FuKarlEc 

Sources:

The primary source of data is the official 2020-2023 NRL database. This database includes comprehensive information on matches, players, teams, events, and venues. The data includes:
-	Event data: A detailed collection of events from each game (Start of game/half, Ruck Infringement, Try, etc) 
-	Match data: Results, Date, scores, teams, officials, weather, and venue information. Player data: Name, DOB, Position, Club, and Physical Attribute.

Workflow: Briefly outline the steps you plan to take to process the data

WPA and EPA:
1.	Data Collection: Extract event, match, and player data from the NRL 2020-2023 database.
2.	Data Cleaning: Handle missing data, standardize formats, and remove outliers.
3.	Feature Engineering: Create features like field position, game clock, score differential, and possession. Use the formulas:
-	WPA = Post-play Win Probability − Pre-play Win Probability
-	EPA = Expected Points After Event − Expected Points Before Event
4.	Data Validation: Perform exploratory analysis (EDA) and apply transformations (normalization, log transformations, Kalman filters).
5.	Modelling: Organize the data for modelling, split into training/testing sets, and use logistic regression to calculate WPA and EPA. Analyse the results to identify impactful plays.

Data description: 

The dataset consists of approximately 4.6 million observations (rows), with each row representing a unique event or game state during an NRL match. These events could include possessions, tackles, passes, scoring attempts, and turnovers.

Each observation captures essential details such as the match ID, sequence ID, possession times, player actions, and physical attributes of players, among other metrics. The dataset covers every match from 2020 to 2023, ensuring a robust amount of data for building predictive models.

Rows:

Each observation (row) will represent a game state at a given moment, typically captured when an event (e.g., score change, possession switch) occurs in the match. The number of observations will depend on the number of matches and the number of events in each match.
Guidance:
1.	Feature Selection:
-	Focus on key features like possession time, score differential, field position, points, and game clock. These variables are critical for predicting WPA and EPA.
2.	Feature Engineering:
-	Create new variables such as score difference, elapsed time, and ball speed (from X-coordinate movement and possession time). These will help model ball movement and event impact.
3.	Normalization and Scaling:
-	Normalize continuous variables (e.g., possession time, player attributes) and apply transformations (e.g., log transformations) for skewed data. Use Kalman filters for smoothing time-series data.
4.	Data Splitting:
-	Split data into training and testing sets by season, using earlier seasons (2020-2022) for training and the latest season (2023) for testing. Maintain event sequence integrity for accurate modelling.
5.	WPA Modelling:
-	Use pre-play and post-play probabilities to calculate WPA, focusing on features related to possession, score difference, and game context.
6.	EPA Modelling:
-	Predict EPA by evaluating features such as field position, player actions, and possession metrics, considering the timing and context of each event.
7.	Physical Attributes & Ball Speed:
-	Use average player physical attributes (height, weight, age) to model team ball speed. Correlate these metrics with ball movement to predict the speed of new teams.
Project status:
Weekly tasks.csv 
Modeling Team: refining the data and calculating WPA/EPA following guidelines. 
The data product is currently in the earliest stages of development. The team is coordinating this development in an efficient way to ensure its completion by week 5.

Usage: 

The product will be used by NRL teams and analysts to optimize in-game strategies, evaluate player performance, and identify key plays using WPA/EPA metrics. This will support real-time decision-making, post-match analysis, and player selection.

Support information: 
Please contact anyone from our team if one needs help. 

Contributors: 
Ahmad Nasiruddin (Data Scientist) Belinda Wang (Data Scientist) Hye Jun Jee (Data Scientist) Lavan Indrajit (Data Scientist). Others can get involved by utilizing the above descriptions too. 

