# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:35:58 2022

@author: anasakkar18
"""


# from pylab import *
import math
import numpy as np
import random

# All uncommented because this was original algorithm used to build new algorithm.
# Code used in this project is in the determineMove method.
#
# def game(pool):
#     deck = [0]*52
#     for i in range(52):
#         deck[i] = (i % 13)+1
#
#     dealerCards, playerCards = deal(deck)
#     dealerVisibleCard = dealerCards[0]
#     print("Your cards are" + str(playerCards))
#     print("The dealer's visible card is " + str(dealerVisibleCard))
#     sums = basicStrategy(playerCards, dealerVisibleCard, deck, False)
#     if len(sums) == 1 :
#         for i in sums:
#             if i > 21 :
#                 print("Busted")
#                 newPool = pool - 1
#                 return newPool
#     print("The Dealer's cards are" + str(dealerCards))
#     sumDealer = dealerTurn(dealerCards, deck)
#     for i in sums:
#         if i == 21:
#             print("You Won !!")
#             newPool = pool + 1
#         elif i <21:
#             print("dealer's cards are" + str(dealerCards))
#             print(sumDealer)
#             if i > sumDealer:
#                 print("You Won !!")
#                 newPool = pool + 1
#             elif i == sumDealer:
#                 print("It's a tie !!")
#                 newPool = pool
#             elif sumDealer > 21:
#                 print("You Won !!")
#                 newPool = pool + 1
#             else:
#                 print("Dealer Won !!")
#                 newPool = pool - 1
#         else:
#             print("Busted")
#             newPool = pool - 1
#     return newPool
#
#
# def deal(deck):
#     dealerCards = []
#     playerCards = []
#
#     for i in range(2):
#         r = random.randint(0, 51)
#         while (deck[r] == 0):
#             r = random.randint(0, 51)
#         if(deck[r] > 10):
#             dealerCards.append(10)
#         else:
#             dealerCards.append(deck[r])
#         deck[r] = 0
#
#     for i in range(2):
#         r = random.randint(0, 51)
#         while (deck[r] == 0):
#             r = random.randint(0, 51)
#         if(deck[r] > 10):
#             playerCards.append(10)
#         else:
#             playerCards.append(deck[r])
#         deck[r] = 0
#
#     return dealerCards, playerCards
#
#
# def basicStrategy(playerCards, dealerVisibleCard, deck, doubleCheck):
#     sumPlayer = sum(playerCards)
#     sums = []
#     if 1 in playerCards:
#         ace = playerCards.count(1)
#         for i in playerCards:
#             if i == 1:
#               sumPlayer+=10
#
#         while sumPlayer>21 and ace>0:
#             sumPlayer-=10
#             ace-=1
#     sums.append(sumPlayer)
#     print("Your sum",sumPlayer)
#
#     if sumPlayer >= 17:
#         print("Stand")
#         return sums
#
#     elif sumPlayer>=13:
#         if dealerVisibleCard in range(2,7):
#             print("Stand")
#             return sums
#         else:
#             playerCards = hit(playerCards,deck)
#
#     elif sumPlayer == 12 :
#         if dealerVisibleCard in range(4,7):
#             print("Stand")
#             return sums
#         else:
#             playerCards = hit(playerCards,deck)
#
#     elif sumPlayer == 11:
#         if len(playerCards)==2 and doubleCheck == False:
#             sums = double(playerCards, dealerVisibleCard, deck)
#             print("Stand")
#             return sums
#         else:
#             playerCards = hit(playerCards,deck)
#
#     elif sumPlayer == 10:
#         if dealerVisibleCard == 10 or dealerVisibleCard == 1:
#             playerCards = hit(playerCards,deck)
#         else:
#             if len(playerCards)==2 and doubleCheck == False:
#                 sums = double(playerCards, dealerVisibleCard,deck)
#                 print("Stand")
#                 return sums
#             else:
#                 playerCards = hit(playerCards,deck)
#
#     elif sumPlayer == 9:
#         if dealerVisibleCard in range(3,7):
#             if len(playerCards)==2 and doubleCheck == False:
#                 sums = double(playerCards, dealerVisibleCard, deck)
#                 print("Stand")
#                 return sums
#             else:
#                 playerCards = hit(playerCards,deck)
#         else:
#             playerCards = hit(playerCards,deck)
#
#     else:
#         playerCards = hit(playerCards,deck)
#     return basicStrategy(playerCards, dealerVisibleCard, deck, doubleCheck)
#
#
# def double(playerCards, dealerVisibleCard, deck):
#     print("double")
#     sums = []
#
#     firstCards = []
#     firstCards.append(playerCards[0])
#     firstCards = hit(firstCards,deck)
#     sumFirstCards = sum(basicStrategy(firstCards, dealerVisibleCard, deck, True))
#     sums.append(sumFirstCards)
#
#     secondCards = []
#     secondCards.append(playerCards[1])
#     secondCards = hit(secondCards,deck)
#     sumSecondCards = sum(basicStrategy(secondCards, dealerVisibleCard, deck, True))
#     sums.append(sumSecondCards)
#
#     return sums
#
#
# def hit(cards, deck):
#     print("hit")
#     r = random.randint(0, 51)
#     while (deck[r] == 0):
#         r = random.randint(0, 51)
#     if(deck[r] > 10):
#         cards.append(10)
#     else:
#         cards.append(deck[r])
#     deck[r] = 0
#    #print(cards)
#     return cards
#
#
# def dealerTurn(dealerCards, deck):
#     print("Dealer's Turn")
#     sumDealer = sum(dealerCards)
#
#     if 1 not in dealerCards:
#         if sumDealer >= 17:
#             print("Dealer's sum:", sumDealer)
#             return sumDealer
#         else:
#             dealerCards = hit(dealerCards, deck)
#             sumDealer = sum(dealerCards)
#             return dealerTurn(dealerCards, deck)
#     else:
#         if sumDealer == 11:
#             print("Dealer's sum: 21")
#             return 21
#         ace = dealerCards.count(1)
#         sumDealer = sumDealer + (10*ace)
#         if sumDealer >= 17:
#             if sumDealer >= 32 and ace>=2:
#                 sumDealer -= ace*10
#             if sumDealer > 21:
#                 sumDealer = sumDealer - 10
#                 if sumDealer >= 17:
#                     print("Dealer's sum:", sumDealer)
#                     return sumDealer
#                 else: dealerCards = hit(dealerCards, deck)
#             else:
#                 print("Dealer's sum:", sumDealer)
#                 return sumDealer
#         else: dealerCards = hit(dealerCards, deck)
#
#         sumDealer = sum(dealerCards)
#         return dealerTurn(dealerCards, deck)

# method determines the best move based on the players and the dealers cards
# logic is based on known blackjack odds
def determineMove(playerCards, dealerVisibleCard, doubleCheck):
    sumPlayer = sum(playerCards)
    if sumPlayer > 21:
        return "Bust"
    if sumPlayer == 21:
        return ";) Nice"
    sums = []
    if 1 in playerCards:
        ace = playerCards.count(1)
        for i in playerCards:
            if i == 1:
                sumPlayer += 10

        while sumPlayer > 21 and ace > 0:
            sumPlayer -= 10
            ace -= 1
    sums.append(sumPlayer)

    if sumPlayer >= 17:
        return "Stand"

    elif sumPlayer >= 13:
        if dealerVisibleCard in range(2, 7):
            return "Stand"
        else:
            return "Hit"

    elif sumPlayer == 12:
        if dealerVisibleCard in range(4, 7):
            return "Stand"
        else:
            return "Hit"

    elif sumPlayer == 11:
        if len(playerCards) == 2 and doubleCheck == False:
            return "Stand"
        else:
            return "Hit"

    elif sumPlayer == 10:
        if dealerVisibleCard == 10 or dealerVisibleCard == 1:
            return "Hit"
        else:
            if len(playerCards) == 2 and doubleCheck == False:
                return "Stand"
            else:
                return "Hit"

    elif sumPlayer == 9:
        if dealerVisibleCard in range(3, 7):
            if len(playerCards) == 2 and doubleCheck == False:
                return "Stand"
            else:
                return "Hit"
        else:
            return "Hit"

    else:
        return "Hit"

