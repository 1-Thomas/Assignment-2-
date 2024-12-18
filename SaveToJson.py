import json
class SaveToJson:
    def save_to_json(file_name, data):

        with open(file_name, "r") as file:
            existing_data = json.load(file)
        
        customer_id = data["customer"][0]["customer_id"]
        customer_found = False

        for record in existing_data:
            if "customer" in record:
                for customer in record["customer"]:
                    if customer["customer_id"] == customer_id:
                        # Update the customer's accounts
                        customer["accounts"] = data["customer"][0]["accounts"]
                        customer_found = True
                        break
        
        if not customer_found:
            existing_data.append(data)

        with open(file_name, "w") as file:
            json.dump(existing_data, file, indent=4)
