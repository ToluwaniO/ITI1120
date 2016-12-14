#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120 
# Assignment Number 3 Game Question

# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

     dealer = deck[0:len(deck)//2]
     other = deck[len(deck)//2:len(deck)]

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    #print(ranks, '\n\n', l, '\n\n') 

    for i in ranks:
        pairs = []
        for j in range (len(l)):
            if i in l[j]:
                pairs.append(l[j])

        #print(pairs, '\n\n')

        if len(pairs) > 1 and len(pairs)%2== 0:
            for i in pairs:
                l.remove(i)
            #print(pairs, '\n\n')
        elif len(pairs) > 1 and len(pairs)%2!= 0:
            for i in range(len(pairs)-1):
                l.remove(pairs[i])
            #print(l, '\n\n')


    no_pairs = l[:]

    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    x = ''
    for i in deck:
        x += i + '  '

    print('\n', x, '\n')

    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     
     try:
         choice = int(input('\nGive me a number that is between 1 and ' +  str(n) + ': '))

     except:
         choice = int(input('Invalid input!' + 'Give me a number that is between 1 and ' +  str(n) + ': '))

         while choice < 1 or choice > n:
            choice = int(input('Invalid input!' + 'Give me a number that is between 1 and ' +  str(n) + ': '))

     return choice -1
             
         
         

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     x = 0

     y = True
     
     while y:
         if x%2 == 0:

             print(50*'*','\nYour turn \nYour current deck of cards is\n')
             print_deck(human)

             #GET INPUT
             if(len(dealer)>1):
                 print('I have', len(dealer), 'cards. If 1 stands for my first card and\n')
                 print(len(dealer), 'stands for my last card, which of my cards would you like?')
                 choice = get_valid_input(len(dealer))
             elif len(dealer) == 1:
                 print('I have', len(dealer), 'card left.')
                 choice = 0
             else:
                 choice = get_valid_input(len(dealer))
                 
             print('\nHere is my card,', dealer[choice])

             human.append(dealer.pop(choice))

             #print decck again
             print('\nHere is your new deck')
             print_deck(human)
             
             human = remove_pairs(human)

             print('\nAfter removing pairs and shuffling, your deck of cards is: ')
             print_deck(human)

         else:
             print(50*'*','\nMy turn\n')

             #GET INPUT

             choice = random.randint(1, len(human))

             if choice >= 4:
                 print('I took your ' + str(choice) + 'th card')
             elif choice == 3:
                 print('I took your ' + str(choice) + 'rd card')
             elif choice == 2:
                 print('I took your ' + str(choice) + 'nd card')
             elif choice == 1:
                 print('I took your ' + str(choice) + 'st card')
                 

             dealer.append(human.pop(choice-1))

             dealer = remove_pairs(dealer)

         x += 1

         if len(human) < 1:
             print('You won, you have no cards left')
             y = False
         elif len(dealer) < 1:
             print('I won, I have no cards left')
             y = False
         

             
             
	
	 

# main
play_game()
