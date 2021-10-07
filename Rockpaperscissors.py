import random

c = input("Type in :\n1.rock\n2.paper\n3.scissors:\n")
prob_moves = ["rock","paper","scissors"]
r = random.choice(prob_moves)
if c == r:
    print("Its a Tie")
elif (c == 'rock' and r == 'scissors') or  (c == 'paper' and r =='rock') or (c=='scissors'and r=='paper'):
    print("You Win!")
elif (c == 'rock' and r == 'paper') or (c == 'paper' and r == 'scissors') or (c == 'scissors' and r =='rock'):
    print("You Lose!!Try Again")
else:
    print("Please enter 'rock', 'paper' or 'scissors'")
          
