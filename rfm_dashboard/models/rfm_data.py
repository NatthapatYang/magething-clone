import json

def get_rfm_data():
    with open('rfm_dashboard/db/rfm_data.json') as file:
        data = json.load(file)
    return data