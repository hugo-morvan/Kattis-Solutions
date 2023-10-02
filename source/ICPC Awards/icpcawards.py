n = int(input())

# Create a set to keep track of universities
universities = set()

# Create a list to store winners
winners = []

# Loop through all n teams
for i in range(n):
    # Get the university and team name
    university, team = input().split()
    
    # If we haven't seen this university before, add it to the set and add the team to the winners list
    if university not in universities:
        universities.add(university)
        winners.append(university + " " + team)
    
    # If we've already seen this university before, skip it
    else:
        continue
    
    # If we have 12 winners, we can stop checking teams
    if len(winners) == 12:
        break

# Print out the first 12 winners
for winner in winners:
    print(winner)
