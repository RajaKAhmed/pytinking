# Import openai and regex libraries
import regex as re
import openai
import os

# Define OpenAI API key
# openai.api_key = "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"
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key
print(api_key)
file_contents = """
This is the content of my file.
It can have multiple lines.
You can include any text or data here.
"""

with open("file.txt", "w") as file:
    file.write(file_contents)

with open("file.txt", "r") as file:
    file_content = file.read()

question = "What is the file about?"
response = openai.Completion.create(
    engine="davinci",
    prompt=file_content + "\n\nQ: " + question + "\nA:",
    max_tokens=50
)

answer = response.choices[0].text.strip()
print("Answer:", answer)