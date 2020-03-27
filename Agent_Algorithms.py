################################################
##Midterm Project COM313
##Date: 2019-10-15
##Created by: Mathieu Vigneault
##Reviewed by: Jake Corcoran & Simon Moreira
##
##File Description:
##
##    The file implements the different algorithms used for the game.
##    It provides a set of 6 variation of players/algorithms as of now.
#################################################

from math import *
from random import *

#The algorithms for our in-game strategies

def NiceGuy(coop, defect):
    #Always plays cooperate
    return coop


def Cheater(coop, defect):
    # always plays defect
    return defect

def Copycat(coop, defect, lastmove):
    #always plays the last move of its opponent, i.e "copies"
    if(lastmove == "X"):
        return coop
    else:
        if(lastmove == "coop"):
            return coop
        else:
            return defect

def Idiot(coop, defect):
    #plays cooperate and defect at a random 50/50 draw
    x = randrange(0,100)

    if(x <= 50):
        return coop
    else:
        return defect

def Grim(coop, defect, current_round, Round):
    #plays cooperate every round until the final round, then it defects
    if (current_round == (Round-1)):
        return defect
    else:
        return coop

def Detective(coop, defect, lastmove, Round_Number):
    #Sequential moves: Moves coop, defect, coop, coop, then determines
    #the last move of its opponent. If the cooperated, it plays cheater. If they defected it plays Copycat.
    if(Round_Number == 1 or Round_Number == 3 or Round_Number == 4):
        return coop
    if(Round_Number == 2):
        return defect
    if(Round_Number > 4):
        if(lastmove == "defect"):
            value = Copycat(coop, defect, lastmove)
            return value
        else:
            value = Cheater(coop, defect)
            return value

