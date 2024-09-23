## NRL Analytics: Ball Speed Prediction and Team Performance Metrics

Project description:
Each round of the league and every draw on each team, NRL provides in-depth analysis on detailed breakdowns of team performances and match draws. The national game league shows its continuous efforts to evolve the sport by offering insights that enhance team strategies and fan engagement with dedication.
The NRL officials provide in-depth analysis of each round and every NRL/NRLW draw with detailed breakdowns of team performances and match outcomes. Through these comprehensive insights, the league demonstrates its commitment to evolving the sport, continually enhancing team strategies and deepening fan engagement by proving their dedication to analytic views on the sports. This project aims to address two critical objectives on the sports’ analytics:
Ball Speed Prediction: The project seeks to predict the speed at which the ball moves toward the goal during a match, using time-stamped positional data, per team. This analysis focuses primarily on the X-coordinate (horizontal movement) to measure the progression of the ball toward the opponent's goal. This data can be used to assess the pace of play and identify key moments where quick ball movement increases scoring opportunities.
New Team Prediction: Additionally this project plans to incorporate the average ball speed of the team and the data on physical characteristics (height, weight, and the age) of the players in each team. In other words, it uses the average figure from the overall players’ physical data of a team to predict a new, upcoming team’s ball speed. 
WPA and EPA Calculation: Another goal of this project is to develop a predictive model that calculates Win Probability Added (WPA) for each team and Expected Points Added (EPA)  for each player in a team during a game. By evaluating key game actions and their impact on the outcome, the model will provide a context-sensitive metric to help assess how each play affects the team's likelihood of winning or scoring.
Significance :
Game Strategy Insights: Understanding the speed of ball movement toward the goal helps coaches and analysts identify moments of rapid offensive play and its impact on scoring chances. 

Use of A Relatively Stable Metric: WPA and EPA are crucial metrics for sports analysts, coaches, and strategists to make informed decisions during a match. WPA helps quantify how individual actions, like scoring, penalties, or infringements, shift the win probability based on the game context. EPA predicts the potential scoring impact of a given play, helping teams optimize their strategies during high-leverage moments.

The importance of kicking analysis on NRL by its nature is, as the article from the link below states, “ In baseball, results-based analysis generally tends to even out over the course of a 600 at-bat season, but NFL kickers only get 30–40 field goal attempts per year.” which implies that the analysis on kicking on NFL or NRL is relatively stable metric form this small-sample sport. 
Ball-Tracking Data and the Anatomy of a Field Goal, Martin K: 
https://medium.com/@matan_k/ball-tracking-data-and-the-anatomy-of-a-field-goal-0c646073fbe8

Previous Work:
WPA and EPA: 
WPA and EPA are both a very interesting analysis that is widely used in multiple sports such as xG in Football or even WPA and EPA in American Football. Although some similar analysis has been done, it is still not widely used in the NRL. Therefore, we are focusing on modeling both WPA and EPA in each NRL game from 2020-2023 to show the significance of the analysis for the NRL, teams, players and also the viewers. 

Some previous works that are related with WPA and EPA are in these links:
https://www.rugbyleagueeyetest.com/2022/02/07/explainer-eye-test-expected-points-etxp-for-the-nrl/ 
https://www.sfu.ca/~tswartz/papers/nrl.pdf 

Sources:

The primary source of data is the official 2020-2023 NRL database. This database includes comprehensive information on matches, players, teams, events, and venues. The data includes:

Event data: A detailed collection of events from each game (Start of game/half, Play The Ball, Ruck Infringement, Try, etc) 
Match data: Results, Date, scores, teams, officials, weather, and venue information. Player data:Name, DOB, Position, Club, and Physical Attribute.

Workflow: 
WPA and EPA:

Data Collection: The event, match and player data will be extracted from the official NRL 2020-2023 database.
Data Cleaning: Handling null data, standardizing data formats, and handling outliers.
Feature Engineering: Create new features such as Field Position, Field Position, Game Clock, Score Differential, and Possession, and calculate WPA and EPA using the formulas:

