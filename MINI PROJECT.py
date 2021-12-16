#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""#Miniproject:


paper/stone/scissor ===>

paper + stone ==>  paper
paper + scissor ===> scissor

stone + scissor ==> stone
stone + paper ==> paper

Scissor + stone ==> stone
Scissor + paper  ==> scissor

Computer + User 


Li1 = ["paper", "scissor", "stone"]

import random

Get input from user for number of attempts

computer_input = random.choice(Li1)
user_input = input('please enter any one value "paper", "scissor", "stone"')


Point: Computer: 5 User: 3 Tie: 2
                
Computer wins the game"""


# In[3]:


import random

comp_wins = 0
player_wins = 0
def choose_option():
    user_choice =input("choose 'Rock' , 'Paper' or 'Scissors': ")
    if user_choice in ("rock","ROCK","r","R"):
        user_choice ="r"
    elif user_choice in ("PAPER","paper","p","P"):
        user_choice ="p"
    elif user_choice in ("scissors","SCISSORS","S","s"):
        user_choice ="s"
    else:
        print("sorry i dint get your choice please choose accordingly")
        choose_option()
    return user_choice
def computer_option():
    comp_choice =random.randint(1,3)
    if comp_choice ==1:
        comp_choice = "r"
    elif comp_choice ==2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice
while True:
    print("")
    user_choice =choose_option()
    comp_choice =computer_option()
    print("")
    if user_choice =='r':
        if comp_choice =='r':
            print("you choose rock and the computer choose rock you tied")
        if comp_choice =='p':
            print("you choose rock and the computer choose paper you lose")
            comp_wins += 1
        if comp_choice =='s':
            print("you choose rock and the computer choose Scissors you win")
            player_wins +=1
    elif user_choice =='p':
        if comp_choice =='p':
            print("you choose paper and the computer choose paper you tied")
        if comp_choice =='s':
            print("you choose paper and the computer choose Scissors you lose")
            comp_wins += 1
        if comp_choice =='r':
            print("you choose paper and the computer choose rock you win")
            player_wins +=1
    if user_choice =='s':
        if comp_choice =='s':
            print("you choose Scissors and the computer choose Scissors you tied")
        if comp_choice =='r':
            print("you choose Scissors and the computer choose rock you lose")
            comp_wins += 1
        if comp_choice =='p':
            print("you choose Scissors and the computer choose paper you win")
            player_wins +=1
        print("")
        print("player wins : " + str(player_wins))
        print("computer wins : " + str(comp_wins))
        print("")
        user_choice =input("do you want to play again? (y/n)")
        if user_choice in ["Y","y","YES","yes"]:
            pass
        elif user_choice in ["N","n","NO","no"]:
            break
        else:
            break
            
        
        
        


# In[ ]:





# In[ ]:





# In[ ]:




