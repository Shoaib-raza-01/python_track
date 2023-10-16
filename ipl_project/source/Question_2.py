import csv
import matplotlib.pyplot as plt

with open('../dataset/deliveries.csv', 'r') as file:
    reader = csv.DictReader(file)
    player_run_dict = {}

    for row in reader:
        batting_team = row.get("batting_team")

        if batting_team == "Royal Challengers Bangalore":
            player = row.get("batsman")
            runs = row.get('batsman_runs')


            if player not in player_run_dict:
                player_run_dict[player]=int(runs)
            else:
                player_run_dict[player]+=int(runs)
    # print(player_run_dict)
    sorted_player_dict = dict(sorted(player_run_dict.items(), key= lambda item : item[1], reverse= True))
    # print(sorted_player_dict)
    top_10_scorer = list(sorted_player_dict.items())[:10]
    top_10_scorer = dict(top_10_scorer)
    print(top_10_scorer)
    player_name = list(top_10_scorer.keys())
    total_runs = list(top_10_scorer.values())
    plt.bar(player_name, total_runs,)
    plt.xlabel("Player")
    plt.ylabel("Total Runs")
    plt.title("Top 10 Scorers of RCB over the year")
    plt.xticks(rotation =45)
    plt.savefig("../images/top_10_of_RCB.png")