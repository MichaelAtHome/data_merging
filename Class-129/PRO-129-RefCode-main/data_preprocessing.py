import csv

dataset_1 = []
dataset_2 = []

with open("List of brown dwarfs - Wikipedia1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers = headers_1 
planet_data = []
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] )

with open("List of brown dwarfs - Wikipedia1.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

    