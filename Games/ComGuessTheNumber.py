print 'Please think of a number between 0 and 100!'

high = 100
low = 0
guess = (high + low) / 2
isCorrect = ''

while isCorrect != 'c':
    print 'Is your secret number ' + str(guess) + '?'
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",
    isCorrect = raw_input()
    if isCorrect == 'c':
        print 'Game over. Your secret number was: ' + str(guess)
    elif isCorrect == 'h':
        high = guess
        guess = (high + low) / 2
    elif isCorrect == 'l':
        low = guess
        guess = (high + low) / 2
    else:
        print "Sorry, I did not understand your input."