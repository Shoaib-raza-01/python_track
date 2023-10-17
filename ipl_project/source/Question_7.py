import csv
import matplotlib.pyplot as plt

MATCHES = '../dataset/matches.csv'
DELIVERIES = '../dataset/deliveries.csv'

with open(MATCHES, 'r') as file:
    matches = csv.DictReader(file)

    match_id_for_2015 = {}

    for _match in matches:
        match_id = _match.get('id')
        season = _match.get('season')

        if season == '2015':
            if match_id not in match_id_for_2015:
                match_id_for_2015[match_id] = match_id
            
        print(match_id_for_2015)