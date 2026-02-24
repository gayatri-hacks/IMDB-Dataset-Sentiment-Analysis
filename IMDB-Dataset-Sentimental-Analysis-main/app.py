import streamlit as st
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification

st.set_page_config(page_title='Sentiment Analysis of IMDB Dataset')

@st.cache_resource
def load_model():
    return TFBertForSequenceClassification.from_pretrained('outputs/models/bert-imdb-hf')

@st.cache_resource
def load_tokenizer():
    return BertTokenizer.from_pretrained('outputs/models/bert-base-uncased_tokenizer')

# Load tokenizer and model
model = load_model()
tokenizer = load_tokenizer()
st.success("Model and tokenizer loaded!")

# Function to predict sentiment
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="tf", truncation=True, padding="max_length", max_length=128)
    output = model(inputs)
    prediction = tf.argmax(output.logits, axis=1).numpy()[0]
    return "Positive" if prediction == 1 else "Negative"

# Streamlit app UI
st.title('🎬 Sentiment Analysis of IMDB Movie Reviews')
st.write('Enter a movie review to predict whether it is **positive** or **negative**.')

user_input = st.text_area("✍️ Movie Review")
if st.button("Predict"):
    if user_input:
        sentiment = predict_sentiment(user_input)
        st.success(f"The sentiment of the review is: **{sentiment}**")
    else:
        st.warning("Please enter a movie review to get a prediction.")
