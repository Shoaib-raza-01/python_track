import csv
import matplotlib.pyplot as plt

with open('../dataset/matches.csv', 'r') as file:
    data = csv.DictReader(file)
    team_count_by_season = {}
    for row in data:
        season = row.get('season')
        team1 = row.get('team1')

        #making the names same to calculate easily
        if team1 == "Rising Pune Supergiant":
            team1 = "Rising Pune Supergiants"


        if season not in team_count_by_season:
            team_count_by_season[season] = {}

        # counting the number of occurance for all the team in every season
        if team1 not in team_count_by_season[season]:
            team_count_by_season[season][team1] = 1
        else:
            team_count_by_season[season][team1] += 1

    total_match = []
    seasons = []
    for season , details in team_count_by_season.items():
        height = []
        # print(f"Season : {season}")
        seasons.append(season)
        for name , count in details.items():
            height.append(count)
            # print(f"team : {name} , count : {count}")
        total_match.append(sum(height))
    print(total_match)
    print(seasons)

    # plt.pie(total_match, labels=total_match)
    plt.bar(seasons, total_match)
    plt.title("Number of matches played per year for all the years in IPL")
    # plt.legend(
    #     loc="center left",
    #     bbox_to_anchor=(1, 0, 0.5, 1)
    # )
    plt.savefig('../images/match_played_per_year.png')
    # plt.savefig('../images/test2.png')

