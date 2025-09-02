import csv

def extract(filename="input.csv"):
    data = []
    with open(filename, "r") as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            data.append(line)
        return data

data = extract()
print(data)