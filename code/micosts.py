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
ages, sexes, bmis, childrens, smokers, regions, chargeses = [], [], [], [], [], [], []

with open('data/insurance.csv', newline='') as ins:
    insDict = csv.DictReader(ins)
    for row in insDict:
        ages.append(row['age'])
        sexes.append(row['sex'])
        bmis.append(row['bmi'])
        childrens.append(row['children'])
        smokers.append(row['smoker'])
        regions.append(row['region'])
        chargeses.append(row['charges'])


# calculate the average
def averageValue(values):
    sumValues = 0
    for value in values:
        sumValues += float(value)
    averageValue = sumValues / len(values)
    return averageValue

# print the average age
print("the average age of the patients: {:.2f}".format(averageValue(ages)))


# print the average charges
print("the average insurance charges: {:.2f}".format(averageValue(chargeses)))

uniqueRegions = []
for region in regions:
    if region not in uniqueRegions:
        uniqueRegions.append(region)

print("the regions are: {}".format(uniqueRegions))
