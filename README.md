# NRL WPA AND EPA CALCULATION

## Project description:

This project aims to develop two key predictive models: Win Probability Added (WPA) and Expected Points Added (EPA). The WPA model calculates the impact of each player's actions on the team’s probability of winning, while the EPA model measures the impact of field position on the team’s likelihood of scoring.

WPA is crucial for identifying game-changing moments, such as when a player’s action significantly alters the win probability, helping coaches and teams adjust strategies during matches. The concept of Win Probability Added has been widely applied in other sports like American Football, where advanced models like the one described in Stern (1999) have led to strategic improvements by emphasizing critical moments in games. Similarly, EPA is essential for understanding scoring opportunities based on field position, which allows teams to make informed decisions on plays, such as whether to kick or run based on the likelihood of scoring (Swartz, 2022).

Although WPA and EPA models have been applied in sports like American football, rugby league remains underexplored. This project aims to build upon existing research and introduce WPA and EPA models to NRL (National Rugby League), providing insights into player performance and in-game decision-making. As discussed in Swartz and Armitage's research (2007), rugby is a dynamic sport that could benefit from advanced analytics for team management and player evaluation.

# Sources
The dataset is composed of multiple CSV files, each capturing different aspects of the game and its participants. The key data sources included:

Events.txt: Stores event reference data, listing all possible in-game events such as passes, tackles, or scores. Each event has a unique EventCode and EventName.

Matches.txt: Contains match-level data including match timings, participating clubs, final scores, and venue information, using fields like MatchId, TeamAName, TeamBName, and WeatherCondition.

Players.txt: Holds player reference data, including basic details like PlayerId, PlayerName, and physical attributes like height and weight.

These files enabled detailed analysis of player performance, team dynamics, and match outcomes. The data was processed and cleaned to extract useful features for WPA and EPA modeling.

However, a limitation of the data was that there were many missing values present. 

# Workflow: 

The dataset was first sorted by MatchId and then by SeqNumber to ensure that the sequence of events within each match was properly ordered. Only significant columns were retained, such as MatchId, SeqNumber, ClubId, OppositionId, PlayerId, and key game event details like Elapsed Time, Possession Information, Event Information, and Scoring Data. Missing values were addressed using a combination of backward fill and forward fill, with any remaining missing values set to 0.

The dataset was standardized by changing the format of certain columns from float to integer, followed by merging relevant information from auxiliary files. This included merging ClubName, OppositionName, and InPossessionClubName from Players.csv, as well as PlayerName and PlayerPositionName from the same file. Additional details like WeatherConditionName, TeamAName, and TeamBName were merged from Matches.csv. Columns were then renamed for clarity, and new features such as HomeScore, AwayScore, HomePossessionSecs, and OppPossessionSecs were created. A win column was also generated to label match outcomes.

Key events were also categorized as follows:

Scoring Events: Events that directly affect the score and impact both WPA and EPA, such as tries (TRY), penalty tries (PTRY), conversions (CVOK), penalty goals (PGOK), and field goals (FGOK).

Field Progression Events: These include actions like runs, kicks, and linebreaks, which help predict future scoring potential and affect EPA.

Possession Changes: Events like turnovers, errors, and penalties, which shift possession and influence both WPA and EPA by changing the game momentum.

Set Completions and Tackles: These represent team progress during a set, impacting field position and possession, crucial for EPA.

Defensive and Kicking Events: Missed field goals, defensive plays, and pressure-inducing kicks that influence both WPA and EPA by affecting game flow.

For Exploratory Data Analysis (EDA), univariate analysis was performed using count plots for categorical data and histograms for numerical data. Bivariate analysis involved comparing categorical and numerical data using count plots and boxplots, while multivariate analysis was conducted using heatmaps to examine relationships between numerical features.

Several feature engineering steps were taken, including creating a HomeAwayIndicator, ScoreDifference, TimeRemaining, and event-specific indicators such as TryIndicator, ConversionIndicator, PenaltyIndicator, and FieldGoalIndicator. Additional features such as ConsecutiveEvent and binned XmPhysical values were also created. To handle high cardinality, frequency encoding and target encoding were applied, and categorical features were encoded using ordinal encoding for weather conditions and OneHotEncoding for other categorical data.

