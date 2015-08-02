# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

# background image: 1600x1200 
background_img = simplegui.load_image("https://www.dropbox.com/s/rlat6qe9705olwt/cardgamebg1.jpg?dl=1")
#background_img = simplegui.load_image("https://www.dropbox.com/s/9646bn0mryx1jqv/cardgamebg.jpg?dl=1")

width = 1600
height = 1200

cvs_width = 1600 * 0.6
cvs_height = 1200 * 0.6

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    
cards_back = simplegui.load_image("https://www.dropbox.com/s/9xu2zd0dt0aqfua/cardback.png?dl=1")
# initialize some useful global variables
in_play = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# helper functions

# compare 2 hand values, add/subtract chips and return outcome
def compare(dp, pp, dchips, pchips, bets):
    if dp < pp:
        oc = "Dealer:" + str(dp) + " points, You:" + str((pp)) + " points, You Win!"
        if dp == 21:
            pchips += bets * 2
            dchips -= bets * 2
        else:
            pchips += bets
            dchips -= bets
    else:
        oc = "Dealer:" + str(dp) + " points, You:" + str((pp)) + " points, Dealer Win!"
        if pp == 21:
            dchips += bets * 2
            pchips -= bets * 2
        else:
            dchips += bets
            pchips -= bets
    return oc, dchips, pchips
        

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        string = ""
        for i in range(len(self.hand)):
            string += str(self.hand[i])
            string += " "
        return "Hand Cotains: " + string

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.value = 0
        handlst = [c.get_rank() for c in self.hand]
        for c in self.hand:
            self.value += VALUES[c.get_rank()]
        if "A" not in handlst:
            return self.value
        else:
            if (self.value + 10) <= 21:
                return self.value + 10
            else:
                return self.value
   
    def draw(self, canvas, pos):
        for c in self.hand:
            c.draw(canvas, pos)
            pos[0] += 88
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for c in SUITS:
            for r in RANKS:
                self.deck.append(Card(c, r))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        string = ""
        for i in range(len(self.deck)):
            string += str(self.deck[i])
            string += " "
        return string



#define event handlers for buttons
def plus10():
    global player_bet, in_play
    if player_bet + 10 <= player_chips and in_play:
        player_bet += 10
    
    
def plus100():
    global player_bet, in_play
    if player_bet + 100 <= player_chips and in_play:
        player_bet += 100

def allin():
    global player_bet, player_chips, in_play
    if player_chips > 0 and in_play:
        player_bet = player_chips
    
    
def reset():
    global player_chips, computer_chips, in_play
    in_play = False
    player_chips = 1000
    computer_chips = 1000
    deal()

    

def deal():
    global outcome, in_play, cur_deck, computer_hand, player_hand, player_bet, player_chips, player_bet, computer_chips
    if in_play:
        player_chips -= player_bet
        computer_chips += player_bet
    player_bet = 10
    outcome = "Hit or Stand?"
    computer_hand = Hand()
    player_hand = Hand()
    cur_deck = Deck()
    cur_deck.shuffle()
    computer_hand.add_card(cur_deck.deal_card())
    player_hand.add_card(cur_deck.deal_card())
    computer_hand.add_card(cur_deck.deal_card())
    player_hand.add_card(cur_deck.deal_card())
    in_play = True


def hit():
    global outcome, in_play, cur_deck, player_hand, player_points, player_chips, computer_chips
    
    if in_play:
        player_hand.add_card(cur_deck.deal_card())
    
    if player_hand.get_value() > 21:
        outcome = "Oops, You busted!!"
        if in_play:
            player_chips -= player_bet
            computer_chips += player_bet
        in_play = False

        
        
def stand():
    global in_play, outcome, computer_hand, player_hand, player_points, player_chips, computer_chips, player_bet
    player_points = player_hand.get_value()
    
    if in_play and outcome != "Oops, You busted!!":
        
        while computer_hand.get_value() < 17:
            computer_hand.add_card(cur_deck.deal_card())
        
        if computer_hand.get_value() > 21:
            outcome = "Dealer busted, You Win!!"
            player_chips += player_bet
            computer_chips -= player_bet
        else:
            computer_points = computer_hand.get_value()
            outcome = compare(computer_points, player_points, computer_chips, player_chips, player_bet)[0]
            computer_chips = compare(computer_points, player_points, computer_chips, player_chips, player_bet)[1]
            player_chips = compare(computer_points, player_points, computer_chips, player_chips, player_bet)[2]
        in_play = False
        

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_image(background_img, (1600/2, 1200/2), (1600, 1200), (cvs_width/2, cvs_height/2), (cvs_width, cvs_height))
    com_pos = [50, 280] 
    computer_hand.draw(canvas, com_pos)
    canvas.draw_image(cards_back, (80/2, 106/2), (80, 106), (90, 100),(80, 106) )
    
    plr_pos = [50, 530]
    player_hand.draw(canvas, plr_pos)
    
    canvas.draw_text("Chips: " + str(computer_chips), [50, 210], 25, "Maroon", "sans-serif")
    canvas.draw_text("Dealer", [50, 250], 35, "Maroon", "sans-serif")
    canvas.draw_text("Chips: " + str(player_chips), [50, 460], 25, "Maroon", "sans-serif")
    canvas.draw_text("Player", [50, 500], 35, "Maroon", "sans-serif")
    canvas.draw_text("(bets:"+str(player_bet)+")", [160, 500], 25, "Maroon", "sans-serif")
    canvas.draw_text(outcome, [300, 500], 30, "Maroon", "sans-serif")
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (50+36, 280+48), CARD_BACK_SIZE)
    

    


# initialization frame
frame = simplegui.create_frame("Blackjack", cvs_width, cvs_height)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_label("---------------------")
frame.add_button("Reset (Chips)", reset, 150)
frame.add_label("---------------------")
frame.add_button("Deal", deal, 150)
frame.add_button("Hit",  hit, 150)
frame.add_button("Stand", stand, 150)
frame.add_label("---------------------")
frame.add_button("+ 10 Chips", plus10, 100)
frame.add_button("+ 100 Chips", plus100, 100)
frame.add_button("All in", allin, 100)
frame.add_label("---------------------")
frame.add_label("If you have Chips, then you can add bet amount through 3 buttons, if you have no Chips, you still can play the game, but in fixed amount(10) Chips at a time, until you push the 'Reset' button.")

frame.set_draw_handler(draw)


# get things rolling
reset()
frame.start()


# remember to review the gradic rubric