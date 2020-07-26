import os
import csv

csvpath = os.path.join("Resources/election_data.csv")
with open(csvpath, 'r') as csvfile:
    pypoll_csv = csv.reader(csvfile, delimiter = ',')
    csv_header = next(pypoll_csv)

    total_votes_lst = []
    candidates_lst = []
    candidates = []
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    pct_counts = []
    

    for row in pypoll_csv:
        total_votes_lst.append(int(row[0]))
        candidates_lst.append(row[2])
        if row[2] == "Khan":
            khan_votes += 1
        if row[2] == "Correy":
            correy_votes += 1
        if row[2] == "Li":
            li_votes += 1
        if row[2] == "O'Tooley":
            otooley_votes += 1
vote_count_lst = [khan_votes, correy_votes, li_votes, otooley_votes]
total_votes = len(total_votes_lst)
for name in candidates_lst:
    if name not in candidates:
        candidates.append(name)
for count in vote_count_lst:
    pct_counts.append("{0:.0f}%".format((count/total_votes)*100))

results_lst = list(zip(candidates, pct_counts, vote_count_lst))

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results_lst:
    print(f"{result[0]}: {result[1]} ({result[2]})")
print("-------------------------")
for result in results_lst:
    if result[2] == max(vote_count_lst):
        print(f"Winner: {result[0]}")
print("-------------------------")


file = open("export.txt", "w")
file.write("Election Results" + "\n")
file.write("-------------------------" + "\n")
file.write(f"Total Votes: {total_votes}" + "\n")
file.write("-------------------------" + "\n")
for result in results_lst:
    file.write(f"{result[0]}: {result[1]} ({result[2]})" + "\n")
file.write("-------------------------" + "\n")
for result in results_lst:
    if result[2] == max(vote_count_lst):
        file.write(f"Winner: {result[0]}")
file.close()