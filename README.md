# Undergraduate-Final-Year-Research
### Can Twitter Data Add Value to Historical Data?: A Comparative Study for T20I Cricket Match Outcome  Prediction Using Machine Learning

Due to the dynamic nature of the game and the numerous variables that might affect the 
outcome, predicting the result of a cricket match before it begins can be a very difficult 
task. Each match leaves thousands of data points, but real-time information cannot be 
produced utilizing that data. Social media platforms like Twitter have proven their capacity 
to produce real-time information in many fields. In this study, a machine learning-based 
method for predicting the result of the match before it starts by considering historical data 
and Twitter data is proposed. From 2011-01-01 to 2022-10-14, historical data such as 
batting and bowling statistics, and Tweets related to matches were scraped, and useful 
features were derived from those data. Sentiment score is one of the variables that needed 
to be created from tweets. For that, identifying tweets' sentiments was needed, and to 
achieve that, sentiment analysis was carried out as a part of this study. The fine-tuned 
RoBERTa-based model outperformed with a 95.3% F1 score the models created using 
LSTM and VADER. Using those created variables, three datasets were formulated: one 
with only historical data, another with only Twitter data, and a third with both types of data. 
Running each file to obtain values for the variables of Twitter dataset was a difficult task. Therefore, using 
Streamlit, a web application was developed to automate that process. This web application's 
primary goal was to determine a tweet's sentiment. However, this application was expanded 
to obtain the values for each basic Twitter variable for each team for a specific match.
Then several machine-learning algorithms (i.e., Logistic Regression, SVM, Naive Bayes, 
KNN, Random Forest, and XGBoost) were trained and evaluated on these datasets. The 
best models were produced by the XGBoost classifier for all three datasets, and it was 
noticed that removing correlated and least important variables improved the models’ 
performances. The findings suggested that features derived from Twitter can be quite useful 
for making predictions. The models generated using only Twitter data performed better 
than the models built using historical data, and the models created using both historical and 
Twitter data exceeded the performances of both of the individual data models with a 73.7% 
F1 score. This best model performed better than the bookmakers’ predictions with a profit 
for the T20I World Cup 2022 data by accurately predicting 11 matches out of 14, while the 
bookmakers predicted only 9 matches correctly.
