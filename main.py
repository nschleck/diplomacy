### Main code body for running a Diplomacy game

################################################## Initial Setup and Imports ########################################################
import boardSetup, adjudicator
import moveFunctions as move
import pprint
# GUI Imports #
import tkinter as tk
from PIL import Image, ImageTk
import math, time

terrs = boardSetup.territories
nationality = boardSetup.nationality
unitColors = {
    "austria" : "pink",
    "england" : "purple",
    "france" : "blue",
    "germany" : "black",
    "italy" : "green",
    "russia" : "white",
    "turkey" : "yellow"
}

######################################################## GUI Setup #################################################################
def rootWindow():
    global root
    root = tk.Tk()
    root.title("Diplomacy")
    root.iconbitmap("GUI\\window_icon.ico")
    root.configure(background="#5e573e")
    return root
def graphicsWindow(master):
    
    global graphicsFrame
    global graphicsCanvas
    graphicsFrame = tk.Frame(master, bg="black")
    graphicsFrame.grid(row=0,column=0)

    graphicsCanvas = tk.Canvas(graphicsFrame, width=1202, height=1010, bg="black")
    graphicsCanvas.pack()
    return graphicsCanvas, graphicsFrame
def textWindow(master, year_string): 
    global textFrame, text_title, textSubframe, scrollbar, text
    textFrame = tk.Frame(master, bg="#4f5763", width=300, height=1010, padx=5, pady=10)
    textFrame.grid(row=0,column=1)

    #title
    text_title = tk.Text(textFrame, 
        bg="#616b7a", fg="white",
        font=("Courier", 14, "bold"), 
        width=60, height=1, 
        padx=10, pady=10,
        relief=tk.RIDGE)
    text_title.insert(tk.INSERT, year_string)
    text_title.pack()

    #main text lines
    textSubframe = tk.Frame(textFrame, bg="#4f5763")
    textSubframe.pack()
    text = tk.Text(textSubframe, 
        bg="#616b7a", fg="white", 
        font=("Courier", 10), 
        width=80, height=40, 
        padx=10, pady=10, 
        wrap=tk.WORD)
    text.pack(fill="both", expand=True, padx=10, pady=10, side=tk.LEFT)

    #sidebar/scrollbar
    scrollbar = tk.Scrollbar(textSubframe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH, pady=10)

    text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text.yview)

    #text box style tags
    text.tag_config("fail", foreground="#ffa3a3")
    text.tag_config("success", foreground="#84db84")

    return textFrame, text_title, textSubframe, scrollbar, text

def buttonNext(master):
    global button_results
    var = tk.IntVar()                   # Dummy variable
    button_results = tk.Button(master, 
        text="Next>>", 
        command = lambda: var.set(1), 
        bg="#4f5763", fg="white",
        font=("Courier", 12))
    button_results.pack()
    button_results.wait_variable(var)   #Execution waits until var is altered by button press
    button_results.pack_forget()
    return button_results

# TODO kloogy - placeholder empty icon images
build_icon = None
convoy_icon = None
disband_icon = None
dislodged_icon = None
hold_icon = None
fail_icon = None
# Initialize globals so images don't get garbage collected
bg_image = None #TODO?
all_units = None
button_results = None

def drawBackground(canv):
    global bg_image
    bg_image = ImageTk.PhotoImage(Image.open("GUI\\bg_small.jpg"))
    canv.create_image(0,0,image=bg_image,anchor="nw")
    return bg_image

