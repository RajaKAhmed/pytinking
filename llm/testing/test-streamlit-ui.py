import streamlit as st
import regex as re
import openai
import os

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

def chatbot_ui():
    st.title("Welcome to AI/ML using OpenAI API")

    # Create three selectboxes for choosing persona, AI Model
    persona = st.selectbox("Please select a role", ["Student", "Doctor", "Lawyer", "Mathematician", "Engineer", "Idiot"])
    ai_model = st.selectbox("Select an AI model", ["GPT-3", "GPT-4", "ChatGPT", "Codex", "Davinci"])
    
    # Create a text input box for user input
    user_input = st.text_input("Please ask me a question")

    
    # Generate a response when the user submits input
    if st.button("Submit"):
        response = generate_response(user_input, persona)
        st.text_area("Bot Response", value=response, height=200)



def generate_response(user_input, persona):
    # Replace this function with your chatbot logic
    # Here, you can use any Natural Language Processing or Machine Learning techniques
    # to generate a response based on the user's input and selected persona
    if persona == "Student":
        temperature = 1.0
        response = f"You are a student and said: {user_input}"
    elif persona == "Doctor":
        temperature = 0.0
        response = f"You are a doctor and said: {user_input}"
    elif persona == "Lawyer":
        temperature = 0.3
        response = f"You are a lawyer and said: {user_input}"
    elif persona == "Mathematician":
        temperature = 0.1
        response = f"You are a mathematician and said: {user_input}"
    elif persona == "Engineer":
        temperature = 0.2
        response = f"You are an engineer and said: {user_input}"
    elif persona == "Idiot":
        temperature = 2.0
        response = f"You are an idiot and said: {user_input}"
    else:
        temperature = 0.5
        response = f"You said: {user_input}"


    return response

if __name__ == "__main__":
    chatbot_ui()
