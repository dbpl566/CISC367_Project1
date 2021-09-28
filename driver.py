import csv
import input_file
import analysis
from input_file import data
from analysis import checkUrls, fields, rows

#print(data) #testing inputfile output data in list

checkUrls(data)

#spreadsheet name
filename = "chat_analysis_output.csv"

#write to csv
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

