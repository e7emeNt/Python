# ----------------------- Word Game ! ------------------------ #
# This game provide 83367 English words and random size of letters(determine by global variable "HAND_SIZE") for you, and you can combine those letters to words! The program will calculate your score!


import random
import string


# ----------------------- Global Variable Zone ------------------------ #


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"



# ----------------------- Helper Function Zone ------------------------ #


# Load 83367 words!!!
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    print
    return wordList



# I Didn't use this
def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	


# Get the score of the word
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    word = str(word)
    for c in word:
        score += SCRABBLE_LETTER_VALUES[c]
    score *= len(word)
    if len(word) == n:
        score += 50
    return score



# Just print the remaing letters in the game
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line



# Create a new random hand
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand



# This function used by PlayHand or comPlayHand
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()
    for c in word:
        newHand[c] -= 1
    return newHand



# Determine whether the word in the wordlist
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    result = True

    if word in wordList:
        for c in word:
            if c in hand.keys():
                if word.count(c) <= hand[c]:
                    result = result and True
                else:
                    result = False
            else:
                result = False
    else:
        result = False

    return result

 

# Computer choose the best word for game(a bit slowly, 83367 words after all !)
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        currentScore = 0
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            for c in word:
                currentScore += getWordScore(word, n)
            # If the score for that word is higher than your best score
            if currentScore > maxScore:
                # Update your best score, and best word accordingly
                maxScore = currentScore
                bestWord = word
    # return the best word you found.
    return bestWord



# This Function Actually Useless!
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())


# ----------------------- Main Function Zone ------------------------ #


# Human Play Function
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print 'Current hand: ', 
        displayHand(hand)
        # Ask user for input
        print 'Enter word, or a "." to indicate that you are finished: ',
        word = str(raw_input())
        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            print 'Goodbye!',
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print 'Invalid word, please try again.'
                print
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                totalScore += getWordScore(word, n)
                print '"' + word + '" earned ' + str(getWordScore(word, n)) + 'points.', 'Total: ' + str(totalScore) + 'points'
                print
                # Update the hand 
                hand = updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) == 0:
        print 'Run out of letters.',
    print 'Total score: ' + str(totalScore) + '.'
    print



# Computer Play Function
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while sum(hand.values()) > 0:
        # Display the hand
        print 'Current hand: ', 
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)

        if word == None:
            # End the game (break out of the loop)
            break
        # Otherwise
        else:
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            totalScore += getWordScore(word, n)
            print '"' + word + '" earned ' + str(getWordScore(word, n)) + 'points.', 'Total: ' + str(totalScore) + 'points'
            print
            # Update the hand 
            hand = updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print 'Total score: ' + str(totalScore) + '.'
    print



# Main Function
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    userInput = ''
    hand = {}
    while userInput != 'e':
        print 'Enter n to deal a new hand, r to replay the last hand, or e to end game:',
        userInput = str(raw_input())
        
        if userInput == 'n':
            print 'Enter u to have yourself play, c to have the computer play:',
            playInput = str(raw_input())
            
            while playInput != 'c' and playInput != 'u':
                print 'Invalid command.'
                print
                print 'Enter u to have yourself play, c to have the computer play:',
                playInput = str(raw_input())
            
            if playInput == 'c':
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand, wordList, HAND_SIZE)

            elif playInput == 'u':
                hand = dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)

        elif userInput == 'r':
            if hand == {}:
                print 'You have not played a hand yet. Please play a new hand first!'
                print
            else:
                print 'Enter u to have yourself play, c to have the computer play:',
                playInput = str(raw_input())
            
                while playInput != 'c' and playInput != 'u':
                    print 'Invalid command.'
                    print
                    print 'Enter u to have yourself play, c to have the computer play:',
                    playInput = str(raw_input())
            
                if playInput == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)

                elif playInput == 'u':
                    playHand(hand, wordList, HAND_SIZE)

        elif userInput != 'e':
            print 'Invalid command.'
            print

   





# ---------------------------- Start Zone ----------------------------- #


if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
