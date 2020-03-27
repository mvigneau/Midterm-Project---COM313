### Game Action ###

from Agent_Algorithms import *
from DiscoverySettings import *

def result(result1, result2, CCpayoff, CDpayoff,DDpayoff, DCpayoff):

    if(result1 == result2):
        if(result1 == CCpayoff):
            return CCpayoff, "coop", "coop"
        
        else:
            return DDpayoff, "defect", "defect"
        
    else:
        if(result1 == CCpayoff):
            return CDpayoff, "coop", "defect"
        
        else:
            return DCpayoff, "defect", "coop"
        
#GAME FUNCTION
#This function pits p1 strategies vs p2 strategies
def game1(CCpayoff, CDpayoff, DDpayoff, DCpayoff, Round, Total_Round, player1, player2, lm1, lm2, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score):

        algorithm1 = player1
        algorithm2 = player2


        #FIRST 6 out of 30... Player 1 = NICE GUY
        #NICE GUY vs CHEATER
        if(algorithm1 == 1 and algorithm2 == 2):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            NiceGuy_score.setText(NiceGuy_score.getText() + int(tot_result[0]))
            Cheater_score.setText(Cheater_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NICE GUY vs IDIOT
        if(algorithm1 == 1 and algorithm2 == 3):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = Idiot(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            NiceGuy_score.setText(NiceGuy_score.getText() + int(tot_result[0]))
            Idiot_score.setText(Idiot_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NICE GUY vs COPYCAT
        if(algorithm1 == 1 and algorithm2 == 4):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = Copycat(CCpayoff, DDpayoff, lm1)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            NiceGuy_score.setText(NiceGuy_score.getText() + int(tot_result[0]))
            CopyCat_score.setText(CopyCat_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NICE GUY vs GRIM
        if(algorithm1 == 1 and algorithm2 == 5):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            NiceGuy_score.setText(NiceGuy_score.getText() + int(tot_result[0]))
            Grim_score.setText(Grim_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NICE GUY vs DETECTIVE
        if(algorithm1 == 1 and algorithm2 == 6):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = Detective(CCpayoff, DDpayoff, lm1, Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            NiceGuy_score.setText(NiceGuy_score.getText() + int(tot_result[0]))
            Detective_score.setText(Detective_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NEXT 6...(7-12)/36 Player 1 = CHEATER
        #CHEATER vs NICE GUY
        if(algorithm1 == 2 and algorithm2 == 1):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Cheater_score.setText(Cheater_score.getText() + int(tot_result[0]))
            NiceGuy_score.setText(NiceGuy_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2
        #CHEATER vs IDIOT
        if(algorithm1 == 2 and algorithm2 == 3):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = Idiot(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Cheater_score.setText(Cheater_score.getText() + int(tot_result[0]))
            Idiot_score.setText(Idiot_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2
        
        #CHEATER vs COPYCAT
        if(algorithm1 == 2 and algorithm2 == 4):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = Copycat(CCpayoff, DDpayoff, lm1)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Cheater_score.setText(Cheater_score.getText() + int(tot_result[0]))
            CopyCat_score.setText(CopyCat_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #CHEATER vs GRIM
        if(algorithm1 == 2 and algorithm2 == 5):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Cheater_score.setText(Cheater_score.getText() + int(tot_result[0]))
            Grim_score.setText(Grim_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #CHEATER vs DETECTIVE
        if(algorithm1 == 2 and algorithm2 == 6):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = Detective(CCpayoff, DDpayoff, lm1, Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Cheater_score.setText(Cheater_score.getText() + int(tot_result[0]))
            Detective_score.setText(Detective_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NEXT 6...(13-18)/36 Player 1 = IDIOT
        #IDIOT vs NICE GUY
        if(algorithm1 == 3 and algorithm2 == 1):

            result1 = Idiot(CCpayoff, DDpayoff)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Idiot_score.setText(Idiot_score.getText() + int(tot_result[0]))
            NiceGuy_score.setText(NiceGuy_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #IDIOT vs CHEATER
        if(algorithm1 == 3 and algorithm2 == 2):

            result1 = Idiot(CCpayoff, DDpayoff)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Idiot_score.setText(Idiot_score.getText() + int(tot_result[0]))
            Cheater_score.setText(Cheater_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #IDIOT vs COPYCAT
        if(algorithm1 == 3 and algorithm2 == 4):

            result1 = Idiot(CCpayoff, DDpayoff)
            result2 = Copycat(CCpayoff, DDpayoff, lm1)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Idiot_score.setText(Idiot_score.getText() + int(tot_result[0]))
            CopyCat_score.setText(CopyCat_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #IDIOT vs GRIM
        if(algorithm1 == 3 and algorithm2 == 5):

            result1 = Idiot(CCpayoff, DDpayoff)
            result2 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Idiot_score.setText(Idiot_score.getText() + int(tot_result[0]))
            Grim_score.setText(Grim_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #IDIOT vs DETECTIVE
        if(algorithm1 == 3 and algorithm2 == 6):

            result1 = Idiot(CCpayoff, DDpayoff)
            result2 = Detective(CCpayoff, DDpayoff, lm1, Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Idiot_score.setText(Idiot_score.getText() + int(tot_result[0]))
            Detective_score.setText(Detective_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NEXT 6...(19-24)/36 Player 1 = COPYCAT
        #COPYCAT vs NICE GUY
        if(algorithm1 == 4 and algorithm2 == 1):

            result1 = Copycat(CCpayoff, DDpayoff, lm2)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            CopyCat_score.setText(CopyCat_score.getText() + int(tot_result[0]))
            NiceGuy_score.setText(NiceGuy_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #COPYCAT vs CHEATER
        if(algorithm1 == 4 and algorithm2 == 2):

            result1 = Copycat(CCpayoff, DDpayoff, lm2)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            CopyCat_score.setText(CopyCat_score.getText() + int(tot_result[0]))
            Cheater_score.setText(Cheater_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #COPYCAT vs IDIOT
        if(algorithm1 == 4 and algorithm2 == 3):

            result1 = Copycat(CCpayoff, DDpayoff, lm2)
            result2 = Idiot(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            CopyCat_score.setText(CopyCat_score.getText() + int(tot_result[0]))
            Idiot_score.setText(Idiot_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #COPYCAT vs GRIM
        if(algorithm1 == 4 and algorithm2 == 5):

            result1 = Copycat(CCpayoff, DDpayoff, lm2)
            result2 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            CopyCat_score.setText(CopyCat_score.getText() + int(tot_result[0]))
            Grim_score.setText(Grim_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #COPYCAT vs DETECTIVE
        if(algorithm1 == 4 and algorithm2 == 6):

            result1 = Copycat(CCpayoff, DDpayoff, lm2)
            result2 = Detective(CCpayoff, DDpayoff, lm1, Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            CopyCat_score.setText(CopyCat_score.getText() + int(tot_result[0]))
            Detective_score.setText(Detective_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NEXT 6...(25-30)/36 Player 1 = GRIM
        #GRIM vs NICE GUY
        if(algorithm1 == 5 and algorithm2 == 1):

            result1 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Grim_score.setText(Grim_score.getText() + int(tot_result[0]))
            NiceGuy_score.setText(NiceGuy_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2
        
        #GRIM vs CHEATER
        if(algorithm1 == 5 and algorithm2 == 2):

            result1 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Grim_score.setText(Grim_score.getText() + int(tot_result[0]))
            Cheater_score.setText(Cheater_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #GRIM vs IDIOT
        if(algorithm1 == 5 and algorithm2 == 3):

            result1 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            result2 = Idiot(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Grim_score.setText(Grim_score.getText() + int(tot_result[0]))
            Idiot_score.setText(Idiot_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #GRIM vs COPYCAT
        if(algorithm1 == 5 and algorithm2 == 4):

            result1 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            result2 = Copycat(CCpayoff, DDpayoff, lm1)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Grim_score.setText(Grim_score.getText() + int(tot_result[0]))
            CopyCat_score.setText(CopyCat_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2
        
        #GRIM vs DETECTIVE
        if(algorithm1 == 5 and algorithm2 == 6):

            result1 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            result2 = Detective(CCpayoff, DDpayoff, lm1, Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Grim_score.setText(Grim_score.getText() + int(tot_result[0]))
            Detective_score.setText(Detective_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NEXT 6...(30-36)/36 Player 1 = DETECTIVE
        #DETECTIVE vs NICE GUY
        if(algorithm1 == 6 and algorithm2 == 1):

            result1 = Detective(CCpayoff, DDpayoff, lm2, Round)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Detective_score.setText(Detective_score.getText() + int(tot_result[0]))
            NiceGuy_score.setText(NiceGuy_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #DETECTIVE vs CHEATER
        if(algorithm1 == 6 and algorithm2 == 2):

            result1 = Detective(CCpayoff, DDpayoff, lm2, Round)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Detective_score.setText(Detective_score.getText() + int(tot_result[0]))
            Cheater_score.setText(Cheater_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #DETECTIVE vs IDIOT
        if(algorithm1 == 6 and algorithm2 == 3):

            result1 = Detective(CCpayoff, DDpayoff, lm2, Round)
            result2 = Idiot(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Detective_score.setText(Detective_score.getText() + int(tot_result[0]))
            Idiot_score.setText(Idiot_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #DETECTIVE vs COPYCAT
        if(algorithm1 == 6 and algorithm2 == 4):

            result1 = Detective(CCpayoff, DDpayoff, lm2, Round)
            result2 = Copycat(CCpayoff, DDpayoff, lm1)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Detective_score.setText(Detective_score.getText() + int(tot_result[0]))
            CopyCat_score.setText(CopyCat_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #DETECTIVE vs GRIM
        if(algorithm1 == 6 and algorithm2 == 5):

            result1 = Detective(CCpayoff, DDpayoff, lm2, Round)
            result2 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            Detective_score.setText(Detective_score.getText() + int(tot_result[0]))
            Grim_score.setText(Grim_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        else:
            print("Try Again!")
            return (0,0)

def game2(CCpayoff, CDpayoff, DDpayoff, DCpayoff, Round, Total_Round, player1, player2, lm1, lm2, P1_score, P2_score):


        algorithm1 = player1
        algorithm2 = player2


        #FIRST 6 out of 30... Player 1 = NICE GUY
        #NICE GUY vs NICE GUY
        if(algorithm1 == 1 and algorithm2 == 1):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NICE GUY vs CHEATER
        if(algorithm1 == 1 and algorithm2 == 2):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NICE GUY vs IDIOT
        if(algorithm1 == 1 and algorithm2 == 3):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = Idiot(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NICE GUY vs COPYCAT
        if(algorithm1 == 1 and algorithm2 == 4):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = Copycat(CCpayoff, DDpayoff, lm1)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NICE GUY vs GRIM
        if(algorithm1 == 1 and algorithm2 == 5):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NICE GUY vs DETECTIVE
        if(algorithm1 == 1 and algorithm2 == 6):

            result1 = NiceGuy(CCpayoff, DDpayoff)
            result2 = Detective(CCpayoff, DDpayoff, lm1, Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NEXT 6...(7-12)/36 Player 1 = CHEATER
        #CHEATER vs NICE GUY
        if(algorithm1 == 2 and algorithm2 == 1):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #CHEATER vs CHEATER
        if(algorithm1 == 2 and algorithm2 == 2):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #CHEATER vs IDIOT
        if(algorithm1 == 2 and algorithm2 == 3):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = Idiot(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2
        
        #CHEATER vs COPYCAT
        if(algorithm1 == 2 and algorithm2 == 4):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = Copycat(CCpayoff, DDpayoff, lm1)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #CHEATER vs GRIM
        if(algorithm1 == 2 and algorithm2 == 5):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #CHEATER vs DETECTIVE
        if(algorithm1 == 2 and algorithm2 == 6):

            result1 = Cheater(CCpayoff, DDpayoff)
            result2 = Detective(CCpayoff, DDpayoff, lm1, Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NEXT 6...(13-18)/36 Player 1 = IDIOT
        #IDIOT vs NICE GUY
        if(algorithm1 == 3 and algorithm2 == 1):

            result1 = Idiot(CCpayoff, DDpayoff)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #IDIOT vs CHEATER
        if(algorithm1 == 3 and algorithm2 == 2):

            result1 = Idiot(CCpayoff, DDpayoff)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #IDIOT vs COPYCAT
        if(algorithm1 == 3 and algorithm2 == 4):

            last_move = None
            result1 = Idiot(CCpayoff, DDpayoff)
            result2 = Copycat(CCpayoff, DDpayoff, lm1)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #IDIOT vs GRIM
        if(algorithm1 == 3 and algorithm2 == 5):

            result1 = Idiot(CCpayoff, DDpayoff)
            result2 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #IDIOT vs DETECTIVE
        if(algorithm1 == 3 and algorithm2 == 6):

            result1 = Idiot(CCpayoff, DDpayoff)
            result2 = Detective(CCpayoff, DDpayoff, lm1, Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NEXT 6...(19-24)/36 Player 1 = COPYCAT
        #COPYCAT vs NICE GUY
        if(algorithm1 == 4 and algorithm2 == 1):

            result1 = Copycat(CCpayoff, DDpayoff, lm2)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #COPYCAT vs CHEATER
        if(algorithm1 == 4 and algorithm2 == 2):

            result1 = Copycat(CCpayoff, DDpayoff, lm2)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #COPYCAT vs IDIOT
        if(algorithm1 == 4 and algorithm2 == 3):

            result1 = Copycat(CCpayoff, DDpayoff, lm2)
            result2 = Idiot(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #COPYCAT vs GRIM
        if(algorithm1 == 4 and algorithm2 == 5):

            result1 = Copycat(CCpayoff, DDpayoff, lm2)
            result2 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #COPYCAT vs DETECTIVE
        if(algorithm1 == 4 and algorithm2 == 6):

            result1 = Copycat(CCpayoff, DDpayoff, lm2)
            result2 = Detective(CCpayoff, DDpayoff, lm1, Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NEXT 6...(25-30)/36 Player 1 = GRIM
        #GRIM vs NICE GUY
        if(algorithm1 == 5 and algorithm2 == 1):

            result1 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2
        
        #GRIM vs CHEATER
        if(algorithm1 == 5 and algorithm2 == 2):

            result1 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #GRIM vs IDIOT
        if(algorithm1 == 5 and algorithm2 == 3):

            result1 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            result2 = Idiot(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #GRIM vs COPYCAT
        if(algorithm1 == 5 and algorithm2 == 4):

            result1 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            result2 = Copycat(CCpayoff, DDpayoff, lm1)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2
        
        #GRIM vs DETECTIVE
        if(algorithm1 == 5 and algorithm2 == 6):

            result1 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            result2 = Detective(CCpayoff, DDpayoff, lm1, Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #NEXT 6...(30-36)/36 Player 1 = DETECTIVE
        #DETECTIVE vs NICE GUY
        if(algorithm1 == 6 and algorithm2 == 1):

            result1 = Detective(CCpayoff, DDpayoff, lm2, Round)
            result2 = NiceGuy(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #DETECTIVE vs CHEATER
        if(algorithm1 == 6 and algorithm2 == 2):

            result1 = Detective(CCpayoff, DDpayoff, lm2, Round)
            result2 = Cheater(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #DETECTIVE vs IDIOT
        if(algorithm1 == 6 and algorithm2 == 3):

            result1 = Detective(CCpayoff, DDpayoff, lm2, Round)
            result2 = Idiot(CCpayoff, DDpayoff)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #DETECTIVE vs COPYCAT
        if(algorithm1 == 6 and algorithm2 == 4):

            result1 = Detective(CCpayoff, DDpayoff, lm2, Round)
            result2 = Copycat(CCpayoff, DDpayoff, lm1)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        #DETECTIVE vs GRIM
        if(algorithm1 == 6 and algorithm2 == 5):

            result1 = Detective(CCpayoff, DDpayoff, lm2, Round)
            result2 = Grim(CCpayoff, DDpayoff, Round, Total_Round)
            tot_result, lm1, lm2 = result(result1, result2, CCpayoff, CDpayoff, DDpayoff, DCpayoff)
            P1_score.setText(P1_score.getText() + int(tot_result[0]))
            P2_score.setText(P2_score.getText() + int(tot_result[1]))
            return tot_result, lm1, lm2

        else:
            print("Try Again!")
            return (0,0), "Nothing", "Nothing"


def playingGame1(win, p1, p2, CC, CD, DC, DD, Rounds, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score,
                p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5,
                p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8):

    #Payoff tuples for prisoner's game
    #First letter = player 1, 2nd letter = player 2
    #C = cooperate, D = defect
    
    #**MAIN GAME LOOP**

    p1Total = 0
    p2Total = 0
    last_move1 = ["X"]
    last_move2 = ["X"]
    
    for i in range(Rounds):

        result, lm1, lm2 = game1(CC,CD,DD,DC,i,Rounds,p1,p2,last_move1[i], last_move2[i], NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score)

        if(i == 0):
            p1_round1.setText(result[0])
            p2_round1.setText(result[1])
        if(i == 1):
            p1_round2.setText(result[0])
            p2_round2.setText(result[1])
        if(i == 2):
            p1_round3.setText(result[0])
            p2_round3.setText(result[1])
        if(i == 3):
            p1_round4.setText(result[0])
            p2_round4.setText(result[1])
        if(i == 4):
            p1_round5.setText(result[0])
            p2_round5.setText(result[1])
        if(i == 5):
            p1_round6.setText(result[0])
            p2_round6.setText(result[1])
        if(i == 6):
            p1_round7.setText(result[0])
            p2_round7.setText(result[1])
        if(i == 7):
            p1_round8.setText(result[0])
            p2_round8.setText(result[1])
            
        p1Total += result[0]
        p2Total += result[1]
        last_move1.append(lm1)
        last_move2.append(lm2)
    
  
    return (p1Total, p2Total)

def playingGame2(win, p1, p2, last_move1, last_move2, CC, CD, DC, DD, current_round, Rounds,
                 p1_score, p2_score, p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5,
                 p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8):

    #Payoff tuples for prisoner's game
    #First letter = player 1, 2nd letter = player 2
    #C = cooperate, D = defect
    
    #**MAIN GAME LOOP**

    p1Total = 0
    p2Total = 0
    

    result, lm1, lm2 = game2(CC,CD,DD,DC,current_round,Rounds,p1,p2,last_move1[current_round], last_move2[current_round], p1_score, p2_score)

    if(current_round == 0):
        p1_round1.setText(result[0])
        p2_round1.setText(result[1])
    if(current_round == 1):
        p1_round2.setText(result[0])
        p2_round2.setText(result[1])
    if(current_round == 2):
        p1_round3.setText(result[0])
        p2_round3.setText(result[1])
    if(current_round == 3):
        p1_round4.setText(result[0])
        p2_round4.setText(result[1])
    if(current_round == 4):
        p1_round5.setText(result[0])
        p2_round5.setText(result[1])
    if(current_round == 5):
        p1_round6.setText(result[0])
        p2_round6.setText(result[1])
    if(current_round == 6):
        p1_round7.setText(result[0])
        p2_round7.setText(result[1])
    if(current_round == 7):
        p1_round8.setText(result[0])
        p2_round8.setText(result[1])
            
    p1Total += result[0]
    p2Total += result[1]
    last_move1.append(lm1)
    last_move2.append(lm2)

  
    return (p1Total, p2Total, last_move1, last_move2)
        
        
if __name__ == "__main__":
    main()

        

    
