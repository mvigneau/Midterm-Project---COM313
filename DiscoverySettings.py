from graphics import *
from Button import *

def DiscoverySettings(win):

        x = 400
        y = 250
        ptp = Point(x,y)
        niceGuy = Button(win, ptp, 150, 25, "Nice Guy")
        niceGuy.activate()
        cheater = Button(win, Point((ptp.getX() - 200), (ptp.getY() + 50)), 150, 25, "Cheater")
        cheater.activate()
        idiot = Button(win, Point((ptp.getX() + 200), (ptp.getY() + 50)), 150, 25, "Idiot")
        idiot.activate()
        copyCat = Button(win, Point((ptp.getX() - 200), (ptp.getY() + 150)), 150, 25, "Copy Cat")
        copyCat.activate()
        grim = Button(win, Point((ptp.getX() + 200), (ptp.getY() + 150)), 150, 25, "Grim")
        grim.activate()
        detective = Button(win, Point(x, (ptp.getY() + 200)), 150, 25, "Detective")
        detective.activate()

        Instruction = Button(win, Point(400, 50), 100, 50, "Instructions")
        Instruction.activate()
        RoundRobin = Button(win, Point(400, 100), 100, 25, "Round Robin")
        RoundRobin.activate()
        Menu = Button(win, Point(400, 700), 100, 25, "Main Menu")
        Menu.activate()
        Reset = Button(win, Point(400, 650), 100, 25, "Reset")
        Reset.activate()
        Play = Button(win, Point(400, 600), 100, 25, "Play")
        Play.activate()
        Exit = Button(win, Point(400, 750), 100, 25, "Exit")
        Exit.activate()

        
        main_text = Text(Point(400,350),"' Please Select Player 1'")
        main_text.setSize(14)
        main_text.draw(win)

        
        return ptp, niceGuy, cheater, idiot, copyCat, grim, detective, Exit, Menu, Reset, Play, Instruction, RoundRobin, main_text

def payoffTableDraw(win, CC, CD, DC, DD):

        ### Making the payoff table ###
        payoff_table = Rectangle(Point(0,800), Point(325,525))
        payoff_table.setFill("light blue")
        payoff_table.draw(win)

        table_tl = Rectangle(Point(100,675), Point(200,600))
        table_tl.setFill("white")
        table_tl.draw(win)

        table_tr = Rectangle(Point(200,675), Point(300,600))
        table_tr.setFill("white")
        table_tr.draw(win)

        table_bl = Rectangle(Point(100,750), Point(200,675))
        table_bl.setFill("white")
        table_bl.draw(win)

        table_br = Rectangle(Point(200,750), Point(300,675))
        table_br.setFill("white")
        table_br.draw(win)
        
        p1_sign = Text(Point(200,545),"Player 1")
        p1_sign.setSize(20)
        p1_sign.draw(win)
        
        p1_coop = Text(Point(150,575),"Cooperate")
        p1_coop.setSize(14)
        p1_coop.draw(win)

        p1_defect = Text(Point(250,575),"Defect")
        p1_defect.setSize(14)
        p1_defect.draw(win)

        p2_sign = Text(Point(50,675),"Player 2")
        p2_sign.setSize(20)
        p2_sign.draw(win)
        
        p2_coop = Text(Point(60,635),"Cooperate")
        p2_coop.setSize(14)
        p2_coop.draw(win)

        p2_defect = Text(Point(60,715),"Defect")
        p2_defect.setSize(14)
        p2_defect.draw(win)

        CC_text = Text(Point(150,637.5), CC) ### need to output tuple 
        CC_text.setSize(14)
        CC_text.draw(win)

        CD_text = Text(Point(250,637.5), CD) ### need to output tuple 
        CD_text.setSize(14)
        CD_text.draw(win)

        DC_text = Text(Point(150,712.5), DC) ### need to output tuple 
        DC_text.setSize(14)
        DC_text.draw(win)

        DD_text = Text(Point(250,712.5), DD) ### need to output tuple 
        DD_text.setSize(14)
        DD_text.draw(win)

        return CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect

def payoffTableUndraw(CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect):

    ## Deleting the payoff table from the GUI ##
    CC_text.undraw()
    CD_text.undraw()
    DC_text.undraw()
    DD_text.undraw()
    payoff_table.undraw()
    table_tl.undraw()
    table_tr.undraw()
    table_bl.undraw()
    table_br.undraw()
    p1_sign.undraw()
    p1_coop.undraw()
    p1_defect.undraw()
    p2_sign.undraw()
    p2_coop.undraw()
    p2_defect.undraw()

