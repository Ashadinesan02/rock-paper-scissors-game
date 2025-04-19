
# Rock Paper Scissors Game
#======================================================================

import random
from getpass import getpass

# function for player vs computer game

def player_vs_computer():
    
  choices = ["rock", "paper", "scissors"]

  player_score = 0

  computer_score = 0

  max_points = int(input("Enter the max points you want to play: "))


  i = 0 

  while (i < max_points):

    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if player_choice not in choices:

        print(f"invalid choice.try again")

        continue


    computer_choice = random.choice(choices)


    print(f"Player: {player_choice}")

    print(f"Computer: {computer_choice}")


    if player_choice == computer_choice:
      print("It's a tie!")

    elif player_choice == 'rock' and computer_choice == 'scissors':
      print("You win in this round")
      player_score+=1

    elif player_choice == 'paper' and computer_choice == 'rock':
      print("You win in this round")
      player_score+=1

    elif player_choice == 'scissors' and computer_choice == 'paper':
      print("You win in this round")
      player_score+=1

    else:
      print("You lose in this round")
      computer_score+=1

    
    i = i + 1

  print()

  print(f"Game over!!!!!!")

  if player_score>computer_score:

    print(f"Congratulations! You win\nfinal score: player:{player_score}  computer:{computer_score}")

  elif player_score<computer_score:

    print(f"You lose!!\n final score: player:{player_score}  computer:{computer_score}")

  else:

    print(f"It's a tie match!!\n final score: player:{player_score}  computer:{computer_score}")


# function for player vs player game

def player_vs_player():
    
    
  choices = ["rock", "paper", "scissors"]

  player1_score = 0

  player2_score = 0

  max_points = int(input("Enter the max points you want to play:"))


  i = 0 

  while (i < max_points):

    while True:

      print("Player1,enter your choice (rock,paper,scissors): ")

      player1_choice = getpass().lower()

      if player1_choice in choices:

        break

      print(f"invalid choice.try again")

        
    while True:

      print(f"Player2,enter the choice (rock, paper, scissors): ")

      player2_choice = getpass().lower()

      if player2_choice in choices:

        break

      print(f"invalid choice.try again")

        

    print(f"Player1: {player1_choice}")

    print(f"Player2: {player2_choice}")


    if player1_choice == player2_choice:
      print("It's a tie!")

    elif player1_choice == 'rock' and player2_choice == 'scissors':
      print("Player1 win in this round")
      player1_score+=1

    elif player1_choice == 'paper' and player2_choice == 'rock':
      print("Player1 win in this round")
      player1_score+=1

    elif player1_choice == 'scissors' and player2_choice == 'paper':
      print("Player1 win in this round")
      player1_score+=1

    else:
      print("Player2 win in this round")
      player2_score+=1

    
    i = i + 1

  print()

  print(f"Game over!!!!!!")

  if player1_score>player2_score:

    print(f"Congratulations! Player1 wins\nfinal score: player1:{player1_score}  player2:{player2_score}")

  elif player1_score<player2_score:

    print(f"Congratulations! Player2 wins\n final score: player2:{player2_score}  player1:{player1_score}")

  else:

    print(f"It's a tie match!!\n final score: player1:{player1_score}  player2:{player2_score}")




# main game loop

def game():

  print(f"Welcome to Rock Paper Scissor game!!")

  while True:

    print(f"Choose the game mode: \n 1.player vs computer \n 2.player vs player")

    choice = int(input("Enter 1 or 2: "))

    if choice == 1:

      player_vs_computer()

    elif choice == 2:

      player_vs_player()

    else:

      print(f"Invalid option.Please choose 1 or 2.")

    
    play_again = input("Do you want to play again? (y/n):").lower()

    if play_again != 'y':

      print(f"Thanks for playing!")

      break

    elif play_again == 'y':

      continue

    else:

      print(f"Invalid option.Please enter y/n.")


game()


  


















