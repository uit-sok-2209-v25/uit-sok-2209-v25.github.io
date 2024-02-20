import json

# Function to format and print the chat conversation
def print_conversation(chat_data):
    for session in chat_data.get("history", []):
        print(f"Session Name: {session.get('name')}\n")
        for msg in session.get("messages", []):
            speaker = "User" if msg.get("role") == "user" else "Assistant"
            print(f"{speaker}: {msg.get('content')}\n")
        print("\n" + "="*50 + "\n")

# Load JSON data from a file
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Specify the path to your JSON file
file_path = "c:\\Users\\mia100\\OneDrive - UiT Office 365\\My Documents\\SOK-2209\\vår_2024\\chat_data.json"

# Load the data
chat_data = load_json_data(file_path)

# Call the function with the loaded JSON data
print_conversation(chat_data)

import os




import json

# Load JSON data from a file
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to write the chat conversation to a file
def write_conversation_to_file(chat_data, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for session in chat_data.get("history", []):
            file.write(f"Session Name: {session.get('name')}\n\n")
            for msg in session.get("messages", []):
                speaker = "User" if msg.get("role") == "user" else "Assistant"
                file.write(f"{speaker}: {msg.get('content')}\n\n")
            file.write("\n" + "="*50 + "\n\n")

# Specify the path to your JSON file
file_path = r"c:\Users\mia100\OneDrive - UiT Office 365\My Documents\SOK-2209\vår_2024\chat_data.json"

# Specify the path to the output file where you want to write the conversation
output_file_path = "conversation_output.txt"

# Load the data
chat_data = load_json_data(file_path)

# Call the function with the loaded JSON data and output file path
write_conversation_to_file(chat_data, output_file_path)

print(f"The conversation has been written to {output_file_path}")
