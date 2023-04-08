import pytorch_pretrained_bert as ppb
assert 'bert-large-cased' in ppb.modeling.PRETRAINED_MODEL_ARCHIVE_MAP
import pandas as pd
import streamlit as st
from transformers import pipeline
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig

st.header('Cric-Tweets')
sentiment_model = pipeline(model="sppm/cric-tweets-sentiment-analysis")
with st.expander('Analyze Tweet'):
    text = st.text_input('Tweet here: ')
    if text:
        senti = list(sentiment_model(text)[0].values())[0]
        if senti=='LABEL_1':
            label = senti.replace(senti, 'Positive')
        elif senti=='LABEL_0':
            label = senti.replace(senti, 'Negative')
        st.write('Label: ', label)
with st.expander('Analyze CSV'):
    upl = st.file_uploader('Upload file: ')
    if upl:
        df = pd.read_csv(upl, encoding='latin1')
        del df['Unnamed: 0']
        b=[]
        for i in range(len(df)):
            b.append(list(sentiment_model(df['Tweet'][i])[0].values())[0])
        df['Sentiment'] = b
        # Convert label1/label2 string columns into int columns of 1/0
        df[['Sentiment']] = \
        (df[['Sentiment']] == 'LABEL_1').astype(int)
        st.write(df.head())
        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')
        csv = convert_df(df)
        st.download_button(
            label="Download",
            data=csv,
            file_name= upl.name,
            mime='text/csv',
        )

        team = upl.name.split('-')[0]
        if team == 'AUS':
            words = ['Australia will win', 'Australia win' ,'Aus win', 'Aus will win']
        elif team == 'BAN':
            words = ['Bangladesh will win', 'Bangladesh win' ,'Ban win', 
                     'Ban will win']
        elif team == 'ENG':
            words = ['England will win', 'England win' ,'Eng win', 'Eng will win']
        elif team == 'IND':
            words = ['India will win', 'India win' ,'Ind win', 'Ind will win']
        elif team == 'NZ':
            words = ['New Zealand will win', 'New Zealand win' ,'NZ win', 'NZ will win']
        elif team == 'PAK':
            words = ['Pakistan will win', 'Pakistan win' ,'Pak win', 'Pak will win']
        elif team == 'SA':
            words = ['South Africa will win', 'South Africa win' ,'SA win', 'SA will win',
                     'RSA win', 'RSA will win']
        elif team == 'SL':
            words = ['Sri Lanka will win', 'Sri Lanka win' ,'SL win', 'SL will win']
        elif team == 'WI':
            words = ['West Indies will win', 'West Indies win' ,'WI win', 'WI will win']

        df['Tweet'] = df['Tweet'].str.lower()
        sentence = df['Tweet'].tolist()
        words = [word.lower() for word in words]

        res = [any([k in s for k in words]) for s in sentence]
        output =  [sentence[i] for i in range(0, len(res)) if res[i]]  

        st.write('Winner prediction count: ', len(output)) 
        st.write('Number of Positive Tweets: ', df.Sentiment.sum())
        st.write('Total Number of Tweets: ',  len(df)) 

        