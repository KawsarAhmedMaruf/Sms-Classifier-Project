import streamlit as st
import joblib
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string

# Load the trained model
model = joblib.load('mnb_model.pkl')

# Load the fitted TF-IDF vectorizer
tfidf = joblib.load('vectorizer.pkl')

# Initialize stemmer and stopwords
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

# Function to classify the text
def classify_text(text):
    transformed_text = transform_text(text)
    tfidf_text = tfidf.transform([transformed_text]).toarray()
    prediction = model.predict(tfidf_text)
    if prediction == 0:
        return 'HAM'
    else:
        return 'SPAM'

# Text classification streamlit app
def main():
    st.title("SMS Classifier")

    # Text input for user to enter the message
    text = st.text_input("Enter the text message", "")

    # Classify button to classify the text
    if st.button("Classify"):
        if text:
            result = classify_text(text)
            st.write("Classification:", result)
        else:
            st.write("Please enter a text message to classify")

if __name__ == '__main__':
    main()