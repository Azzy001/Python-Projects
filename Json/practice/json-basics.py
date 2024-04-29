import json

users = {
    "user_one": {
        "Firstname":"a",
        "Lastname":"a",
        "Age":27
    },

    "user_two": {
        "Firstname":"b",
        "Lastname":"b",
        "Age":29
    },
    "user_three": {
        "Firstname":"c",
        "Lastname":"c",
        "Age":26
    },
    "user_four": {
        "Firstname":"d",
        "Lastname":"d",
        "Age":26
    },
    "user_five": {
        "Firstname":"e",
        "Lastname":"e",
        "Age":26
    }   
}

print()
json_str = json.dumps(users, indent=2)
with open("json/json-basics-data.json", "w") as f:
    f.write(json_str)

