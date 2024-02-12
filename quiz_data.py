import json

# Assuming your JSON file is named 'data.json' and is in the same directory as your Python script
file_path = 'questions_bank.json'

with open(file_path, 'r', encoding='utf-8') as f:
    question_data = json.load(f)

# Now 'data' contains the contents of your JSON file




