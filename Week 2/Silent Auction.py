# import os
# os.system("clear")

# bids = {}

# print("Welcome to the secret auction program. \n")

# more_bidders = True

# while more_bidders:
#     os.system("clear")
#     name = input("What's ya name, homie: ")
#     bid = int(input("What's ya bid, bro: "))
#     bids.update({name : bid})
#     again = input("Is there another bidder: ").lower().strip()
#     if again in ("no", "n"):
#         more_bidders = False

# for i,k in bids.items():
#     print(f"{i}     -     {k}")
# print(max(bids, key = bids.get))

def is_leap_year(year):
    if year %4 == 0:
        if year % 100 != 0:
            if year % 400 == 0:
                print("Leap year")
            elif year % 400 != 0:
                print("Not a leap year")
                

is_leap_year(400)