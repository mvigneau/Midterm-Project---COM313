################################################
##Midterm Project COM313
##Date: 2019-10-15
##Created by: Mathieu Vigneault
##Edited by: Jake Corcoran
##
##File Description:
##
## The purpose of this file is to parse the different sets of tuples that can arise
## when the user changes the payoffs. We have to account for tuples with lengths of
## from 3 to 7 ~ i.e (3,3) or (-33, -33) and everything in between up to
## two-digit integers.
#################################################


def getValues(CC_input, CD_input, DC_input, DD_input, rounds_input):

    #Cooperate/Cooperate 
    CC = tuple(CC_input.getText())
    if(len(CC) == 3): #if length tuple is 3, i.e (3,3)
        CC = int(CC[0]), int(CC[2])
    if(len(CC) == 4):
        if(CC[0] == "-"):
            CC = (int(CC[1])*-1), int(CC[3])
        elif(CC[2] == "-"):
            CC = int(CC[0]), (int(CC[3])*-1)
        elif(CC[1] == "," and CC[2] != "-"):
            str1 = CC[2]
            str2 = CC[3]
            str3 = str1+str2
            CC = int(CC[0]), (int(str3))
        else:
            str1 = CC[0]
            str2 = CC[1]
            str3 = str1+str2
            CC = int(str3), (int(CC[3]))
    if(len(CC) == 5):
        if(CC[0] == "-" and CC[3] == "-"):
            CC = ((int(CC[1])*-1), (int(CC[4])*-1))
        elif(CC[0] == "-" and CC[2] == ","):
            str1 = CC[3]
            str2 = CC[4]
            str3 = str1+str2
            CC = (int(CC[1])*-1), (int(str3))
        elif(CC[0] == "-" and CC[3] == ","):
            str1 = CC[1]
            str2 = CC[2]
            str3 = str1+str2
            CC = (int(str3)*-1), (int(CC[4]))
        elif(CC[2] == "-" and CC[1] == ","):
            str1 = CC[3]
            str2 = CC[4]
            str3 = str1+str2
            CC = int(CC[0]), (int(str3)*-1)
        else:
            str1 = CC[0]
            str2 = CC[1]
            str3 = str1+str2
            str4 = CC[3]
            str5 = CC[4]
            str6 = str4+str5
            CC = int(str3), (int(str6))
    if(len(CC) == 6):
        if(CC[0] == "-"):
            str1 = CC[1]
            str2 = CC[2]
            str3 = str1+str2
            str4 = CC[4]
            str5 = CC[5]
            str6 = str4+str5
            CC = (int(str3)*-1), (int(str6))
        else:
            str1 = CC[0]
            str2 = CC[1]
            str3 = str1+str2
            str4 = CC[4]
            str5 = CC[5]
            str6 = str4+str5
            CC = (int(str3)), (int(str6)*-1) 
    if(len(CC) == 7):
        str1 = CC[1]
        str2 = CC[2]
        str3 = str1+str2
        str4 = CC[5]
        str5 = CC[6]
        str6 = str4+str5
        CC = (int(str3)*-1), (int(str6)*-1)

    #P1 = cooperate, p2 = defect
    CD = tuple(CD_input.getText())
    if(len(CD) == 3):
        CD = int(CD[0]), int(CD[2])
    if(len(CD) == 4):
        if(CD[0] == "-"):
            CD = (int(CD[1])*-1), int(CD[3])
        elif(CD[2] == "-"):
            CD = int(CD[0]), (int(CD[3])*-1)
        elif(CD[1] == "," and CD[2] != "-"):
            str1 = CD[2]
            str2 = CD[3]
            str3 = str1+str2
            CD = int(CD[0]), (int(str3))
        else:
            str1 = CD[0]
            str2 = CD[1]
            str3 = str1+str2
            CD = int(str3), (int(CD[3]))
    if(len(CD) == 5):
        if(CD[0] == "-" and CD[3] == "-"):
            CD = ((int(CD[1])*-1), (int(CD[4])*-1))
        elif(CD[0] == "-" and CD[2] == ","):
            str1 = CD[3]
            str2 = CD[4]
            str3 = str1+str2
            CD = (int(CD[1])*-1), (int(str3))
        elif(CD[0] == "-" and CD[3] == ","):
            str1 = CD[1]
            str2 = CD[2]
            str3 = str1+str2
            CD = (int(str3)*-1), (int(CD[4]))
        elif(CD[2] == "-" and CD[1] == ","):
            str1 = CD[3]
            str2 = CD[4]
            str3 = str1+str2
            CD = int(CD[0]), (int(str3)*-1)
        else:
            str1 = CD[0]
            str2 = CD[1]
            str3 = str1+str2
            str4 = CD[3]
            str5 = CD[4]
            str6 = str4+str5
            CD = int(str3), (int(str6))
    if(len(CD) == 6):
        if(CD[0] == "-"):
            str1 = CD[1]
            str2 = CD[2]
            str3 = str1+str2
            str4 = CD[4]
            str5 = CD[5]
            str6 = str4+str5
            CD = (int(str3)*-1), (int(str6))
        else:
            str1 = CD[0]
            str2 = CD[1]
            str3 = str1+str2
            str4 = CD[4]
            str5 = CD[5]
            str6 = str4+str5
            CD = (int(str3)), (int(str6)*-1)
            
    if(len(CD) == 7):
        str1 = CD[1]
        str2 = CD[2]
        str3 = str1+str2
        str4 = CD[5]
        str5 = CD[6]
        str6 = str4+str5
        CD = (int(str3)*-1), (int(str6)*-1)

    #p1 = defect, p2 = cooperate
    DC = tuple(DC_input.getText())
    if(len(DC) == 3):
        DC = int(DC[0]), int(DC[2])
    if(len(DC) == 4):
        if(DC[0] == "-"):
            DC = (int(DC[1])*-1), int(DC[3])
        elif(DC[2] == "-"):
            DC = int(DC[0]), (int(DC[3])*-1)
        elif(DC[1] == "," and DC[2] != "-"):
            str1 = DC[2]
            str2 = DC[3]
            str3 = str1+str2
            DC = int(DC[0]), (int(str3))
        else:
            str1 = DC[0]
            str2 = DC[1]
            str3 = str1+str2
            DC = int(str3), (int(DC[3]))
    if(len(DC) == 5):
        if(DC[0] == "-" and DC[3] == "-"):
            DC = ((int(DC[1])*-1), (int(DC[4])*-1))
        elif(DC[0] == "-" and DC[2] == ","):
            str1 = DC[3]
            str2 = DC[4]
            str3 = str1+str2
            DC = (int(DC[1])*-1), (int(str3))
        elif(DC[0] == "-" and DC[3] == ","):
            str1 = DC[1]
            str2 = DC[2]
            str3 = str1+str2
            DC = (int(str3)*-1), (int(DC[4]))
        elif(DC[2] == "-" and DC[1] == ","):
            str1 = DC[3]
            str2 = DC[4]
            str3 = str1+str2
            DC = int(DC[0]), (int(str3)*-1)
        else:
            str1 = DC[0]
            str2 = DC[1]
            str3 = str1+str2
            str4 = DC[3]
            str5 = DC[4]
            str6 = str4+str5
            DC = int(str3), (int(str6))
    if(len(DC) == 6):
        if(DC[0] == "-"):
            str1 = DC[1]
            str2 = DC[2]
            str3 = str1+str2
            str4 = DC[4]
            str5 = DC[5]
            str6 = str4+str5
            DC = (int(str3)*-1), (int(str6))
        else:
            str1 = DC[0]
            str2 = DC[1]
            str3 = str1+str2
            str4 = DC[4]
            str5 = DC[5]
            str6 = str4+str5
            DC = (int(str3)), (int(str6)*-1)
            
    if(len(DC) == 7):
        str1 = DC[1]
        str2 = DC[2]
        str3 = str1+str2
        str4 = DC[5]
        str5 = DC[6]
        str6 = str4+str5
        DC = (int(str3)*-1), (int(str6)*-1)

    #p1 = defect, p2 = defect
    DD = tuple(DD_input.getText())
    if(len(DD) == 3):
        DD = int(DD[0]), int(DD[2])
    if(len(DD) == 4):
        if(DD[0] == "-"):
            DD = (int(DD[1])*-1), int(DD[3])
        elif(DD[2] == "-"):
            DD = int(DD[0]), (int(DD[3])*-1)
        elif(DD[1] == "," and DD[2] != "-"):
            str1 = DD[2]
            str2 = DD[3]
            str3 = str1+str2
            DD = int(DD[0]), (int(str3))
        else:
            str1 = DD[0]
            str2 = DD[1]
            str3 = str1+str2
            DD = int(str3), (int(DD[3]))
    if(len(DD) == 5):
        if(DD[0] == "-" and DD[3] == "-"):
            DD = ((int(DD[1])*-1), (int(DD[4])*-1))
        elif(DD[0] == "-" and DD[2] == ","):
            str1 = DD[3]
            str2 = DD[4]
            str3 = str1+str2
            DD = (int(DD[1])*-1), (int(str3))
        elif(DD[0] == "-" and DD[3] == ","):
            str1 = DD[1]
            str2 = DD[2]
            str3 = str1+str2
            DD = (int(str3)*-1), (int(DD[4]))
        elif(DD[2] == "-" and DD[1] == ","):
            str1 = DD[3]
            str2 = DD[4]
            str3 = str1+str2
            DD = int(DD[0]), (int(str3)*-1)
        else:
            str1 = DD[0]
            str2 = DD[1]
            str3 = str1+str2
            str4 = DD[3]
            str5 = DD[4]
            str6 = str4+str5
            DD = int(str3), (int(str6))
    if(len(DD) == 6):
        if(DD[0] == "-"):
            str1 = DD[1]
            str2 = DD[2]
            str3 = str1+str2
            str4 = DD[4]
            str5 = DD[5]
            str6 = str4+str5
            DD = (int(str3)*-1), (int(str6))
        else:
            str1 = DD[0]
            str2 = DD[1]
            str3 = str1+str2
            str4 = DD[4]
            str5 = DD[5]
            str6 = str4+str5
            DD = (int(str3)), (int(str6)*-1)
            
    if(len(DD) == 7):
        str1 = DD[1]
        str2 = DD[2]
        str3 = str1+str2
        str4 = DD[5]
        str5 = DD[6]
        str6 = str4+str5
        DD = (int(str3)*-1), (int(str6)*-1)



    rounds = int(rounds_input.getText())

    return CC, CD, DC, DD, rounds

def setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text):

        CC_text.setText(CC)
        CD_text.setText(CD)
        DC_text.setText(DC)
        DD_text.setText(DD)
