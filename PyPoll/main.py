# import required modules
import os
import csv
# set path to csv file
csvpath = os.path.join('.', 'files', 'election_data.csv')
# open csv file
with open(csvpath) as csvfile:
    # set deliminator and start reading file
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    print(next(csvreader))
    # print total votes
    total_months = "Total Votes: " + str(sum(1 for row in csvfile ))
    print(total_months)