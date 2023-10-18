"""READING THE CSV and PLOTING GRAPH"""
import csv
import matplotlib.pyplot as plt

FILE = '../dataset/deliveries.csv'
BATTING_TEAM = 'batting_team'
RUNS = 'total_runs'

with open(FILE , 'r', encoding="utf-8") as file:
    teams_run_dict = {}
    data=csv.DictReader(file)

    for row in data:
        runs = row.get(RUNS)
        batting_team = row.get(BATTING_TEAM)

        if batting_team == "Rising Pune Supergiant":
            batting_team = "Rising Pune Supergiants"

        if batting_team not in teams_run_dict:
            teams_run_dict[batting_team]=int(runs)
        else:
            teams_run_dict[batting_team]+=int(runs)
    team_name = list(teams_run_dict.keys())
    total_runs = list(teams_run_dict.values())
    plt.figure(figsize=(20,15))
    plt.bar(team_name, total_runs)
    plt.xlabel("Teams")
    plt.ylabel("Total Runs")
    plt.title("Total runs scored by each team throughout the season")
    plt.xticks(rotation = 90)
    plt.savefig("../images/total_score_graph.png")