def scoreboardDraw(win):

    ## Making a scoreboard to keep track of all algorithms scorees ##
    
    scoreboard = Rectangle(Point(525,200), Point(800,0))
    scoreboard.setFill("light blue")
    scoreboard.draw(win)
    
    scoreboard_sign = Text(Point(675,15),"Scoreboard")
    scoreboard_sign.setSize(20)
    scoreboard_sign.draw(win)

    NiceGuy_sign = Text(Point(625,50),"Nice Guy")
    NiceGuy_sign.setSize(14)
    NiceGuy_sign.draw(win)

    NiceGuy_score = Text(Point(750,50),int(0))
    NiceGuy_score.setSize(14)
    NiceGuy_score.draw(win)

    Cheater_sign = Text(Point(625,75),"Cheater")
    Cheater_sign.setSize(14)
    Cheater_sign.draw(win)

    Cheater_score = Text(Point(750,75), int(0))
    Cheater_score.setSize(14)
    Cheater_score.draw(win)

    Idiot_sign = Text(Point(625,100),"Idiot")
    Idiot_sign.setSize(14)
    Idiot_sign.draw(win)

    Idiot_score = Text(Point(750,100), int(0))
    Idiot_score.setSize(14)
    Idiot_score.draw(win)
    
    CopyCat_sign = Text(Point(625,125),"Copy Cat")
    CopyCat_sign.setSize(14)
    CopyCat_sign.draw(win)

    CopyCat_score = Text(Point(750,125), int(0))
    CopyCat_score.setSize(14)
    CopyCat_score.draw(win)

    Grim_sign = Text(Point(625,150),"Grim")
    Grim_sign.setSize(14)
    Grim_sign.draw(win)

    Grim_score = Text(Point(750,150),int(0))
    Grim_score.setSize(14)
    Grim_score.draw(win)

    Detective_sign = Text(Point(625,175),"Detective")
    Detective_sign.setSize(14)
    Detective_sign.draw(win)

    Detective_score = Text(Point(750,175), int(0))
    Detective_score.setSize(14)
    Detective_score.draw(win)
    
    return scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score 

def scoreboardUndraw(scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score):

    ## Deleting the scoreboard to keep track of all algorithms scorees ##
    NiceGuy_sign.undraw()
    NiceGuy_score.undraw()
    Cheater_sign.undraw()
    Cheater_score.undraw()
    Idiot_sign.undraw()
    Idiot_score.undraw()
    CopyCat_sign.undraw()
    CopyCat_score.undraw()
    Grim_sign.undraw()
    Grim_score.undraw()
    Detective_sign.undraw()
    Detective_score.undraw()
    scoreboard_sign.undraw()
    scoreboard.undraw()

def gameOptionDraw(win):

    option_rect = Rectangle(Point(0,200), Point(275,0))
    option_rect.setFill("light blue")
    option_rect.draw(win)
    
    game_option = Text(Point(140,15),"Game Options")
    game_option.setSize(20)
    game_option.draw(win)

    CC_text = Text(Point(75,50),"Cooperate, Cooperate :")
    CC_text.setSize(12)
    CC_text.draw(win)
    
    CC_input = Entry(Point(200, 50), 15)
    CC_input.setText("3,3")
    CC_input.draw(win)

    #CC = CC_input.getText()

    CD_text = Text(Point(75,75),"Cooperate, Defect :")
    CD_text.setSize(12)
    CD_text.draw(win)
    
    CD_input = Entry(Point(200, 75), 15)
    CD_input.setText("-1,5")
    CD_input.draw(win)

    #CD = CD_input.getText()
    
    DC_text = Text(Point(75,100),"Defect, Cooperate :")
    DC_text.setSize(12)
    DC_text.draw(win)
    
    DC_input = Entry(Point(200, 100), 15)
    DC_input.setText("5,-1")
    DC_input.draw(win)

    #DC = DC_input.getText()

    DD_text = Text(Point(75,125),"Defect, Defect :")
    DD_text.setSize(12)
    DD_text.draw(win)
    
    DD_input = Entry(Point(200, 125), 15)
    DD_input.setText("0,0")
    DD_input.draw(win)

    #DD = DD_input.getText()
    
    rounds_text = Text(Point(75,150),"Number Of Rounds :")
    rounds_text.setSize(12)
    rounds_text.draw(win)
    
    rounds_input = Entry(Point(200, 150), 15)
    rounds_input.setText(int(5))
    rounds_input.draw(win)

    return CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option


def gameOptionUndraw(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option):

    CC_text.undraw()
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

def DrawIntro(win):

    Intro_Back = Rectangle(Point(0,0), Point(800,800))
    Intro_Back.setFill("royal blue")
    Intro_Back.draw(win)
    
    Intro = Text(Point(400,100),"Welcome to Prisonner's Dilemma Game")
    Intro.setSize(30)
    Intro.draw(win)

    Intro_message = Text(Point(400,300),"Please Select an Option")
    Intro_message.setSize(20)
    Intro_message.draw(win)


    DiscoverButton = Button(win, Point(200,400), 250, 50, "Discover Our Algorithms & How They Perform")
    DiscoverButton.activate()

    PlayButton = Button(win, Point(600, 400), 250, 50, "Play Against Algorithms")
    PlayButton.activate()

    Exit = Button(win, Point(400, 750), 100, 25, "Exit")
    Exit.activate()

    return win, Intro_Back, Intro, Intro_message, DiscoverButton, PlayButton, Exit

    
