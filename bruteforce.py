import csv
import pprint
import sys #K systemes
from collections import defaultdict
import time

def read_csv_file(csv_filename): #Recup des valeurs du shares.csv
    shares = []
    with open(csv_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            shares.append([*map(float, row)])
    return shares

def get_max_performance(shares, max_amount):
    start = time.time()
    # Ici on trie les actions de la plus performante à la moins perforamte selon leurs rendement 
    performances = sorted( 
        [(round(price * (rate / 100), 2), price, rate) for price, rate in shares],
        key=lambda e: e[0],
        reverse=True
    )
    # Ici on stock la performance maximum et la liste des actions qui correspondent
    max_performance = 0
    max_result = None
    i = 0
    while i < len(performances):
        amount = max_amount
        j = 0 
        result = [performances[i]]
        performance = performances[i][0]
        while j < len(performances):
            if i == j:
                j += 1
                continue
            # On verifie qu'il reste de l'argent à placer
            if amount >= performances[j][1] and performances[j][1] > 0: #Verification du dataset (valeurs Négatives)
                result.append(performances[j])
                amount -= performances[j][1]
                performance += performances[j][0]
            j += 1
        # Onsauvegarde la performance maximale si besoin
        if performance > max_performance:
            max_result = result 
            max_performance = performance
        i += 1
    # on imprim les résultats
    end = time.time()
    print(f"Avec {max_amount} euros d'investissement : " )
    for share in max_result:
        print(f"1 action à {share[1]} euros à {share[2]} % sur 2 ans (Performance = {share[0]} euros)")
    print(f"Performance totale : {round(max_performance, 2)} euros")
    print(f"Temps d'éxecution du programme : {end-start} secondes")




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
    

    
    