import csv

with open('annual-enterprise-survey-2023-financial-year-provisional-size-bands.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Print each row

# dict
    reader = csv.DictReader(file) 
    cars = [row for row in reader]