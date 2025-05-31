#rock_paper_scissors
import random

rock='''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
 _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors='''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
print("welcome to rock,paper,scissors game\n")
user_choice=int(input("please enter your number\n(for rock type 0,for paper 1 and for scissors 2)\n"))

if user_choice not in [0,1,2] :
    print("Invalid choice. Game Over.")
else :
    print(game_images[user_choice])
    camputer_choices=random.randint(0,2)
    print(game_images[camputer_choices])
    
    if camputer_choices == user_choice :
        
        print("Draw")
    elif camputer_choices==0 and user_choice==1 :
        print("you win")
    elif camputer_choices==0 and user_choice==2:
        print("you loose")
    elif camputer_choices==1 and user_choice==0:
        print("you loose")
    elif camputer_choices==1 and user_choice==2 :
        print("you win")
    elif camputer_choices==2 and user_choice==0 :
        print("you win")
    elif camputer_choices==2 and user_choice==1 :
        print("you loose")

