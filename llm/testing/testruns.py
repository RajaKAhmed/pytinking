import os, datetime, time, tiktoken, openai,csv,json,getpass,sys
import regex as re

def init_setup():
    input_file = 'json-to-jsonl-2023-07-02_201443.json'
    current_folder = os.getcwd()
    in_folder = os.path.join(current_folder, "in_folder")
    out_folder = os.path.join(current_folder, "out_folder")
    input_file_path = os.path.join(in_folder,input_file )
    #print(f"""Current Folder uses:\nos.getcwd and returns {current_folder}\nin_folder and out_folder use:\nos.path.join and return {in_folder}\n{out_folder}\n{input_file_path}""")
    return input_file_path, out_folder

def jsonl_encoder(input_file_path):
    encoding = tiktoken.encoding_for_model("davinci")
    encoded_data = []
    token_count = 0

    with open(input_file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            #print(f""" Here is stuff from{data}""")
            #print(f"""Here is the output from {line}""")
            encoded_line = encoding.encode(line)
            #print(encoded_line)
            encoded_data.append(encoded_line)
            token_count += len(encoded_line)
    return encoded_data,token_count  



def encoded_write_to_file(encoded_data,token_count):
    token_count_file = os.path.join(out_folder, f"sum_of_tokens_in_encoded_jsonl_on_{datetime.datetime.now():%Y-%m-%d_%H%M%S}.txt")
    with open(token_count_file, 'w') as f:
        f.write(str(token_count))

    # Save encoded data
    encoded_jsonl_file = os.path.join(out_folder, f"encoded_jsonl_on_{datetime.datetime.now():%Y-%m-%d_%H%M%S}.json")
    with open(encoded_jsonl_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(encoded_data)
    return token_count_file, encoded_jsonl_file





input_file_path, out_folder = init_setup()

encoded_data, token_count = jsonl_encoder(input_file_path)
token_count_file, encoded_jsonl_file = encoded_write_to_file( encoded_data,token_count)
print("done")

