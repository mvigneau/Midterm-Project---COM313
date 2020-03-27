from graphics import *

def Select_Algorithm(win, pt, ptp, niceGuy, cheater, idiot, copyCat, grim, detective, click_number):

    if(click_number == 0):
        color = "Blue"
        player = "Player 1"
    if(click_number == 1):
        color = "Red"
        player = "Player 2"
    
    if(niceGuy.isClicked(pt)):
        text = Text(Point(ptp.getX(), ptp.getY()-25), player)
        text.setTextColor(color)
        text.draw(win)
        point = 1
        click_number+=1

    if(cheater.isClicked(pt)):
        text = Text(Point(ptp.getX()-200, ptp.getY()+25), player)
        text.setTextColor(color)
        text.draw(win)
        point = 2
        click_number+=1

    if(idiot.isClicked(pt)):
        text = Text(Point(ptp.getX()+200, ptp.getY()+25), player)
        text.setTextColor(color)
        text.draw(win)
        point = 3
        click_number+=1

    if(copyCat.isClicked(pt)):
        text = Text(Point(ptp.getX()-200, ptp.getY()+125), player)
        text.setTextColor(color)
        text.draw(win)
        point = 4
        click_number+=1

    if(grim.isClicked(pt)):
        text = Text(Point(ptp.getX()+200, ptp.getY()+125), player)
        text.setTextColor(color)
        text.draw(win)
        point = 5
        click_number+=1

    if(detective.isClicked(pt)):
        text = Text(Point(ptp.getX(), (ptp.getY()+175)), player)
        text.setTextColor(color)
        text.draw(win)
        point = 6
        click_number+=1

    return point, click_number, text

def Select_AlgPair(win, click_number, pt, ptp, Menu, Reset, Exit, niceGuy, cheater, idiot, copyCat, grim, detective):

    player, click_number, text = Select_Algorithm(win, pt,  ptp, niceGuy, cheater, idiot, copyCat, grim, detective, click_number)
    
    return player, click_number, text







            
