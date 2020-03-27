################################################
##Midterm Project COM313
##Date: 2019-10-15
##Created by: Mathieu Vigneault
##Reviewed by: Jake Corcoran & Simon Moreira
##
##File Description:
##
##    The file support an introduction interface and two different game or setup that allows the user to;
##    1. Play games against different algorithms.
##    2. See how each algorithm can perform against each other.
##    The file contains the main function, which primary function is to make sure the game runs properly and
##    efficiently in a logical manner for the user. 
#################################################

#Import other files to allow graphing to the GUI, create buttons, modify excel files,
#but also use all other files functions that were coded up to shorten up the main and do specific things
from graphics import *
from random import randrange
from Game import *
from DiscoverySettings import *
from getValues import *
from PlaySettings import *
from Select_Algorithm import *
from Round_Robin import *
from Button import *
import sys
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

## The main functions contains all the part of the game by importing them from other files and uses logic to make the game work. ##
def main():

    ### Upload the window & the Intro menu ###
    win = GraphWin("Midterm Project 313", 800, 800)
    win, Intro_Back, Intro, Intro_message, DiscoverButton, PlayButton, Exit = DrawIntro(win)

    pt = win.getMouse() #Get a mouse click from the user


    ## The introduction page is being shown until the exit button is pressed ##
    while Exit.isClicked(pt) == False:

        ## Keep prompting the user for a click until one of the 2 game buttons is clicked ##
        while (DiscoverButton.isClicked(pt) == False) and (PlayButton.isClicked(pt) == False):
            pt = win.getMouse()

        ## Go to the user vs. algorithm game if the user click is on the play button ##
        if PlayButton.isClicked(pt):
        
            ##### Undrawing the introduction page #####
            Exit = UndrawIntro(win, Intro_Back, Intro, Intro_message)

            ##### Drawing the game page for the user to play random cpu algorithms #####
            Exit, Menu, Reset, Play, Instruction, name_input, main_text = PlaySettings(win) ##Add utility buttons
            scoreboard_sign, p1_sign, p1_score, p2_sign, p2_score = DrawScoreboard(win) ## Add scoreboard in the top right
            CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = DrawGameOption(win) ## Add Game option in the bottom left
            CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input) ## get current value inside the Game option panel
            CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, Coop_Button, Defect_Button, p2_sign, p2_coop, p2_defect = DrawPayoffTable(win, CC, CD, DC, DD) ## Add payoff table
            p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8 = DrawRoundOutput(win) ## Add round preview in bottom right


            ## The game is being played until the menu button is pressed ##
            ## If menu button is pressed, then goes back to main menu ##
            while(Menu.isClicked(pt) == False):

                ## Implements a a list of players (algorithms) and get the length of that list ##
                ## Note that we have 6 algorithms coded total and each number is associated with a name ##
                list_players = [1,2,3,4,5,6]
                alg_num = len(list_players)

                ## The game is being played until the reset button is pressed ##
                ## If the reset button is hit, all scores are reset and the entire game is back to original as well ##
                while(Reset.isClicked(pt) == False):
                    
                    CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                    setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)
                    
                    while(len(list_players) > 0):
                        
                        current_round = 0 # keep tracks of current round being played
                        dummy = 0
                        last_move1 = ["X"] # list that keep track of p1 move
                        last_move2 = ["X"] # list that keep track of p2 move
                        CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                        setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)

                        p2 = randrange(1,(alg_num+1)) #Assign a random value to player 2 (p2) & remove the player from entire player list
                        while p2 not in list_players:
                            p2 = randrange(1,(alg_num+1))

                        list_players.remove(p2)
                        alg_name = AlgorithmName(p2)

                        while(current_round != rounds):

            
                            while(Coop_Button.isClicked(pt) == False) and (Defect_Button.isClicked(pt) == False):

                                main_text.setText("'Please Select Cooperate or Defect'")
                                pt = win.getMouse()
                                ## Check if any major buttons who stop the game are press ##
                                if(Exit.isClicked(pt)):
                                    win.close()
                                    sys.exit()
                                if(Menu.isClicked(pt)):
                                    break
                                if(Instruction.isClicked(pt)):

                                    #### Delete Game Option Panel ####
                                    UndrawGameOption(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)
                                    main_text.undraw()
                                    name_input.undraw()

                                    #### Draw Instruction GUI ###
                                    instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction1(win)

                                    #### Wait until the user click again ####
                                    pt = win.getMouse()
                                    
                                    #### Undraw Instruction GUI & go back to current game ####
                                    UndrawInstruction1(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                                    ##### Drawing the game page again for the user to play random cpu algorithms #####
                                    Exit, Menu, Reset, Play, Instruction, name_input, main_text = PlaySettings(win)
                                    CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = DrawGameOption(win)
                                    CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                                    CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, Coop_Button, Defect_Button, p2_sign, p2_coop, p2_defect = DrawPayoffTable(win, CC, CD, DC, DD)
                                
                                CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                                setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)


                            if(Menu.isClicked(pt)):
                                    break
                            while Play.isClicked(pt) == False:

                                click_count = 0
                                if(Coop_Button.isClicked(pt) == True):
                                    p1 = 1

                                    if(dummy == 2):
                                        bold2.undraw()
                                        
                                    bold1 = Rectangle(Point(180,230), Point(270,270))
                                    bold1.setFill("Black")
                                    bold1.draw(win)

                                    Coop_Button = Button(win, Point(225, 250), 75, 25, "Cooperate")
                                    Coop_Button.activate()

                                    dummy = 1
                                    
                                if(Defect_Button.isClicked(pt) == True):
                                    p1 = 2

                                    if(dummy == 1):
                                        bold1.undraw()
                                        
                                    bold2 = Rectangle(Point(180,330), Point(270,370))
                                    bold2.setFill("Black")
                                    bold2.draw(win)

                                    Defect_Button = Button(win, Point(225, 350), 75, 25, "Defect")
                                    Defect_Button.activate()

                                    dummy = 2


                                pt = win.getMouse()
                                CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                                setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)
                                if(dummy == 1):
                                    bold1.undraw()
                                    dummy = 0
                                if(dummy == 2):
                                    bold2.undraw()
                                    dummy = 0 

                                if(Exit.isClicked(pt)):
                                    win.close()
                                    sys.exit()
                                if(Menu.isClicked(pt)):
                                    break
                                if(Instruction.isClicked(pt)):

                                    #### Delete Game Option Panel ####
                                    UndrawGameOption(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)
                                    main_text.undraw()
                                    name_input.undraw()

                                    #### Draw Instruction GUI ###
                                    instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction1(win)

                                    #### Wait until the user click again ####
                                    pt = win.getMouse()
                                    
                                    #### Undraw Instruction GUI & go back to current game ####
                                    UndrawInstruction1(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                                    ##### Drawing the game page again for the user to play random cpu algorithms #####
                                    Exit, Menu, Reset, Play, Instruction, name_input, main_text = PlaySettings(win)
                                    CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = DrawGameOption(win)
                                    CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                                    CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, Coop_Button, Defect_Button, p2_sign, p2_coop, p2_defect = DrawPayoffTable(win, CC, CD, DC, DD)
                         

                            if(Exit.isClicked(pt)):
                                win.close()
                                sys.exit()
                            if(Menu.isClicked(pt)):
                                break
                            if(Reset.isClicked(pt)):
                                break

                            tupleOut = playingGame2(win, p1, p2, last_move1, last_move2, CC, CD, DC, DD, current_round, rounds, p1_score, p2_score,
                                                                            p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5,
                                                                            p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)

                            current_round += 1
                            
                            ## Open existing workbook ##
                            book = open_workbook("Database.xls")

                            ## Get the first sheet inside the workbook ##
                            r_sheet = book.sheet_by_index(0)


                            ## Copy the workbook read over into a workbook we can write into ##
                            wb = copy(book)
                            ## Get the sheet to write to within the writable copy ##
                            w_sheet = wb.get_sheet(0)

                            w_sheet.write(0, 0, 'Name')
                            w_sheet.write(0, 1, 'Player 1 Move')
                            w_sheet.write(0, 2, 'Player 2 Move')
                            w_sheet.write(0, 3, 'Player 1 Payoff')
                            w_sheet.write(0, 4, 'Player 2 Payoff')
                            w_sheet.write(0, 5, 'Player 1 Score')
                            w_sheet.write(0, 6, 'Player 2 Score')
                            w_sheet.write(0, 7, 'Player 2 Algorithm')
                            

                            number_rows = r_sheet.nrows
                            
                            ## Write to writable sheet ##
                            w_sheet.write(number_rows, 0, name_input.getText())
                            w_sheet.write(number_rows, 1, last_move1[current_round])
                            w_sheet.write(number_rows, 2, last_move2[current_round])
                            w_sheet.write(number_rows, 3, tupleOut[0])
                            w_sheet.write(number_rows, 4, tupleOut[1])
                            w_sheet.write(number_rows, 5, p1_score.getText())
                            w_sheet.write(number_rows, 6, p2_score.getText())
                            w_sheet.write(number_rows, 7, alg_name)

                            ## save the writable workbook 
                            wb.save("Database.xls")

                            number_rows += 1

                            
                            last_move1 = tupleOut[2]
                            last_move2 = tupleOut[3]
                            
                            output1 = Text(Point(400,450), "Player 1 Score: " + str(tupleOut[0]))
                            output1.setTextColor("Black")
                            output1.setSize(16)
                            output1.draw(win)

                            output2 = Text(Point(400, 475), "Player 2 Score: " + str(tupleOut[1]))
                            output2.setTextColor("Black")
                            output2.setSize(16)
                            output2.draw(win)

                            
                            if(current_round == rounds):
                                break
                            if(Menu.isClicked(pt)):
                                break
                            if(Reset.isClicked(pt)):
                                break
                            pt = win.getMouse()
                            main_text.setText("'Please Select Cooperate or Defect'")
                            CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                            setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)
                            output1.undraw()
                            output2.undraw()
                            if(Exit.isClicked(pt)):
                                win.close()
                                sys.exit()
                            if(Menu.isClicked(pt)):
                                break
                            if(Reset.isClicked(pt)):
                                break
                            if(Instruction.isClicked(pt)):

                                #### Delete Game Option Panel ####
                                UndrawGameOption(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)
                                main_text.undraw()
                                name_input.undraw()

                                #### Draw Instruction GUI ###
                                instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction1(win)

                                #### Wait until the user click again ####
                                pt = win.getMouse()
                                
                                #### Undraw Instruction GUI & go back to current game ####
                                UndrawInstruction1(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                                ##### Drawing the game page again for the user to play random cpu algorithms #####
                                Exit, Menu, Reset, Play, Instruction, name_input, main_text = PlaySettings(win)
                                CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = DrawGameOption(win)
                                CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                                CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, Coop_Button, Defect_Button, p2_sign, p2_coop, p2_defect = DrawPayoffTable(win, CC, CD, DC, DD)
                                

                        
                        if(Exit.isClicked(pt)):
                            win.close()
                            sys.exit()
                        if(Menu.isClicked(pt)):
                            break
                        if(Reset.isClicked(pt)):
                            break
                        if(len(list_players) == 0):
                            break
                        main_text.setText("Your are now playing a new opponent.\nPlease click anywhere to start next round.")
                        pt = win.getMouse()
                        CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                        setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)
                        if(Exit.isClicked(pt)):
                            win.close()
                            sys.exit()
                        if(Menu.isClicked(pt)):
                            break
                        if(Reset.isClicked(pt)):
                            break
                        if(Instruction.isClicked(pt)):

                            #### Delete Game Option Panel ####
                            UndrawGameOption(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)
                            main_text.undraw()
                            name_input.undraw()

                            #### Draw Instruction GUI ###
                            instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction1(win)

                            #### Wait until the user click again ####
                            pt = win.getMouse()
                            
                            #### Undraw Instruction GUI & go back to current game ####
                            UndrawInstruction1(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                            ##### Drawing the game page again for the user to play random cpu algorithms #####
                            Exit, Menu, Reset, Play, Instruction, name_input, main_text = PlaySettings(win)
                            CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = DrawGameOption(win)
                            CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                            CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, Coop_Button, Defect_Button, p2_sign, p2_coop, p2_defect = DrawPayoffTable(win, CC, CD, DC, DD)
                            
                        output1.undraw()
                        output2.undraw()
                        ResetRoundPayoff(p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)
                        main_text.setText("'Please Select Cooperate or Defect'")
                        

                    if(Menu.isClicked(pt)):
                        break
                    if(Reset.isClicked(pt)):
                        break
                    main_text.setText("GAME OVER\nPlease Click Reset to Play Again")
                    #count_score = 0
                    pt = win.getMouse()
                    CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                    setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)
                    if(Exit.isClicked(pt)):
                        win.close()
                        sys.exit()
                    if(Menu.isClicked(pt)):
                        break
                    if(Reset.isClicked(pt)):
                        break
                    if(Instruction.isClicked(pt)):

                        #### Delete Game Option Panel ####
                        UndrawGameOption(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)
                        main_text.undraw()
                        name_input.undraw()
                        #### Delete Scoreboard ####
                        UndrawScoreboard(scoreboard_sign, p1_sign, p1_score, p2_sign, p2_score, name_input)

                        #### Draw Instruction GUI ###
                        instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction1(win)

                        #### Wait until the user click again ####
                        pt = win.getMouse()
                        
                        #### Undraw Instruction GUI & go back to current game ####
                        UndrawInstruction1(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                        ##### Drawing the game page again for the user to play random cpu algorithms #####
                        Exit, Menu, Reset, Play, Instruction, name_input, main_text = PlaySettings(win)
                        scoreboard_sign, p1_sign, p1_score, p2_sign, p2_score = DrawScoreboard(win)
                        CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = DrawGameOption(win)
                        CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                        CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, Coop_Button, Defect_Button, p2_sign, p2_coop, p2_defect = DrawPayoffTable(win, CC, CD, DC, DD)
                        

                if(Menu.isClicked(pt)):
                    break
                ResetRoundPayoff(p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)
                p1_score.setText(int(0))
                p2_score.setText(int(0))
                pt = win.getMouse()
                CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)
                if(Exit.isClicked(pt)):
                    win.close()
                    sys.exit()
                if(Menu.isClicked(pt)):
                    break
                if(Instruction.isClicked(pt)):

                        #### Delete Game Option Panel ####
                        UndrawGameOption(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)
                        main_text.undraw()
                        name_input.undraw()

                        #### Delete Scoreboard ####
                        UndrawScoreboard(scoreboard_sign, p1_sign, p1_score, p2_sign, p2_score,name_input)

                        #### Draw Instruction GUI ###
                        instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction1(win)

                        #### Wait until the user click again ####
                        pt = win.getMouse()
                        
                        #### Undraw Instruction GUI & go back to current game ####
                        UndrawInstruction1(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                        ##### Drawing the game page again for the user to play random cpu algorithms #####
                        Exit, Menu, Reset, Play, Instruction, name_input, main_text = PlaySettings(win)
                        scoreboard_sign, p1_sign, p1_score, p2_sign, p2_score = DrawScoreboard(win)
                        CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = DrawGameOption(win)
                        CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                        CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, Coop_Button, Defect_Button, p2_sign, p2_coop, p2_defect = DrawPayoffTable(win, CC, CD, DC, DD)
                        


            #### Delete Game Option Panel ####
            UndrawGameOption(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)

            #### Delete Scoreboard ####
            UndrawScoreboard(scoreboard_sign, p1_sign, p1_score, p2_sign, p2_score, name_input)
            p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8 = DrawRoundOutput(win)

            
            #### Delete Payoff Table ####
            #payoffTableUndraw(CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect)

            #### Draw Intro of Game ####
            win, Intro_Back, Intro, Intro_message, DiscoverButton, PlayButton, Exit = DrawIntro(win)

            pt = win.getMouse()
            if(Exit.isClicked(pt)):
                win.close()
                sys.exit()
                
            


        if DiscoverButton.isClicked(pt):

            ##### NEED UNDRAW FUNCTION  HERE #####
            Exit = UndrawIntro(win, Intro_Back, Intro, Intro_message)

            ## Create interface and buttons to allow game to be played ##
            CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = gameOptionDraw(win)
            scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score = scoreboardDraw(win)        
            ptp, niceGuy, cheater, idiot, copyCat, grim, detective, Exit, Menu, Reset, Play, Instruction, RoundRobin, main_text = DiscoverySettings(win)
            CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
            CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect = payoffTableDraw(win, CC, CD, DC, DD)
            p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8 = DrawRoundScore(win)
            
            while(Menu.isClicked(pt) == False):

                while(Reset.isClicked(pt) == False):

                    click_number = 0
                    CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                    setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)

                    main_text.setText("'Please Select Player 1'")

                    while click_number != 1:
                        pt = win.getMouse()
                        CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                        setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)
                        if(Exit.isClicked(pt)):
                            win.close()
                            sys.exit()
                        if(Menu.isClicked(pt)):
                            break
                        if(Reset.isClicked(pt)):
                            break
                        if(Instruction.isClicked(pt)):

                            #### Delete Game Option Panel ####
                            gameOptionUndraw(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)  

                            #### Delete Scoreboard ####
                            scoreboardUndraw(scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score)

                            #### Delete Payoff Table ####
                            payoffTableUndraw(CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect)

                            #### Draw Instruction GUI ###
                            instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction2(win)

                            #### Wait until the user click again ####
                            pt = win.getMouse()
                            
                            #### Undraw Instruction GUI & go back to current game ####
                            UndrawInstruction2(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                            ## Create interface and buttons to allow game to be played ##
                            CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = gameOptionDraw(win)
                            scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score = scoreboardDraw(win)        
                            CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                            CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect = payoffTableDraw(win, CC, CD, DC, DD)
                            
                        if(RoundRobin.isClicked(pt)):
                            winner_text, winner_name = round_robin(win, CC, CD, DC, DD, rounds, p1_round1, p2_round1, p1_round2, p2_round2, p1_round3,
                                                                    p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6,
                                                                    p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)

                            pt = win.getMouse()
                            winner_text.undraw()
                            winner_name.undraw()

                        if (niceGuy.isClicked(pt) == True) or (cheater.isClicked(pt) == True) or (idiot.isClicked(pt) == True) or (copyCat.isClicked(pt) == True) or (grim.isClicked(pt) == True) or (detective.isClicked(pt) == True):
                            p1, click_number, text1 = Select_AlgPair(win, click_number, pt, ptp, Menu, Reset, Exit, niceGuy, cheater, idiot, copyCat, grim, detective)


                    if(Menu.isClicked(pt)):
                            break
                    if(Reset.isClicked(pt)):
                            break
                    if(Instruction.isClicked(pt)):

                        #### Delete Game Option Panel ####
                        gameOptionUndraw(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)  

                        #### Delete Scoreboard ####
                        scoreboardUndraw(scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score)

                        #### Delete Payoff Table ####
                        payoffTableUndraw(CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect)

                        #### Draw Instruction GUI ###
                        instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction2(win)

                        #### Wait until the user click again ####
                        pt = win.getMouse()
                        
                        #### Undraw Instruction GUI & go back to current game ####
                        UndrawInstruction2(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                        ## Create interface and buttons to allow game to be played ##
                        CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = gameOptionDraw(win)
                        scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score = scoreboardDraw(win)        
                        CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                        CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect = payoffTableDraw(win, CC, CD, DC, DD)
                        
                    if(RoundRobin.isClicked(pt)):
                        winner_text, winner_name = round_robin(win, CC, CD, DC, DD, rounds, p1_round1, p2_round1, p1_round2, p2_round2, p1_round3,
                                                                p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6,
                                                                p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)

                        pt = win.getMouse()
                        winner_text.undraw()
                        winner_name.undraw()
                        
                    main_text.setText("'Please Select Player 2'")
                    while click_number != 2:
                        pt = win.getMouse()
                        CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                        setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)
                        if(Exit.isClicked(pt)):
                            win.close()
                            sys.exit()
                        if(Menu.isClicked(pt)):
                            break
                        if(Reset.isClicked(pt)):
                            break
                        if(Instruction.isClicked(pt)):

                            #### Delete Game Option Panel ####
                            gameOptionUndraw(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)  

                            #### Delete Scoreboard ####
                            scoreboardUndraw(scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score)

                            #### Delete Payoff Table ####
                            payoffTableUndraw(CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect)

                            #### Draw Instruction GUI ###
                            instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction2(win)

                            #### Wait until the user click again ####
                            pt = win.getMouse()
                            
                            #### Undraw Instruction GUI & go back to current game ####
                            UndrawInstruction2(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                            ## Create interface and buttons to allow game to be played ##
                            CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = gameOptionDraw(win)
                            scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score = scoreboardDraw(win)        
                            CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                            CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect = payoffTableDraw(win, CC, CD, DC, DD)
                            
                        if(RoundRobin.isClicked(pt)):
                            winner_text, winner_name = round_robin(win, CC, CD, DC, DD, rounds, p1_round1, p2_round1, p1_round2, p2_round2, p1_round3,
                                                                    p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6,
                                                                    p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)

                            pt = win.getMouse()
                            winner_text.undraw()
                            winner_name.undraw()

                        if (niceGuy.isClicked(pt) == True) or (cheater.isClicked(pt) == True) or (idiot.isClicked(pt) == True) or (copyCat.isClicked(pt) == True) or (grim.isClicked(pt) == True) or (detective.isClicked(pt) == True):
                            p2, click_number, text2 = Select_AlgPair(win, click_number, pt, ptp, Menu, Reset, Exit, niceGuy, cheater, idiot, copyCat, grim, detective)

                    
                    if(Menu.isClicked(pt)):
                            break
                    if(Reset.isClicked(pt)):
                            break
                    main_text.setText("'Press Play to see Results'")


                    while Play.isClicked(pt) == False:
                        pt = win.getMouse()
                        if(Exit.isClicked(pt)):
                            win.close()
                            sys.exit()
                        if(Menu.isClicked(pt)):
                            break
                        if(Reset.isClicked(pt)):
                            break
                        if(Instruction.isClicked(pt)):

                            #### Delete Game Option Panel ####
                            gameOptionUndraw(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)  

                            #### Delete Scoreboard ####
                            scoreboardUndraw(scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score)

                            #### Delete Payoff Table ####
                            payoffTableUndraw(CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect)

                            #### Draw Instruction GUI ###
                            instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction2(win)

                            #### Wait until the user click again ####
                            pt = win.getMouse()
                            
                            #### Undraw Instruction GUI & go back to current game ####
                            UndrawInstruction2(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                            ## Create interface and buttons to allow game to be played ##
                            CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = gameOptionDraw(win)
                            scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score = scoreboardDraw(win)        
                            CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                            CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect = payoffTableDraw(win, CC, CD, DC, DD)
                            
                        if(RoundRobin.isClicked(pt)):
                            winner_text, winner_name = round_robin(win, CC, CD, DC, DD, rounds, p1_round1, p2_round1, p1_round2, p2_round2, p1_round3,
                                                                    p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6,
                                                                    p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)

                    if(Menu.isClicked(pt)):
                        break
                    if(Reset.isClicked(pt)):
                        break
                    main_text.setText("'Click to Re-choose Players'")
                    CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                    setValues(CC, CD, DC, DD, CC_text, CD_text, DC_text, DD_text)

                    tupleOut = playingGame1(win, p1, p2, CC, CD, DC, DD, rounds, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score,
                                           p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5,
                                           p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)
                    
                    text1pt = text1.getAnchor()
                    output1 = Text(Point(text1pt.getX(),(text1pt.getY()+50)), "Score: " + str(tupleOut[0]))
                    output1.setTextColor("Blue")
                    output1.draw(win)

                    text2pt = text2.getAnchor()
                    output2 = Text(Point(text2pt.getX(), (text2pt.getY()+50)), "Score: " + str(tupleOut[1]))
                    output2.setTextColor("Red")
                    output2.draw(win)


                    pt = win.getMouse()
                    output1.undraw()
                    output2.undraw()
                    if(Exit.isClicked(pt)):
                        win.close()
                        sys.exit()
                    if(Menu.isClicked(pt)):
                        break
                    if(Reset.isClicked(pt)):
                        break
                    if(Instruction.isClicked(pt)):

                            #### Delete Game Option Panel ####
                            gameOptionUndraw(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)  

                            #### Delete Scoreboard ####
                            scoreboardUndraw(scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score)

                            #### Delete Payoff Table ####
                            payoffTableUndraw(CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect)

                            #### Draw Instruction GUI ###
                            instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction2(win)

                            #### Wait until the user click again ####
                            pt = win.getMouse()
                            
                            #### Undraw Instruction GUI & go back to current game ####
                            UndrawInstruction2(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                            ## Create interface and buttons to allow game to be played ##
                            CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = gameOptionDraw(win)
                            scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score = scoreboardDraw(win)        
                            CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                            CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect = payoffTableDraw(win, CC, CD, DC, DD)
                            
                    if(RoundRobin.isClicked(pt)):
                        winner_text, winner_name = round_robin(win, CC, CD, DC, DD, rounds, p1_round1, p2_round1, p1_round2, p2_round2, p1_round3,
                                                                p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6,
                                                                p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)
                    main_text.setText("'Please Select Player 1'")
                    text1.undraw()
                    text2.undraw()


                if(Exit.isClicked(pt)):
                    win.close()
                    sys.exit()
                if(Menu.isClicked(pt)):
                    break
                if(click_number == 1):
                    text1.undraw()
                if(click_number == 2):
                    text1.undraw()
                    text2.undraw()
                NiceGuy_score.setText(int(0))
                Cheater_score.setText(int(0))
                Idiot_score.setText(int(0))
                CopyCat_score.setText(int(0))
                Grim_score.setText(int(0))
                Detective_score.setText(int(0))
                ResetRoundPayoff(p1_round1, p2_round1, p1_round2, p2_round2, p1_round3, p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6, p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)
                main_text.setText("'Please Click Anywhere to Start Over!'")
                pt = win.getMouse()
                if(Instruction.isClicked(pt)):

                    #### Delete Game Option Panel ####
                    gameOptionUndraw(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)  

                    #### Delete Scoreboard ####
                    scoreboardUndraw(scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score)

                    #### Delete Payoff Table ####
                    payoffTableUndraw(CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect)

                    #### Draw Instruction GUI ###
                    instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7 = DrawInstruction2(win)

                    #### Wait until the user click again ####
                    pt = win.getMouse()
                    
                    #### Undraw Instruction GUI & go back to current game ####
                    UndrawInstruction2(instruction_rectangle, instructiontitle, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7)

                    ## Create interface and buttons to allow game to be played ##
                    CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option = gameOptionDraw(win)
                    scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score = scoreboardDraw(win)        
                    CC, CD, DC, DD, rounds = getValues(CC_input, CD_input, DC_input, DD_input, rounds_input)
                    CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect = payoffTableDraw(win, CC, CD, DC, DD)
                    
                if(RoundRobin.isClicked(pt)):
                    winner_text, winner_name = round_robin(win, CC, CD, DC, DD, rounds, p1_round1, p2_round1, p1_round2, p2_round2, p1_round3,
                                                            p2_round3, p1_round4, p2_round4, p1_round5, p2_round5, p1_round6,
                                                            p2_round6, p1_round7, p2_round7, p1_round8, p2_round8)

                
            #### Delete Game Option Panel ####
            gameOptionUndraw(CC_text, CC_input, CD_text, CD_input, DC_text, DC_input, DD_text, DD_input, rounds_text, rounds_input, option_rect, game_option)  

            #### Delete Scoreboard ####
            scoreboardUndraw(scoreboard, scoreboard_sign, NiceGuy_sign, Cheater_sign, Idiot_sign, CopyCat_sign, Grim_sign, Detective_sign, NiceGuy_score, Cheater_score, Idiot_score, CopyCat_score, Grim_score, Detective_score)

            #### Delete Payoff Table ####
            payoffTableUndraw(CC_text, CD_text, DC_text, DD_text, payoff_table, table_tl, table_tr, table_bl, table_br, p1_sign, p1_coop, p1_defect, p2_sign, p2_coop, p2_defect)

            #### Draw Intro of Game ####
            win, Intro_Back, Intro, Intro_message, DiscoverButton, PlayButton, Exit = DrawIntro(win)

            pt = win.getMouse()
            if(Exit.isClicked(pt)):
                win.close()
                sys.exit()
            
    win.close() #Close the window and game ends
        
 
    

main()
