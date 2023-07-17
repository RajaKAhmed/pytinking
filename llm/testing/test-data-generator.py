import os, datetime, time, tiktoken, openai,csv,json,getpass,sys,random
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
    out_folder = os.path.join(current_folder, "out_folder")
    #json_file = os.path.join(out_folder, f"random-json-data-{datetime.datetime.now():%Y-%m-%d_%H%M%S}.json")
    #csv_file = os.path.join(out_folder, f"random-csv-data-{datetime.datetime.now():%Y-%m-%d_%H%M%S}.csv")
    return username, current_time, format_time, current_folder,  out_folder #csv_file, json_file

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

def generate_random_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'App_Name': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3)).upper(),
            'App_ID': random.randint(000000, 999999),
            'App_Env': random.choice(['Dev', 'Test', 'UAT', 'QA', 'Perf', 'Prod', 'DR', 'Archive']),
            'App_LOB': random.choice(['TSS','WSS','CCM', 'IB', 'ETS','Legal', 'HR']),
            'App_LOC': random.choice(['Hybrid','Cloud','On-Prem']),
            'App_Type': random.choice(['Web','DB','Compute','CRM']),
            'App_SLA': random.choice(['8','12','24','48','72']),
            'App_Risk': random.choice(['SOX','BASEL','Internal','Cust Facing','Investment', 'None']),
            'App_Region': random.choice(['EMEA','LATAM','USNA','S.ASIA','E.ASIA','SE.ASIA','AUS']),
            'App_Assets': random.choice(['Servers','Desktops','Serverless Functions','Transaction Machines'])

        }
        data.append(record)
    return data

def write_json_file(data):
    output_json_file = os.path.join(out_folder, f"random-jason-data-{datetime.datetime.now():%Y-%m-%d_%H%M%S}.json")
    with open(output_json_file, 'w') as f:
        json.dump(data, f, indent=4)
    return output_json_file

def convert_to_jsonl(output_json_file):
    output_jsonl_file = os.path.join(out_folder, f"json-to-jsonl-{datetime.datetime.now():%Y-%m-%d_%H%M%S}.json")
    with open(output_json_file, 'r') as json_file, open(output_jsonl_file, 'w') as jsonl_file:
        data = json.load(json_file)
        for item in data:
            jsonl_file.write(json.dumps(item) + '\n')  
    return output_jsonl_file


def write_csv_file(data):
    output_csv_file = os.path.join(out_folder, f"random-csv-data-{datetime.datetime.now():%Y-%m-%d_%H%M%S}.csv")
    fieldnames = data[0].keys()
    with open(output_csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return output_csv_file
    

init_message = (f"""Starting Data generator!! Please Wait""")
message(init_message)
username, current_time, format_time, current_folder,  out_folder = init_setup()
spinning_wheel()

start_message = (f"""\U0001F682 Hello {username}! It is {format_time}\nStep #1 We will generate random data in csv and json format.\nGenerating Data""")
message(start_message)
num_records = 10
data = generate_random_data(num_records)
spinning_wheel()

process_message = (f"""\U0001F682 Done generating data.\nStep #2 Writing to data to files.""")
message(process_message)
output_json_file= write_json_file(data)
output_csv_file= write_csv_file(data)
jsonl_output_file = convert_to_jsonl(output_json_file)
spinning_wheel()

end_message = (f"""\U0001F682 Step #3 Please open {out_folder} and look for\n{output_json_file}\n{output_csv_file}\n and\n{jsonl_output_file}\nNow that you have data you can run our token-generator program to encode it for Open AI APIs.""")
message(end_message)



