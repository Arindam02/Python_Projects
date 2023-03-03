############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
def deal_card():
  """return a random card form the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards)== 21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score,computer_score):
  if user_score == computer_score:
    return "Match Is Draw 🫡 🙃!!!"
  elif computer_score == 0:
    return "You Loose! Opponent Wins With A Black-jack😮"
  elif user_score == 0:
    return"You Win 😃 😁, With a Black-Jack 🏆"
  elif user_score > 21:
    return"You Loose !!🥲 🥹"
  elif computer_score > 21:
    return"You Win 😃 😁"
  elif user_score > computer_score :
    return"You Win 😃 😁"
  else:
    return"You Loose !!🥲 🥹"

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"user cards {user_cards} and score is {user_score}")
    print(f"computer first cards {computer_cards[0]}")
    
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      
      user_should_deal = input("You Want To Draw Another Card ? If YES then write 'y' If NO Then Write 'n':-  ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
    
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your Final-Cards {user_cards} and Final-Score {user_score}")
  print(f"Opponents Final-Cards {computer_cards} and Final-Score {computer_score}")
  print(compare(user_score,computer_score)) 
      
  
while input("Do You Want To Play The Game , Type 'y' Or 'n'") == 'y':
    play_game()