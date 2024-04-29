import json

with open("json/dsst-pass-project/pass-site-matching.json", "r") as f1:
    link_data = json.load(f1)

with open("json/dsst-pass-project/pass-matching.json", "r") as f2:
    pass_data = json.load(f2)


input_link = input("Enter link: ")

for pass_key, pass_items in pass_data.items():
    print(pass_key, pass_items)