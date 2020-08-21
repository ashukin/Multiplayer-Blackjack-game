import random

#Assign the values to dealer's cards.
def dealer_show(a):
    for i in range(len(a)):
        if dealer[i] in ('J', 'Q', 'K', '1'):
            dealer[i] = int(10)
        if dealer[i] == 'A':
            print('\n')
            print('Dealer\n')
            num = input("Do you want this Ace to be 1 or 11?\n")
            if num == '1':
                dealer[i] = int(1)
            elif num == '11':
                dealer[i] = int(11)
        if dealer[i] in (2, 3, 4, 5, 6, 7, 8, 9):
            dealer[i] = int(dealer[i])
    print('corrected dealer(for convenience)', dealer)                       # for our convenience

# Assign the values to player's cards.
def card_show(a):
    # a = player[i]
    for j in range(2):
        if a[j] in ('J', 'Q', 'K', '1'):
            a[j] = int(10)

        if a[j] == 'A':
            print('\n')
            print('Player',i,'\n')
            num = input("Do you want this Ace to be 1 or 11?\n")
            if num == '1':
                a[j] = int(1)
            elif num == '11':
                a[j] = int(11)
        if a[j] in (2,3,4,5,6,7,8,9):
            a[j] = int(a[j])
    print('corrected player(for convenience)',a)                         # for our convenience
    return (a)

