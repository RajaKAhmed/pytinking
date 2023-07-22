import random
import json
import os
import datetime
import csv
#Input and Output Folders

output_folder = "C:\\Users\\rajaa\\OneDrive\\DataScience\\Python\\llm\\testing\out_folder"
output_folder_path = os.path.abspath(output_folder)
output_json_path = os.path.join(output_folder_path, f"random-data-generator_{datetime.datetime.now():%Y-%m-%d_%H%M%S}.json")
output_csv_path = os.path.join(output_folder_path, f"random-data-generator_{datetime.datetime.now():%Y-%m-%d_%H%M%S}.csv")




#app_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3)).upper()


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

def write_json_file(data, output_json_file):
    with open(output_json_file, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"JSON file '{output_json_file}' generated successfully!")

def write_csv_file(data,output_csv_file):
    fieldnames = data[0].keys()
    with open(output_csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"CSV file '{output_csv_file}' generated successfully!")


# Generate random data
num_records = 10
data = generate_random_data(num_records)

# Write to JSON file
output_json_file = output_json_path
output_csv_file = output_csv_path

write_json_file(data, output_json_file)
write_csv_file(data, output_csv_file)
