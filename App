import json
uname = input("Enter Username")
pwd = input("Enter Password")

toWrite = {
    "Username": uname,
    "Password": pwd
    }

with open("accounts.json", "a") as f:
    json.dump(toWrite, f, indent = 4)