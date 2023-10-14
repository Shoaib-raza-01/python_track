# import csv
# with open('../dataset/deliveries.csv', 'r') as deliveries:
#     dictReader = csv.DictReader(deliveries)
#     # i = 0
#     teams =[]
#     for row in dictReader:
#         # teams = set(row['batting_team'])
#         # if row['batting_team'] == "Sunrisers Hyderabad":
#         #     print("yess")
#         #     i += 1
#         # else:
#         #     continue
#         print(row['batting_team'], row['TOTAL_RUNS'])
    # print(teams)



import csv

FILE = '../dataset/deliveries.csv'
FIELF_NAME = 'batting_team'

unique_values = set()
runs_of_diff_teams ={}

with open(FILE, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    TOTAL_RUNS = 0

    for row in reader:
        value = row.get(FIELF_NAME)
        runs = row.get('total_runs')

        if value == "Chennai Super Kings":
            TOTAL_RUNS += int(runs)
            unique_values.add(value)

    # for value in unique_values:
    #     print(value)

    print(TOTAL_RUNS)