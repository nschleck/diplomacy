# contains functions for running move phases, retreat phases, and build phases
from boardSetup import territories as territories



########################### Move phase input functions ############################

def validMove(terrs, startPoint, endPoint, unitType): #returns whether the selected unit can move from start to end point

    #TODO - add double coast territories

    if startPoint not in terrs or endPoint not in terrs:    #checks to see that start and end points are real
        return False
    elif endPoint not in terrs[startPoint]["borders"]:    #checks to see if the given end point borders the start point
        return False                                    

    if unitType == "army":                          #checks to see if the unit type can move to the end point
        if terrs[endPoint]["type"] == "sea":
            return False
    elif unitType == "fleet":
        if terrs[endPoint]["type"] == "land":
            return False            
        if terrs[startPoint]["type"] == "coast" and terrs[endPoint]["type"] == "coast":           #checks edge case: can navy move along coast?
            for connectingSea in terrs:
                if terrs[connectingSea]["type"] == "sea" and startPoint in terrs[connectingSea]["borders"] and endPoint in terrs[connectingSea]["borders"]:
                    return True
            return False
    return True


def inputUserMove(inputOrder, terrs, nation, turnMoves, nationality): #Adds user input move to turnMoves dict/list
    #input order cleanup: - (a bit clunky at the moment but it kind of works)
    order = (inputOrder.lower()).split()
    try:
        if order[0] in ("a", "army", "n", "navy"):
            del order[0]
        order[1]    #fails if the list has less than 2 remaining items
        if len(order) > 2:
            if order[2] == "to":       
                del order[2]
    except IndexError:
        print("\t\tInvalid move detected.")
        return

    moveType = ''
    moveTargetStart = ''
    moveTargetEnd = ''
    unit = order[0]


    #checks for valid user unit location   
    if unit not in nation:
        print("\t\tNo user unit found in " + str(unit))
        return
    #else:
        #print("User unit found in " + str(terrs[unit]["name"]) + ". Type - " + str(nation[unit]["type"]))
    if unit in turnMoves:
        print("\t\tOrder already exists for " + unit + "; previous order has been overwritten")

    unitType = nation[unit]["type"]


    #sorts input into move types
    orderType = order[1]
    if orderType in ("move", "moves", "attack", "attacks", "to", "m", ">"):
        moveType = 'move'
        #print("Move type = " + moveType)

        try:
            moveTargetEnd = order[2]
        except IndexError:
            print ("\t\tMove format not recognized. Try again.\n")
            return
    elif orderType in ("support", "supports", "s"):
        moveType = 'support'
        #print("Move type = " + moveType)

        if len(order) > 4:
            if order[4] not in terrs or order[2] not in terrs:
                print("\t\tSupport target start/end not recognized. Try again.\n")
                return
            moveTargetStart = order[2]
            moveTargetEnd = order[4]
        else:
            if order[2] not in terrs:
                print("\t\tSupport target not recognized. Try again.\n")
                return
            moveTargetEnd = order[2]
    elif orderType in ("convoy", "convoys", "c"):
        moveType = 'convoy'
        #print("Move type = " + moveType)

        if len(order) > 4:
            if order[4] not in terrs or order[2] not in terrs:
                print("\t\tConvoy target start/end not recognized. Try again.")
                return
            moveTargetEnd = order[4]
            moveTargetStart = order[2]
        else:
            print("\t\tConvoy order format not recognized. Try again with the format: unit convoys unit to territory")
            return
    elif orderType in ("hold", "holds", "h"):
        moveType = 'hold'
        #print("Move type = " + moveType)

        moveTargetEnd = order[0]
    else:
        print("\t\tNo move type recognized")
        return

    try:
        moveTargetName = terrs[moveTargetEnd]["name"]
    except KeyError:
        print ("\t\tMove target location not recognized. Try again.\n")
        return    

    #checks for a valid move
    if not validMove(terrs, unit, moveTargetEnd, unitType) and moveType not in ("convoy", "hold"):
        print("\t\tInvalid move - %s in %s cannot %s %s\n" % (unitType,terrs[order[0]]["name"],moveType,moveTargetName))
        return
    elif len(order) > 4:
        if moveType == "convoy" and unitType == "army":
            print("\t\tArmies can't convoy units. Try again.\n")
            return
        print("\t\tValid move - %s in %s %s %s to %s\n" % (unitType,terrs[order[0]]["name"],moveType,terrs[moveTargetStart]["name"],moveTargetName))
    else:
        print("\t\tValid move - %s in %s %s %s\n" % (unitType,terrs[order[0]]["name"],moveType,moveTargetName))
    
    #adds move dictionary of unit to turnMoves list
    turnMoves[unit] = {
        'nation' : nationality,
        "unit type" : unitType,
        "order" : moveType,
        #"target start" : moveTargetStart, 
        #'target end' : moveTargetEnd,
        'outcome' : "undecided",
        "dislodge status" : "undecided"
    }
    #movetype-dependent optional keys
    if moveType == "support":
        if moveTargetStart !='':
            turnMoves[unit]["support type"] = 'move support'
        else:
            turnMoves[unit]["support type"] = 'hold support'
    if moveType in ["move", "support","convoy"]:
        turnMoves[unit]['target end'] = moveTargetEnd
    if moveType == "convoy" or (moveType == "support" and turnMoves[unit]["support type"] == "move support"):
        turnMoves[unit]['target start'] = moveTargetStart
    #TODO -- add in "via convoy" move type for move orders

    return unit

