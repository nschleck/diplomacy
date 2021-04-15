### Main code body for running a Diplomacy game

############################### Initial Setup #######################################
import boardSetup, pprint, adjudicator
import moveFunctions as move

terrs = boardSetup.territories
allUnits = {
    'austria' : boardSetup.unitsAustria,
    "england" : boardSetup.unitsEngland,
    'france' :  boardSetup.unitsFrance,
    'germany' :  boardSetup.unitsGermany,
    'italy' : boardSetup.unitsItaly,
    'russia' :  boardSetup.unitsRussia,
    'turkey' : boardSetup.unitsTurkey,
}
nationality = {
    'austria' : {
        'austria' : 'Austrian',
    },
    "england" : {
        "england" : 'English',
    },
    'france' : {
        'france' : 'French',
    },
    'germany' : {
        'germany' : 'German',
    },
    'italy' : {
        'italy' : 'Italian',
    },
    'russia' : {
        'russia' : 'Russian',
    },
    'turkey' : {
        'turkey' : 'Turkish',
    },
}


############### Initialize some variables ###############
turnNumber = 0
yearState = ['Spring ', 'Fall ']

############################### Main Code Loop #######################################

while True:
    turnNumber += 1
    yearNumber = 1900 + (turnNumber + 1) // 2
    print()

    turnMoves = {}
    dislodgedUnits = {}

    ############################### MOVE PHASE #######################################
    #get user input moves for all units
    print(yearState[(turnNumber + 1) % 2] + str(yearNumber) + " User Move Inputs: \n" )
    for nation in nationality.keys():
        print("\t" + nationality[nation][nation] + " Orders:")
        move.getUserMoves(terrs, allUnits[nation], turnMoves, nation)
        print()

    #Adjudicate user moves and return outcomes/dislodge status
    print("Adjudicating turn outcome..." )
    adjudedMoves = adjudicator.adjudicate(turnMoves)
    print()

    #Write adjuded moves to dicts of new unit positions, and dislodged units
    print(yearState[(turnNumber + 1) % 2] + str(yearNumber) + " Move Outcomes: \n" )
    for nation in nationality.keys():
        outputLists = move.movePhaseOutput(adjudedMoves, nationality, nation)
        allUnits[nation] = outputLists[0]
        dislodgedUnits[nation] = outputLists[1]
        print()

    ############################### DISLODGE PHASE #######################################
    print(yearState[(turnNumber + 1) % 2] + str(yearNumber) + " Dislodge Phase: \n" )
    userDislodgeList = {}
    for nation in nationality.keys():    
        if dislodgedUnits[nation] != {}:            
            print("\t" + nationality[nation][nation] + " dislodged units -- please specify where to dislodge:")
            userDislodgeList[nation] = move.getUserDislodges(dislodgedUnits[nation], allUnits)


    #These should come after all-nations loop
    allUnits = adjudicator.adjudicateDislodge(userDislodgeList, allUnits)


    ############################### BUILD PHASE #######################################
    if turnNumber % 2 == 0:
        print("\nWinter of " + str(yearNumber) + ": Build/Disband Phase")

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


######################### Defunct Testing Code #########################

#temp testing
dislodgedUnits = {
    'austria' : {
        'alb' : {'type' : 'fleet'}
    },
}


#move.moveUnit(terrs, unitsTurk[1], "apu", "adr")
#move.support(terrs, unitsTurk[1], unitsTurk[2], 'adr')
#move.support(terrs, unitsTurk[1], unitsTurk[2], 'smy')
#move.support(terrs, unitsTurk[1], unitsTurk[2], 'ank')
#move.support(terrs, unitsTurk[1], unitsTurk[2], 'con')

#move.moveUnit(terrs, unitsTurk[1], "ank", "smy")
#print(str(move.validMove(terrs,"ank","arm","navy")))
#print(str(move.validMove(terrs,"rom","apu","navy")))