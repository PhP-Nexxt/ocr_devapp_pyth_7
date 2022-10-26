import csv
import sys #Recupere les éléments de la console
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem


def display_main_menu(shares, csv_name):
    menu = ConsoleMenu("List", "shares" )
    menu.append_item(FunctionItem("Create share", create_share, [shares]))
    menu.append_item(FunctionItem("Read shares file", read_shares_file, [shares]))
    menu.append_item(FunctionItem("Update share", update_share, [shares]))
    menu.append_item(FunctionItem("Delete share", del_share, [shares]))
    menu.append_item(FunctionItem("Save shares", write_csv_file, [shares, csv_name]))
    
    menu.show()

def read_csv_file(csv_filename): #Recup des valeurs du shares.csv
    shares = []
    with open(csv_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            shares.append([*map(int, row)])
    return shares


def create_share(shares):
    
    stockprice = int(input("Stock Price ? : "))
    performance = int(input("Performance (2years) ? : "))
    shares.append([stockprice, performance])
    
    
def read_shares_file(shares):
   
    for share in shares:
        print(share)
    input("Press Enter to continue... ")

def update_share(shares):
    print("Update share")
    input("Press Enter to continue... ")

def del_share(shares):
    print("Delete shares")
    input("Press Enter to continue... ")


def write_csv_file(shares, csv_filename):
    with open(csv_filename, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for share in shares:
            writer.writerow(share)
    


def main(args):
    if len(args) < 2:
        print(f"usage : {args[0]} csv_file", file=sys.stderr)
        raise SystemExit(-1)   
    csv_filename = args[1]
    shares = read_csv_file(csv_filename)
    display_main_menu(shares, csv_filename)
    print(shares)

if __name__ == "__main__":
    main(sys.argv)