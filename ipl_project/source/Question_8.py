import csv
import matplotlib.pyplot as plt

MATCHES = '../dataset/matches.csv'
DELIVERIES = '../dataset/deliveries.csv'

match_id_for_2015 = []

with open(MATCHES, 'r') as file:
    matches = csv.DictReader(file)


    for _match in matches:
        match_id = _match.get('id')
        season = _match.get('season')

        
        if season == '2015' and match_id not in match_id_for_2015:
            match_id_for_2015.append(match_id)
            
# print(match_id_for_2015)

with open(DELIVERIES , 'r') as file:
    deliveries = csv.DictReader(file)
    total_run_deliveries = {}

    for delivery in deliveries:
        match_id = delivery.get('match_id')
        bowler = delivery.get('bowler')
        total_run = delivery.get('total_runs')
        
        if match_id in match_id_for_2015:
            if bowler not in total_run_deliveries:
                total_run_deliveries[bowler] = {'total' : 0, 'over' :  0}

        #calculating total runs conceded by the bowler and count of overs he delivered
        for bowler in total_run_deliveries:
            total_run_deliveries[bowler]['total'] += int(total_run)

        
    # print(total_run_deliveries)
    # print(bowler_count)
