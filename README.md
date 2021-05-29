# Blackjack Project
100days of Python's First capstone Project, TO build a code that runs blackjack simulation. No hints were used, and the project was complete in 2.5hours.

### Taken Difficulty Expert 🤯: Only used Hint 1 to complete the project.

## Our Blackjack House Rules

- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The the Ace can count as 11 or 1.
- Use the following list as the deck of cards:

- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.

## Hints 

### Hint 1: Go to this website and try out the Blackjack game:
-   https://games.washingtonpost.com/games/blackjack/
### Then try out the completed Blackjack project here:
-   http://blackjack-final.appbrewery.repl.run

### Functions used: 

- __start_deal__ : to give out starting cards, takes empty (dealer/player) list in _arg_, _returns_ list with two cards, if both comes A(i.e 11 by default) it handles last card as 1
- __deal__ : to add card when hit, handles A(1/11), takes (dealer/player) list in _arg_, _returns_ a card 
- __check_bust__ : to check if sum of the (dealer/player) list is more than 21 or not, _returns_ true if exceeds, false if not.
- __comp_check__ : serves new card to if dealer has less sum of cards., returns a new card when called.
- __result__ : checks who has more sum of cards, takes dealer and player list as _arg_, calls winner_print function with player, dealer list and winner name string
- __winner_print__ : prints the list of cards and sum of cards for both player and dealer and announces the winner.
- __usual_print__ : prints list of cards for the players, sum of cards so far, first card of dealer
