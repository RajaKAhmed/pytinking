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
    
    # Create a radio button for selecting input method
    input_method = st.radio("Select input method", ["Text Input", "Upload and ask questions"])
    
    if input_method == "Text Input":
        user_input = st.text_input("Please ask me a question")
    else:
        uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "csv"])
        user_input = st.text_input("Ok now that the file is loaded, Please ask me a question")
    
    # Generate a response when the user submits input
    if st.button("Ask"):
        response = openai.Completion.create(
        engine=ai_model,
        prompt=user_input,
        temperature = persona,
        max_tokens=100
    )
    generated_text = response.choices[0].text.strip()
    #response = generated_text #generate_response(user_input, persona)
    st.text_area("Bot Response", value=generated_text, height=200)

def generate_response(persona):
    # Replace this function with your chatbot logic
    # Here, you can use any Natural Language Processing or Machine Learning techniques
    # to generate a response based on the user's input and selected persona
    if persona == "Student":
        temp_select = 1.0
        temp_val = temp_select #f"You are a student and said: {user_input}"
    elif persona == "Doctor":
        temp_select = 0.0
        temp_val = temp_select #f"You are a doctor and said: {user_input}"
    elif persona == "Lawyer":
        temp_select = 0.3
        temp_val = temp_select #f"You are a lawyer and said: {user_input}"
    elif persona == "Mathematician":
        temp_select = 0.1
        temp_val = temp_select #f"You are a mathematician and said: {user_input}"
    elif persona == "Engineer":
        temp_select = 0.2
        temp_val = temp_select #f"You are an engineer and said: {user_input}"
    elif persona == "Idiot":
        temp_select = 2.0
        temp_val = temp_select #f"You are an idiot and said: {user_input}"
    else:
        temp_select = 0.5
        temp_val = temp_select #f"You said: {user_input}"

    return temp_val

if __name__ == "__main__":
    chatbot_ui()
