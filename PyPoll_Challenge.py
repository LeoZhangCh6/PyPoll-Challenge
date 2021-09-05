import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
county_options = []
candidate_votes = {}
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""
winning_country_count = 0
winning_country_percentage = 0.


with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        total_votes += 1
        county_name, candidate_name = row[1], row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0

        candidate_votes[candidate_name] += 1
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.

    for county_name in county_options:
        county_vote = county_votes[county_name]
        vote_percentage = float(county_vote) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({county_vote:,})\n")
        print(county_results)
        txt_file.write(county_results)

        if county_vote > winning_country_count:
            winning_country_count = county_vote
            winning_county = county_name
            winning_county_percentage = float(county_vote) / float(total_votes) * 100

    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
