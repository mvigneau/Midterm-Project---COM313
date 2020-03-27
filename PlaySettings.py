################################################
##Midterm Project COM313
##Date: 2019-10-15
##Created by: Mathieu Vigneault
##Reviewed by: Jake Corcoran & Simon Moreira
##
##File Description:
##
##    The file support the prisonner's game dilemma that involves the user playing the different algorithms.
##    It is mainly functions that draw and undraw the interface of the game depending on the user's decision.
##    Most of this function are beneficial for the main since they can shorten up the code inside the main and
##    bundle a bunch of actions and part of the interface together.
#################################################
    
#Import other files to allow graphing to the GUI & create buttons
from graphics import *
from Button import *

#PlaySettings function creates the button and important text object that help the user play the game.
def PlaySettings(win):

    Menu = Button(win, Point(400, 700), 100, 25, "Main Menu") #Create a button 
    Menu.activate()

    Reset = Button(win, Point(400, 650), 100, 25, "Reset")
    Reset.activate()

    Play = Button(win, Point(400, 600), 100, 25, "Play")
    Play.activate()

    Exit = Button(win, Point(400, 750), 100, 25, "Exit")
    Exit.activate()

    Instruction = Button(win, Point(400, 50), 100, 50, "Instructions")
    Instruction.activate()

    name_text = Text(Point(150,25),"' Please Insert Name Below '") #Create a text object 
    name_text.setSize(14)
    name_text.draw(win) #Draw text object to the window

    name_input = Entry(Point(150, 50), 15)
    name_input.setText("")
    name_input.draw(win)

    main_text = Text(Point(400,525),"' Please Select Cooperate or Defect '")
    main_text.setSize(16)
    main_text.draw(win)

    #return all the created buttons & text objects to the main
    return Exit, Menu, Reset, Play, Instruction, name_input, main_text


#DrawGameOption draws the game option part inside the window.It allows the user to be able to change the settings and parameters of the game. 
def DrawGameOption(win):

    option_rect = Rectangle(Point(0,575), Point(275,800)) #Create a rectangle object 
    option_rect.setFill("light blue")
    option_rect.draw(win)   #Draw rectangle to the window
    
    game_option = Text(Point(140,615),"Game Options") #Create a text object 
    game_option.setSize(20)
    game_option.draw(win)

    CC_text = Text(Point(75,650),"Cooperate, Cooperate :")
    CC_text.setSize(12)
    CC_text.draw(win)
    
    CC_input = Entry(Point(200, 650), 15) #Create an entry box object 
    CC_input.setText("3,3")
    CC_input.draw(win)  #Draw entry box to the window 

    CD_text = Text(Point(75,675),"Cooperate, Defect :")
    CD_text.setSize(12)
    CD_text.draw(win)
    
    CD_input = Entry(Point(200, 675), 15)
    CD_input.setText("-1,5")
    CD_input.draw(win)
    
    DC_text = Text(Point(75,700),"Defect, Cooperate :")
    DC_text.setSize(12)
    DC_text.draw(win)
    
    DC_input = Entry(Point(200, 700), 15)
    DC_input.setText("5,-1")
    DC_input.draw(win)


    DD_text = Text(Point(75,725),"Defect, Defect :")
    DD_text.setSize(12)
    DD_text.draw(win)
    
    DD_input = Entry(Point(200, 725), 15)
    DD_input.setText("0,0")
    DD_input.draw(win)
    
    rounds_text = Text(Point(75,750),"Number Of Rounds :")
    rounds_text.setSize(12)
    rounds_text.draw(win)
    
    rounds_input = Entry(Point(200, 750), 15)
    rounds_input.setText(int(5))
    rounds_input.draw(win)

    #return all the created entry boces & text objects to the main
    return CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option


#UndrawGameOption erases the game option part inside the window.It allows the user to be able to change to a different part of the game without being stuck with the game option section. 
def UndrawGameOption(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option):

    CC_text.undraw() #Undraw an object from the window
    CC_input.undraw()
    CD_text.undraw()
    CD_input.undraw()
    DC_text.undraw()
    DC_input.undraw()
    DD_text.undraw()
    DD_input.undraw()
    rounds_text.undraw()
    rounds_input.undraw()
    option_rect.undraw()
    game_option.undraw()

