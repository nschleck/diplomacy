### This Code is intended to take diplomacy turnmoves and create a graphic of the game state, showing moves and failed moves ###

############################################# Imports ##############################################
import tkinter as tk #, tkinter.messagebox, tkinter.font?
from PIL import Image, ImageTk
import math

from boardSetup import territories as terrs
from boardSetup import nationality

#terrsTemporary = {    #TODO: replace with real terrs list with full coordinates
#    "brest" : {
#        "x_coord": 320,
 #       "y_coord": 590
 #   },
#    "tunis" : {
#        "x_coord": 480,
#        "y_coord": 950
#    },
#    "black sea" : {
#        "x_coord": 960,
#        "y_coord": 750
#    }
#}

unitsTemporary = {    #TODO: replace with real unit moves
    "bre" : {
        "nation": "england",
        "unit type": "fleet",
        "order": "move",
        "outcome": "fails",
        "dislodge status": 'sustains',
        "target end": "tunis"

    },
    "tun" : {
        "nation": "russia",
        "unit type": "fleet",
        "order": "hold",
        "outcome": "holds",
        "dislodge status": 'sustains',
    },
    "bla" : {
        "nation": "italy",
        "unit type": "fleet",
        "order": "support",
        "outcome": "cut",
        "dislodge status": 'sustains',
        "target start": "brest",        
        "target end": "tunis",
        "support type" : "move support"
    }
}

unitColors = {
    "austria" : "pink",
    "england" : "purple",
    "france" : "blue",
    "germany" : "black",
    "italy" : "green",
    "russia" : "white",
    "turkey" : "yellow"
}

############################### Setup Root Window + Frame #########################################
root = tk.Tk()
root.title("Diplomacy")
root.iconbitmap("GUI\\window_icon.ico")
root.configure(background="grey")

# Setup Graphics Frame #
graphicsFrame = tk.Frame(root)
graphicsFrame.grid(row=0,column=0)

graphicsCanvas = tk.Canvas(graphicsFrame, bg="black", width=1202, height=1010)
graphicsCanvas.pack()

# Initialize globals so images don't get garbage collected
bg_image = None
all_units = None

def drawBackground():
    global bg_image
    bg_image = ImageTk.PhotoImage(Image.open("GUI\\bg_small.jpg"))
    graphicsCanvas.create_image(0,0,image=bg_image,anchor="nw")

# Setup Text Frame #
textFrame = tk.Frame(root)
textFrame.grid(row=0,column=1)

textCanvas = tk.Canvas(textFrame, bg="grey", width=500, height=1010)
textCanvas.pack()

text = tk.Text(textCanvas)
text.insert(tk.INSERT, "Spring 1901 \n\n")
text.pack()

# Import Add-on Icons #
build_icon = ImageTk.PhotoImage(Image.open("GUI\\build_icon.png").resize((60,60), Image.ANTIALIAS))
convoy_icon = ImageTk.PhotoImage(Image.open("GUI\\convoy_icon.png").resize((50,9), Image.ANTIALIAS))
disband_icon = ImageTk.PhotoImage(Image.open("GUI\\disband_icon.png").resize((50,50), Image.ANTIALIAS))
dislodged_icon = ImageTk.PhotoImage(Image.open("GUI\\dislodge_icon.png").resize((60,60), Image.ANTIALIAS))
hold_icon = ImageTk.PhotoImage(Image.open("GUI\\hold_icon.png").resize((50,4), Image.ANTIALIAS))
fail_icon = ImageTk.PhotoImage(Image.open("GUI\\disband_icon.png").resize((25,25), Image.ANTIALIAS))


