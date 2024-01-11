#Multiclipboard

import sys
import clipboard
import json


SAVED_DATA = "clipboard.json"
# clipboard.copy("abc")
# data = clipboard.paste()
# print(data)

#print(sys.argv) #['task1.py', 'test', 'hello', 'world']

#print(sys.argv[1:]) #['test', 'hello', 'world']

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
         with open(filepath, "r") as f:
             data = json.load(f)
             return data  
    except:
        return {}
        
#save_items("test.json", {"key": "value"})

if len(sys.argv)  == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    #print(command)
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("saved")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("key does not exist")
        #print("load")
    elif command == "list":
        print(data)
        #print("list")
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")