play_again = ''
while play_again != 'EXIT':
    hvs = [0]  # To store all the hand values of players when they stand and then calculate the max from it
    hv = []  # To get all the hand values in integer form
    print('WELCOME BACK!!!\nTRY YOUR LUCK!!\nLETS PLAY BLACKJACK!!')
    n = int(input('Enter the number of players: '))
    player = {}
    playerbet = {}
    dealer = []
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 'A', 'J', 'Q', 'K'] * 100  # equivalent to infinite decks

    # Shuffles the deck and assigns 2 cards to each player
    for i in range(1, n + 1):
        random.shuffle(cards)
        for z in range(2):
            player[i] = [cards[z], cards[z + 1]]

    # Shuffles the deck and assigns 2 cards to the dealer
    random.shuffle(cards)
    for z in range(2):
        dealer.append(cards[z])

    dealer_bet = int(input('Dealer, how much do you wanna bet?\n'))
    print('LET THE GAME BEGIN!!')
    print('The dealer smiles and reveals his one card', dealer[0], 'and keeps the other card face down')
    for i in range(1,n+1):
        print("Player",i)
        playerbet[i] = int(input(" How much do you wanna bet?\n"))
        print('player',i,'your cards are',player[i])
        hv = card_show(player[i])                        #for our convenience
        hand_value = sum(hv)

        if hand_value == 21:
            print('Congrats! YOU WIN!! Its a blackjack!!')
            playerbet[i] += playerbet[i]*1.5
            print('The money won by you is',playerbet[i])
            break
        else:
            while(hand_value <= 21):
                ans = input("Would you like to hit or stand or double down(press d)?\n ")
                if ans.lower() == 'hit':
                    random.shuffle(cards)
                    player[i].append(cards[1])
                    print('player',i,'your cards are',player[i])
                 # Add the new card value to hand value
                    if cards[1] in ('J', 'Q', 'K', '1'):
                        hand_value += int(10)
                    if cards[1] == 'A':
                        print('\n')
                        print('Player', i, '\n')
                        num = input("Do you want this Ace to be 1 or 11?\n")
                        if num == '1':
                            hand_value += int(1)
                        elif num == '11':
                            hand_value += int(11)
                    if cards[1] in (2, 3, 4, 5, 6, 7, 8, 9):
                        hand_value += int(cards[1])

                    if hand_value > 21:  # lose condition
                        print("BUSTED!! You LOSE!!")
                        dealer_bet += playerbet[i]
                    elif hand_value == 21:  # winning condition
                        print("HURRAYY!! You WIN!!")
                        playerbet[i] += playerbet[i] * 1.5
                        print('The money won by you is', playerbet[i])
                        play_again = 'EXIT'
                    else:
                        continue
                elif ans.lower() == 'stand':
                    hvs.append(hand_value)                                 # Note that i starts from 1
                    break                                               # So that the next player's turn comes(i+1)
                elif ans.lower() == 'd':
                    playerbet[i] += playerbet[i]
                    print('You decided to double down so your bet money is doubled now which is',playerbet[i])
                    random.shuffle(cards)
                    player[i].append(cards[1])
                    print('player', i, 'your cards are', player[i])
                    print('You cannot receive any additional cards now.')
                    # Add the new card value to hand value
                    if cards[1] in ('J', 'Q', 'K', '1'):
                        hand_value += int(10)
                    if cards[1] == 'A':
                        print('\n')
                        print('Player', i, '\n')
                        num = input("Do you want this Ace to be 1 or 11?\n")
                        if num == '1':
                            hand_value += int(1)
                        elif num == '11':
                            hand_value += int(11)
                    if cards[1] in (2, 3, 4, 5, 6, 7, 8, 9):
                        hand_value += int(cards[1])
                    print('Your hand value is', hand_value)
                    if hand_value > 21:  # lose condition
                        print("BUSTED!! You LOSE!!")
                        dealer_bet += playerbet[i]
                    elif hand_value == 21:  # winning condition
                        print("HURRAYY!! You WIN!!")
                        playerbet[i] += playerbet[i] * 1.5
                        print('The money won by you is', playerbet[i])
                        play_again = 'EXIT'
                    break
    max_hv = max(hvs)               # To calculate maximum hand value among all
    ind = hvs.index(max(hvs))       # To get the index at which max value is stored
    print('Player',ind+1,'has maximum hand value which is', max_hv)         #ind+1 coz player starts from 1
    print("Now that all the players have played their chances, the dealer nods and reveals his face down card ")
    dealer_show(dealer)
    hvd = sum(dealer)
    print('Earlier card was',dealer[0])
    print("And now its a ", dealer[1], "which makes hand value of dealer ",hvd)
    if hvd < 17:
        print("The Dealer hits again.")
        random.shuffle(cards)
        dealer.append(cards[1])
        if cards[1] in ('J', 'Q', 'K', '1'):
            hvd += int(10)
        if cards[1] == 'A':
            print('\n')
            print('Player', i, '\n')
            num = input("Do you want this Ace to be 1 or 11?\n")
            if num == '1':
                hvd += int(1)
            elif num == '11':
                hvd += int(11)
        if cards[1] in (2, 3, 4, 5, 6, 7, 8, 9):
            hvd += int(cards[1])

        print("The card is a ", cards[1])
        print('The dealers cards are', dealer)
        print('Dealers hand value is',hvd)
    elif hvd > 21 and max_hv <= 21:
        print("DEALER BUSTED! PLAYER",ind+1," WINS!")
        playerbet[i] += playerbet[i]
        print('The money won by you is', playerbet[i])
    elif hvd < 21 and hvd > max_hv:
        print('DEALER HAS HANDVALUE', hvd,'GREATER THAN PLAYER. PLAYER',ind+1,' LOSES!!')
        dealer_bet += playerbet[i]
    elif hvd == max_hv:
        print("Equal Deals, no winner")
    elif hvd < max_hv:
        print("HURRAYY!! PLAYER",ind+1," WINS!!")
        playerbet[i] += playerbet[i]
        print('The money won by you is', playerbet[i])
    elif hvd == 21 and max_hv<21:
        print('PlAYER',ind+1,' LOSES!')
        dealer_bet += playerbet[i]
    else:
        print("PLAYER", ind+1," LOSES!")
        dealer_bet += playerbet[i]
    play_again = input("\nWould you like to continue? EXIT to leave\n")
print("THANK YOU FOR PLAYING.")