def DrawPayoffTable(win, CC, CD, DC, DD):

        ### Making the payoff table ###
        payoff_table = Rectangle(Point(150,100), Point(650,500))
        payoff_table.setFill("light blue")
        payoff_table.draw(win)

        table_tl = Rectangle(Point(300,200), Point(400,300))
        table_tl.setFill("white")
        table_tl.draw(win)

        table_tr = Rectangle(Point(500,200), Point(400,300))
        table_tr.setFill("white")
        table_tr.draw(win)

        table_bl = Rectangle(Point(300,400), Point(400,300))
        table_bl.setFill("white")
        table_bl.draw(win)

        table_br = Rectangle(Point(500,400), Point(400,300))
        table_br.setFill("white")
        table_br.draw(win)
        
        p1_sign = Text(Point(225,300),"Player 1 - You")
        p1_sign.setSize(20)
        p1_sign.draw(win)

        Coop_Button = Button(win, Point(225, 250), 75, 25, "Cooperate")
        Coop_Button.activate()

        Defect_Button = Button(win, Point(225, 350), 75, 25, "Defect")
        Defect_Button.activate()

        p2_sign = Text(Point(400,150),"Player 2 - CPU Opponent")
        p2_sign.setSize(20)
        p2_sign.draw(win)
        
        p2_coop = Text(Point(350,185),"Cooperate")
        p2_coop.setSize(14)
        p2_coop.draw(win)

        p2_defect = Text(Point(450,185),"Defect")
        p2_defect.setSize(14)
        p2_defect.draw(win)

        CC_text = Text(Point(350,250), CC) ### need to output tuple 
        CC_text.setSize(18)
        CC_text.draw(win)

        CD_text = Text(Point(450,250), CD) ### need to output tuple 
        CD_text.setSize(18)
        CD_text.draw(win)

        DC_text = Text(Point(350,350), DC) ### need to output tuple 
        DC_text.setSize(18)
        DC_text.draw(win)

        DD_text = Text(Point(450,350), DD) ### need to output tuple 
        DD_text.setSize(18)
        DD_text.draw(win)

        return CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, Coop_Button, Defect_Button, p2_sign, p2_coop, p2_defect


def DrawScoreboard(win):

    scoreboard_sign = Text(Point(700,15),"Scoreboard")
    scoreboard_sign.setSize(20)
    scoreboard_sign.draw(win)

    P1_sign = Text(Point(650,50),"Player 1")
    P1_sign.setSize(14)
    P1_sign.draw(win)

    P1_score = Text(Point(750,50),int(0))
    P1_score.setSize(14)
    P1_score.draw(win)

    P2_sign = Text(Point(650,75),"Player 2")
    P2_sign.setSize(14)
    P2_sign.draw(win)

    P2_score = Text(Point(750,75), int(0))
    P2_score.setSize(14)
    P2_score.draw(win)


    return scoreboard_sign, P1_sign, P1_score, P2_sign, P2_score
    
def UndrawScoreboard(scoreboard_sign, p1_sign, p1_score, p2_sign, p2_score, name_input):

    ## Deleting the scoreboard to keep track of players scores ##
    p1_sign.undraw()
    p2_sign.undraw()
    p1_score.undraw()
    p2_score.undraw()
    scoreboard_sign.undraw()
    name_input.undraw()


def DrawRoundOutput(win):

        ### Making Each Round Scoring Table ###

        payoff_round = Rectangle(Point(525,575), Point(800,800))
        payoff_round.setFill("light blue")
        payoff_round.draw(win)

        nb_round = Text(Point(585,565),"Round Number")
        nb_round.setSize(15)
        nb_round.draw(win)

        p1_round = Text(Point(675,565),"Player 1")
        p1_round.setSize(15)
        p1_round.draw(win)

        p2_round = Text(Point(750,565),"Player 2")
        p2_round.setSize(15)
        p2_round.draw(win)

        round_1 = Text(Point(585,600),"Round 1")
        round_1.setSize(14)
        round_1.draw(win)

        p1_round1 = Text(Point(675,600), int(0))
        p1_round1.setSize(14)
        p1_round1.draw(win)

        p2_round1 = Text(Point(750,600), int(0))
        p2_round1.setSize(14)
        p2_round1.draw(win)

        round_2 = Text(Point(585,625),"Round 2")
        round_2.setSize(14)
        round_2.draw(win)

        p1_round2 = Text(Point(675,625), int(0))
        p1_round2.setSize(14)
        p1_round2.draw(win)

        p2_round2 = Text(Point(750,625), int(0))
        p2_round2.setSize(14)
        p2_round2.draw(win)

        round_3 = Text(Point(585,650),"Round 3")
        round_3.setSize(14)
        round_3.draw(win)

        p1_round3 = Text(Point(675,650), int(0))
        p1_round3.setSize(14)
        p1_round3.draw(win)

        p2_round3 = Text(Point(750,650), int(0))
        p2_round3.setSize(14)
        p2_round3.draw(win)

        round_4 = Text(Point(585,675),"Round 4")
        round_4.setSize(14)
        round_4.draw(win)

        p1_round4 = Text(Point(675,675), int(0))
        p1_round4.setSize(14)
        p1_round4.draw(win)

        p2_round4 = Text(Point(750,675), int(0))
        p2_round4.setSize(14)
        p2_round4.draw(win)

        round_5 = Text(Point(585,700),"Round 5")
        round_5.setSize(14)
        round_5.draw(win)

        p1_round5 = Text(Point(675,700), int(0))
        p1_round5.setSize(14)
        p1_round5.draw(win)

        p2_round5 = Text(Point(750,700), int(0))
        p2_round5.setSize(14)
        p2_round5.draw(win)
        
        round_6 = Text(Point(585,725),"Round 6")
        round_6.setSize(14)
        round_6.draw(win)

        p1_round6 = Text(Point(675,725), int(0))
        p1_round6.setSize(14)
        p1_round6.draw(win)

        p2_round6 = Text(Point(750,725), int(0))
        p2_round6.setSize(14)
        p2_round6.draw(win)

        round_7 = Text(Point(585,750),"Round 7")
        round_7.setSize(14)
        round_7.draw(win)

        p1_round7 = Text(Point(675,750), int(0))
        p1_round7.setSize(14)
        p1_round7.draw(win)

        p2_round7 = Text(Point(750,750), int(0))
        p2_round7.setSize(14)
        p2_round7.draw(win)

        round_8 = Text(Point(585,775),"Round 8")
        round_8.setSize(14)
        round_8.draw(win)

        p1_round8 = Text(Point(675,775), int(0))
        p1_round8.setSize(14)
        p1_round8.draw(win)

        p2_round8 = Text(Point(750,775), int(0))
        p2_round8.setSize(14)
        p2_round8.draw(win)

        return p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8

