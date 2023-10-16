import csv
import matplotlib.pyplot as plt

with open('../dataset/umpires.csv', 'r') as file:
    umpire = csv.DictReader(file)
    country_count ={}

    for row in umpire:
        country = row.get(' country')

        if country != ' India':  # Excluding India
            if country not in country_count:
                country_count[country] = 1
            else:
                country_count[country] += 1

    # print(country_count)
    country_name = list(country_count.keys())
    count = list(country_count.values())
    plt.figure(figsize=(15,10))
    plt.bar(country_name, count)
    plt.xlabel("Country Name")
    plt.ylabel("Total Count")
    plt.title("Number of Umpires from different countries excluding INDIA")
    plt.xticks(rotation = 90)
    plt.savefig("../images/umpires_from_diff_country.png")