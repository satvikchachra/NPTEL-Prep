# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:07:59 2019

@author: Satvik Chachra
"""
import random

def choose():
  words = ["alphabet","chocolate","rainbow","psychology","spirituality","dictionary","tuition","mathematics","laughter","chemistry"]
  pick = random.choice(words)
  return pick
  
def jumble(word):
  jumbled = "".join(random.sample(word,len(word)))
  return jumbled

def thank(player1,player2,pp1,pp2):
  print(player1,"your score : ",pp1)
  print(player2,"your score : ",pp2)
  print("thankyou for playing")

def play():
  player1 = input("Player1 your name: ")
  player2 = input("Player2 your name: ")
  pp1=0
  pp2=0
  turn=0
  
  while(1):
    #choose word
    picked_word = choose()
    #create question
    qn = jumble(picked_word)
    print("Question: ",qn)
    
    if(turn%2==0):
      print(player1,"your turn:")
      ans = input("Your guess: ")
      if(ans==qn):
        print("You are right")
        pp1 = pp1+1
        print("Your score",pp1)
      else:
        print("better luck next time")
        print("Your score:",pp1)
        x = int(input("Press 0 to exit or 1 to continue"))
        if(x==0):
          thank(player1,player2,pp1,pp2)
          break
    else:
      print(player2,"Your turn")
      ans = input("Your guess: ")
      if(ans==qn):
        print("you are right")
        pp2=pp2+1
        print("Your score:",pp2)
      else:
        print("Better luck next time")
        print("Your score:",pp2)
        x = int(input("press 0 to exit or 1 to continue"))
        if(x==0):
          thank(player1,player2,pp1,pp2)
          break
    turn = turn + 1

play()