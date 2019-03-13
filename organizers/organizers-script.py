names = []
speakers = []
organisations = []

import csv

with open('partners.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        speakers.append(row[1])
        speakers.append(row[1])
        organisations.append(row[2])
        organisations.append(row[2])
print(speakers,organisations)
sIndex = 0
oIndex = 0
even = False
newSVG = []
for i in range(0,100):
    with open ("partners.svg", "r") as myfile:
        data=myfile.readlines()
        currentSVG = []

    try:
        for line in data:
            if 'Name' in line:
                line = line.replace('Name', speakers[sIndex])
                print(line)
                sIndex = sIndex+1
            if 'Organization' in line:
                line = line.replace('Organization', organisations[oIndex])
                print(line)
                oIndex = oIndex + 1

            currentSVG.append(line)

        newSVG.append(currentSVG)

        with open("output" + str(i) + ".svg", "w") as output:
            for line in newSVG[i]:
                output.write(line)
    except:
        print('error')


# print(newSVG)


