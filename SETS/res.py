
file = open("menu.txt", "r")

menu = {}
print("------ MENU ------")

for line in file:
    item_id, name, price = line.strip().split(",")
    menu[int(item_id)] = (name, int(price))
    print(item_id + ".", name, "-", price)

file.close()

total = 0

while True:
    choice = int(input("\nEnter Item Number (0 to stop): "))

    if choice == 0:
        break

    if choice in menu:
        quantity = int(input("Enter Quantity: "))
        item_name, item_price = menu[choice]
        amount = item_price * quantity
        total += amount
        print(item_name, "added. Amount:", amount)
    else:
        print("Invalid choice")

print("\n----- Final Bill -----")
print("Total Amount:", total)
