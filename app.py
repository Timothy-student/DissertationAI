import streamlit as st
import pickle
import re  # For basic text cleaning
import os

st.balloons() #baloons

# Check if models exist, if not prompt to download
if not os.path.exists('models/vectorizer.pkl') or not os.path.exists('models/ensemble_model.pkl'):
    st.error("Model files not found! Please run 'python download_models.py' first to download the required models.")
    st.stop()

# Load the saved model and vectorizer
with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("models/ensemble_model.pkl", "rb") as f:
    model = pickle.load(f)

# Basic Text Cleaning FunctionS
def clean_text(text):
    text = re.sub(r'\n', ' ', text)        # Remove newline characters
    text = re.sub(r'\s+', ' ', text)       # Replace multiple spaces with a single space
    return text.strip()                    # Remove leading/trailing spaces


# Streamlit App
st.title("AI Text Detection App")

# Input box
user_input = st.text_area("Enter text for detection:")

if st.button("Detect"):
    if user_input.strip():
       # Clean the input text
        cleaned_input = clean_text(user_input)
        
        # Transform input text
        transformed_text = vectorizer.transform([cleaned_input])

        #predict using the model
        prediction = model.predict(transformed_text)[0]
        
        # Show result
        result = "AI-Generated" if prediction == 1 else "Human-Written"
        st.success(f"Prediction: {result}")
    else:
        st.warning("Please enter some text.")
