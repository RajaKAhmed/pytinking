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
    csv_file = 'random-csv-data-2023-07-02_172830.csv'
    input_file_path = os.path.join(in_folder, csv_file)
    return username, current_time, format_time, current_folder, in_folder, out_folder, csv_file, input_file_path

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

#  Open the csv file, read and retun the content
def read_csv_file(input_file_path):
    with open(input_file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        csvdata = list(reader)
        csvdata_str = '\n'.join([','.join(row) for row in csvdata])
    return csvdata,csvdata_str

# Encode csv file and count tokens
def encode_csv(csvdata_str):
    encoding = tiktoken.encoding_for_model("davinci")
    encoded_dict = []
    x = 0
    for csvdata in csvdata_str:
        encoded_csv = encoding.encode(csvdata)
        encoded_dict.append(encoded_csv) #print(encoded_csv)
        x += len(encoded_csv)
    return x, encoded_dict 

# Write results to a file
def write_encoded_csv(token_count, encoded_data):
    # Save token count
    token_count_file = os.path.join(out_folder, f"sum_of_tokens_in_encoded_csv_on_{datetime.datetime.now():%Y-%m-%d_%H%M%S}.txt")
    with open(token_count_file, 'w') as f:
        f.write(str(token_count))

    # Save encoded data
    encoded_csv_file = os.path.join(out_folder, f"encoded_csv_on_{datetime.datetime.now():%Y-%m-%d_%H%M%S}.csv")
    with open(encoded_csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(encoded_data)
    return token_count_file, encoded_csv_file
    
# Main body of the program
init_message = (f"""Initializing Engine!! Please Wait""")
message(init_message)
spinning_wheel()
username, current_time, format_time, current_folder, in_folder, out_folder, csv_file, input_file_path = init_setup() # Initialize Environment

# Start Message
start_message = (f"""Hello {username}! It is {format_time}\nStep #1 Python script is reading your file from:\n{input_file_path}""")
message(start_message)
csvdata,csvdata_str = read_csv_file(input_file_path) #Step 1. Read File
spinning_wheel()
# Processing Message
process_message = (f"""File reading completed moving to\nStep #2 Python Script will now create two files, one with encoded content and the other containing token count""")
message(process_message)
toklen,encode_csvdata = encode_csv(csvdata_str) #Step 2. Encode file and count tokens 
spinning_wheel()
count_info, file_info = write_encoded_csv(toklen, encode_csvdata) #Step 3. Write output to two files

# Goodbye Message
end_message = (f"""Step #3 Please open {out_folder} and look for\n{count_info} and\n{file_info}\nYou can now take the encoded file and move to embeddings and fine tuning features of open AI.""")
message(end_message)


