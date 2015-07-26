# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
background_img = simplegui.load_image("https://www.dropbox.com/s/rlat6qe9705olwt/cardgamebg1.jpg?dl=1")
width = 1600
height = 1200

cvs_width = 1600 * 0.6
cvs_height = 1200 * 0.6

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


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
        for c in self.hand:
            self.value += VALUES[c.get_rank()]
        if "CA" not in self.hand and "SA" not in self.hand and "HA" not in self.hand and "DA" not in self.hand:
            return self.value
        else:
            if (self.value + 10) <= 21:
                return self.value + 10
            else:
                return self.value
   
    def draw(self, canvas, pos):
        pass    # draw a hand on the canvas, use the draw method for cards
 
        
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
def deal():
    global outcome, in_play, cur_deck, computer_hand, player_hand

    cur_deck = Deck()
    computer_hand = Hand()
    player_hand = Hand()
    
    cur_deck.shuffle()
    computer_hand.add_card(cur_deck.deal_card())
    player_hand.add_card(cur_deck.deal_card())
    computer_hand.add_card(cur_deck.deal_card())
    player_hand.add_card(cur_deck.deal_card())

    
    
    in_play = True

def hit():
    pass    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    pass    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_image(background_img, (1600/2, 1200/2), (1600, 1200), (cvs_width/2, cvs_height/2), (cvs_width, cvs_height))


# initialization frame
frame = simplegui.create_frame("Blackjack", cvs_width, cvs_height)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric