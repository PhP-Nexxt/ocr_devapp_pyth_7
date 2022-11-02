import random
import sys
import csv


def generate_shares(num_shares):
    list_shares = []
    for i in range(num_shares):
        share = (f"Action-{i+1}", random.randint(1, 100), random.randint(1, 20))
        list_shares.append(share)
    return list_shares
    

def write_shares_file(random_shares_file, list_shares):
    with open(random_shares_file, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["Action", "Cout par action", "Benefice"])
        for share in list_shares:
            writer.writerow(share)


# python3 createshares.py randomshares.csv 10000
def main(args):
    if len(args) < 3:
        print(f"usage : {args[0]} csv_file num_shares", file=sys.stderr)
        raise SystemExit(-1)   
    csv_filename, num_shares, *_ = args[1:] #Prend le deuxieme et troisieme argument en entrée
    shares = generate_shares(int(num_shares))
    write_shares_file(csv_filename, shares)
    
    

if __name__ == "__main__":
    main(sys.argv)