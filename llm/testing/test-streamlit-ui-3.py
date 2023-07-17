import streamlit as st
import openai
import os

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

def chatbot_ui():
    st.title("Welcome to AI/ML using OpenAI API")

    # Create three selectboxes for choosing persona, AI Model
    persona = st.selectbox("Please select a role", ["Student", "Doctor", "Lawyer", "Mathematician", "Engineer", "Silly Response"])
    # ai_model = st.selectbox("Select an AI model", ["gpt-3.5-turbo", "gpt-4.0-turbo", "text-davinci-003"])
    ai_model = "text-davinci-003"

    # Create a radio button for selecting input method
    input_method = st.radio("Select input method", ["Text Input", "Upload and ask questions"])

    if input_method == "Text Input":
        user_input = st.text_input("Please ask Open AI a question")
    else:
        uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "csv"])
        if uploaded_file is not None:
            user_input = uploaded_file.read().decode("utf-8")
        else:
            user_input = st.text_input("Ok now that the file is loaded, Please ask me a question")

    # Generate a response when the user submits input
    if st.button("Ask"):
        temperature = get_temperature(persona)
        response = openai.Completion.create(
            engine=ai_model,
            prompt=user_input,
            max_tokens=100,
            temperature=temperature
        )
        generated_text = response.choices[0].text.strip()
        st.text_area("Open AI Response", value=generated_text, height=200)

def get_temperature(persona):
    if persona == "Student":
        return 1.0
    elif persona == "Doctor":
        return 0.0
    elif persona == "Lawyer":
        return 0.3
    elif persona == "Mathematician":
        return 0.1
    elif persona == "Engineer":
        return 0.2
    elif persona == "Silly Response":
        return 2.0
    else:
        return 0.5

if __name__ == "__main__":
    chatbot_ui()