############################## GUI -- Define Unit Classes #TODO use this outside of GUI ###################################################
class Unit:
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
    def drawUnitDisband(self):
        graphicsCanvas.create_image(self.x_pos, self.y_pos, image= disband_icon, anchor="center")
    def drawUnitDislodged(self):
        graphicsCanvas.create_image(self.x_pos, self.y_pos, image= dislodged_icon, anchor="center")
    def drawUnitHold(self):
        graphicsCanvas.create_image(self.x_pos, self.y_pos + 23, image= hold_icon, anchor="center")

    # Harder Draw Methods
    def calculateLineOffsets(self, offset, targ_x, targ_y):
        # Quick Maths - calculate offsets for line start and endpoints
        delta_x = targ_x - self.x_pos
        delta_y = targ_y - self.y_pos
        theta = math.atan(delta_y / delta_x)
        offset_y = int(math.sin(theta) * offset)
        offset_x = int(math.cos(theta) * offset)
        if delta_x < 0:
            offset_x = offset_x * -1
            offset_y = offset_y * -1

        return offset_x, offset_y

    def drawUnitMove(self, target):
        target_x = terrs[target]["x_coord"]
        target_y = terrs[target]["y_coord"]

        offset_x, offset_y = self.calculateLineOffsets(15, target_x, target_y)

        # Draw Line
        start_x = self.x_pos + offset_x
        start_y = self.y_pos + offset_y
        end_x = target_x - offset_x
        end_y = target_y - offset_y
        graphicsCanvas.create_line(start_x, start_y, end_x, end_y,  width = 3, fill=unitColors[self.nation], arrow=tk.LAST, arrowshape=(20,30,8))
    def drawUnitSupport(self, target, target_start): #TODO NTH
        
        # Hold Support
        if target_start == None:
            target_x = terrs[target]["x_coord"]
            target_y = terrs[target]["y_coord"]

            offset_x, offset_y = self.calculateLineOffsets(25, target_x, target_y)
            
            # Draw Line
            start_x = self.x_pos + offset_x
            start_y = self.y_pos + offset_y
            end_x = target_x - offset_x
            end_y = target_y - offset_y
            graphicsCanvas.create_line(start_x, start_y, end_x, end_y,  width = 3, fill=unitColors[self.nation])
            graphicsCanvas.create_oval(target_x - 25, target_y - 25, target_x + 25, target_y + 25,  width = 4, outline=unitColors[self.nation])
        
        #Move Support #TODO add indication arrow for direction of move support?
        else:
            target_x = abs(int((terrs[target]["x_coord"] + terrs[target_start]["x_coord"]) / 2 ))
            target_y = abs(int((terrs[target]["y_coord"] + terrs[target_start]["y_coord"]) / 2 ))

            offset_x, offset_y = self.calculateLineOffsets(25, target_x, target_y)
            
            # Draw Line
            start_x = self.x_pos + offset_x
            start_y = self.y_pos + offset_y
            end_x = target_x - int(offset_x * (2/5))
            end_y = target_y - int(offset_y * (2/5))
            graphicsCanvas.create_line(start_x, start_y, end_x, end_y,  width = 3, fill=unitColors[self.nation])
            graphicsCanvas.create_oval(target_x - 10, target_y - 10, target_x + 10, target_y + 10,  width = 3, outline=unitColors[self.nation])          
    def drawMoveFails(self, target):
        target_x = terrs[target]["x_coord"]
        target_y = terrs[target]["y_coord"]

        icon_x = int((target_x + self.x_pos) / 2)
        icon_y = int((target_y + self.y_pos) / 2)

        graphicsCanvas.create_image(icon_x, icon_y, image= fail_icon, anchor="center")
    def drawSupportCut(self, target, target_start):
        # Hold Support cut
        if target_start == None:
            target_x = terrs[target]["x_coord"]
            target_y = terrs[target]["y_coord"]
        #Move Support cut
        else:
            target_x = abs(int((terrs[target]["x_coord"] + terrs[target_start]["x_coord"]) / 2 ))
            target_y = abs(int((terrs[target]["y_coord"] + terrs[target_start]["y_coord"]) / 2 ))
            
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

################################### GUI -- Drawing Functions ####################################################################### 
#create a list of Unit (Army/Fleet) objects
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

def drawUnits(Units): # 1 -> Draws Units
    for Unit in Units:
        Unit.drawUnit()
def drawMoves(Units, unitMoves): # 2 -> Draws Unit Moves and writes them to the text frame
    global text
    text.insert(tk.INSERT, 'Orders: \n')

    for Unit in Units:
        #unit variables
        unit_nation = nationality[Unit.nation][Unit.nation]
        unit_type = Unit.unitType
        unit_territory = terrs[Unit.territory]["name"]
        target_start = None
        try:
            target = unitMoves[Unit.territory]["target end"]
            target_end = terrs[target]["name"]
        except:
            target_end = None


        if Unit.order == "hold":
            Unit.drawUnitHold()
            text.insert(tk.INSERT, '-> {} {} in {} holds\n'.format(unit_nation, unit_type, unit_territory))
        elif Unit.order == "convoy":
            Unit.drawUnitConvoy()
            text.insert(tk.INSERT, '-> {} {} in {} convoys\n'.format(unit_nation, unit_type, unit_territory))
        elif Unit.order == "move":
            Unit.drawUnitMove(target)
            text.insert(tk.INSERT, '-> {} {} in {} -- moves to {}\n'.format(unit_nation, unit_type, unit_territory, target_end))
        elif Unit.order == "support":
            #adds additional info for support order target and move target start
            target_move_start = None
            if unitMoves[Unit.territory]["support type"] == "move support":
                target_move_start = unitMoves[Unit.territory]["target start"]
                target_start = terrs[target_move_start]["name"]
                text.insert(tk.INSERT, '-> {} {} in {} -- supports move: {} to {}\n'.format(unit_nation, unit_type, unit_territory, target_start, target_end))
            else:
                text.insert(tk.INSERT, '-> {} {} in {} -- supports {}\n'.format(unit_nation, unit_type, unit_territory, target_end))
            Unit.drawUnitSupport(target, target_move_start)       