######################################## Define Unit Classes ######################################################
class Unit:    #TODO finish methods and clean up temporary variables
    def __init__(self, nation, territory, order, status):
        self.nation = nation
        self.territory = territory
        self.order = order
        self.status = status
        self.icon = None
        self.unitType = None
        self.x_pos = terrs[territory]["x_coord"] #TODO pull coordinates from territory info
        self.y_pos = terrs[territory]["y_coord"] #TODO pull coordinates from territory info

    def __str__(self):
        return '{} {} in {} -- order: {}'.format(self.nation, self.unitType, self.territory, self.order)

    def drawUnit(self):
        graphicsCanvas.create_image(self.x_pos, self.y_pos, image=self.icon, anchor="center")

    #### Draw additional icons for unit move, hold, and disband phases ####
    
    # Easy Draw Methods
    def drawUnitBuild(self):
        graphicsCanvas.create_image(self.x_pos, self.y_pos, image= build_icon, anchor="center")
    def drawUnitConvoy(self):
        graphicsCanvas.create_image(self.x_pos, self.y_pos + 26, image= convoy_icon, anchor="center")
    def drawUnitDisband(self): #TODO?
        graphicsCanvas.create_image(self.x_pos, self.y_pos, image= disband_icon, anchor="center")

        #if self.order == "new build": #TODO: think about this. reuse order attribute? how to get "new build" status?
        #   canvas.create_image(self.x_pos, self.y_pos, image="new build icon", anchor="center")
        #elif self.order == "disband": #TODO: think about this. reuse order attribute? how to get "disband" status?
        #   canvas.create_image(self.x_pos, self.y_pos, image="disband icon", anchor="center")
    def drawUnitDislodged(self):
        graphicsCanvas.create_image(self.x_pos, self.y_pos, image= dislodged_icon, anchor="center")
    def drawUnitHold(self):
        graphicsCanvas.create_image(self.x_pos, self.y_pos + 23, image= hold_icon, anchor="center")

    # Harder Draw Methods
    def drawUnitMove(self, target):
        target_x = terrs[target]["x_coord"]#TODO
        target_y = terrs[target]["y_coord"]#TODO

        # Quick Maths - calculate offsets for line start and endpoints #TODO elim duplicate code in drawUnitSupport method
        offset = 25
        delta_x = target_x - self.x_pos
        delta_y = target_y - self.y_pos
        theta = math.atan(delta_y / delta_x)
        offset_y = int(math.sin(theta) * offset)
        offset_x = int(math.cos(theta) * offset)
        if delta_x < 0:
            offset_x = offset_x * -1
            offset_y = offset_y * -1

        # Draw Line
        start_x = self.x_pos + offset_x
        start_y = self.y_pos + offset_y
        end_x = target_x - offset_x
        end_y = target_y - offset_y
        graphicsCanvas.create_line(start_x, start_y, end_x, end_y,  width = 3, fill=unitColors[self.nation], arrow=tk.LAST, arrowshape=(20,30,8))
    def drawUnitSupport(self, target, target_start): #TODO elim repeat code
        # Hold Support
        if target_start == None:
            target_x = terrs[target]["x_coord"]#TODO
            target_y = terrs[target]["y_coord"]#TODO

            # Quick Maths - calculate offsets for line start and endpoints #TODO elim duplicate code
            offset = 25
            delta_x = target_x - self.x_pos
            delta_y = target_y - self.y_pos
            theta = math.atan(delta_y / delta_x)
            offset_y = int(math.sin(theta) * offset)
            offset_x = int(math.cos(theta) * offset)
            if delta_x < 0:
                offset_x = offset_x * -1
                offset_y = offset_y * -1
            
            # Draw Line
            start_x = self.x_pos + offset_x
            start_y = self.y_pos + offset_y
            end_x = target_x - offset_x
            end_y = target_y - offset_y
            graphicsCanvas.create_line(start_x, start_y, end_x, end_y,  width = 3, fill=unitColors[self.nation])
            graphicsCanvas.create_oval(target_x - 25, target_y - 25, target_x + 25, target_y + 25,  width = 4, outline=unitColors[self.nation])
        
        #Move Support #TODO add indication arrow for direction of move support?
        else:
            target_x = abs(int((terrs[target]["x_coord"] + terrs[target_start]["x_coord"]) / 2 )) #TODO
            target_y = abs(int((terrs[target]["y_coord"] + terrs[target_start]["y_coord"]) / 2 )) #TODO

            # Quick Maths - calculate offsets for line start and endpoints #TODO elim duplicate code
            offset = 25
            delta_x = target_x - self.x_pos
            delta_y = target_y - self.y_pos
            theta = math.atan(delta_y / delta_x)
            offset_y = int(math.sin(theta) * offset)
            offset_x = int(math.cos(theta) * offset)
            if delta_x < 0:
                offset_x = offset_x * -1
                offset_y = offset_y * -1
            
            # Draw Line
            start_x = self.x_pos + offset_x
            start_y = self.y_pos + offset_y
            end_x = target_x - int(offset_x * (2/5))
            end_y = target_y - int(offset_y * (2/5))
            graphicsCanvas.create_line(start_x, start_y, end_x, end_y,  width = 3, fill=unitColors[self.nation])
            graphicsCanvas.create_oval(target_x - 10, target_y - 10, target_x + 10, target_y + 10,  width = 3, outline=unitColors[self.nation])          
    def drawMoveFails(self, target):#TODO
        target_x = terrs[target]["x_coord"]#TODO
        target_y = terrs[target]["y_coord"]#TODO

        icon_x = int((target_x + self.x_pos) / 2)
        icon_y = int((target_y + self.y_pos) / 2)

        graphicsCanvas.create_image(icon_x, icon_y, image= fail_icon, anchor="center")
    def drawSupportCut(self, target, target_start):#TODO
        # Hold Support cut
        if target_start == None:
            target_x = terrs[target]["x_coord"]#TODO
            target_y = terrs[target]["y_coord"]#TODO
        #Move Support cut
        else:
            target_x = abs(int((terrs[target]["x_coord"] + terrs[target_start]["x_coord"]) / 2 )) #TODO
            target_y = abs(int((terrs[target]["y_coord"] + terrs[target_start]["y_coord"]) / 2 )) #TODO
            
        icon_x = int((target_x + self.x_pos) / 2)
        icon_y = int((target_y + self.y_pos) / 2)

        graphicsCanvas.create_image(icon_x, icon_y, image= fail_icon, anchor="center")

