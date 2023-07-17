# Import openai and regex libraries
import regex as re
import openai

# Define OpenAI API key
openai.api_key = "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"


# Function to check input from user using Regular expression
def validate_input(input_str):
    pattern = r'^(?:[0-5]|10)$'
    if re.match(pattern, input_str):
        return True
    else:
        return False
    
# Function that run the main AI engine.    

def temperature_selection(user_input_int):
    if user_input_int == 5:
        temp_select: float = 2.0
        return temp_select
    elif user_input_int == 4 | 3 | 2:
        temp_select: float = 0.5
        return temp_select
    elif user_input_int == 1:
        temp_select: float = 0.0
        return temp_select
    else:
        user_input_int == 0
        temp_select: float = 1.0
        return temp_select

def ai_engine(model_engine,prompt,temp_select):

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens= 2048,
        n=1,
        stop=None,
        temperature=temp_select,
    )
    return completion.choices[0].text

# Our list of personas    
persona = [ "Student", "Doctor", "Lawyer", "Mathematician", "Engineer", "Idiot"]

# We iterate through our list to provide options to the end user
for index, item in enumerate(persona):
    print("Select ", index, "for ", item)

# An input loop to capture user input
while True:
    user_input = input("Please enter your selection or type QUIT to exit:")
    if user_input.upper() == "QUIT":
        print("Exiting the progrm")
        break

    elif validate_input(user_input):
        print("How are you", persona[int(user_input)],"Lets begin!")
        break
    else:
        print("Invalid input. Please try again.")

# Setting up the model
model_engine = "text-davinci-003"

# Setting up the temperature
print("Temperature")
print(persona[int(user_input)])
#user_input_int = int(user_input)
#temperature_selection(user_input_int)


# Setting up the prompt
prompt_input = input("How can I help you " + persona[int(user_input)]+ "::\t > ")
if prompt_input.upper() == "QUIT":
   print("Exiting the progrm")
   
else:
    prompt = ("As a " + persona[int(user_input)] +" "+ prompt_input)
    user_input_int = int(user_input)
    temperature_selection(user_input_int)
    ai_engine_results = ai_engine(model_engine,prompt,temp_select)
    print(ai_engine_results)

# x = openai.Engine.list()
#response = completion.choices[0].text
#print(response)
