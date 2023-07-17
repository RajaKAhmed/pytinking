import os, datetime, time, tiktoken, openai,csv,json,getpass,sys
import regex as re

# Get API_KEY and set the encoding model
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Initialization and Setup
def init_setup():
    username = getpass.getuser()
    current_time = datetime.datetime.now()
    format_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    current_folder = os.getcwd()
    in_folder = os.path.join(current_folder, "in_folder")
    out_folder = os.path.join(current_folder, "out_folder")
    input_file = 'json-to-jsonl-2023-07-02_201443.json'
    #output_file = ''
    input_file_path = os.path.join(in_folder, input_file)
    return username, current_time, format_time, current_folder, in_folder, out_folder, input_file_path

def spinning_wheel(delay=0.1):
    sequence = '|/-\\'  # Sequence of characters for the spinning wheel animation

    for _ in range(5):  # Number of spins (adjust as needed)
        for char in sequence:
            sys.stdout.write(f'\r{char} ')
            sys.stdout.flush()
            time.sleep(delay)

    sys.stdout.write('\r')  # Clear the spinning wheel animation
    sys.stdout.flush()

def message(msg_input):
    for char in msg_input:
        print(char, end='', flush=True)
        time.sleep(0.055)  # Add a delay between each character
    print() 

def encode_jsonl_file(input_file):
    encoding = tiktoken.encoding_for_model("davinci")
    encoded_data = []
    x = 0
    with open(input_file, 'r') as file:
        for line in file:
            encode_data = json.loads(line)
            encoded_data = encoding.encode(encode_data)
            encoded_data.append(encode_data)
            x += len(encoded_data)

    encoded_file = os.path.join(out_folder, f"encoded_jsonl_{datetime.datetime.now():%Y-%m-%d_%H%M%S}")
    with open(encoded_file, 'w') as file:
        for encoded_line in encoded_data:
            file.write(json.dumps(encoded_line) + '\n')

    token_count_file = os.path.join(out_folder, f"sum_of_tokens_in_encoded_jsonl_{datetime.datetime.now():%Y-%m-%d_%H%M%S}.txt")
    with open(token_count_file, 'w') as f:
        f.write(str(x))
    return encoded_file,token_count_file    

    # print(f"JSONL file '{input_file}' encoded and saved as '{output_file}'.")

def encode_data(data):
    # Encode your data using OpenAI API
    encoded_data = openai.Completion.create(
        engine="text-davinci-003",
        prompt=data,
        max_tokens=100,
        temperature=0.7
    )

    return encoded_data.choices[0].text.strip()
    
# Main body of the program
init_message = (f"""Initializing Engine!! Please Wait""")
message(init_message)
#spinning_wheel()
username, current_time, format_time, current_folder, in_folder, out_folder, input_file_path = init_setup() # Initialize Environment
print(f"""{username}\n{current_time}\n{format_time}\n{current_folder}\n{in_folder}\n{out_folder}\ninputfilepath is {input_file_path}""")
encoded_file = encode_jsonl_file(input_file_path)

# Start Message
#start_message = (f"""Hello {username}! It is {format_time}\nStep #1 Python script is encoding your file from:\n{input_file_path}""")
#message(start_message)
#encoded_file,token_count_file = encode_jsonl_file(input_file,output_file)
#spinning_wheel()
# Processing Message
#process_message = (f"""File reading completed moving to\nStep #2 Python Script will now create two files, one with encoded content and the other containing token count""")
#message(process_message)
#spinning_wheel()
message(f"""Done!""")



