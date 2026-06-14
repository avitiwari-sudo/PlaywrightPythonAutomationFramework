import json

def update_testdata(file_path, key, value):
    with open(file_path, "r") as f:
        data = json.load(f)

    data[key] = value

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)