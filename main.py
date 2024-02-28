
import csv
import random

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

# print(apartments[0][2])

def sort_price(apartments):
    return int(apartments[-1])


while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. -- Filter of your choice --")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        Visi_apartamenti = 0
        Visi_apartamenti = int(input("Kāds ir jūsu apartametu kārtas nummurs? Ievadiet to: "))
        print("Apartamentu kārtas nummurs: ", Visi_apartamenti)
        print(apartments[Visi_apartamenti])

        pass
    elif choice == '2':
        apartments.sort(key = sort_price, reverse = True)
        print(apartments[0:10])

        pass
    elif choice == '3':
        apartments.sort(key = sort_price, reverse = False)
        print(apartments[0:10])

        pass
    elif choice == '4':
        budzets = int(input("Ievadiet jūsu budžetu: "))
        apartment_list = []

        for apartment in apartments:
            if int(apartment[8]) < budzets:
                apartment_list.append(apartment)

        print("Rekur apartamenti pēc jūsu budžeta ", apartment_list[:20])

        pass
    elif choice == '5':
        budzets = int(input("Ievadiet jūsu budžetu: "))
        apartment_list = []

        for apartment in apartments:
            if int(apartment[8]) > budzets:
                apartment_list.append(apartment)

        print("Rekur apartamenti kuri ir lielāki nekā Jūsu budžets ", apartment_list[:20])
        pass

    elif choice == '6':
        
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("==========================")
