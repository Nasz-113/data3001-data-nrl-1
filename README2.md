# NRL WPA AND EPA CALCULATION

## Project description:

The project aims to create two key predictive models: Win Probability Added (WPA) and Expected Points Added (EPA). The WPA model aims to calculate the impact of each player on the team’s probability of winning, whilst the EPA model aims to calculate the impact of field position on the team’s likelihood of scoring. 
WPA evaluates how individual game actions, such as scoring or conceding penalties, shift a team's probability of winning. EPA, on the other hand, measures how specific actions contribute to scoring potential, helping teams optimize high-leverage plays.

The EPA (Expected Points Added) model is important because it quantifies the value of field position in terms of scoring opportunities. By understanding how each field position affects the likelihood of scoring, teams can make more informed, data-driven decisions about play-calling, whether to kick, run, or pass. EPA also allows teams to evaluate the effectiveness of offensive and defensive plays, providing valuable insights into the overall efficiency of their strategy.

The WPA (Win Probability Added) model helps to identify game-changing moments, where a player's actions significantly alter the course of the game, and assists in making strategic adjustments based on these insights. It also aids in identifying high-impact players, supporting better player development and team management decisions.

While WPA and EPA have been successfully applied in various sports such as American Football, a low amount of research has been conducted on expected points in the NRL. By modelling WPA and EPA for rugby league, we aim to build upon existing research and introduce a new analytical perspective to the sport. 

Relevant work can be found in the following sources:
https://www.rugbyleagueeyetest.com/2022/02/07/explainer-eye-test-expected-points-etxp-for-the-nrl/ 

https://www.sfu.ca/~tswartz/papers/nrl.pdf 

Additionally, a very insightful podcast on optimising rugby performance is the one below with Rugby Legend Sam Tomkins:
https://www.youtube.com/watch?v=xt6FuKarlEc 

Workflow: 

Null handling: removing the rows of data with null values Standardizing data format Removing outliers
The feature engineering done including the addition of the following columns: HomeAway Indicator, Score Difference, Time Remaining, Possession Indicator, FieldGoalIndicator, ConversionIndicator.

Data Description:
The dataset consists of approximately 4.6 million observations (rows), with each row representing a unique event or game state during an NRL match. These events could include possessions, tackles, passes, scoring attempts, and turnovers.

Each observation captures essential details such as the match ID, sequence ID, possession times, player actions, and physical attributes of players, among other metrics. The dataset covers every match in 2021, ensuring a robust amount of data for building predictive models.

Number of observations:
Each observation (row) will represent a game state at a given moment, typically captured when an event (e.g., score change, possession switch) occurs in the match. The number of observations will depend on the number of matches and the number of events in each match.
The data product will consist of approximately 10,000 observations, each representing a unique event from NRL matches. Each row will include time-stamped data on specific plays, capturing ball movement dynamics and player attributes during key events (e.g., score changes, possession switches).

Features:

Match ID: Identifies the specific match.

Sequence ID: Ensures events are in chronological order.

Team A ID / Team B ID: Identifies the competing teams.

Win/Loss column

Event Name: Type of event (e.g., tackle, try, pass).

Possession Time: Total and opponent's possession time.

Physical Coordinates: XmPhysical and YmPhysical for field position.

Score Tracking: Current and opponent's scores.

Elapsed Game Time: Includes Elapsed Minutes, Elapsed Seconds, and Half.

Field Position: Normalized XmPhysical and YmPhysical based on field zones.

Game Context: Score differential and game clock information

Usage:

A logistic regression is intended to be modelled on the data for both the WPA and EPA models. This will be used to calculate the pre-play and post-play values for both WPA and EPA, with their respective final value being the difference between them. 

For both WPA and EPA project, key features to be used as variables in the regression include Score Difference, Possession Time, Event Type, and Remaining time. These features help the logistic regression model predict how a player’s action impacts the team’s win probability.

After logistic regression, the WPA for each event is calculated and assigned to the player responsible for the action. The average WPA for each player is then derived by taking the mean of their individual WPA contributions across multiple plays or games, providing a clear measure of how much each player contributes to the team's likelihood of winning.

A similar analysis should be done with EPA for each field position zone, allowing us to see how specific field position changes (for example, moving the ball from one zone to another) influenced the team’s scoring potential.

The 2021 dataset is intended to be used for training the logistic regression model, with testing on the 2020-2023 dataset. This way we ensure the model learns from a specific set of data but is robust enough to generalize well across multiple seasons, reflecting its ability to predict win probability (WPA) or expected points (EPA) over a broader range of real-world scenarios.

Support information: 

Contributors: 

Who has contributed to this data product? 

Ahmad Nasiruddin, Hye Jun Jee, Lavan Indrajit.

How can others get involved?

If you are interested in contributing to the WPA and EPA analysis for NRL, You can share Your Insights, Provide Feedback, or Spread the Word: For any inquiries or to express your interest, please contact any of the team members listed above. We gratefully appreciate any support or contributions to our project
