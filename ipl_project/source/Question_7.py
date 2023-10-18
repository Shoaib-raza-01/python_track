import csv
import matplotlib.pyplot as plt

MATCHES = '../dataset/matches.csv'
DELIVERIES = '../dataset/deliveries.csv'

match_id_for_2016 = []

with open(MATCHES, 'r') as file:
    matches = csv.DictReader(file)


    for _match in matches:
        match_id = _match.get('id')
        season = _match.get('season')

        # if season == '2015':
        if season == '2016' and match_id not in match_id_for_2016:
            match_id_for_2016.append(match_id)
            
# print(match_id_for_2016)

with open(DELIVERIES, 'r') as file:
    deliveries = csv.DictReader(file)
    team_and_extra_run_2016 ={}
    for delivery in deliveries:
        match_id = delivery.get('match_id')
        batting_team = delivery.get('batting_team')
        extras = delivery.get('extra_runs')
        if match_id in match_id_for_2016:
            if batting_team not in team_and_extra_run_2016:
                team_and_extra_run_2016[batting_team] = int(extras)
            else:
                team_and_extra_run_2016[batting_team] += int(extras)
    
    # print(team_and_extra_run_2016)

    plt.figure(figsize=(12,10))
    plt.bar(team_and_extra_run_2016.keys(),team_and_extra_run_2016.values())
    plt.xlabel("Teams")
    plt.ylabel("Extra Runs")
    plt.title("Team wise extra runs 2016")
    plt.xticks(rotation = 90)
    plt.savefig('../images/extra_runs_per_team_2016.png')