def getUserMoves(terrs, nation, turnMoves, nationality): #Prompts user for all their move inputs and adds them to turnMoves list
    unassignedUnits = set()
    for unit in nation:
        unassignedUnits.add(unit)
    while len(unassignedUnits) > 0:
        unAssUnitsStr = ''
        for unit in unassignedUnits:
            unAssUnitsStr += (str(nation[unit]["type"]) + ' in ' + str(terrs[unit]["name"]) + " (" + unit + "), ")
        unAssUnitsStr = unAssUnitsStr[:-2]
        print("\tUnassigned user units: " + unAssUnitsStr + ". Enter the order \"hold all\" to hold all remaining units")
        userMove = input("\tEnter order:")
        if userMove == "hold all":
            for unit in unassignedUnits:
                inputUserMove(unit + " h", terrs, nation, turnMoves, nationality)
            break
        move = inputUserMove(userMove, terrs, nation, turnMoves, nationality)
        if move in unassignedUnits:
            unassignedUnits.remove(move)
    print("\t\tAll unit moves submitted")



########################### Move phase output functions ############################

def movePhaseOutput(movelistAdj, nationalityList, inputNation): #write movelist output to new gamestate after adjudicator runs; write to terminal
    outputList = {}
    dislodgedList = {}
    for unit in movelistAdj:

        fullName = territories[unit]["name"]
        nation = movelistAdj[unit]["nation"]
        if nation != inputNation:   #this should only sort moves from the inputNation into the output move lists
            continue

        nationality = nationalityList[nation][nation]
        unitType = movelistAdj[unit]["unit type"]
        order = movelistAdj[unit]["order"]
        outcome = movelistAdj[unit]["outcome"]
        dislodged = movelistAdj[unit]["dislodge status"]

        #not necessary: #TODO remove
        #del movelistAdj[unit]["order"]
        #del movelistAdj[unit]["outcome"]
        #del movelistAdj[unit]["dislodge status"]

        #Breaks loop if movelistAdj has not been fully adjudicated
        if outcome == "undecided":
            print("ERROR -- " + fullName + "outcome still undecided")
            return {},{}
        elif dislodged == "undecided":
            print("ERROR -- " + fullName + "dislodge status still undecided")
            return {},{}

        #removes dislodged units to separate list
        if dislodged == "dislodged":
            print('\t' + nationality + ' ' + unitType + ' in ' + fullName + ' has been dislodged')
            dislodgedList[unit] = {'type' : unitType, "dislodging attacker" : movelistAdj[unit]["dislodging attacker"]}
            continue

        if order == "move":
            if outcome == "moves":
                print('\t' + nationality + ' ' + unitType + ' in ' + fullName + ' successfully moves to ' + territories[movelistAdj[unit]["target end"]]["name"])
                outputList[movelistAdj[unit]["target end"]] = {'type' : unitType}
            else:
                print('\t' + nationality + ' ' + unitType + ' in ' + fullName + ' fails move to ' + territories[movelistAdj[unit]["target end"]]["name"])
                outputList[unit] = {'type' : unitType}
        elif order == "hold":
            print('\t' + nationality + ' ' + unitType + ' in ' + fullName + ' holds')
            outputList[unit] = {'type' : unitType}
        elif order == "convoy": #TODO -- fill out convoy information given to terminal
            print('\t' + nationality + ' ' + unitType + ' in ' + fullName + ' convoys')
            outputList[unit] = {'type' : unitType}
        elif order == "support":
            sType = movelistAdj[unit]["support type"]
            moveEnd = movelistAdj[unit]["target end"]
            if sType == "move support":
                moveStart = movelistAdj[unit]["target start"]
                if outcome == "given":
                    print('\t' + nationality + ' ' + unitType + ' in ' + fullName + ' supports ' + territories[moveStart]["name"] + " move into " + territories[moveEnd]["name"])
                else:
                    print('\t' + nationality + ' ' + unitType + ' in ' + fullName + ' support is cut for '+ territories[moveStart]["name"] + " move into " + territories[moveEnd]["name"])
            elif sType == "hold support":
                if outcome == "given":
                    print('\t' + nationality + ' ' + unitType + ' in ' + fullName + ' supports ' + territories[moveEnd]["name"])
                else:
                    print('\t' + nationality + ' ' + unitType + ' in ' + fullName + ' support is cut for ' + territories[moveEnd]["name"])
            outputList[unit] = {'type' : unitType}

    return outputList, dislodgedList
        
