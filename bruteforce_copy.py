import math
import csv
import pprint
import sys #K systemes
from collections import namedtuple
import time

Share = namedtuple("Share", ["name", "price", "rate", "performance"]) # Creation d'un namedtuple(Attributs)

def read_csv_file(csv_filename): #Recup des valeurs du fichier.csv indiqué en entrée et on calcul directement les performances au chargement(Car on ne peut acheter qu'une seule action de chaque)
    shares = []
    with open(csv_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader) # Skip header du csv
        for row in reader:
            name = row[0]
            price, rate = map(float, row[1:])
            share = Share(name, price, rate, round(price * (rate / 100), 2)) # 2chiffres apres la virgule
            shares.append(share)
    return shares


def knapsack01(max_investment, performances):
    if max_investment == 0 or not performances:
        return 0
    if performances[-1].price > max_investment:
        return knapsack01(max_investment, performances[:-1])
    else:
        return max(performances[-1].price + knapsack01(max_investment - performances[:-1].price, performances[:-1]), knapsack01(max_investment, performances[:-1]))


def get_max_performance(shares, max_amount):
    start = time.time()
    # Ici on trie les actions de la plus performante à la moins performante selon leurs rendement
    performances = sorted(shares, key=lambda share: share.performance,  reverse=True)
    
    # Ici on stock la performance maximum et la liste des actions qui correspondent
    max_performance = 0
    max_spent_amount = 0
    max_result = None
    i = 0
    while i < len(performances):
        if performances[i].price < 0: #Skip prix négatifs
            i += 1
            continue
        amount = max_amount - performances[i].price
        j = 0
        result = [performances[i]]
        performance = performances[i].performance
        while j < len(performances):
            if i == j:
                j += 1
                continue
            # Ici on verifie qu'il reste de l'argent à placer
            if amount >= performances[j].price and performances[j].price > 0: # Verification du dataset (valeurs Négatives)
                result.append(performances[j])
                amount -= performances[j].price
                performance += performances[j].performance
            j += 1
        # On sauvegarde la performance maximale si besoin
        if performance > max_performance:
            max_result = list(result)
            max_performance = performance
            max_spent_amount = amount
        i += 1
    end = time.time()
    # on imprime les résultats
    print(f"\nAvec {max_amount} euros d'investissement, vous pouvez maximiser votre randement en achetant : \n" )
    for share in max_result:
        print(f"> 1 action -{share.name}- à {share.price} euros à {share.rate} % sur 2 ans (Performance = {share.performance} euros)")
    print(f"\n> Performance totale : {round(max_performance, 2)} euros\n")
    print(f"Total dépensé {max_amount - max_spent_amount} euros \n")
    print(f"> Temps d'éxecution du programme : {end-start} secondes \n")

# Lancement du programme avec nom du fichier.py choixdudataset.csv et montant choisi
def main(args):
    if len(args) < 3:
        print(f"usage : {args[0]} csv_file max_amount", file=sys.stderr)
        raise SystemExit(-1)   
    csv_filename, max_amount, *_ = args[1:]
    print()
    print(f"Calcul du rendement sur le dataset : {csv_filename} avec un montant investi de : {max_amount} euros")
    shares = read_csv_file(csv_filename)
    get_max_performance(shares, int(max_amount))

if __name__ == "__main__":
    main(sys.argv)
    

    
    