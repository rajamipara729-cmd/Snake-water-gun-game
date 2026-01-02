
import random
print("select your choice: \n 1.snake \n 2.water \n 3.gun" )
number=int(input("enter a number according to your choice: "))
if number==1:
    user_choice="snake"    
elif number==2:
    user_choice="water"  
else:
    user_choice="gun" 

print("your choice is: ",user_choice)    


def game():
    b=["snake","water","gun"]
    return (random.choice(b))
computers_choice=game()
print("computer's choice is: ",computers_choice)

if user_choice == computers_choice:
    print("it is a draw")
elif user_choice == "snake" and  computers_choice == "water":
    print("you won") 
elif user_choice == "water" and  computers_choice == "gun":
    print("you won")    
elif user_choice == "gun" and  computers_choice == "snake":
    print("you won")
else:
    print("you loose")          

