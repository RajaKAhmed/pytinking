import regex as re
import openai
import os

# Define OpenAI API key

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Read the schema file
file_path = r"C:\Users\rajaa\OneDrive\DataScience\Python\llm\events\locations.csv"
with open(file_path, "r", encoding="utf-8") as file:
    file_contents = file.read()

# Upload the schema file
response = openai.File.create(file=file_contents, purpose="davinci")

# Retrieve the file ID
file_id = response.id

# Prepare the prompt and documents
question = "What is this file and what does it contain"
# Generate text using OpenAI API
response = openai.Completion.create(
    model="davinci-codex",
    documents=[file.id],
    question=question,
    max_tokens=50
)

# Extract the generated text from the response
answer = response['choice'][0]['text']

print("Question: ", question)
print("Answer: " , answer)