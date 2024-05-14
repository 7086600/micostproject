# investigating a medical insurance costs dataset

'''
Goals: ideas for analysis:
 - Find out the average age of the patients in the dataset.
 - Analyze where a majority of the individuals are from.
 - Look at the different costs between smokers vs. non-smokers.
 - Figure out what the average age is for someone who has at least one child in this dataset.
'''

'''
Data
 - csv-file which contents the dataset with: age,sex,bmi,children,smoker,region,charges
'''

import csv

# inspect the contents of data

# with open('data/insurance.csv', newline='') as ins:
#     reader = csv.reader(ins)
#     for row in reader:
#         print(row)

age, sex, bmi, children, smoker, region, charges = [], [], [], [], [], [], []

with open('data/insurance.csv', newline='') as ins:
    insDict = csv.DictReader(ins)
    for row in insDict:
        age.append(row['age'])
        sex.append(row['sex'])
        bmi.append(row['bmi'])
        children.append(row['children'])
        smoker.append(row['smoker'])
        region.append(row['region'])
        charges.append(row['charges'])

