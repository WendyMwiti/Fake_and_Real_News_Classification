import streamlit as st
import joblib, os
import pandas as pd
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

stopwords = nltk.corpus.stopwords.words('english')
lemma = WordNetLemmatizer()
stopwords = set(stopwords)


def load_model():
        """Loads the model from the disk"""
        model = joblib.load(open(os.path.join("./models/model.pkl"), "rb"))
        return model
    
def clean_text(text):
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [lemma.lemmatize(word) for word in tokens if word not in stopwords]
    return text

def main():
    
    """News Classifier App with Streamlit """
    st.title("📰 Fake and Real News Classifier")
    st.subheader("This app classifies whether the news is fake or real")

    news_text = st.text_area("Enter the news text here:")
    
    news_text = pd.Series(news_text)

    if st.button("Classify"):
        st.text("Classiying...")
            
        model = load_model()
        model.predict(news_text)
            
        if model.predict(news_text) == 0:
            st.error("Fake News")
        else:
            st.success("Real News")

if __name__ == '__main__':
    main()