class Army(Unit):
    def __init__(self, nation, territory, order, status):
        super().__init__(nation, territory, order, status)
        self.icon = ImageTk.PhotoImage(Image.open("GUI\\army_"+nation+".png").resize((40,40), Image.ANTIALIAS))
        self.unitType = "army"

    def __repr__(self):
        return 'Army({}, {}, {})'.format(self.nation, self.territory, self.order)

class Fleet(Unit):
    def __init__(self, nation, territory, order, status):
        super().__init__(nation, territory, order, status)
        self.icon = ImageTk.PhotoImage(Image.open("GUI\\fleet_"+nation+".png").resize((40,40), Image.ANTIALIAS))
        self.unitType = "fleet"

    def __repr__(self):
        return 'Fleet({}, {}, {})'.format(self.nation, self.territory, self.order)

###################### Create an Initial List of Unit (Army/Fleet) objects from input turnMoves dictionary ######################

def UnitList(turnMoves):
    unit_list = []
    for unit in turnMoves:
        if turnMoves[unit]["unit type"] == "army":
            unitObj = Army(turnMoves[unit]["nation"], unit, turnMoves[unit]["order"], turnMoves[unit]["dislodge status"])
        elif turnMoves[unit]["unit type"] == "fleet":
            unitObj = Fleet(turnMoves[unit]["nation"], unit, turnMoves[unit]["order"], turnMoves[unit]["dislodge status"])
        
        # Add unitObj to unitList
        unit_list.append(unitObj)

    return unit_list


################################ Drawing Functions ############################### 

# 1 -> Draws Units
def drawUnits(Units):
    for Unit in Units:
        Unit.drawUnit()

