import os
import auction_art

bidders = {}
while True:
    name = input("What's your name? ")
    bid_amount = int(input("What your bid amount? $"))
    bidders[name] = bid_amount
    other_user = input("Is there any other person? 'Yes' or No' ").lower()
    if other_user == 'yes':
        os.system('cls')
        continue
    else:
        winner = max(bidders, key= bidders.get)
        print(f"Winner is {winner} with the bid amount of ${bidders[winner]}")
        break
