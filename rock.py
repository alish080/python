import random
option=["rock","paper","scissor"]
user_option=input("chose a rock,papper,scissor:")
computer_choice=random.choice(option)

print("your choise",user_option)
print("computer choise",computer_choice)

if user_option==computer_choice:
    print("its a draw")
elif user_option=="paper" and computer_choice=="rock":
    print("you win")
elif user_option=="rock"and computer_choice=="scissor":
    print("you win")
elif user_option=="scissor" and computer_choice=="paper":
    print("you win")
else:
    print("computer wins")