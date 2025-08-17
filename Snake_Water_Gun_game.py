import random
computer=random.choice(["s","g","w"])
print("INSTRUCTIONS:","\n","      1:For choosing water enter 'w'","\n","      2:For choosing snake enter 's'","\n","      3:For choosing gun enter 'g'")

your_choice=str((input("Enter your choice:")))
your_choice=your_choice.lower()

my_dict={"s":"snake","g":"gun","w":"water"}
if your_choice not in my_dict:
    print ("Please choose only from g,s or w" )
    exit()
else:
    print(f"You chose {my_dict[your_choice]} and computer chose {my_dict[computer]}")


if computer==your_choice:
    print("Its a draw")
else:
    if computer=="w" and your_choice=="s":
        print("You win!")
    elif computer=="w" and your_choice=="g":
        print("You lose!")
    elif computer=="s" and your_choice=="w":
        print("You lose!")
    elif computer=="s" and your_choice=="g":
        print("You win!")
    elif computer=="g" and your_choice=="s":
        print("You lose!")
    elif computer=="g" and your_choice=="w":
        print("You win!")
    else:
        print("Something went wrong")

