# Rock-paper-scissors-lizard-Spock project!!!
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

########## ----- Inport Zone ----- ##########

import random



########## ----- Function Zone ----- ##########

def name_to_number(name):
    """convert name to number"""
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "Name is invalid!"
        return 1
    return number


def number_to_name(number):
    """convert number to name"""
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "Number is invalid!"
        return 1
    return name



########## ----- Main Zone ----- ##########

def rpsls(player_choice): 
    """get choices and print out the results(main function)"""
    print 

    print "Player chooses " + player_choice

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0, 5)

    comp_choice = number_to_name(comp_number)

    print "Computer chooses " + comp_choice


    if 0 < (player_number - comp_number) % 5 <= 2:
        print "Player wins!"
    
    elif (player_number - comp_number) % 5 > 2:
        print "Computer wins!"
    
    elif (player_number - comp_number) % 5 == 0:
        print "Player and computer tie!"
   
    else:
        print "Error!!!"
        return 1

    return 0



########## ----- Test Zone ----- ##########

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




