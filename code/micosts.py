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


# function: calculate the average
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



# Analyze where a majority of the individuals are from
# Wich regions are there?
uniqueRegions = []
for region in regions:
    if region not in uniqueRegions:
        uniqueRegions.append(region)
# Number of insured in each region
countRegions = {
    uniqueRegions[0]:0,
    uniqueRegions[1]:0,
    uniqueRegions[2]:0,
    uniqueRegions[3]:0
    }
for region in regions:
    if region == uniqueRegions[0]:
        countRegions[uniqueRegions[0]] += 1
    if region == uniqueRegions[1]:
        countRegions[uniqueRegions[1]] += 1
    if region == uniqueRegions[2]:
        countRegions[uniqueRegions[2]] += 1
    if region == uniqueRegions[3]:
        countRegions[uniqueRegions[3]] += 1

print("the count of individuals are from: {}".format(countRegions))

# Look at the different costs between smokers vs. non-smokers.
chargesAndSmoker = zip(chargeses, smokers)
noSmokerCharges = []
yesSmokerCharges = []
for item in chargesAndSmoker:
    if item[1] == 'no':
        noSmokerCharges.append(item[0])
    if item[1] == 'yes':
        yesSmokerCharges.append(item[0])


# print the average charges no smoker patient
print("the no smoker patient average insurance charges: {:.2f}".format(averageValue(noSmokerCharges)))

# print the average charges smoker patient
print("the smoker patient average insurance charges: {:.2f}".format(averageValue(yesSmokerCharges)))

'''
uniqueCountChildren = []
for count in childrens:
    if count not in uniqueCountChildren:
        uniqueCountChildren.append(count)
print(uniqueCountChildren)
'''

# Look at the different costs by children counts
chargesAndChildren = zip(chargeses, childrens)
noChildrenCharges, oneChildCharges, twoChildrenCharges, threeChildrenCharges, fourChildrenCharges, fiveChildrenCharges = [], [], [], [], [], []
for item in chargesAndChildren:
    if int(item[1]) == 0:
        noChildrenCharges.append(item[0])
    if int(item[1]) == 1:
        oneChildCharges.append(item[0])
    if int(item[1]) == 2:
        twoChildrenCharges.append(item[0])
    if int(item[1]) == 3:
        threeChildrenCharges.append(item[0])
    if int(item[1]) == 4:
        fourChildrenCharges.append(item[0])
    if int(item[1]) == 5:
        fiveChildrenCharges.append(item[0])

print("Average charges for number of children 0: {:.2f}".format(averageValue(noChildrenCharges)))
print("Average charges for number of children 1: {:.2f}".format(averageValue(oneChildCharges)))
print("Average charges for number of children 2: {:.2f}".format(averageValue(twoChildrenCharges)))
print("Average charges for number of children 3: {:.2f}".format(averageValue(threeChildrenCharges)))
print("Average charges for number of children 4: {:.2f}".format(averageValue(fourChildrenCharges)))
print("Average charges for number of children 5: {:.2f}".format(averageValue(fiveChildrenCharges)))