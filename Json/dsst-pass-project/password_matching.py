import json

# line will read json file
with open("json/dsst-pass-project/link_address.json", "r") as f1:
    # line to load json file into variable
    sites_address = json.load(f1)


def find_link(input_link):
    for link in sites_address.values():
        if link in input_link:
            print("Link exists", f"{link}")
            return
    print("Link does not exist")

    
if __name__ == "__main__":
    find_link(input_link = input("\nEnter link: "))