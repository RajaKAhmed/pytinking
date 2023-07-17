from flask import Flask, render_template, request
import os
import openai

# OpenAI API credentials
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

template_folder = "C:\\Users\\rajaa\\OneDrive\\DataScience\\Python\\llm\\openaiui\\templates" 
index_filename = "index.html"

template_path = os.path.abspath(template_folder)
index_path = os.path.join(template_path, index_filename)

app= Flask(__name__)
@app.route('/')
def home():
    rendered_template = render_template(index_filename)
    return rendered_template

# Route for generating OpenAI-like responses
@app.route('/generate', methods=['POST'])
def generate():
    # Get the user input from the HTML form
    user_input = request.form['user_input']

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_input,
        max_tokens= 1024,
        n=1,
        temperature=0.2
        
    )

    # Extract the generated response from the API response
    generated_text = response.choices[0].text.strip()
    # Render the template with the generated response
    return render_template(index_filename, generated_text=generated_text) 


if __name__ == '__main__':
    app.run()