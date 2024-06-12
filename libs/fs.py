import ujson

def ReadJsonFile(filename):
    try:
        with open(filename, 'r') as f:
            config = ujson.load(f)
        return config
    except OSError:
        print("Error reading file.")
        return None
    
def WriteJsonFile(filename, jsonContent):
    try:
        with open(filename, 'w') as f:
            ujson.dump(jsonContent, f)
    except OSError:
        print("Error writing file")
        
def UpdateJsonFile(filename, fieldName, newValue):
    try:
        with open(filename, 'r') as f:
            data = ujson.load(f)

        if fieldName in data:
            data[fieldName] = newValue
            WriteJsonFile(filename, data)
        else:
            print(f"Field '{fieldName}' not found in JSON data.")

    except OSError as e:
        print(f"Error updating JSON data: {e}")
