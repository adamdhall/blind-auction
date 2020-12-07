from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
auction_in_session =  True
def place_bid(name, bid):
  bids[name] = bid

while auction_in_session == True:
  name = input("What is your name?")
  bid = int(input("how much do you want to bid?"))
  place_bid(name, bid)
  more_bids = input("Are there any more biiders?(y/n)")
  if more_bids == "y":
    auction_in_session = True
    clear()
  else:
    auction_in_session = False

highest_bid = 0

for key in bids:
  if bids[key] > highest_bid:
    highest_bid = bids[key]
    highest_bidder = key

print(f"The winner is {key} with a bid of {highest_bid}.")









