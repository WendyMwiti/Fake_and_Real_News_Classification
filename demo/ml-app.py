import streamlit as st
import joblib, os
import re
from nltk.stem import WordNetLemmatizer
import nltk
import unidecode
from word2number import w2n
import contractions


def load_model():
        """Loads the model from the disk"""
        model = joblib.load(open(os.path.join("./models/model.pkl"), "rb"))
        return model
    
    
def remove_web_tags(text):
    """Remove html tags from a string"""
    # Remove https links
    clean = re.compile(r'https\S*')
    text = re.sub(clean, '', text)

    # Remove data '.com' links
    clean = re.compile(r'\S+\.com\S+')
    return re.sub(clean, '', text)


# Function to remove twitter handles
def remove_twitter_handles(text):
    """This function removes twitter handles from a string"""
    clean = re.compile(r'@\S*')
    return re.sub(clean, '', text)


# Function to convert Non-ASCII characters to ASCII
def remove_accented_chars(text):
    """This function removes accented characters from text, e.g. café"""
    text = unidecode.unidecode(text)
    return text


# Function to expand contractions
def expand_contractions(text):
    """Expand shortened words, e.g. don't to do not"""
    text = contractions.fix(text)
    return text


# Function to remove special characters
def remove_special_characters(text):
    """This function removes special characters from text, e.g. $"""
    clean = re.compile(r'[^a-zA-Z0-9\s]')
    return re.sub(clean, ' ', text)


# Function to lowercase text
def lowercase_text(text):
    """This function converts characters to lowercase"""
    return text.lower()


# Function to convert number words to digits
def convert_number_words(text):
    """Convert number words to digits and remove them"""
    
    pattern = r'(\W+)'
    tokens = re.split(pattern, text)

    for i, token in enumerate(tokens):
        try:
            tokens[i] = str(w2n.word_to_num(token))
        except:
            pass
    
    return ''.join(tokens)


# Function to remove numbers
def remove_numbers(text):
    """This function removes numbers from text"""
    clean = re.compile(r'\d+')
    return re.sub(clean, '', text)


# Function to remove short words
def remove_small_words(text):
    """This function removes words with length 1 or 2"""
    clean = re.compile(r'\b\w{1,2}\b')
    return re.sub(clean, '', text)


# Function to remove names of people
def remove_names(text):
    """This is a function that removes the names from text"""
    with open('data_preprocessing/names.txt', 'r') as f:
        NAMES = set(f.read().splitlines())

        NAMES = [name.lower() for name in NAMES]
        
    pattern = r'\W+'
    tokens = re.split(pattern, text)
    
    words = tokens
      
    for token in tokens:
        if token in NAMES:
            while token in words:
                words.remove(token)
    
    text = ' '.join(words)
    
    return text


# Function to remove countries
def remove_countries(text):
    """This is a function that removes the countries from text"""
    with open('data_preprocessing/countries.txt', 'r') as f:
        COUNTRIES = set(f.read().splitlines())

        COUNTRIES = [name.lower() for name in COUNTRIES]
        
    pattern = r'(\W+)'
    tokens = re.split(pattern, text)
    
    words = tokens
    
    for token in tokens:
        if token in COUNTRIES:
            while token in words:
                words.remove(token)
    
    text = ' '.join(words)
    
    return text


# Function to remove US cities of people
def remove_cities(text):
    """This is a function that removes the US cities from text"""
    with open('data_preprocessing/cities.txt', 'r') as f:
        CITIES = set(f.read().splitlines())

        CITIES = [name.lower() for name in CITIES]
        
    pattern = r'(\W+)'
    tokens = re.split(pattern, text)
    
    words = tokens
    
    for token in tokens:
        if token in CITIES:
            while token in words:
                words.remove(token)
    
    text = ' '.join(words)
    
    return text


# Function to remove days and months
def remove_days_and_months(text):
    """This is a function that removes the months and years from text"""
    
    # Load the months
    with open('data_preprocessing/months.txt', 'r') as f:
        MONTHS = set(f.read().splitlines())

        MONTHS = [name.lower() for name in MONTHS]
    
    # Load the days of the week
    with open('data_preprocessing/week.txt', 'r') as f:
        WEEK = set(f.read().splitlines())

        WEEK = [name.lower() for name in WEEK]
      
    pattern = r'(\W+)'
    tokens = re.split(pattern, text)  
    
    words = tokens
    
    for token in tokens:
        if token in MONTHS:
            while token in words:
                words.remove(token)
     
    for token in tokens:
        if token in WEEK:
            while token in words:
                words.remove(token)
            
    text = ' '.join(words)
            
    return text


def stopwords(text):
    """This function removes the stopwords in the text"""
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords = set(stopwords)
    
    tokens = re.split(r'(\W+)', text)
    
    text = [token for token in tokens if token not in stopwords]

    return ' '.join(text)


# Function to remove extra spaces
def remove_whitespace(text):
    """Remove extra spaces from a string"""
    
    clean = re.compile(r'\s{2,10000}')
    text = re.sub(clean, ' ', text)
    
    # Remove leading white spaces
    first_character = 1
    
    while text[0] == ' ':
        text = text[first_character:]
        first_character += 1
    
    # Remove trailing white spaces   
    last_character = -1
    
    while text[-1] == ' ':
        text = text[:last_character]
        last_character -= 1
    
    return text


# Lemmatize text
def lemmatize(text):
    lemma = WordNetLemmatizer()
    
    tokens = re.split('\W+', text)
    
    text = [lemma.lemmatize(token) for token in tokens]
    
    return ' '.join(text)

def preprocess(text):
    """This function preprocesses text"""
    text = remove_web_tags(text)
    text = remove_twitter_handles(text)
    text = remove_accented_chars(text)
    text = expand_contractions(text)
    text = remove_special_characters(text)
    text = lowercase_text(text)
    # text = convert_number_words(text)
    text = remove_numbers(text)
    text = remove_small_words(text)
    # text = remove_names(text)
    text = remove_countries(text)
    # text = remove_cities(text)
    text = remove_days_and_months(text)
    text = stopwords(text)
    text = remove_whitespace(text)
    text = lemmatize(text)
    return text

def main():
    
    """News Classifier App with Streamlit """
    st.title("📰 Fake and Real News Classifier")
    st.subheader("This app classifies whether the news is fake or real")

    news_text = st.text_area("Enter the news text here:")
    
    # news_text = pd.Series(news_text)
    

    if st.button("Classify"):
        st.text("Classiying...")
        
        news_text = [preprocess(news_text)]
         
        model = load_model()
        
        model.predict(news_text)
            
        if model.predict(news_text) == 0:
            st.error("Fake News")
        else:
            st.success("Real News")

if __name__ == '__main__':
    main()
    