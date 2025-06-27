'''
Topics covered
1.Conditional statements
2.Logical operators
3.code blocks and scope

'''
print("Welcome to Treasure Island.Your mission is to find the treasure")
choose_1 = input("Choose right or left: Type 'RIGHT' or 'LEFT':  ").lower()
if choose_1 == "right":
    print("Fall into a hole...Game Over")
else:
    choose_2 = input("Do you like to swim or wait: Type 'SWIM' or 'WAIT': ").lower()
    if choose_2 == "swim":
        print("Attacked by trout.....Game over")
    choose_3 =input("Which colour door would you like to choose: 'RED' or 'BLUE' or 'YELLOW': ").lower()
    if choose_3 == 'red':
        print("Burned by fire....Game Over")
    elif choose_3 == 'yellow':
        print("You WIN")
    elif choose_3 == "blue":
        print("Eaten by beats...Game over")
    else:
        print("Game Over")

