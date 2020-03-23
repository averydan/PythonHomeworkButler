# import required modules
import os
import csv
import operator
# set path to csv file
csvpath = os.path.join('.', 'files', 'election_data.csv')
# open csv file
with open(csvpath) as csvfile:
    # set deliminator and start reading file
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    next(csvreader)
    # print total votes
    total_votes = sum(1 for row in csvfile )
    print(f"Total Votes: {total_votes}")
    print()
    candidates = {}
    csvfile.seek(0)
    next(csvreader)
    for row in csvreader:
        if row[2] in candidates:
            candidates[row[2]]["Votes"] += 1
        else:
            candidates.update({row[2]: {"Votes": 1}})
for i in candidates:
    candidates[i].update({"Percentage": candidates[i]["Votes"] / total_votes * 100})
print("List of Candidates:")
for i in candidates:
    print(i)
print()
print("Each Candidates percetnage of votes:")
for i in candidates:
    print(f"{i} received {round(candidates[i]['Percentage'])} of votes.")
print()
print("Each Candidate recieved this many votes:")
for i in candidates:
    print(f"{i} received {round(candidates[i]['Votes'])} votes.")
print()
vote_counts = {}
for i in candidates:
    vote_counts.update({i : candidates[i]['Votes']})
print(f"{max(vote_counts.items(), key=operator.itemgetter(1))[0]} won the vote.")