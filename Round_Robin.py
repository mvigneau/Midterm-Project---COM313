################################################
##Midterm Project COM313
##Date: 2019-10-15
##Created by: Mathieu Vigneault
##Reviewed by: Jake Corcoran & Simon Moreira
##
##File Description:
##
##    The file is used for the implementation of the round robin simulator,
##    which provide the user with the best algorithms depending on the game settings.

#################################################

from Game import *
from PlaySettings import *

def round_robin(win, CC, CD, DC, DD, rounds, p1_round1, p2_round1,p1_round2, p2_round2,
                p1_round3, p2_round3, p1_round4, p2_round4, p1_round5,
                p2_round5, p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8):

    
    NiceGuy_score = int(0)
    Cheater_score = int(0)
    Idiot_score = int(0)
    CopyCat_score = int(0)
    Grim_score = int(0)
    Detective_score = int(0)
    last_move1 = ["X"]
    last_move2 = ["X"]

    p1_score = Text(Point(675,15),int(0))
    p2_score = Text(Point(675,15),int(0))
    
    for i in range(1,7):
        for j in range((i+1),7):

            player1 = i
            player2 = j
            current_round = 0
            while(current_round != rounds):

                tupleOut = playingGame2(win, player1, player2, last_move1, last_move2, CC, CD, DC, DD, current_round, rounds, p1_score, p2_score,
                                                                                            p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5,
                                                                                            p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)
                if(player1 == 1):
                    NiceGuy_score = NiceGuy_score + tupleOut[0]
                elif(player1 == 2):
                    Cheater_score = Cheater_score + tupleOut[0]
                elif(player1 == 3):
                    Idiot_score = Idiot_score + tupleOut[0]
                elif(player2 == 4):
                    CopyCat_score = CopyCat_score + tupleOut[0]
                elif(player2 == 5):
                    Grim_score = Grim_score + tupleOut[0]
                else:
                    Detective_score = Detective_score + tupleOut[0]

                
                if(player2 == 1):
                    NiceGuy_score = NiceGuy_score + tupleOut[1]
                elif(player2 == 2):
                    Cheater_score = Cheater_score + tupleOut[1]
                elif(player2 == 3):
                    Idiot_score = Idiot_score + tupleOut[1]
                elif(player2 == 4):
                    CopyCat_score = CopyCat_score + tupleOut[1]
                elif(player2 == 5):
                    Grim_score = Grim_score + tupleOut[1]
                else:
                    Detective_score = Detective_score + tupleOut[1]

                current_round += 1
            

    winner_text = Text(Point(400,150), "Round Robin Winner")
    winner_text.setSize(14)
    winner_text.draw(win)

    winner_name = Text(Point(400,175), "")
    winner_name.setSize(14)
    winner_name.draw(win)

    if(NiceGuy_score >= Cheater_score and NiceGuy_score >= Idiot_score and NiceGuy_score >= CopyCat_score and NiceGuy_score >= Grim_score and NiceGuy_score >= Detective_score):
        winner_name.setText("Nice Guy")    
    elif(Cheater_score >= NiceGuy_score and Cheater_score >= Idiot_score and Cheater_score >= CopyCat_score and Cheater_score >= Grim_score and Cheater_score >= Detective_score):
        winner_name.setText("Cheater")
    elif(Idiot_score >= NiceGuy_score and Idiot_score >= Cheater_score and Idiot_score >= CopyCat_score and Idiot_score >= Grim_score and Idiot_score >= Detective_score):
        winner_name.setText("Idiot")
    elif(CopyCat_score >= NiceGuy_score and CopyCat_score >= Cheater_score and CopyCat_score >= Idiot_score and CopyCat_score >= Grim_score and Idiot_score >= Detective_score):
        winner_name.setText("Copy Cat")
    elif(Grim_score >= NiceGuy_score and Grim_score >= Cheater_score and Grim_score >= Idiot_score and Grim_score >= CopyCat_score and Grim_score >= Detective_score):
        winner_name.setText("Grim")
    else:
        winner_name.setText("Detective")

    return winner_text, winner_name




    
