import json

def save_data(data, filename='data.json'):
    
    datalist = load_data(filename)
    if datalist is None:
        datalist = []
        
    datalist.append(data)
    
    with open(filename, 'w') as file:
        json.dump(datalist, file, indent=4)
        
def load_data(filename='data.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if len(data) == 0 or data is None:
                print("No data found. Please save your data first.")
                return []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found. Please save your data first.")