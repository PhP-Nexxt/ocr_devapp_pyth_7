import csv
import pprint
from re import I
import sys #K systemes
from collections import defaultdict

def read_csv_file(csv_filename): #Recup des valeurs du shares.csv
    shares = []
    with open(csv_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            shares.append([*map(float, row)])
    return shares

def get_max_performance(shares, max_amount):
    # Ici on trie les actions de la plus performante à la moins perforamte selon leurs rendement 
    performances = sorted( 
        [(round(price * (rate / 100), 2), price, rate) for price, rate in shares],
        key=lambda e: e[0],
        reverse=True
    )
    
    # Ici on stock la performance maximum et la liste des actions qui correspondent
    performance = 0
    result = []
    i = 0
    amount = max_amount
    while i < len(performances):
        # On verifie qu'il reste de l'argent à placer
        if amount >= performances[i][1] and performances[i][1] > 0: #Verification du dataset (valeurs Négatives):
            result.append(performances[i])
            amount -= performances[i][1]
            performance += performances[i][0]
        i += 1
    # on imprim les résultats
    print(f"Avec {max_amount} euros d'investissement : " )
    for share in result:
        print(f"1 action à {share[1]} euros à {share[2]} % sur 2 ans (Performance = {share[0]} euros)")
    print(f"Performance totale : {round(performance, 2)} euros")




def main(args):
    if len(args) < 3:
        print(f"usage : {args[0]} csv_file max_amount", file=sys.stderr)
        raise SystemExit(-1)   
    csv_filename, max_amount, *_ = args[1:]
    print(csv_filename, max_amount)
    shares = read_csv_file(csv_filename)
    get_max_performance(shares, int(max_amount))

if __name__ == "__main__":
    main(sys.argv)
    

    
    