# Project Title: ------

# Project description:

Objective:

These are some of the proposed objectives:
1. Based on the overall team position(location) when the ruck infringement(penalty) happened, could we identify the stronger/weaker team?
2. Determine the players best position based on their BMI (weight and height), ball speed they create, and if they score a point
3. Predict total infringement in a game for a team and what are the main factors influencing it?

<!-- The objective of this project is to develop a data product that captures detailed match and player-level data from the NRL Women's Elite competition, suitable for use in predictive modeling and statistical analysis. The data will be organized into a structured dataframe ready for use by analysts, researchers, and other interested parties for tasks such as performance evaluation, player comparison, and match outcome prediction. -->

Significance:

<!-- This data product is significant as it provides detailed insights into player performance and match events that can be used to inform decision-making within professional rugby league. By creating a comprehensive dataset, stakeholders such as coaches, analysts, and sports scientists can better understand key aspects of game dynamics, player contributions, and team strategies. This will enhance the predictive modeling capabilities within the sport. -->

Previous Work:

<!-- This data product builds on previous research into rugby league performance analysis, which has traditionally focused on male competitions. There is a growing interest in developing analytical models for women's sports, where data availability has been limited. Our project will expand the data landscape for the NRL Women's Elite competition by incorporating match events, player positions, physical attributes, and possession metrics. -->

# Sources: 

The primary source of data is the 2020-2023 NRL database. This database includes comprehensive information on matches, players, teams, events, and venues. The data includes:

Event data: A detailed collection of events from each game (Start of game/half, Play The Ball, Ruck Infringement, Try, etc)
Match data: Results, Date, scores, teams, officials, weather, and venue information.
Player data:Name, DOB, Position, Club, and Physical Attribute.

Workflow:

1. Data Extraction: The event, match and player data will be extracted from the NRL 2020-2023 database
2. Data Cleaning: 
<!-- Data will be cleaned to ensure consistency across variables (e.g., ensuring player names are standardized, filling missing data, handling outliers). -->
3. Feature Engineering: 
<!-- We will create new variables based on the locational and event data. This might include distance covered, average possession time, scoring zones, etc. -->
4. Data Validation: 
<!-- Perform exploratory data analysis (EDA) and use visualizations to confirm the accuracy and completeness of the data. -->
5. Final Product: 
<!-- The final product will be a well-structured dataframe with clear and concise documentation for users. -->

Data description: 

how many observations (rows) there will be and what they represent
its features (columns), what they represent, how they will be constructed

<!-- Number of Observations:
The final dataset will contain approximately 1,000 to 5,000 observations, each representing a unique match event.
Each observation will represent a player’s action within a specific match (e.g., tackle, pass, try).
Features:
The dataframe will include the following columns:
MatchId: Unique identifier for the match.
PlayerId: Unique identifier for the player.
EventCode: Code representing the type of event (e.g., tackle, pass, try).
XmPhysical: X-coordinate of the event on the field.
YmPhysical: Y-coordinate of the event on the field.
ZonePhysical: Field zone where the event occurred.
PossessionSecs: Time of possession for the team.
PlayerPositionName: Player's position in the match (e.g., Fullback, Wing).
PlayerHeightCms: Player’s height in centimeters.
PlayerWeightKgs: Player’s weight in kilograms.
MatchOutcome: Outcome of the match (win/loss/draw).
VenueName: Name of the venue where the match took place.
WeatherCondition: Weather conditions during the match.
These features will be selected to ensure that the dataframe is informative for various types of analyses, including predictive models and player comparisons. -->

# Project status:

Progress:

Data extraction from the database has been completed.
<!-- Data cleaning is in progress, including resolving missing values and ensuring consistency in naming conventions.
Feature engineering is currently underway to derive meaningful metrics from the raw event data. -->

Remaining Tasks:

<!-- Finalize data cleaning and feature engineering by Week 3.
Construct the dataframe by Week 4, ensuring all necessary transformations and calculations are complete.
Test the dataframe by running simple analyses to validate its structure and usefulness for predictive models.
Submit the final product and README by Week 5. -->

<!-- what progress has been made towards developing this product? 
what more needs to be done (and by who) to get this completed on time?  -->

# Usage: 

how do you intend that this product be used (e.g. describe a simple analysis model)

# Support information: 

who should be contacted if a user needs help?

# Contributors: 

Ahmad Nasiruddin (Data Scientist)
Role: 
Belinda Wang (Data Scientist)
Role: 
Hye Jun Jee (Data Scientist)
Role: 
Lavan Indrajit (Data Scientist)
Role:

How to Get Involved:
Other researchers or analysts interested in contributing to this data product or providing feedback can reach out via the contact details provided.