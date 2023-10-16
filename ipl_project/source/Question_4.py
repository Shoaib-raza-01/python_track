import csv
import matplotlib.pyplot as plt

with open('../dataset/matches.csv', 'r') as file:
    data = csv.DictReader(file)
    team_count_by_season = {}
    for row in data:
        season = row.get('season')
        team1 = row.get('team1')
        team2 = row.get('team2')

        if season not in team_count_by_season:
            team_count_by_season[season] = {}

        # counting the number of occurance for all the team in every season
        if team1 not in team_count_by_season[season]:
            team_count_by_season[season][team1] = 1
        else:
            team_count_by_season[season][team1] += 1

        if team2 not in team_count_by_season[season]:
            team_count_by_season[season][team2] = 1
        else:
            team_count_by_season[season][team2] += 1
        
    print(team_count_by_season)
    season = list(team_count_by_season.keys())
    inner_dict = list(team_count_by_season.values())
    
    print(inner_dict)












    # team_data = {}
    # year_data = {}

    # # Iterate through the outer dictionary
    # for year, inner_dict in team_count_by_season.items():
    #     # Store the year's data
    #     year_data[year] = inner_dict
        
    #     # Iterate through the inner dictionary
    #     for team, value in inner_dict.items():
    #         # Store data for each team
    #         if team not in team_data:
    #             team_data[team] = {}
    #         team_data[team][year] = value
    # print(team_data.keys())
    # print()
    # print()
    # print()
    # print(team_data.values())