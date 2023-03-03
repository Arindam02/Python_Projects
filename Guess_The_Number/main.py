
from random import randint
from art import logo
Easy_Level_Turn = 10
Hard_Level_Turn = 5

def game():  
  print(logo)
  def check_answer(guess , answer,turns):
    if guess > answer:
      print("Too High")
      return turns-1
    elif guess < answer:
      print("Too Low")
      return turns-1
    else:
      print(f"You got it! The answer was {answer}")
  
  def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':- ")
    if level == "easy":
      return Easy_Level_Turn
    else:
      return Hard_Level_Turn
  
      
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1,100)
  
  turns = set_difficulty()
  
  guess = 0
  while guess != answer:
    
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make A Guess:- "))
    turns = check_answer(guess , answer,turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return

game()