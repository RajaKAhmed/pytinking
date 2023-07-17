import tiktoken
import json
import os

def encode_jsonl_file(input_file):
    encoding = tiktoken.encoding_for_model("davinci")
    encoded_data = []
    token_count = 0

    with open(input_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            encoded_line = encoding.encode(data)
            encoded_data.append(encoded_line)
            token_count += len(encoded_line)

    output_folder = os.path.dirname(input_file)
    encoded_file = os.path.join(output_folder, f"encoded_{os.path.basename(input_file)}")
    with open(encoded_file, 'w') as file:
        for encoded_line in encoded_data:
            file.write(json.dumps(encoded_line) + '\n')

    token_count_file = os.path.join(output_folder, f"token_count_{os.path.basename(input_file)}.txt")
    with open(token_count_file, 'w') as f:
        f.write(str(token_count))

    return encoded_file, token_count_file
