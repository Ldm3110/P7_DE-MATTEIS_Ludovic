import time

import pandas as pd

source = './csv/BruteForce.csv'
dataset1 = './csv/dataset1_Python+P7.csv'
dataset2 = './csv/dataset2_Python+P7.csv'

WALLET = 500
sum_coast_max_action = 0
max_benefit = 0

data = pd.read_csv(source)


class Actions:
    LIST_ACTIONS = []

    def __init__(self, name, cost, benefit):
        self.name = name
        self.cost = cost
        self.benefit_percent = benefit
        self.benefit_euro = self.cost * (self.benefit_percent / 100)

        self.LIST_ACTIONS.append(self)

    def __str__(self):
        return f"- {elem.name}"

    @classmethod
    def return_list(cls):
        return cls.LIST_ACTIONS


# Tri du meilleur rendement au plus mauvais sans prise en compte de la valeur de l'action
data_sorted = data.sort_values(by='profit', ascending=False)

for action in data_sorted.index:
    if data_sorted['price'][action] < WALLET:
        if data_sorted['price'][action] <= 0:
            pass
        else:
            Actions(data_sorted['name'][action], data_sorted['price'][action], data_sorted['profit'][action])
            WALLET -= data_sorted['price'][action]
    else:
        pass

final_list = Actions.return_list()
print("\nAprès analyse, la meilleure combinaison est :")
for elem in final_list:
    print(elem)
    sum_coast_max_action += elem.cost
    max_benefit += elem.benefit_euro

print("\nLe coût de cette combinaison est de {:0.2f}€".format(sum_coast_max_action))
print("Le bénéfice de cette combinaison est de {:0.2f}€ sur 2 ans".format(max_benefit))
