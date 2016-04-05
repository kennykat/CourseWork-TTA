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
