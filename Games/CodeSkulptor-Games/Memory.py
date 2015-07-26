# ------------------------ Memory ! ------------------------- #

import simplegui
import random



# ----------------- Helper Function Zone ! ------------------ #
def new_game():
    global CARDLIST, CARDWIDTH, exposed, state, turns
    CARDLIST = range(8) + range(8)
    random.shuffle(CARDLIST)
    CARDWIDTH = 800 / 16
    exposed = [False for i in range(16)]
    state = 0
    card1 = 0
    card2 = 0
    turns = 0
     
# define event handlers
def mouseclick(pos):
    # check click postion and change list:exposed
    global state, card1, card2, turns
    idx = pos[0] / CARDWIDTH
    if not exposed[idx]:
        exposed[idx] = True
        if state == 0:
            card1 = idx
            state = 1
            turns += 1
        elif state == 1:
            card2 = idx
            state = 2
        else:
            if CARDLIST[card1] != CARDLIST[card2]:
                exposed[card1] = False
                exposed[card2] = False
            card1 = idx
            state = 1
            turns += 1

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global CARDLIST
    label.set_text('Turns = ' + str(turns))
    tmp = 0

    # draw sequence of card numbers on the canvas
    for card in CARDLIST:
        canvas.draw_text(str(card), [CARDWIDTH + tmp - 35, 60], 40, 'White', 'sans-serif')
        tmp += CARDWIDTH
    
    # determine whether cards face up or face down based on list:exposed

    for i in range(len(exposed)):
        if exposed[i] == False:
            canvas.draw_polygon([[i*CARDWIDTH, 0], [(i+1)*CARDWIDTH, 0], [(i+1)*CARDWIDTH, 100],
                                 [i*CARDWIDTH, 100]], 1, 'Maroon', 'Green')

        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric