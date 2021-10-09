import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = 'election_results.csv'
# Open the election results and read the file
#with open(file_to_load) as election_data:
     # To do: perform analysis.
     #print(election_data)    
# reading csv file
with open(file_to_load, 'r') as election_data:
    # creating a csv reader object
	votes = csv.reader(election_data)
	print(votes)
	header = next(votes)
	for column in header:
		print(column)
	for row in votes:
		print(row)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write three counties to the file.
 txt_file.write("Arapahoe\nDenver\nJefferson")

