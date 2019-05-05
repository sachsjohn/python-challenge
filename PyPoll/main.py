import os
import csv

budget_path = os.path.join("Resources", "election_data.csv")

with open(budget_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Priming the variables we will be using

    votes = 0
    candidates = []
    k_votes = 0
    c_votes = 0
    l_votes = 0
    o_votes = 0

    for row in csv_reader:

        # Tallying the votes
        votes = votes + 1
        
        # Compiling the candidate list
        if row[2] not in candidates:
            candidates.append(row[2])

        # Tallying votes by candidate
        if row[2] == 'Khan':
            k_votes = k_votes + 1
        elif row[2] == 'Correy':
            c_votes = c_votes + 1
        elif row[2] == 'Li':
            l_votes = l_votes + 1
        elif row[2] == "O'Tooley":
            o_votes = o_votes + 1

    print(candidates)
    
    # Declaring the Winner
    if k_votes > c_votes and k_votes > l_votes and k_votes > o_votes:
        winner = candidates[0]
    elif c_votes > k_votes and c_votes > l_votes and c_votes > o_votes:
        winner = candidates[1]
    elif l_votes > k_votes and l_votes > c_votes and k_votes > o_votes:
        winner = candidates[2]
    elif o_votes > k_votes and o_votes > c_votes and o_votes > l_votes:
        winner = candidates[3]


    # Printing
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votes}")
    print("-------------------------")
    print(f"{candidates[0]}: {round(k_votes / votes * 100, 3)}% ({k_votes})")
    print(f"{candidates[1]}: {round(c_votes / votes * 100, 3)}% ({c_votes})")
    print(f"{candidates[2]}: {round(l_votes / votes * 100, 3)}% ({l_votes})")
    print(f"{candidates[3]}: {round(o_votes / votes * 100, 3)}% ({o_votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")


    # Printing to txt file
    text = open("PyPoll.txt","w+")
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {votes}\n")
    text.write("-------------------------\n")
    text.write(f"{candidates[0]}: {round(k_votes / votes * 100, 3)}% ({k_votes})\n")
    text.write(f"{candidates[1]}: {round(c_votes / votes * 100, 3)}% ({c_votes})\n")
    text.write(f"{candidates[2]}: {round(l_votes / votes * 100, 3)}% ({l_votes})\n")
    text.write(f"{candidates[3]}: {round(o_votes / votes * 100, 3)}% ({o_votes})\n")
    text.write("-------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("-------------------------\n")