def UndrawIntro(win, Intro_Back, Intro, Intro_message):

    Intro_Back.undraw()
    Intro.undraw()
    Intro_message.undraw()
    

    clearRect = Rectangle(Point(-100,-100), Point(800,800))
    clearRect.setFill("white")
    clearRect.draw(win)

    Exit = Button(win, Point(400, 750), 100, 25, "Exit")
    Exit.activate()

    return Exit

def DrawRoundScore(win):

        ### Making Each Round Scoring Table ###

        payoff_round = Rectangle(Point(475,800), Point(800,525))
        payoff_round.setFill("light blue")
        payoff_round.draw(win)

        nb_round = Text(Point(550,550),"Round Number")
        nb_round.setSize(18)
        nb_round.draw(win)

        p1_round = Text(Point(665,550),"Player 1")
        p1_round.setSize(18)
        p1_round.draw(win)

        p2_round = Text(Point(750,550),"Player 2")
        p2_round.setSize(18)
        p2_round.draw(win)

        round_1 = Text(Point(550,575),"Round 1")
        round_1.setSize(14)
        round_1.draw(win)

        p1_round1 = Text(Point(665,575), int(0))
        p1_round1.setSize(14)
        p1_round1.draw(win)

        p2_round1 = Text(Point(750,575), int(0))
        p2_round1.setSize(14)
        p2_round1.draw(win)

        round_2 = Text(Point(550,600),"Round 2")
        round_2.setSize(14)
        round_2.draw(win)

        p1_round2 = Text(Point(665,600), int(0))
        p1_round2.setSize(14)
        p1_round2.draw(win)

        p2_round2 = Text(Point(750,600), int(0))
        p2_round2.setSize(14)
        p2_round2.draw(win)

        round_3 = Text(Point(550,625),"Round 3")
        round_3.setSize(14)
        round_3.draw(win)

        p1_round3 = Text(Point(665,625), int(0))
        p1_round3.setSize(14)
        p1_round3.draw(win)

        p2_round3 = Text(Point(750,625), int(0))
        p2_round3.setSize(14)
        p2_round3.draw(win)

        round_4 = Text(Point(550,650),"Round 4")
        round_4.setSize(14)
        round_4.draw(win)

        p1_round4 = Text(Point(665,650), int(0))
        p1_round4.setSize(14)
        p1_round4.draw(win)

        p2_round4 = Text(Point(750,650), int(0))
        p2_round4.setSize(14)
        p2_round4.draw(win)

        round_5 = Text(Point(550,675),"Round 5")
        round_5.setSize(14)
        round_5.draw(win)

        p1_round5 = Text(Point(665,675), int(0))
        p1_round5.setSize(14)
        p1_round5.draw(win)

        p2_round5 = Text(Point(750,675), int(0))
        p2_round5.setSize(14)
        p2_round5.draw(win)
        
        round_6 = Text(Point(550,700),"Round 6")
        round_6.setSize(14)
        round_6.draw(win)

        p1_round6 = Text(Point(665,700), int(0))
        p1_round6.setSize(14)
        p1_round6.draw(win)

        p2_round6 = Text(Point(750,700), int(0))
        p2_round6.setSize(14)
        p2_round6.draw(win)

        round_7 = Text(Point(550,725),"Round 7")
        round_7.setSize(14)
        round_7.draw(win)

        p1_round7 = Text(Point(665,725), int(0))
        p1_round7.setSize(14)
        p1_round7.draw(win)

        p2_round7 = Text(Point(750,725), int(0))
        p2_round7.setSize(14)
        p2_round7.draw(win)

        round_8 = Text(Point(550,750),"Round 8")
        round_8.setSize(14)
        round_8.draw(win)

        p1_round8 = Text(Point(665,750), int(0))
        p1_round8.setSize(14)
        p1_round8.draw(win)

        p2_round8 = Text(Point(750,750), int(0))
        p2_round8.setSize(14)
        p2_round8.draw(win)

        return p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8

def DrawInstruction2(win):

    instruction_rectangle = Rectangle(Point(-100,-100), Point(900,900))
    instruction_rectangle.setFill("light blue")
    instruction_rectangle.draw(win)

    instructiontitle = Text(Point(400, 50), "INSTRUCTIONS")
    instructiontitle.setSize(20)
    instructiontitle.setStyle("bold")
    instructiontitle.draw(win)

    title1 = Text(Point(400, 100), "General")
    title1.setSize(16)
    title1.draw(win)

    label1 = Text(Point(400, 150), "Click on any two of the strategies you want to see pitted against eachother. \n Then, press play, and you will see the game played out for x amount of rounds.")
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
    
    title4 = Text(Point(400, 400), "Round Robin")
    title4.setSize(16)
    title4.draw(win)

    label4 = Text(Point(400, 450),'Press this button to see a "Round Robin" tournament play out. \n Each player will play against the other for x amount of rounds.')
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

    label7 = Text(Point(400, 725), "It shows the the payoffs or outcome for the first 8 rounds, for Player 1 and Player 2.")
    label7.draw(win)

    return instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 

def UndrawInstruction2(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 ):

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
