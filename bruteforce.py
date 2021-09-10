# Importing utilities
from itertools import combinations
import csv

# Define fixed variables
source = './csv/BruteForce.csv'
WALLET = 500

# Open the csv file with 'csv.DictReader'
data2 = []
all_comb = []
good_comb = []
with open(source, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for elem in reader:
        data2.append(elem)

# Declaration of variables useful for execution
all_nb_comb = 0  # allows you to complete all combinations
max_benefit = 0  # saves the benefit of the best combination
sum_coast_max_action = 0  # saves the cost of the best combination
max_action = []  # saves the best combination

# Create all the possible combinations
for n in range(0, len(data2) + 1):
    all_comb.append([i for i in combinations(data2, n)])

# Storage of each combination if cost less or equal than 500€
for comb in all_comb:
    for small_comb in comb:
        sum_cost = 0
        all_nb_comb += 1
        for element in small_comb:
            sum_cost += int(element['price'])
        if sum_cost <= WALLET:
            good_comb.append(small_comb)

# Calculation of the 2-year profit for each combination and display of the best combination
for comb in good_comb:
    sum_benefit = 0
    sum_coast = 0
    for action in comb:
        sum_benefit += int(action['price']) * (int(action['profit']) / 100)
        sum_coast += int(action['price'])
        if sum_benefit > max_benefit:
            max_benefit = sum_benefit
            max_action.clear()
            max_action.append(comb)
            sum_coast_max_action = sum_coast

# Conclusion
print("\nAprès analyse, la meilleure combinaison est :")
for elem in max_action:
    for action in elem:
        print(f"- {action['name']}")
print("\nLe coût de cette combinaison est de {:0.2f}€".format(sum_coast_max_action))
print("Le bénéfice de cette combinaison est de {:0.2f}€ sur 2 ans".format(max_benefit))

'''
# Display results
good_nb_comb = len(good_comb)
print(f"Total combinaisons : {all_nb_comb}")
print(f"Combinaisons valides : {good_nb_comb}")
print(f"Soit {(good_nb_comb / all_nb_comb) * 100} % de combinaisons <= 500€")
'''
'''     
# Afficher toutes les actions suite à l'extraction du csv
for action in data2:
    print(f"{action['Name']} : coût {action['price']} € - {action['benefit']} %")

# Calculer le bénéfice par action
for action in data2:
    benefit = int(action['price']) * (int(action['benefit']) / 100)
    print(f"Bénéfice de {action['Name']} = {benefit} €")
'''
