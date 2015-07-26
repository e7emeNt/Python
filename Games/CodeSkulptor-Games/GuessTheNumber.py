#<======================== Guess the number! ======================>

import math
import random
import simplegui

########## ---------- Function and Variables Zone ---------- ##########
game_mode = 100

def new_game():
    """Start a new game"""
    global secret_number
    secret_number = random.randrange(0, 100)
    if game_mode == 100:
        range100()
    elif game_mode == 1000:
        range1000()
        
def range100():
    """[0, 100) range function"""
    global secret_number
    global game_mode
    game_mode = 100
    secret_number = random.randrange(0, 100)
    print "<------- New game, Range is from 0 to 100 ------->"
    global guess_remain
    guess_remain = int(math.ceil(math.log(100 - 0 + 1, 2)))
    print "Number of remaining guesses is " + str(guess_remain)
    print 

def range1000():
    """[0, 1000) range function"""    
    global secret_number
    global game_mode
    game_mode = 1000
    secret_number = random.randrange(0, 1000)
    print "<------- New game, Range is from 0 to 1000 ------->"
    global guess_remain
    guess_remain = int(math.ceil(math.log(1000 - 0 + 1, 2)))
    print "Number of remaining guesses is " + str(guess_remain)
    print 
    
def input_guess(guess):
    """Main logic function"""
    
    global secret_number
    
    global guess_remain
    print "Guess was " + guess
    
    guess_remain = guess_remain - 1
    print "Number of remaining guesses is " + str(guess_remain)
    
    try:
        guess_number = int(guess)
    except(ValueError):
        print "Please enter a valid number!"
        print
        new_game()
        return 1
              
        
    if guess_number == secret_number:
        print "Correct!"
        print 
        new_game()
        
    elif guess_number < secret_number and guess_remain > 0:
        print "Higher!"
        print 
        
    elif guess_number > secret_number and guess_remain > 0:
        print "Lower!"
        print 
        
    elif guess_remain < 1:
        print "You ran out of gueeses, The number is " + str(secret_number)
        print
        new_game()
        
    else:
        print "Error!"
        print 
    

    
########## ------------------ Frame Zone ------------------- ##########

# create frame
f = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements and start frame
f.add_button("[0, 100)", range100, 200)
f.add_button("[0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

########## ------------------ Start Zone ----------------- ##########
new_game()


