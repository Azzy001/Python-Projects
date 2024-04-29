import json

# load data from json file
with open("json/account/users.json", "r") as f:
    user_data = json.load(f)

with open("json/account/accounts.json", "r") as f:
    account_data = json.load(f)

user_input = input("enter username: ")


# Check if the input matches any user in the first JSON file
matching_user = user_data.get(user_input)

# If a matching user is found, check if there is a corresponding account
if matching_user:
    matching_account = next(
        ((account_key, account_info) for account_key, account_info in account_data.items() if account_info["firstname"] == matching_user["firstname"]),
        None
    )

    # Print the results in a human-readable format
    if matching_account:
        print(f"Matching account for user '{user_input}':")
        print(f"User Info:")
        for key, value in matching_user.items():
            print(f"  {key.capitalize()}: {value}")

        print(f"Account Info:")
        for key, value in matching_account[1].items():
            print(f"  {key.capitalize()}: {value}")
    else:
        print(f"No matching account found for user '{user_input}'.")
else:
    print(f"No matching user found for username '{user_input}'.")