########################### Dislodge phase functions ############################

def inputUserDislodge(unit, unitDict, allExistingUnits):
    print('\t\t' + unitDict["type"] + " in " + territories[unit]["name"] + " -- retreat to where? If unit cannot retreat anywhere, enter \'disband\'")

    def targetInExistingUnits(target):
        for country in allExistingUnits:
            if target in allExistingUnits[country].keys():
                return True
        return False

    while True: #keep asking for user input until a valid retreat target is provided
        dislodgeTarget = input('\t\t')
        if dislodgeTarget in territories.keys():
            if not validMove(territories, unit, dislodgeTarget, unitDict["type"]):
                print("\t\tInvalid; " + unitDict["type"] + " in " + territories[unit]["name"] +  " cannot retreat to " + territories[dislodgeTarget]["name"] + ". Try again")
            elif targetInExistingUnits(dislodgeTarget):
                print("\t\tInvalid; a unit already exists in " + territories[dislodgeTarget]["name"] + ". Try again")
            elif dislodgeTarget == unitDict["dislodging attacker"]:
                print("\t\tInvalid; a dislodged unit cannot swap places with the dislodging attacker. Try again")
            else:
                print('\t\t' + unitDict["type"] + " in " + territories[unit]["name"] +  " retreats to " + territories[dislodgeTarget]["name"])
                #TODO:pop out unitDict["dislodging attacker"]?
                return dislodgeTarget
        elif dislodgeTarget == "disband":
            print('\t\t' + unitDict["type"] + " in " + territories[unit]["name"] +  " disbands.")
            return ''
        else:
            print("\t\tTarget territory not recognized; try again")

def getUserDislodges(dislodgeList, allExistingUnits): #gets user input for a single nation's dislodgeList dislodge targets
    for unit in dislodgeList.keys():
        dislodgeList[unit]["dislodge target"] = inputUserDislodge(unit, dislodgeList[unit], allExistingUnits)
    return dislodgeList


########################### Build/Disband phase functions ############################

def build(terrs, allUnits, nation, buildCount):
    while buildCount > 0:
        buildOrder = input("\t" + str(buildCount) + " build(s) remaining. Please specify a build order (enter \"end builds\" if you have no more valid builds to make):\n\t\t")
        print()
        #sanitize buildOrder input
        if buildOrder == 'end builds':
            break
        try:
            buildOrder = (buildOrder.lower()).split()
            unitType = buildOrder[0]
            unitArea = buildOrder[1]
        except:
            print("\tOrder not recognized. Please format build order as: unittype area, e.g fleet mar")
            continue

        if unitType == "a":
            unitType = 'army'
        elif unitType == "f":
            unitType = 'fleet'
        if unitType not in ["army", "fleet"] or unitArea not in terrs.keys():
            print("\tOrder not recognized. Please format build order as: unittype area, e.g fleet mar")
            continue

        #check for occupied build territory
        alreadyOccupied = False
        for anyNation in allUnits.keys():
            if unitArea in allUnits[anyNation].keys():
                alreadyOccupied = True
        if alreadyOccupied:
            print("\tYou cannot build on an occupied territory.")
            continue            

        #check for valid fleet build
        if unitType == "fleet" and terrs[unitArea]["type"] == "land":
            print("\tYou cannot build a fleet on land, dumb dumb.")
            continue

        if terrs[unitArea]["supplyCenter"] and terrs[unitArea].get("homeCenter", '') == nation and terrs[unitArea]["country"] == nation:
            print("\t\t" + (str(unitType)).capitalize() + " built in " + str(terrs[unitArea]["name"]))
            allUnits[nation][unitArea] = {"type" : unitType}
        else:
            #invalid build
            print("\tYou cannot build a(n) " + str(unitType) + " in " + str(terrs[unitArea]["name"]))
            continue
    
        buildCount -= 1
    return allUnits

def disband(allUnits, nation, buildCount):
    while buildCount < 0:
        disbandOrder = (input("\t" + str(abs(buildCount)) + " disband(s) remaining. Please specify a unit to disband:\n\t\t")).lower()
        print()
        if disbandOrder in allUnits[nation].keys():
            print("\t\t" + (str(allUnits[nation][disbandOrder]["type"])).capitalize() + " disbanded in " + str(territories[disbandOrder]["name"]))
            allUnits[nation].pop(disbandOrder)
        else:
            print("\tDisband order not recognized. Please specify a unit to disband (don't include unit type e.g. army/fleet)")
            continue

        buildCount += 1
    return allUnits