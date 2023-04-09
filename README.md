# BSc-Final-Year-Research
## Can Twitter Data Add Value to Historical Data?: A Comparative Study for T20I Cricket Match Outcome  Prediction Using Machine Learning

### Objectives of the study
The study's main objective is to build a suitable model using machine learning to predict 
the winner of the Twenty20 International cricket matches before the match starts by 
considering historical data, and features derived from Twitter.
The secondary objectives of the study are as follows:

• To build a more reliable and efficient model in order to identify the sentiment of 
pre-match tweets, whether the tweet is positive or negative

• To study whether Twitter-derived features can provide useful information on top of 
historical data to predict the match outcome

• To check whether there is any profit to be gained from pre-match betting using the 
proposed model

### Data Collection
The datasets were created by considering 519 games played between the top 9 teams (as of 
October 14, 2022) from the 1st of January 2011 to the 14th of October 2022. 
Three main datasets were built. 
1) Historical dataset (contained historical data related to 
past matches)
2) Twitter dataset (features extracted from the collected 
tweets)
3) Historical+Twitter dataset (a combination of both the first two datasets) 

Additionally, data from the ICC T20 World Cup 2022, which took place in Australia 
from the 16th of October to the 13th of November, as well as pre-match betting odds for 
those matches, were collected with the aim of evaluating the effectiveness of the proposed 
methodology.

####  Historical dataset
The historical match data were obtained from Statsguru 
(https://stats.espncricinfo.com/ci/engine/stats/index.html) using the Pandas package ( read_html() function) because 
Statsguru provides data in tabular format. The final "Historical" dataset contained 519 observations and 16 variables.

#### Twitter dataset
There were two primary phases in the process of creating this dataset. Tweets were 
scraped in the first phase, and then features were extracted from those scraped tweets in the 
second phase. The Snscrape library was used to scrape the tweets. Those 
tweets were converted to lowercase, and duplicates were removed. With the use of regular expression 
patterns tweets that raise a question were removed and tweets with multiple hashtags and handles were classified according to the first hashtag or first handle. 

Then, using these scraped tweets, the following important information was extracted as the 
second phase of generating the “Twitter" dataset:

• Total number of tweets of a team for a match

• Count of positive tweets of a team for a match

• Count of tweets with the pattern “Team j win” or “Team j will win” of a team for a 
match

Here, Team j represents the team names or the shortened names of each team. Running each file to obtain values for these variables was a difficult task. Therefore, using Streamlit, a web application was developed to automate that process. 
The final "Twitter" dataset contained 519 observations and 7 variables.

#### Historical+Twitter dataset
The variables in this dataset are a combination of 
variables from the previous two datasets. Therefore, the "Historical+Twitter" dataset 
contained 519 observations and 22 variables.

Each instance of the three datasets represented a match, and the instance was mainly 
split into three parts: Team1 features, Team2 features, and the target variable. Here, Team 1 is the team that has the highest win/loss ratio for past matches 
of the two teams in each match. Team 2 is the team that has the lowest win-loss ratio.


 