def AlgorithmName(p2):

    if(p2 == 1):
        alg_name = "Nice Guy"
    if(p2 == 2):
        alg_name = "Cheater"
    if(p2 == 3):
        alg_name = "Idiot"
    if(p2 == 4):
        alg_name = "Copy Cat"
    if(p2 == 5):
        alg_name = "Grim"
    if(p2 == 6):
        alg_name = "Detective"
        
    return alg_name

def ResetRoundPayoff(p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8):

    p1_round1.setText(int(0))
    p2_round1.setText(int(0))
    p1_round2.setText(int(0))
    p2_round2.setText(int(0))
    p1_round3.setText(int(0))
    p2_round3.setText(int(0))
    p1_round4.setText(int(0))
    p2_round4.setText(int(0))
    p1_round5.setText(int(0))
    p2_round5.setText(int(0))
    p1_round6.setText(int(0))
    p2_round6.setText(int(0))
    p1_round7.setText(int(0))
    p2_round7.setText(int(0))
    p1_round8.setText(int(0))
    p2_round8.setText(int(0))

def DrawInstruction1(win):

    instruction_rectangle = Rectangle(Point(-100,-100), Point(900,900))
    instruction_rectangle.setFill("light blue")
    instruction_rectangle.draw(win)

    instructiontitle = Text(Point(400, 50), "INSTRUCTIONS")
    instructiontitle.setSize(20)
    instructiontitle.setStyle("bold")
    instructiontitle.draw(win)

    title1 = Text(Point(400, 100), "Name")
    title1.setSize(16)
    title1.draw(win)

    label1 = Text(Point(400, 150), "Please type your name in the grey box in the upper left corner as it will be recorded inside our database.")
    label1.draw(win)

    title2 = Text(Point(400, 200), "Scoreboard")
    title2.setSize(16)
    title2.draw(win)

    label2 = Text(Point(400, 250), "The scoreboard shows the total score or payoff of each player over the course of the game.\n It updates every round and only resets when game is over or reset.")
    label2.draw(win)

    title3 = Text(Point(400, 300), "Game Options")
    title3.setSize(16)
    title3.draw(win)

    label3 = Text(Point(400, 350), "The game option table allows the user to change the parameters of the payoff table as well as the number of rounds played.\nIt can be updated at all time throughout the game.")
    label3.draw(win)
    
    title4 = Text(Point(400, 385), "Rules")
    title4.setSize(16)
    title4.draw(win)

    label4 = Text(Point(400, 440), "1. The user should input their name in the top left corner\n 2. Change the game options if needed.\n 3. Click on either the cooperate button or the defect button dependiing on wht you want to do.\n 4. Press Play button and repeat step 3 & 4 until all rounds are played.\n 5. In each iteration of the game, you will play a new opponent until you reach game over.")
    label4.draw(win)

    title5 = Text(Point(400, 500), "Utility Buttons")
    title5.setSize(16)
    title5.draw(win)

    label5 = Text(Point(400, 550), "Click Exit button to quit the program.\n Press the Menu button to go back to the original page.\n Click Reset button to restart the game, payoffs and scores.\n Press Play to execute a round.")
    label5.draw(win)

    title6 = Text(Point(400, 600), "Payoff Table")
    title6.setSize(16)
    title6.draw(win)

    label6 = Text(Point(400, 650), "It shows the user the payoffs of every possible outcome for each round.\nIt also allows the user to have better understanding of the game and its opponent possible choices.")
    label6.draw(win)
    
    title7 = Text(Point(400, 700), "Payoffs Per Round ")
    title7.setSize(16)
    title7.draw(win)

    label7 = Text(Point(400, 750), "It shows the user the payoffs or outcome for the first 8 rounds.\n It helps the user keep track of the previous moves of its opponent.")
    label7.draw(win)

    return instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 

def UndrawInstruction1(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 ):

    instructiontitle.undraw()
    title1.undraw()
    label1.undraw()
    title2.undraw()
    label2.undraw()
    title3.undraw()
    label3.undraw()
    title4.undraw()
    label4.undraw()
    title5.undraw()
    label5.undraw()
    title6.undraw()
    label6.undraw()
    title7.undraw()
    label7.undraw()
    instruction_rectangle.undraw()
    
    
