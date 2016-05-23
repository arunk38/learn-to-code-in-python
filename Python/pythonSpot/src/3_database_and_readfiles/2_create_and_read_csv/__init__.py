# creating a csv file
import csv
from operator import gt

names = []
jobs = []

with open('persons.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name', 'Profession'])
    filewriter.writerow(['Derek', 'Software Developer'])
    filewriter.writerow(['Steve', 'Software Developer'])
    filewriter.writerow(['Paul', 'Manager'])


# read from a spread sheet

with open('persons.csv', 'r') as f:
    reader = csv.reader(f)

    # lists for our data.
    names = []
    jobs = []

    rowNr = 0
    for row in reader:
        if row and rowNr != 0:
            names.append(row[0])
            jobs.append(row[1])
        rowNr = 1

print(names)
print(jobs)