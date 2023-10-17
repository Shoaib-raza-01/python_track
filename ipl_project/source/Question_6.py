import csv
import matplotlib.pyplot as plt

MATCHES = '../dataset/matches.csv'

with open(MATCHES, 'r') as file:
    reader = csv.DictReader(file)
    won_per_team_per_year = {}

    for row in reader:
        team_name = row.get('winner')
        season = row.get('season')

        #changing name to make both the team name same
        if team_name == "Rising Pune Supergiant":
            team_name = "Rising Pune Supergiants"

        # creating dict inside a dict for every season
        if season not in won_per_team_per_year:
            won_per_team_per_year[season] = {}
        
        # checking if tetam exist in that season then add 1, else add that team and initialize it with 1
        if team_name not in won_per_team_per_year[season]:
            won_per_team_per_year[season][team_name] = 1
        else:
            won_per_team_per_year[season][team_name] += 1

    print(won_per_team_per_year)