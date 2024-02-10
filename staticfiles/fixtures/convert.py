import csv, json
input_json_file='inventory.json'
output_csv_file='inventory.csv'
input = open(input_json_file)
data = json.load(input)
input.close()
output = csv.writer(open(output_csv_file,'w'))
output.writerow(data[0].keys())  # header row
for row in data:
    output.writerow(row.values())