def drawMoveOutcomes(Units, unitMoves): # 3 -> Draws Move Outcomes and writes them to the text frame
    global text
    text.insert(tk.INSERT, '\nOutcomes: \n')

    for Unit in Units:
        #unit variables
        unit_nation = nationality[Unit.nation][Unit.nation]
        unit_type = Unit.unitType
        unit_territory = terrs[Unit.territory]["name"]
        target_start = None
        try:
            target = unitMoves[Unit.territory]["target end"]
            target_end = terrs[target]["name"]
        except:
            target_end = None

        #indicate failed moves
        if Unit.order == "move" and unitMoves[Unit.territory]["outcome"] == "fails":
            Unit.drawMoveFails(target)
            text.insert(tk.INSERT, '-> {} {} in {} -- fails to move to {}\n'.format(unit_nation, unit_type, unit_territory, target_end), ("fail"))
        #indicate successful moves
        elif Unit.order == "move" and unitMoves[Unit.territory]["outcome"] == "moves":
            text.insert(tk.INSERT, '-> {} {} in {} -- successfully moves to {}\n'.format(unit_nation, unit_type, unit_territory, target_end), ("success"))
        #indicate cut support
        elif Unit.order == "support" and unitMoves[Unit.territory]["outcome"] == "cut":
            #adds additional info for support order target and move target start
            target_move_start = None
            if unitMoves[Unit.territory]["support type"] == "move support":
                target_move_start = unitMoves[Unit.territory]["target start"]
                target_start = terrs[target_move_start]["name"]
                text.insert(tk.INSERT, '-> {} {} in {} -- support for {} to {} is cut\n'.format(unit_nation, unit_type, unit_territory, target_start, target_end), ("fail"))
            else:
                text.insert(tk.INSERT, '-> {} {} in {} -- support for {} is cut\n'.format(unit_nation, unit_type, unit_territory, target_end), ("fail"))
            Unit.drawSupportCut(target, target_move_start)
        #indicate dislodged units
        if Unit.status == "dislodged":
            Unit.drawUnitDislodged()
            text.insert(tk.INSERT, '-> {} {} in {} is dislodged\n'.format(unit_nation, unit_type, unit_territory), ("fail"))        
def drawRetreats(Units, dislodgedList):    #TODO # 4 -> Draws Unit Retreat Moves -> TODO:Remove destroyed units?
    for Unit in Units:
        if Unit.status == "dislodged":
            Unit.drawUnitMove()
def drawBuildsAndDisbands(Units): #TODO # 5 -> (Winter Only) Draws Builds / Disbands
    for Unit in Units:
        if Unit.order == "build":
            Unit.drawUnitBuild()
        elif Unit.order == "disband":
            Unit.drawUnitDisband()

######################################## GUI -- Phase Functions ############################################

def phaseMoveDraw(turnMoves,buttonMaster):#TODO NTH
    global text
    global all_units
    
    drawBackground(graphicsCanvas) #Draw gameboard Background
    all_units = UnitList(turnMoves)
    
    drawUnits(all_units)    #Draw all units on gameboard
    buttonNext(buttonMaster) # "NEXT" button input ->
    
    drawMoves(all_units, turnMoves) #Draw all unit orders on gameboard; list text commands to text frame
    drawUnits(all_units)
    buttonNext(buttonMaster) # "NEXT" button input ->
    
    drawMoveOutcomes(all_units, turnMoves) #Draw all order outcomes on gameboard; list outcomes on text frame
    
    text.insert(tk.INSERT, "\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n") #Footer Bar

    #TODO -- save gamestate?
def phaseDislodgeDraw(turnMoves, dislodged_units, buttonMaster):#TODO
    global text
    global all_units
    #Draw gameboard Background
    drawBackground(graphicsCanvas)
    all_units = UnitList(turnMoves)
    #Draw all units on gameboard
    drawUnits(all_units)
    buttonNext(buttonMaster) # "NEXT" button input ->
    #Draw all retreat orders on gameboard; list text commands to text frame
    drawRetreats(all_units, dislodged_units)
def phaseBuildDraw(turnMoves):#TODO
    units = UnitList(turnMoves)
    drawUnits(units)
    # "NEXT" button input ->
    drawBuildsAndDisbands(units)



######################################### Main Game Loop ##############################################
# Initialize some Variables
turnNumber = 0
allUnits = boardSetup.setupUnits()
yearState = ['Spring ', 'Fall ']

#For disabling builds in custom games
gameType = "standard"
for m in allUnits.keys():
    if len(allUnits[m].keys()) < 3:
        gameType = "custom"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# MAIN GAME LOOP #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

