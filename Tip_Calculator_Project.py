print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip = (tip / 100) + 1

price_per_person = (bill / people) * tip

print(f"Each person should pay: ${price_per_person:.2f}")
