# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:24:26 2019

@author: Satvik Chachra
"""

import random

movies = ['anand','drishyam','anbe sivam','gol maal','vikram vedha','black friday','dangal','taare zameen par']
def play():
    p1name = input("Enter player 1 name : ")
    p2name = input("Enter player 2 name : ")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while willing:
        if(turn%2==0):
            print(p1name," your turn")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            not_said = True
            while not_said:
                letter = input("Your letter : ")
                if(is_present(letter,picked_movie)):
                    #unlock
                else:
                    print("Not found")
        else:
            print(p2name," your turn")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            not_said = True
            while not_said:
                letter = input("Your letter : ")
                if(is_present(letter,picked_movie)):
                    #unlock
                else:
                    print("Not found")
        tutn = turn + 1
        
                
                
            
        