# import os
import os, csv

# the path to the script
currentPath = os.path.dirname(os.path.abspath(__file__))
print currentPath

# make the spreadsheet path
outputCsv = currentPath + '/spreadsheet.csv'
print outputCsv

# open the file
csvFile = open(outputCsv, "wb")

# # inproper way of writing to a file
# csvFile.write('Testing')
# csvFile.close()

# create writer object
writer = csv.writer(csvFile, delimiter=',')
# remember to use module csv

# data to go in csv
row_1 = [1, "Row 1", 123]
row_2 = [2, "Row 2", 456]
row_3 = [3, "Row 3", 789]

# .writerow()
# write rows to csv

writer.writerow(row_1)
writer.writerow(row_2)
writer.writerow(row_3)
