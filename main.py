############### Blackjack Project #####################

#Difficulty Normal 😎: Used all Hints below to complete the project.

import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#to deal cards when player/dealer chosyes hit
#takes dealed list, check sum, check card is A, return with new card appended in the dealed.
def deal(dealed):
    card = random.choice(cards)
    sum_cards = sum(dealed)
    if card == 11:
        if sum_cards < 11:
            card = 1
    return card


#check if the sum exceeded 21, return false to break the loop
def checkBust(dealed):
    if sum(dealed) > 21:
        return True
    else:
        return False


#to give out starting cards
def start_deal(to_deal):
    to_deal = []
    to_deal.append(random.choice(cards))
    to_deal.append(random.choice(cards))
    if to_deal[0]==11 and to_deal[1]==11:
      to_deal[1]==1
    return to_deal


#check if dealer has less sum of cards.
def comp_check(dealer):
    new_card = deal(dealer)
    return new_card


#return string which has the name of the winner
def result(player, dealer):
    dealer_sum = sum(dealer)
    player_sum = sum(player)
    if dealer_sum > player_sum:
        winner = 'Dealer'
    elif player_sum > dealer_sum:
        winner = 'Player'
    else:
        winner = 'Draw'
    winner_print(player, dealer, winner)


def usual_print(player, dealer):
    print(f'Your Cards : {player}\n Sum so far: {sum(player)}')
    print(f"\nComputer's first card: {dealer[0]}")


def winner_print(player, dealer, name):
    print(f'Your Cards : {player}                  Sum so far: {sum(player)}')
    print(f"\nComputer's Cards: {dealer}                    Sum so far: {sum(dealer)}")
    print(f'\n \nWinner of this round is: \n {name}')


#PLAY FUNCTION!
def play():
    player = []
    dealer = []
    flag = True
    player = start_deal(player)
    dealer = start_deal(dealer)
    while (flag):
        usual_print(player, dealer)
        ans1 = input("Type 'y' to get another card, type 'n' to pass: ")
        if ans1 == 'y':
            player.append(deal(player))
            if checkBust(player):
                winner_print(player, dealer, 'Dealer')
                flag = False
                continue
        elif ans1 == 'n':
            if sum(dealer) < 16:
              dealer.append(comp_check(dealer))
            if checkBust(dealer):
                winner_print(player, dealer, 'Player')
                flag = False
                continue
            else: 
              result(player, dealer)
              flag = False


#MAIN CODE
mainFlag = True
while (mainFlag):
    print(logo)
    ans0 = input("Do you want to try your luck at Black-Jack? y/n")
    if ans0 == 'n':
        print('Thank you For playing...')
        mainFlag = False
    if ans0 == 'y':
        clear()
        play()
