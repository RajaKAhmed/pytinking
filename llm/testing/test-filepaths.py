import os
import datetime

input_folder = "C:\\Users\\rajaa\\OneDrive\\DataScience\\Python\\llm\\testing\in_folder"
output_folder = "C:\\Users\\rajaa\\OneDrive\\DataScience\\Python\\llm\\testing\out_folder"
filename = "ai_answer_file.txt"

# Get the absolute paths of the input and output folders
input_folder_path = os.path.abspath(input_folder)
output_folder_path = os.path.abspath(output_folder)

print(f"""Input Folder Path {input_folder_path}""")
print(f""" Output Folder Path {output_folder_path}""")

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Construct the input and output file paths
input_file_path = os.path.join(input_folder_path, filename)
output_file_path = os.path.join(output_folder_path, f"{filename}_{datetime.datetime.now():%Y-%m-%d_%H%M%S}")

# Check if the input file exists
if os.path.isfile(input_file_path):
    # Read the contents of the input file
    with open(input_file_path, 'r') as input_file:
        file_contents = input_file.read()

    # Write the contents to the output file with a timestamp
    with open(output_file_path, 'w') as output_file:
        output_file.write(file_contents)

    print(f"File '{filename}' has been copied from '{input_folder}' to '{output_folder}' with timestamp.")
else:
    print(f"File '{filename}' does not exist in the '{input_folder}' folder.")

