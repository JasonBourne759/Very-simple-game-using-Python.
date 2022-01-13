print("Let's play a game!")
print("You choose a number and the program will tell you the color hiding on you number.")
print("Youshould chose from 1 to 4.")

a = int(input("Make you chose here : "))

if a == 1:
    print("GREEN")

elif a == 2:
    print("RED")

elif a == 3:
    print("BLUE")

elif a == 4:
    print("")

else:
    print("Error , you didn't chose a number from 1 to 4.")