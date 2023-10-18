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

    # print(won_per_team_per_year)

    seasons = list(won_per_team_per_year.keys())
    teams = list(set(team for season in won_per_team_per_year.values() for team in season))

    # Initialize a list to keep track of the bottom values for each team
    bottom = [0] * len(seasons)

    plt.figure(figsize=(10, 6))

    for team in teams:
        heights = [won_per_team_per_year[season].get(team, 0) for season in seasons]
        plt.bar(seasons, heights, label=team, bottom=bottom)
        bottom = [h1 + h2 for h1, h2 in zip(bottom, heights)]

    plt.xlabel('Season')
    plt.ylabel('Number of Wins')
    plt.title('Stacked Bar Chart of Matches won per team per season')

    plt.legend(
        loc="center left",
        title = "teams",
        bbox_to_anchor=(1, 0, 0.5, 1))
    plt.savefig('../images/won_per_team_per_year.png')