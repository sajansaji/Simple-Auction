import utils
dict_bid = {}
flag = True
def dict_key_value():
    name = input("Enter the name: ")
    bid_price = int(input("Bid price: $"))
    dict_bid[name] = bid_price
    
dict_key_value()

while flag:
    more_than_one = input("Is there anyone else to bid. Type 'yes' or 'no': ").lower()
    if more_than_one == "no":
        flag = False
        key = max(dict_bid, key=dict_bid.get)
        value = dict_bid[key]
        print(f"{key.title()} is the winner and the bid amount is ${value}.")
    elif more_than_one == "yes":
        dict_key_value()
