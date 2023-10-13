import random

#for i in(1, 9):
    #print(i)

#def speed():
    #distance = float(input("What was the distance in meters: "))
    #time = float(input("What was the time in seconds: "))
    #speed = str(distance / time) 
    #return speed + " m/s"
    

#def test():
  #  print(speed())


#test()


while 1==1:
  RPS = ["Rock", "Paper", "Scissors"]

  player = input("Rock, Paper, or Scissors?")

  player = player.capitalize()
 
  print(player)

  computer = random.choice(RPS)

  print(computer)


  if player == "Rock" and computer == "Paper":
    print("You Lose!")
  elif player == "Rock" and computer == "Scissors":
    print("You Win!")
  elif player == "Rock" and computer == "Rock":
    print("Tie!")
  elif player == "Paper" and computer == "scissors":
    print("You Lose!")
  elif player == "Paper" and computer == "Rock":
    print("You Win!")
  elif player == "Paper" and computer == "Paper":
    print("Tie!")
  elif player == "Scissors" and computer == "Rock":
    print("You Lose!")
  elif player == "Scissors" and computer == "Paper":
    print("You Win!")
  elif player == "Scissors" and computer == "Scissors":
    print("Tie!")

  playAgain = str(input("Do you want to keep playing?"))

  if playAgain == "yes":
    
    
  else: 
    1==2












