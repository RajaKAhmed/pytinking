from flask import Flask, render_template, request
import openai
import os
# Create a Flask application
app = Flask(__name__)

# OpenAI API credentials
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Get the absolute path of the index.html file
template_folder = "C:\\Users\\rajaa\\OneDrive\\DataScience\\Python\\llm\\openaiui\\templates" 
index_filename = "index.html"

template_path = os.path.abspath(template_folder)
index_path = os.path.join(template_path, index_filename)

# Route for the home page
@app.route('/')
def home():
    return Flask(index_path)

# Route for generating OpenAI-like responses
@app.route('/generate', methods=['POST'])
def generate():
    # Get the user input from the HTML form
    user_input = request.form['user_input']

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine='davinci-codex',
        prompt=user_input,
        max_tokens=100
    )

    # Extract the generated response from the API response
    generated_text = response.choices[0].text.strip()

    # Render the template with the generated response
    return render_template(index_path, generated_text=generated_text) 

# Run the Flask application
if __name__ == '__main__':
    app.run()
