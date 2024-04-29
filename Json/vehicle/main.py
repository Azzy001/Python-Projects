import json

with open("json/vehicle/vehicle.json", "r") as f:
    vehicle_data = json.load(f)


for veh_key, veh_info in vehicle_data.items():
    print(veh_key, veh_info)