# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 10:33:07 2023

@author: LousadaR
"""

from art import logo
import os
print(logo)

bidding_finished = False
auction_dict = {}

def calculate_winner(bidding_record):
    hihest_bid=0
    winner = ""
    for bidder in bidding_record:
        bid_ammount = bidding_record[bidder]
        if bid_ammount > hihest_bid:
            hihest_bid = bid_ammount
            winner = bidder
         
    print(f"The Auction winner is {winner} wth a bid of {hihest_bid}€.")
    
        
        

while not bidding_finished:
    name = input("What is you name?\n")
    bid_price = int(input("How much do you want to bid?\n"))
    auction_dict[name] = bid_price
    ask_if_go_on = input("Is there any other user to bid? Type ''yes'' or ''no''.\n")
    if ask_if_go_on == "no":
        bidding_finished = True
        calculate_winner(auction_dict)
    #else:
        #os.system('cls')
        

