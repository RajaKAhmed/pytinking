# Import openai and regex libraries
import regex as re
import os
import tiktoken
import openai
# Get API_KEY
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Open and read the file, then close the file. 
file_path = r"C:\Users\rajaa\OneDrive\DataScience\Python\llm\events\locations.csv"
with open(file_path, "r", encoding="utf-8") as file_reader:
    file_content = file_reader.read()
    file_reader.close()

# Check number of tokens
encoding = tiktoken.encoding_for_model("davinci")
x = encoding.encode(file_content)
print(x)
token_count = len(x)
print(token_count)
y = encoding.decode(x)
print(y)
text_count = len(y)
print(text_count)
while token_count <= 2048:
    
# Open and append to the file, or create the file if it doesnt exist (first time or if the file is deleted)
    with open("answer_event_definition.txt", "a") as file_writer:
# Set the tokens and temperature    
        token_value = [500]
        temperature_value = [1.0, 0.7, 0.5]
# Loop through temperature and token to generate different answers     
        for temperature in temperature_value:
            for token in token_value:
# Open AI implementation   
                question = "What is the file about?"
                response = openai.Completion.create(
                engine="davinci",
                prompt=file_content + "\n\nQ: " + question + "\nA:", 
                max_tokens=token,
                temperature=temperature
            )
# Generate the response/answer and write to the file along with temperature and token values so we can distingush between accuracy            
            answer = response.choices[0].text.strip()
            file_writer.write(f"""\nTemperature value set to: {temperature}\nToken value set to: {token}\nAnswer: {answer}\n""")
        #print("Answer:", answer)
        #file_writer.write(answer)
# We close the file
    file_writer.close()              

print(f"""\nToken count for the current file is {token_count} which is too big.\nPlease reduce the size of the file so that it only contains upto or ess than 2048 tokens inlcuding your question.\n""")


