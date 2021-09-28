# #Debra Lymon
# #CISC367-010 : HW7
import csv
import sys


with open('merged-pythondev-help-concat-group.csv', 'r', errors = 'ignore') as file:
    file_reader = csv.reader(file)
    data = list(file_reader)
    # for row in file_reader:
    #     print(row)
