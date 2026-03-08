print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Sentinel Island.")
print("Your mission is to find the hidden treasure!")

choice_1 = input(
    "You have reached the island will you explore the Beach or Forest:  ")

if choice_1 == "Beach" or choice_1 == "beach":
    print("While walking the beach you were ambush by cannabals and killed. Game Over")
elif choice_1 == "Forest" or choice_1 == "forest":
    print("You enter the forest and discover a forgotten anceint temple")
    choice_2 = input(
        "You follow a light into the temple and are met with a fork in the road. Will you go Left or Right? ")

    if choice_2 == "right" or choice_2 == "Right":
        print("You stepped on a trap and were impaled. Game Over")
    elif choice_2 == "left" or choice_2 == "Left":
        choice_3 = input(
            "You reach the end of the temple and see three colored doors: Red, Purple, and Blue. Which one will you chose? ")
        if choice_3 == "Red" or choice_3 == "red":
            print("The cannabis have cornered you in the room. Game over")
        elif choice_3 == "Purple" or choice_3 == "purple":
            print("The cannabis have cornered you in the room. Game over")
        elif choice_3 == "Blue" or choice_3 == "blue":
            print("Congratulations you have found the treasure. You Won!!!!")
else:
    print("Invaild Answer")
