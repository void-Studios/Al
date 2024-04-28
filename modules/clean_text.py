import re
import ast
import os

# Define the input and output file paths
input_file_path = os.path.join(os.getcwd(), 'program_data/input/clean_text.txt')
output_file_path = os.path.join(os.getcwd(), 'program_data/output/clean_text.txt')

def extract_operacion_id(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Find all serialized PHP data within the file
    serialized_data = re.findall('s:[0-9]+:"[^"]+";', content)

    # Deserialize the data and extract the ID_OPERACION values
    operacion_ids = []
    for data in serialized_data:
        key, value = data.split(':', 1)
        key = key[1:-1]
        value = value[1:-1]
        if key == '12': # ID_OPERACION key
            operacion_ids.append(value)

    # Remove all content outside of the ID_OPERACION values
    cleaned_content = '\n'.join(operacion_ids)

    return cleaned_content

# Read from the input file
cleaned_content = extract_operacion_id(input_file_path)

# Write to the output file
with open(output_file_path, 'w') as file:
    file.write(cleaned_content)
