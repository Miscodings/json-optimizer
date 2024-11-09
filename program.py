import os
import json

# Function to minify JSON files
def minify_json_files(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.json'):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r') as file:
                        data = json.load(file)
                    
                    # Re-saving the file without spaces
                    with open(filepath, 'w') as file:
                        json.dump(data, file, separators=(',', ':'))  # Removes extra spaces
                    print(f"Minified {filename}")
                except Exception as e:
                    print(f"Failed to process {filename}: {e}")

# Specify the directory (adjust as needed)
directory = r'D:\Downloads\pack\models'

minify_json_files(directory)
