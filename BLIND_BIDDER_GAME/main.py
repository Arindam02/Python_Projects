from replit import clear
from art import logo
print(logo)

auction = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The Winner is {winner} and win bids of {highest_bid}")


  
while not bidding_finished:
    print("Welcome To The Secret Auction Program:- ")
    name = input("What is Your Name:- ")
    price = int(input("What Is Your Bid :- $ "))
    auction[name] = price
    should_continue = input("Are There Other Bidders ? yes or no :- ")
    if should_continue == "no":
      bidding_finished = True
      find_highest_bidder(auction)
    elif should_continue == "yes":
      clear()
