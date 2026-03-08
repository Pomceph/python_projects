print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    else:
        print("No addons have been selected.")

elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    else:
        print("No addons have been selected.")

elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3

    if extra_cheese == "Y":
        bill += 1
    else:
        print("No addons have been selected.")

else:
    print("Please select an option from the provided pizza sizes?")

print(f"Your final bill is: ${bill}")