while True:
    turnNumber += 1
    yearNumber = 1900 + (turnNumber + 1) // 2
    yearString = yearState[(turnNumber + 1) % 2] + str(yearNumber) #e.g. "Spring 1901"
    print()

    #Reset moves and dislodge lists
    turnMoves = {}
    dislodgedUnits = {}

############################### MOVE PHASE #######################################
    #get user input moves for all units
    print(yearString + " User Move Inputs: \n" )
    for nation in nationality.keys():
        print("\t" + nationality[nation][nation] + " Orders:")
        move.getUserMoves(terrs, allUnits[nation], turnMoves, nation)
        print()

    #Adjudicate user moves and return outcomes/dislodge status
    print("Adjudicating turn outcome..." )
    adjudedMoves = adjudicator.adjudicate(turnMoves)
    print()

            ################################## GUI ##########################################################
    root = rootWindow()
    graphicsCanvas, graphicsFrame = graphicsWindow(root)
    textFrame, text_title, textSubframe, scrollbar, text = textWindow(root, yearString)

    # TODO kloogy - load in icon images
    build_icon = ImageTk.PhotoImage(Image.open("GUI\\build_icon.png").resize((60,60), Image.ANTIALIAS))
    convoy_icon = ImageTk.PhotoImage(Image.open("GUI\\convoy_icon.png").resize((50,9), Image.ANTIALIAS))
    disband_icon = ImageTk.PhotoImage(Image.open("GUI\\disband_icon.png").resize((50,50), Image.ANTIALIAS))
    dislodged_icon = ImageTk.PhotoImage(Image.open("GUI\\dislodge_icon.png").resize((60,60), Image.ANTIALIAS))
    hold_icon = ImageTk.PhotoImage(Image.open("GUI\\hold_icon.png").resize((50,4), Image.ANTIALIAS))
    fail_icon = ImageTk.PhotoImage(Image.open("GUI\\disband_icon.png").resize((25,25), Image.ANTIALIAS))

    phaseMoveDraw(adjudedMoves, textFrame)

    #root.mainloop()????
            #################################################################################################

    #Write adjuded moves to dicts of new unit positions, and dislodged units
    print(yearString + " Move Outcomes: \n" )
    for nation in nationality.keys():
        outputLists = move.movePhaseOutput(adjudedMoves, nationality, nation)
        allUnits[nation] = outputLists[0]
        dislodgedUnits[nation] = outputLists[1]
        print()

############################### DISLODGE PHASE #######################################
    print(yearString + " Dislodge Phase: \n" )
    userDislodgeList = {}
    for nation in nationality.keys():    
        if dislodgedUnits[nation] != {}:            
            print("\t" + nationality[nation][nation] + " dislodged units -- please specify where to dislodge:")
            userDislodgeList[nation] = move.getUserDislodges(dislodgedUnits[nation], allUnits)

    #TODO:pass adjudedMoves and dislodgedUnits to gui dislodge function
    #gui.phaseDislodgeDraw(adjudedMoves, dislodgedUnits)

    #These should come after all-nations loop
    allUnits = adjudicator.adjudicateDislodge(userDislodgeList, allUnits)


############################### BUILD PHASE #######################################
    if turnNumber % 2 == 0 and gameType != "custom":
        yearString = "Winter " + str(yearNumber)
        print("\n"+ yearString + ": Build/Disband Phase")

        builds = {} #TODO
        disbands = {} #TODO

        #modify terrs to set supplycenter ownership
        for nation in nationality.keys():
            terrs = adjudicator.modifySupplyCenterOwners(terrs, allUnits[nation], nation)

        #Adjudicate current number of builds for each nation; run move.build or move.disband accordingly
        for nation in nationality.keys():
            buildCount = adjudicator.adjudicateBuilds(terrs, allUnits[nation], nation)
            if buildCount > 0:
                print("\n\t" + nationality[nation][nation] + " Builds:")
                allUnits = move.build(terrs, allUnits, nation, buildCount)
                print("\n\tAll " + nationality[nation][nation] + " unit build orders received.")
            elif buildCount < 0:
                print("\n\t" + nationality[nation][nation] + " Disbands:")
                allUnits = move.disband(allUnits, nation, buildCount)
                print("\n\tAll " + nationality[nation][nation] + " unit disband orders received.")
            elif buildCount == 0:
                print("\n\t" + nation.capitalize() + " has no builds or disbands to make.")


        #TODO: figure out how to implement gui build/disband draws


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# /end main loop #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##################################################### Testing Code ######################################################

#TODO -- fix print formatting
#TODO -- fully integrate GUI loop
#TODO -- get multiple coasts, convoys,.... to work

#GUI
#TODO: add a button to hide units, arrows so you can see labels?
#TODO: implement a time delay and/or animation to each move