# 2 -> Draws Unit Moves and writes them to the text frame
def drawMoves(Units): #TODO: update unit list
    global text
    for Unit in Units:
        unit_nation = nationality[Unit.nation]
        unit_type = Unit.unitType
        unit_territory = terrs[Unit.territory]["name"]
        target_start = None
        target_end = None
        if Unit.order == "hold":
            Unit.drawUnitHold()
            text.insert(tk.INSERT, '{} {} in {} holds\n'.format(unit_nation, unit_type, unit_territory))
        elif Unit.order == "convoy":
            Unit.drawUnitConvoy()
            text.insert(tk.INSERT, '{} {} in {} convoys\n'.format(unit_nation, unit_type, unit_territory))
        elif Unit.order == "move":
            target = unitsTemporary[Unit.territory]["target end"]  #TODO replace unitslist
            target_end = terrs[target]["name"]
            Unit.drawUnitMove(target)
            text.insert(tk.INSERT, '{} {} in {} moves to {}\n'.format(unit_nation, unit_type, unit_territory, target_end))
        elif Unit.order == "support":
            #adds additional info for support order target and move target start
            target = unitsTemporary[Unit.territory]["target end"] #TODO replace unitslist
            target_end = terrs[target]["name"]
            target_move_start = None
            if unitsTemporary[Unit.territory]["support type"] == "move support":
                target_move_start = unitsTemporary[Unit.territory]["target start"]
                target_start = terrs[target_move_start]["name"]
                text.insert(tk.INSERT, '{} {} in {} supports move: {} to {}\n'.format(unit_nation, unit_type, unit_territory, target_start, target_end))
            else:
                text.insert(tk.INSERT, '{} {} in {} supports {}\n'.format(unit_nation, unit_type, unit_territory, target_end))
            Unit.drawUnitSupport(target, target_move_start)
        
# 3 -> Draws Move Outcomes
def drawMoveOutcomes(Units): #TODO: update unit list
    for Unit in Units:
        #indicate failed moves
        if Unit.order == "move" and unitsTemporary[Unit.territory]["outcome"] == "fails": #TODO replace unitslist
            target = unitsTemporary[Unit.territory]["target end"]  #TODO replace unitslist
            Unit.drawMoveFails(target)
        #indicate cut support
        elif Unit.order == "support" and unitsTemporary[Unit.territory]["outcome"] == "cut": #TODO replace unitslist
            #adds additional info for support order target and move target start
            target = unitsTemporary[Unit.territory]["target end"] #TODO replace unitslist
            target_move_start = None
            if unitsTemporary[Unit.territory]["support type"] == "move support":
                target_move_start = unitsTemporary[Unit.territory]["target start"]

            Unit.drawSupportCut(target, target_move_start)
        #indicate dislodged units
        if Unit.status == "dislodged":
            Unit.drawUnitDislodged()

# 4 -> Draws Unit Retreat Moves -> TODO:Remove destroyed units?
def drawRetreats(Units):
    for Unit in Units:
        if Unit.status == "dislodged":
            Unit.drawUnitMove()

# 5 -> (Winter Only) Draws Builds / Disbands
def drawBuildsAndDisbands(Units): #TODO
    for Unit in Units:
        if Unit.order == "build":
            Unit.drawUnitBuild()
        elif Unit.order == "disband":
            Unit.drawUnitDisband()

######################################## Phase Functions ############################################

def drawMovePhase():
    drawBackground()

    global all_units
    all_units = UnitList(unitsTemporary)

    drawUnits(all_units)
    # "NEXT" button input ->
    drawMoves(all_units)
    # "NEXT" button input ->
    drawMoveOutcomes(all_units)

def drawDislodgePhase():
    units = UnitList(unitsTemporary)
    drawUnits(units)
    # "NEXT" button input ->
    drawRetreats(units)

def drawBuildPhase():
    units = UnitList(unitsTemporary)
    drawUnits(units)
    # "NEXT" button input ->
    drawBuildsAndDisbands(units)


####################################### Text Window ################################################




######################### Run Main GUI Loop #################################

drawMovePhase()

root.mainloop()

### Year Loop Structure ###
#drawMovePhase()        # Spring 1901
#drawDislodgePhase()    # Spring 1901
#drawMovePhase()        # Fall 1901
#drawDislodgePhase()    # Fall 1901
#drawBuildPhase()       # Winter 1901
#
#Repeat


## Extras ##
#TODO: order_bar.grid(row=0,column=1) wrt root, not frame --> Write out text of orders on the right side of the screen
#TODO: add a button to hide units, arrows so you can see labels?

########################## Extras, testing, etc. ####################################

