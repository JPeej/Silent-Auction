import Art
import ClearScreen

bids = {}

# Uses a for loop to find the highest bid. The bid values are stored as values within the bids dictionary.
def find_winner(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = int(bid_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of ${highest_bid}.")
    input()

# Program loops until all users have inputted their bid. ClearScreen.clrscr() wipes the screen so the next user can't have any advantage over the previous.
while True:
    print(Art.logo)
    print("Welcome to the silent auction program.")

    name = input("What is your name? ")
    price = input("How much would you like to bid? ")

    bids[name] = price

    more_bidders = input("Are there any more bidders? Type yes or no. ").strip().lower()
    

    ClearScreen.clrscr()

    if more_bidders != "yes":
        break

ClearScreen.clrscr
find_winner(bids)