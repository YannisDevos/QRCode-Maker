import json
import os

FILE_PATH = "main/data/"

def save_data(data, filename="data.json"):
    
    datalist = load_data(FILE_PATH + filename)
    if datalist is None:
        datalist = []
        
    datalist.append(data)

    os.makedirs("main/data", exist_ok=True)
    
    with open(FILE_PATH + filename, 'w') as file:
        json.dump(datalist, file, indent=4)
        
def load_data(filename="data.json"):
    print(f"Loading data from {filename}...")
    try:
        with open(FILE_PATH + filename, 'r') as file:
            data = json.load(file)
            if len(data) == 0 or data is None:
                print("No data found. Please save your data first.")
                return []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found. Please save your data first.")