# NRL WPA AND EPA CALCULATION

## Project description:

This project aims to develop two key predictive models: Win Probability Added (WPA) and Expected Points Added (EPA). The WPA model calculates the impact of each player's actions on the team’s probability of winning, while the EPA model measures the impact of field position on the team’s likelihood of scoring.

WPA is crucial for identifying game-changing moments, such as when a player’s action significantly alters the win probability, helping coaches and teams adjust strategies during matches. The concept of Win Probability Added has been widely applied in other sports like American Football, where advanced models like the one described in Stern (1999) have led to strategic improvements by emphasizing critical moments in games. Similarly, EPA is essential for understanding scoring opportunities based on field position, which allows teams to make informed decisions on plays, such as whether to kick or run based on the likelihood of scoring (Swartz, 2022).

Although WPA and EPA models have been applied in sports like American football, rugby league remains underexplored. This project aims to build upon existing research and introduce WPA and EPA models to NRL (National Rugby League), providing insights into player performance and in-game decision-making. As discussed in Swartz and Armitage's research (2007), rugby is a dynamic sport that could benefit from advanced analytics for team management and player evaluation.

Workflow: 

Null handling: removing the rows of data with null values Standardizing data format Removing outliers
The feature engineering done including the addition of the following columns: HomeAway Indicator, Score Difference, Time Remaining, Possession Indicator, FieldGoalIndicator, ConversionIndicator.

Data Description:

The dataset consists of approximately 2 million observations (rows), with each row representing a unique event or game state during an NRL match. These events could include possessions, tackles, passes, scoring attempts, and turnovers.

Each observation captures essential details such as the match ID, sequence ID, possession times, player actions, and physical attributes of players, among other metrics. The dataset covers every match in 2021, ensuring a robust amount of data for building predictive models.

Number of observations:
Each observation (row) will represent a game state at a given moment, typically captured when an event (e.g., score change, possession switch) occurs in the match. The number of observations will depend on the number of matches and the number of events in each match.
The data product will consist of approximately 10,000 observations, each representing a unique event from NRL matches. Each row will include time-stamped data on specific plays, capturing ball movement dynamics and player attributes during key events (e.g., score changes, possession switches).

Key Features:

- Field Position: Represents where the play occurred on the field. In the EPA model, field position is the key target variable used to calculate expected points changes. For WPA, it helps assess how different locations influence win probability.

- Event Type: The type of play (e.g., pass, tackle, try). In both models, event type determines the impact of an action on either expected points or win probability. Scoring plays like tries will increase these values, while turnovers will likely decrease them.

- Score Difference: The current score gap between teams. For WPA, it contextualizes the importance of a play, especially late in the game. In EPA, it helps assess how game dynamics might influence scoring potential.

- Possession Time: Measures how long the team has controlled the ball before the event. Longer possession is usually linked to higher scoring chances and affects both WPA and EPA predictions.

- Elapsed Time: Reflects the time remaining in the game. Late-game events have a greater influence on WPA, while in EPA, it helps predict scoring chances during different phases of the match.

- Possession Status: Whether the team has possession during the play, which is crucial for both EPA (scoring potential) and WPA (winning potential).

These features will serve as the input variables for the logistic regression model. The target variable for WPA will be the win probability (binary outcome: win/loss), and for EPA, it will be the expected points for each play. By using these game context features, the logistic regression model will learn how different situations and events influence the outcome, allowing the ability to map WPA values to players and EPA values to field positions.

Usage:

A logistic regression is intended to be modelled on the data for both the WPA and EPA models. This will be used to calculate the pre-play and post-play values for both WPA and EPA, with their respective final value being the difference between them. 

Win Probability=1/(1+e^(-(β_0+β_1*X_1+β_2*X_2+⋯+β_n*X_n ) ) ) 

[image](https://github.com/user-attachments/assets/312c8af0-f360-4a82-b245-1bbc518047f7)

Expected points=  1/(1+e^(-(α_0+α_1*X_1+α_2*X_2+⋯+α_n*X_n ) ) )  

[image](https://github.com/user-attachments/assets/31ab7546-8fec-4470-af65-e44089faf112)



For both WPA and EPA project, key features to be used as variables in the regression include Score Difference, Possession Time, Event Type, and Remaining time. These features help the logistic regression model predict how a player’s action impacts the team’s win probability.

After logistic regression, the WPA for each event is calculated and assigned to the player responsible for the action. The average WPA for each player is then derived by taking the mean of their individual WPA contributions across multiple plays or games, providing a clear measure of how much each player contributes to the team's likelihood of winning.

A similar analysis should be done with EPA for each field position zone, allowing the ability to see how specific field position changes (for example, moving the ball from one zone to another) influenced the team’s scoring potential.

The 2021 dataset is intended to be used for training the logistic regression model, with testing on the 2020-2023 dataset. This way we ensure the model learns from a specific set of data but is robust enough to generalize well across multiple seasons, reflecting its ability to predict win probability (WPA) or expected points (EPA) over a broader range of real-world scenarios.

Support information: 

Contributors: 

Who has contributed to this data product? 

Ahmad Nasiruddin, Hye Jun Jee, Lavan Indrajit.

How can others get involved?

If you are interested in contributing to the WPA and EPA analysis for NRL, You can share Your Insights, Provide Feedback, or Spread the Word: For any inquiries or to express your interest, please contact any of the team members listed above. We gratefully appreciate any support or contributions to our project

References:

Stern, H.S. (1999). Measuring the success of the game’s big plays. Journal of the American Statistical Association, 94, 347-355.

Swartz, T. (2022). Expected points in rugby league. Rugby League Eye Test, retrieved from link.

Swartz, T.B., & Armitage, R. (2007). Analyzing rugby league with statistical models. Journal of Quantitative Analysis in Sports, 3, 19-34.

Relevant work can also be found on advanced EPA in rugby league (Swartz, 2022) and an insightful podcast featuring Rugby Legend Sam Tomkins discussing optimal performance strategies (YouTube, 2022).