WPA=Post-play Win Probability−Pre-play Win Probability
EPA=Expected Points After Event−Expected Points Before Event

Data Validation: Perform exploratory data analysis (EDA) which are univariate analysis using histogram and box plot, bivariate analysis using barplot, pairplot and scatterplot, and multivariate analysis using heatmap. Also, perform normalization of the columns, log transformations/box cox transformation for skewed data and Kalman Filter for Time Series Data
Final Data Structure: Organize the data into a final dataframe that includes all relevant metrics for further modeling.

For each match, assign 1 for win and 0 for loss, and create snapshots of the game state for chosen significant events (tries, ruck infringements, tackles etc.). Then split the dataset into training and testing data, and train a model (logistic regression) using the training set. Evaluate the model’s performance, and use the trained model to calculate the pre-play and post-play win probabilities for each significant event; this is used to calculate the WPA:

WPA=Post-play Win Probability−Pre-play Win Probability

Analyze this to determine the most impactful plays using WPA.


Data description: 
The data modeling team will work on WPA and EPA rows,  utilizing these datatest to build and refine models for calculating WPA and EPA by referring to their features(rows). From datasets of 2020 to 2023 matches with event data, player metrics will help the process.
WPA rows:
Each observation (row) will represent a game state at a given moment, typically captured when an event (e.g., score change, possession switch) occurs in the match. Number of observations will depend on the number of matches and the number of events in each match.
EPA rows:
The final dataset will contain approximately 4600000 observations, each representing a unique match event for every match from 2020 to 2023.
Each observation will represent a player’s action within a specific match (e.g., tackle, pass, try).
WPA Features:
Key features (column) 
Match ID - to ensure they are in the same match 
Sequence ID - to ensure that events are in time order 
Team A ID 
Team B ID 
Points - ensure that the points are not blank 
Possession Secs - total duration which a team has possessed a ball 
Xm possession - the horizontal location of where a team starts possessing of the ball 
 
Feature engineering: 	
Create a win/loss column 
Create a speed column by calculating xm possession divided by the possession secs 
One hot encoding for categorical data, club ID 
Create avg height, weight, and age of each players 
Create a physical appearance column, a sum of height and weight 
Previous wins (how many matches have they won in the last 10 games?) 
How many games were away, at home?  
 
WPA: 
Create Derived Variables: 
Score difference: Calculate ScoreDifference = TeamAScore - TeamBScore 
Time remaining: Combine ElapsedMins, ElapsedSecs, and Half to derive total minutes remaining. 


EPA Features:
EventName: This identifies what type of play or event occurred (e.g., tackle, try, pass).
PossessionSecs and OppPossessionSecs: These represent the possession time, which can help in estimating the impact of possession on scoring.
XmPhysical, YmPhysical: These represent the physical coordinates on the field, which help in calculating field position.
Points: The points associated with the event, used to update the team's score.
Score and OppScore: Track the current score during the match.
ElapsedMins and ElapsedSecs: Game time is essential to account for game context (early vs. late plays).
Half, Set, Tackle: These add more context about the stage of the game.
Field Position: Normalize XmPhysical and YmPhysical (e.g., map field zones, divide into bins such as 0-20m, 20-50m, etc.).
Possession Information: Use PossessionSecs, OppPossessionSecs, Set, Tackle.
Game Clock: Include ElapsedMins, ElapsedSecs, and Half to capture game progression.
Score Differential: Use Score - OppScore to include the current score difference.


Project status:
Weekly tasks.csv
Modeling Team: refining the data and calculating WPA/EPA following guidelines.
Usage: 


Contributors: 
Ahmad Nasiruddin (Data Scientist)
Belinda Wang (Data Scientist)
Hye Jun Jee (Data Scientist) 
Lavan Indrajit (Data Scientist)



