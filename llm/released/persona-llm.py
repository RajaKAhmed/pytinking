# Import openai and regex libraries
import regex as re
import openai
import os

# Define OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key
print(api_key)

# Function to clear screen
def pause_clear_screen():
    input("Press Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")



# Function to check input from user using Regular expression
def validate_input(input_str):
    pattern = r'^(?:[0-5]|10)$'
    if re.match(pattern, input_str):
        return True
    else:
        return False
    
# Function that determines the temperature selection based on user input    
def temperature_selection(user_input_int):
    if user_input_int == 5:
        temp_select = 1.5
        return temp_select
    elif user_input_int in [4, 3, 2]:
        temp_select = 0.5
        return temp_select
    elif user_input_int == 1:
        temp_select = 0.0
        return temp_select
    else:
        temp_select = 1.0
        return temp_select

# Function that runs the main AI engine    
def ai_engine(model_engine, prompt, temp_select):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=temp_select,
    )
    return completion.choices[0].text

# Our list of personas    
persona = ["Student", "Doctor", "Lawyer", "Mathematician", "Engineer", "Idiot"]

# An input loop to capture user input
while True:
    for index, item in enumerate(persona):
        print("Select", index, "for", item)

    user_input = input("Please enter your selection or type QUIT to exit: ")
    if user_input.upper() == "QUIT":
        print("Exiting the program")
        break
    elif validate_input(user_input):
        user_input_int = int(user_input)
        temp_select = temperature_selection(user_input_int)
        model_engine = "text-davinci-003"
        print("How are you", persona[int(user_input)], "Let's begin!")
        prompt_input = input("How can I help you " + persona[int(user_input)] + "::\t> ")
        prompt = "As a " + persona[int(user_input)] + " " + prompt_input
        ai_engine_results = ai_engine(model_engine, prompt, temp_select)
        print(ai_engine_results)
        pause_clear_screen()
    else:
        print("Invalid input. Please try again.")