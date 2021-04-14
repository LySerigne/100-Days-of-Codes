from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
active = True
bids = {}
def find_winner(bids):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bid is {winner} with ${highest_bid}")

while active:   
    name = input("Enter your name to begin: ")
    price = int(input("Enter your price: \n $ "))
    bids[name] = price
    
    action = input("Are there other user who want to bid? 'yes' or 'no' ").lower()
    if action == "no":
        active = False
        find_winner(bids)
    elif action == "yes":
        clear()
    
    