For scaling and normalization, numerical features such as Points, ElapsedMins, and ElapsedSecs were scaled, while TotalPossessionSecs, XmPhysical, and YmPhysical were normalized. 

Finally, outliers were removed using the Z-score method to ensure that the dataset was prepared for modeling. Rows with events that were insignificant, because they are not directly related to points or winning, were also removed.


Using ball speed as a feature was initially appealing, however it was found that no rows where both duration secs and distance had values. 

# Data Description:

The dataset consists of approximately 200 000 observations (rows), with each row representing a unique event or game state during an NRL match. These events could include possessions, tackles, passes, scoring attempts, and turnovers.

Each observation captures essential details such as the match ID, sequence ID, possession times, player actions, and physical attributes of players, among other metrics. The dataset covers every match in 2021, ensuring a robust amount of data for building predictive models.

The dataset contains approximately 1 million rows and 100 columns, each representing an event during an NRL match (e.g., possession, tackle, pass, scoring attempt). It captures key details like Match ID, Player Actions, Possession Time, and Field Position, providing comprehensive data for building WPA and EPA models.

Key features include Field Position (target for EPA), Event Type, Score Difference, Possession Time, Elapsed Time, and Possession Status. These features are inputs for the logistic regression models, with WPA predicting win probability (binary: win/loss) and EPA predicting expected points, enabling mapping to players and field positions.

These features will serve as the input variables for the logistic regression model. The target variable for WPA will be the win probability (binary outcome: win/loss), and for EPA, it will be the expected points for each play. By using these game context features, the logistic regression model will learn how different situations and events influence the outcome, allowing the ability to map WPA values to players and EPA values to field positions.

# Usage:

A logistic regression is intended to be modelled on the data for both the WPA and EPA models. This will be used to calculate the pre-play and post-play values for both WPA and EPA, with their respective final value being the difference between them. 

Win Probability=1/(1+e^(-(β_0+β_1*X_1+β_2*X_2+⋯+β_n*X_n ) ) ) 

[image](https://github.com/user-attachments/assets/312c8af0-f360-4a82-b245-1bbc518047f7)

Expected points=  1/(1+e^(-(α_0+α_1*X_1+α_2*X_2+⋯+α_n*X_n ) ) )  

[image](https://github.com/user-attachments/assets/31ab7546-8fec-4470-af65-e44089faf112)

* where β & α represent the coefficients, and X_n represents game features

For both WPA and EPA project, key features to be used as variables in the regression include Score Difference, Possession Time, Event Type, and Remaining time. These features help the logistic regression model predict how a player’s action impacts the team’s win probability.

After logistic regression, the WPA for each event is calculated and assigned to the player responsible for the action. The average WPA for each player is then derived by taking the mean of their individual WPA contributions across multiple plays or games, providing a clear measure of how much each player contributes to the team's likelihood of winning.

A similar analysis should be done with EPA for each field position zone, allowing the ability to see how specific field position changes (for example, moving the ball from one zone to another) influenced the team’s scoring potential.

The 2021 dataset is intended to be used for training the logistic regression model, with testing on the 2020-2023 dataset. This way we ensure the model learns from a specific set of data but is robust enough to generalize well across multiple seasons, reflecting its ability to predict win probability (WPA) or expected points (EPA) over a broader range of real-world scenarios.

# Support information: 
Contact Lavan Indrajit, June Jee, and Ahmad Nasiruddin on Microsoft Teams

# Contributors: 

Who has contributed to this data product? 

Ahmad Nasiruddin, Hye Jun Jee, Lavan Indrajit.

How can others get involved?

If you are interested in contributing to the WPA and EPA analysis for NRL, You can share Your Insights, Provide Feedback, or Spread the Word: For any inquiries or to express your interest, please contact any of the team members listed above. We gratefully appreciate any support or contributions to our project

# References:

Stern, H.S. (1999). Measuring the success of the game’s big plays. Journal of the American Statistical Association, 94, 347-355.

Swartz, T. (2022). Expected points in rugby league. Rugby League Eye Test, retrieved from link.

Swartz, T.B., & Armitage, R. (2007). Analyzing rugby league with statistical models. Journal of Quantitative Analysis in Sports, 3, 19-34.

Relevant work can also be found on advanced EPA in rugby league (Swartz, 2022) and an insightful podcast featuring Rugby Legend Sam Tomkins discussing optimal performance strategies (YouTube, 2022).
