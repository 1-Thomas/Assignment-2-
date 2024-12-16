import json
class SaveToJson:
    def save_to_json(file_name, data):

        with open(file_name, "r") as file:
            existing_data = json.load(file)

        existing_data.append(data)

        with open(file_name, "w") as file:
            json.dump(existing_data, file, indent=4)