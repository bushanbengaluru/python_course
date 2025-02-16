#program to manage multiple laptop inventory
current_inventory = []
while True:
    print("=="*25)
    print("\n\rSELECT FROM BELOW MENU\n")
    print("1. Add Products to inventory")
    print("2. Remove Products to inventory")
    print("3. Display current inventory")
    print("4. Exit Program\n")
    try:
        choice = int(input("Enter your selection between 1 to 4: "))
        print("--"*25)
        if choice == 1:
            prod = input("Enter product name to add to inventory: ")
            print()
            current_inventory.append(prod)
            print(prod, " - ADDED TO INVENTORY..!!\n")
        elif choice == 2:
            prod = input("Enter product name to remove from inventory: ")
            if prod in current_inventory:
                print()
                current_inventory.remove(prod)
                print(prod, " - REMOVED FROM INVENTORY..!!\n")
            else:
                print()
                print(prod, "\n - PRODUCT NOT IN INVENTORY..!!\n")
        elif choice == 3:
            print("CURRENT INVENTORY:")
            print()
            for i in current_inventory:
                print([i], end=' ')
            print("\n")
        elif choice == 4:
            break
        else:
            raise ValueError    
    except ValueError:
        print("\n\rERROR: INVALID SELECTION, TRY AGAIN..!!")
        print("\n\rENTER VALID SECTION BETWEEN 1 to 4..!!\n")
        continue