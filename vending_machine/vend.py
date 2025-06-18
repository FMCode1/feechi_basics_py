import json
import csv

json_file = "items.json"
txt_file = "items.txt"
csv_file = "items.csv"

def get_items_from_json(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def get_items_from_txt(txt_file):
    data = {}
    with open(txt_file, 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.strip().split(':', 1)
                data[key.strip()] = [item.strip() for item in value.split(',')]
    return data

def get_items_from_csv(csv_file):
    data = {}
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = row['key']
            data[key] = [item.strip() for item in row['items'].split(',')]
    return data

# Load all data before using in class
json_items = get_items_from_json(json_file)
txt_items = get_items_from_txt(txt_file)
csv_items = get_items_from_csv(csv_file)

class Vending_Machine:
    def __init__(self, name, items=None):
        self.name = name
        # If no items are passed, create a default 5x5 matrix
        if items is None:
            self.items = [
                [json_items["items1"][0], json_items["items2"][0], json_items["items3"][0], json_items["items4"][0], json_items["items5"][0]],
                [json_items["items6"][0], json_items["items7"][0], json_items["items8"][0], json_items["items9"][0], txt_items["items10"][0]],
                [txt_items["items11"][0], txt_items["items12"][0], txt_items["items13"][0], txt_items["items14"][0], txt_items["items15"][0]],
                [txt_items["items16"][0], txt_items["items17"][0], txt_items["items18"][0], csv_items["items19"][0], csv_items["items20"][0]],
                [csv_items["items21"][0], csv_items["items22"][0], csv_items["items23"][0], csv_items["items24"][0], csv_items["items25"][0]]
            ]

        else:
            self.items = items
    
    def __repr__(self):
        return f"Vending_Machine(name={self.name}, items={self.items})"

    def check_price(item_id):
        prices = []

    def vend(items, item_id):
        pass

item_id = ['A1', 'B1', 'C1', 'D1', 'E1']

# Example usage
machine = Vending_Machine("RPL Vending Machine")

columns = ['A', 'B', 'C', 'D', 'E']
for row_idx, row in enumerate(machine.items, start=1):  # row_idx represents the row number
    for col_idx, cell in enumerate(row):  # col_idx represents the column number
        # Generate the ID based on the column and row
        item_id = f'{columns[col_idx]}{row_idx}'  # E.g., A1, B1, C1, etc.
        print(f'|| {item_id:^}: {cell:^12}', end=' ')  # Display item with ID and name
    print('||')  # end of row