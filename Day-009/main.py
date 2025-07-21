"""
Topics Covered:
1.Dictionaries
"""

##Client Auction Program


print("Welcome to the secret aution program!!!")
bid_account = {}
def auction():
    name = (input("What is your name: "))
    amount = int(input("What's your bid?: "))
    bid_account[name] = amount

initial = True
while initial:
    auction()
    a = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if a == 'no':
        initial = False

print("The winner of the bidding is: ")
max = 0
final_winner = ""
for i in bid_account:
    if bid_account[i] > max:
        max = bid_account[i]
        final_winner = i

print("---------------------The winner and the bid amount are as follows---------------")
print(f"Name:{final_winner},Bid_amount:{max}")
