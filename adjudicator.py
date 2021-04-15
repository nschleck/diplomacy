### This Code body contains functions to adjudicate a single turn of diplomacy ###
import pprint
from boardSetup import territories as boardTerritories

##################################################################### Outcome Functions #########################################################
def move(unit, targetArea, movelist): #return "moves", 'fails' or 'undecided'
    ###Preventing power directed at the attacked region:
    largestPreventMin = 0
    largestPreventMax = 0
    for m in movelist:
        if movelist[m]["order"] == "move" and movelist[m]["target end"] == targetArea and m != unit:
            largestPreventMin = max(largestPreventMin, preventStrengthMin(m, targetArea, movelist))
            largestPreventMax = max(largestPreventMax, preventStrengthMax(m, targetArea, movelist))

    attackMin = attackStrengthMin(unit, targetArea, movelist)
    attackMax = attackStrengthMax(unit, targetArea, movelist)
    defendMin = defendStrengthMin(targetArea, unit, movelist)
    defendMax = defendStrengthMax(targetArea, unit, movelist)
    holdMin = holdStrengthMin(targetArea, movelist)
    holdMax = holdStrengthMax(targetArea, movelist)

    if movelist.get(targetArea) != None and (movelist.get(targetArea,{}).get("order") == "move" and movelist.get(targetArea,{}).get("target end") == unit): #head to head
        if attackMin > defendMax and attackMin > largestPreventMax:
            return "moves"
        elif attackMax <= defendMin or attackMax <= largestPreventMin:
            return "fails"
        else:
            return "undecided"
    elif attackMin > holdMax and attackMin > largestPreventMax:
        return "moves"
    elif attackMax <= holdMin or attackMax <= largestPreventMin:
        return "fails"
    else:
        return "undecided"

def support(unit, supportType, movelist, moveSupportTarget): #return "given" or "cut" or 'undecided'
    ###Attacking power directed at the supporting unit:
    largestAttackMin = 0
    largestAttackMax = 0
    for m in movelist: 
        if movelist[m]["order"] == "move" and movelist[m]["target end"] == unit:
            if supportType == "move support" and m == moveSupportTarget:
                continue
            largestAttackMin = max(largestAttackMin, attackStrengthMin(m, unit, movelist))
            largestAttackMax = max(largestAttackMax, attackStrengthMax(m, unit, movelist))
    
    if largestAttackMin == 0 and dislodge(unit, movelist) == 'sustains':
        return "given"
    elif largestAttackMax > 0 or dislodge(unit, movelist) == 'dislodged':
        return "cut"
    else:
        return "undecided"

def dislodge(unit, movelist): #return "sustains" or "dislodged" or "undecided"
    #determine of there is an existing move that successfully attacks this unit's area
    attackSuccess = False
    possibleAttackSuccess = False
    for m in movelist:
        if movelist[m]["order"] == "move" and movelist[m]["target end"] == unit and movelist[m]["outcome"] == "moves":
            attackSuccess = True
            possibleAttackSuccess = True
        elif movelist[m]["order"] == "move" and movelist[m]["target end"] == unit and movelist[m]["outcome"] == "undecided":
            possibleAttackSuccess = True
    
    #determine if the unit succeeded a move to a new area
    successfulMove = False
    if movelist[unit]["order"] == "move" and move(unit, movelist[unit]["target end"], movelist) == "moves":
        successfulMove = True

    failedMove = True
    if movelist[unit]["order"] == "move" and move(unit, movelist[unit]["target end"], movelist) != "fails":
        failedMove = False

    if successfulMove or not possibleAttackSuccess:
        return 'sustains'
    elif attackSuccess and failedMove:
        return "dislodged"
    else:
        return "undecided"

############################################### Strength Functions ##################################################
def attackStrengthMin(unit, targetArea, movelist): #return int >= 0 for unit ordered to move to targetArea
    if path(unit, targetArea, movelist) == "no path" or path(unit, targetArea, movelist) == "undecided":
        return 0
    elif movelist.get(targetArea) != None and (movelist.get(targetArea,{}).get("order") == "move" and movelist.get(targetArea,{}).get("target end") == unit or movelist.get(targetArea,{}).get("order") != "move" or movelist.get(targetArea,{}).get("outcome") in ["fails", "undecided"]): ###head to head move or no move order target or ...
        if movelist[targetArea]["nation"] == movelist[unit]["nation"]:
            return 0
        else:
            aStrength = 1
            for m in movelist:
                if movelist[m]["order"] == "support" and movelist[m]['support type'] == "move support" and movelist[m]["target start"] == unit and movelist[m]["target end"] == targetArea and movelist[m]["outcome"] == "given" and movelist[m]["nation"] != movelist[targetArea]["nation"]:
                    aStrength += 1       
            return aStrength # returns 1 + # of support orders w/ given support, of different nationality only
    else:
        aStrength = 1
        for m in movelist:
            if movelist[m]["order"] == "support" and movelist[m]['support type'] == "move support" and movelist[m]["target start"] == unit and movelist[m]["target end"] == targetArea and movelist[m]["outcome"] == "given":
                aStrength += 1       
        return aStrength # returns 1 + # of support orders w/ given support

def attackStrengthMax(unit, targetArea, movelist): #return int > 0 for unit ordered to move to targetArea
    if path(unit, targetArea, movelist) == "no path":
        return 0
    elif movelist.get(targetArea) != None and (movelist.get(targetArea,{}).get("order") == "move" and movelist.get(targetArea,{}).get("target end") == unit or movelist.get(targetArea,{}).get("order") != "move" or movelist.get(targetArea,{}).get("outcome") == "fails"): ###head to head move or no move order target or ...:
        if movelist[targetArea]["nation"] == movelist[unit]["nation"]:
            return 0        
        else:
            aStrength = 1
            for m in movelist:
                if movelist[m]["order"] == "support" and movelist[m]['support type'] == "move support" and movelist[m]["target start"] == unit and movelist[m]["target end"] == targetArea and movelist[m]["outcome"] in ["given", "undecided"] and movelist[m]["nation"] != movelist[targetArea]["nation"]:
                    aStrength += 1       
            return aStrength # returns 1 + # of support orders w/ given support, of different nationality only
    else:
        aStrength = 1
        for m in movelist:
            if movelist[m]["order"] == "support" and movelist[m]['support type'] == "move support" and movelist[m]["target start"] == unit and movelist[m]["target end"] == targetArea and movelist[m]["outcome"] in ["given", "undecided"]:
                aStrength += 1       
        return aStrength # returns 1 + # of support orders w/ given or undecided support

def holdStrengthMin(area, movelist): #return int >= 0 for area
    if area not in movelist.keys(): #area is empty / has no unit
        return 0
    elif movelist[area]["order"] != "move": #area has unit w/o move order
        hStrength = 1
        for m in movelist:
            if movelist[m]["order"] == "support" and movelist[m]['support type'] == "hold support" and movelist[m]["target end"] == area and movelist[m]["outcome"] == "given":
                hStrength += 1               
        return hStrength # 1 + support orders w/ given support
    elif movelist[area]["order"] == "move": #area has unit w/ move order
        if movelist[area]["outcome"] == "fails":
            return 1
        elif movelist[area]["outcome"] in ["moves","undecided"]:
            return 0

def holdStrengthMax(area, movelist): #return int >= 0 for area
    if area not in movelist.keys(): #area is empty / has no unit
        return 0
    elif movelist[area]["order"] != "move": #area has unit w/o move order 
        hStrength = 1
        for m in movelist:
            if movelist[m]["order"] == "support" and movelist[m]['support type'] == "hold support" and movelist[m]["target end"] == area and movelist[m]["outcome"] in ["given","undecided"]:
                hStrength += 1               
        return hStrength # 1 + support orders w/ given or undecided support
    elif movelist[area]["order"] == "move": #area has unit w/ move order
        if movelist[area]["outcome"] in ["fails","undecided"]:
            return 1
        elif movelist[area]["outcome"] == "moves":
            return 0

def preventStrengthMin(unit, targetArea, movelist): #return int >= 0 for unit ordered to move to targetArea
    if path(unit, targetArea, movelist) == 'no path' or path(unit, targetArea, movelist) == 'undecided':
        return 0
    elif movelist.get(targetArea) != None and (movelist.get(targetArea,{}).get("order") == "move" and movelist.get(targetArea,{}).get("target end") == unit and movelist.get(targetArea,{}).get("outcome") in ["undecided", "moves"]): ###head to head
            return 0
    else:
        pStrength = 1
        for m in movelist:
            if movelist[m]["order"] == "support" and movelist[m]['support type'] == "move support" and movelist[m]["target start"] == unit and movelist[m]["target end"] == targetArea and movelist[m]["outcome"] == "given":
                pStrength += 1       
        return pStrength # returns 1 + # of support orders w/ given support

def preventStrengthMax(unit, targetArea, movelist): #return int >= 0 for unit ordered to move to targetArea
    if path(unit, targetArea, movelist) == 'no path':
        return 0
    elif movelist.get(targetArea) != None and (movelist.get(targetArea,{}).get("order") == "move" and movelist.get(targetArea,{}).get("target end") == unit and movelist.get(targetArea,{}).get("outcome") == "moves"): ###head to head
        return 0
    else:
        pStrength = 1
        for m in movelist:
            if movelist[m]["order"] == "support" and movelist[m]['support type'] == "move support" and movelist[m]["target start"] == unit and movelist[m]["target end"] == targetArea and movelist[m]["outcome"] in ["given", "undecided"]:
                pStrength += 1       
        return pStrength # returns 1 + # of support orders w/ given or undecided support

def defendStrengthMin(unit, targetArea, movelist): #return int >= 0  for unit ordered to move to targetArea
    dStrength = 1
    for m in movelist:
        if movelist[m]["order"] == "support" and movelist[m]['support type'] == "move support" and movelist[m]["target start"] == unit and movelist[m]["target end"] == targetArea and movelist[m]["outcome"] == "given":
            dStrength += 1       
    return dStrength # returns 1 + # of support orders w/ given support

def defendStrengthMax(unit, targetArea, movelist): #return int >= 0  for unit ordered to move to targetArea
    dStrength = 1
    for m in movelist:
        if movelist[m]["order"] == "support" and movelist[m]['support type'] == "move support" and movelist[m]["target start"] == unit and movelist[m]["target end"] == targetArea and movelist[m]["outcome"] in ["given", "undecided"]:
            dStrength += 1       
    return dStrength # returns 1 + # of support orders w/ given or undecided support

#################################################### Misc Functions #######################################################
def path(unit, targetArea, movelist): #return "path" or "no path" or "undecided" #TODO hacky one-path solution
    if movelist.get(unit,{}).get("move type") != "via convoy":
        return "path"
    elif movelist.get(unit,{}).get("move type") == "via convoy":

        #Generate a dict of units with convoy orders for this move, and their outcomes as values
        convoyDict = {}
        for c in movelist:
            if movelist[c]["order"] == "convoy" and movelist[c]["target start"] == unit and movelist[c]["target end"] == targetArea:
                convoyDict[c] = movelist[c]["dislodge status"]
    
        #loop through and determine if there is a sustain/undecided path within convoylist
        initialconvoylist = list(convoyDict.keys())  #TODO unneccesary to make a dict and then a list
        def pathLinks(start, convoylist):
            validPath = []
            pathArea = start
            while True:            
                for p in boardTerritories[pathArea]["borders"]:
                    if p in convoylist:
                        convoylist.remove(p)
                        validPath.append(p)
                        pathArea = p
                    elif p == targetArea:
                        return validPath
                if pathArea in validPath:
                    continue
                else:
                    return None
        
        finalPath = pathLinks(unit, initialconvoylist)
        if finalPath != None:
            undecidedPath = False
            for m in finalPath:
                if movelist[m]["dislodge status"] == "dislodged":
                    return "no path"
                elif movelist[m]["dislodge status"] == "undecided":
                    undecidedPath = True
            if undecidedPath:
                return "undecided"
            else:
                return "path"
        else:
            return "no path"

def modifySupplyCenterOwners(terrs, unitList, nation):
    for unit in unitList.keys():
        if terrs[unit]["supplyCenter"]:
            terrs[unit]["country"] = nation
    return terrs




#################################################### testing notes ######################################################

#TODO C4-C7, 6D6, 6D8, 6D16, 6F and 6G all ----> convoys
#TODO 6D25, 26, 27 failed support moves
#TODO E11 --- multiple coasts


testList1 = {
    "smy" : {
        "nation": "turkey",
        "order": "support",
        'support type': "move support",
        "target start": "ank",
        "target end": "arm",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ank" : {
        "nation": "turkey",
        "order": "move",
        "target end": "arm",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "con" : {
        "nation": "turkey",
        "order": "hold",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #Pass
testList2 = {
    "aeg" : {
        "nation": "turkey",
        "order": "convoy",
        "target start": "smy",
        "target end": "tun",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ion" : {
        "nation": "turkey",
        "order": "convoy",
        "target start": "smy",
        "target end": "tun",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "tyn" : {
        "nation": "turkey",
        "order": "convoy",
        "target start": "smy",
        "target end": "tun",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "smy" : {
        "nation": "turkey",
        "order": "move",
        "move type": "via convoy",        
        "target end": "tun",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nap" : {
        "nation": "italy",
        "order": "move",     
        "target end": "ion",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "apu" : {
        "nation": "italy",
        "order": "support",     
        "support type": "move support",        
        "target start": "nap",
        "target end": "ion",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
} #convoy first test pass!


############################################  Main adjudication functions ####################################################

def adjudicate(tList):
    
    loopLimit = 0
    outputTextList = []

    while True:  
        loopLimit += 1
        print ("\n\tAdjudicating Loop " + str(loopLimit) + "....")

        for m in tList:
            if tList[m]['order'] == "move" and tList[m]['outcome'] == "undecided":
                tList[m]['outcome'] = move(m, tList[m]['target end'], tList)
            elif tList[m]['order'] == "support" and tList[m]['outcome'] == "undecided":
                tList[m]['outcome'] = support(m, tList[m]['support type'], tList, tList[m]['target end'])
            elif tList[m]['order'] == "hold" and tList[m]['outcome'] == "undecided":
                tList[m]['outcome'] = "holds"
            elif tList[m]['order'] == "convoy" and tList[m]['outcome'] == "undecided":
                tList[m]['outcome'] = "convoys"
            
            if tList[m]['dislodge status'] == "undecided":
                tList[m]['dislodge status'] = dislodge(m, tList)
                if tList[m]['dislodge status'] == "dislodged":
                    for attacker in tList:
                        if tList[attacker].get('target end','') == m and tList[attacker]['order'] == "move" and tList[attacker]['outcome'] == "moves":
                            tList[m]['dislodging attacker'] = attacker
                

            mText = str(m) + " " + str(tList[m]['order']) + " order result: " + str(tList[m]['outcome'])
            if mText not in outputTextList:
                print('\t' + mText)
                outputTextList.append(mText)
                
        #Loop through movelist again to check for any undecided statuses; if found, resets While loop
        def findUndecided(movelist):
            for r in movelist:        
                if movelist[r]['outcome'] == "undecided" or movelist[r]['dislodge status'] == "undecided":
                    print("\t" + r + " outcome/dislodge still undecided")
                    return True
            return False
        if findUndecided(tList) and loopLimit < 10:  #resets while loop to beginning
            continue
        elif findUndecided(tList) and loopLimit == 10:                                       #hacky solution to circular movement paradox
            for u in tList:
                if tList[u]['outcome'] == "undecided" and tList[u]['order'] == "move": 
                    tList[u]['outcome'] = "moves"
                if tList[u]['dislodge status'] == "undecided" and tList[u]['order'] == "move": 
                    tList[u]['dislodge status'] = "sustains"


        #pprint.pprint(tList) -- testing output move list
        break

    return tList

def adjudicateDislodge(dislodgeDict, allUnitsDict): #TODO make this actually adjudicate
    for nation in dislodgeDict.keys():
        for unit in dislodgeDict[nation].keys():
            dislodgeTarget = dislodgeDict[nation][unit]['dislodge target']
            if dislodgeTarget != '': #disband order for unit
                allUnitsDict[nation][dislodgeTarget] = dislodgeDict[nation][unit]
                allUnitsDict[nation][dislodgeTarget].pop("dislodge target")
                allUnitsDict[nation][dislodgeTarget].pop("dislodging attacker")

    return allUnitsDict

def adjudicateBuilds(terrs, unitList, nation):
    currentUnitCount = len(unitList.keys())
    ownedCenters = 0
    for area in terrs.keys():
        if terrs[area]["supplyCenter"] and terrs[area]["country"] == nation:
            ownedCenters += 1
    return ownedCenters - currentUnitCount



#################################################### testing cases ######################################################

tList6A11 = {
    "vie" : {
        "nation": "austria",
        "order": "move",
        "target end": "tyr",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ven" : {
        "nation": "italy",
        "order": "move",
        "target end": "tyr",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #Pass
tList6A12 = {
    "vie" : {
        "nation": "austria",
        "order": "move",
        "target end": "tyr",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ven" : {
        "nation": "italy",
        "order": "move",
        "target end": "tyr",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "mun" : {
        "nation": "germany",
        "order": "move",
        "target end": "tyr",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }    
} #Pass
tList6C1 = {
    "ank" : {
        "nation": "turkey",
        "order": "move",
        "target end": "con",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "con" : {
        "nation": "turkey",
        "order": "move",
        "target end": "smy",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "smy" : {
        "nation": "turkey",
        "order": "move",
        "target end": "ank",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }    
} ###Works, Hacky solution to circular movement paradox
tList6C2 = {
    "ank" : {
        "nation": "turkey",
        "order": "move",
        "target end": "con",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "con" : {
        "nation": "turkey",
        "order": "move",
        "target end": "smy",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "smy" : {
        "nation": "turkey",
        "order": "move",
        "target end": "ank",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bul" : {
        "nation": "turkey",
        "order": "support",
        'support type': "move support",
        "target start": "ank",
        "target end": "con",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }        
} #pass
tList6C3 = {
    "ank" : {
        "nation": "turkey",
        "order": "move",
        "target end": "con",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "con" : {
        "nation": "turkey",
        "order": "move",
        "target end": "smy",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "smy" : {
        "nation": "turkey",
        "order": "move",
        "target end": "ank",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bul" : {
        "nation": "turkey",
        "order": "move",
        "target end": "con",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }        
} #pass
tList6D1 = {
    "adr" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "tri",
        "target end": "ven",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "tri" : {
        "nation": "austria",
        "order": "move",
        "target end": "ven",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ven" : {
        "nation": "italy",
        "order": "hold",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "tyr" : {
        "nation": "italy",
        "order": "support",
        'support type': "hold support",
        "target end": "ven",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }    
} #Pass
tList6D2 = {
    "adr" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "tri",
        "target end": "ven",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "tri" : {
        "nation": "austria",
        "order": "move",
        "target end": "ven",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "vie" : {
        "nation": "austria",
        "order": "move",
        "target end": "tyr",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ven" : {
        "nation": "italy",
        "order": "hold",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "tyr" : {
        "nation": "italy",
        "order": "support",
        'support type': "hold support",
        "target end": "ven",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }    
} #Pass!
tList6D3 = {
    "adr" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "tri",
        "target end": "ven",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "tri" : {
        "nation": "austria",
        "order": "move",
        "target end": "ven",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ven" : {
        "nation": "italy",
        "order": "hold",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ion" : {
        "nation": "italy",
        "order": "move",
        "target end": "adr",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }    
} #Pass!
tList6D4 = {
    "ber" : {
        "nation": "germany",
        "order": "support",
        'support type': "hold support",
        "target end": "kie",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "germany",
        "order": "support",
        'support type': "hold support",
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bal" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "pru",        
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "pru" : {
        "nation": "russia",
        "order": "move",
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }    
} #Pass!
tList6D5 = {
    "ber" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "mun",
        "target end": "sil",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "germany",
        "order": "support",
        'support type': "hold support",
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "mun" : {
        "nation": "germany",
        "order": "move",
        "target end": "sil",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "bal" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "pru",        
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "pru" : {
        "nation": "russia",
        "order": "move",
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }    
} #Pass!
tList6D7 = {
    "bal" : {
        "nation": "germany",
        "order": "move",
        "target end": "swe",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "pru" : {
        "nation": "germany",
        "order": "support",
        'support type': "hold support",
        "target end": "bal",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "liv" : {
        "nation": "russia",
        "order": "move",
        "target end": "bal",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "bot" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "liv",        
        "target end": "bal",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "fin" : {
        "nation": "russia",
        "order": "move",
        "target end": "swe",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }    
} #pass --  Rules update: "A unit that is moving, can not receive a hold support for the situation that the move fails."
tList6D9 = {
    "ven" : {
        "nation": "italy",
        "order": "move",
        "target end": "tri",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "tyr" : {
        "nation": "italy",
        "order": "support",
        'support type': "move support",
        "target start": "ven",        
        "target end": "tri",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "alb" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "tri",        
        "target end": "ser",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "tri" : {
        "nation": "austria",
        "order": "hold",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }    
} #pass
tList6D10 = {
    "ber" : {
        "nation": "germany",
        "order": "hold",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "germany",
        "order": "move",
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "mun" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "kie",        
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }    
} #Pass!
tList6D11 = {
    "ber" : {
        "nation": "germany",
        "order": "move",
        "target end": "pru",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "germany",
        "order": "move",
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "mun" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "kie",        
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "war" : {
        "nation": "germany",
        "order": "move",
        "target end": "pru",
        "outcome": 'undecided',
        'dislodge status': 'undecided' 
    }   
} #Pass!
tList6D12 = {
    "tri" : {
        "nation": "austria",
        "order": "hold",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "vie" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "ven",        
        "target end": "tri",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ven" : {
        "nation": "italy",
        "order": "move",
        "target end": "tri",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #Pass!
tList6D13 = {
    "tri" : {
        "nation": "austria",
        "order": "move",
        "target end": "adr",             
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "vie" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "ven",        
        "target end": "tri",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ven" : {
        "nation": "italy",
        "order": "move",
        "target end": "tri",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "apu" : {
        "nation": "italy",
        "order": "move",
        "target end": "adr",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #Pass!
tList6D14 = {
    "tri" : {
        "nation": "austria",
        "order": "move",
        "target end": "adr",             
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "vie" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "ven",        
        "target end": "tri",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ven" : {
        "nation": "italy",
        "order": "move",
        "target end": "tri",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "tyr" : {
        "nation": "italy",
        "order": "support",        
        'support type': "move support",
        "target start": "ven",        
        "target end": "tri",      
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "adr" : {
        "nation": "italy",
        "order": "support",        
        'support type': "move support",
        "target start": "ven",        
        "target end": "tri",      
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #PASS! aStrengthMax fix.  tricky support edge case, supporting foreign attacks
tList6D15 = {
    "con" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "bla",        
        "target end": "ank",             
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bla" : {
        "nation": "russia",
        "order": "move",
        "target end": "ank",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ank" : {
        "nation": "turkey",
        "order": "move",
        "target end": "con",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
} #Pass!
tList6D17 = {
    "con" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "bla",        
        "target end": "ank",             
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bla" : {
        "nation": "russia",
        "order": "move",
        "target end": "ank",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ank" : {
        "nation": "turkey",
        "order": "move",
        "target end": "con",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
        "smy" : {
        "nation": "turkey",
        "order": "support",
        'support type': "move support",
        "target start": "ank",        
        "target end": "con",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
        "arm" : {
        "nation": "turkey",
        "order": "move",
        "target end": "ank",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #PASS! aStrengthMax fix. "The famous dislodge rule"
tList6D18 = {
    "con" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "bla",        
        "target end": "ank",             
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bla" : {
        "nation": "russia",
        "order": "move",
        "target end": "ank",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bul" : {
        "nation": "russia",
        "order": "support",
        'support type': "hold support", 
        "target end": "con",             
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ank" : {
        "nation": "turkey",
        "order": "move",
        "target end": "con",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "smy" : {
        "nation": "turkey",
        "order": "support",
        'support type': "move support",
        "target start": "ank",        
        "target end": "con",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "arm" : {
        "nation": "turkey",
        "order": "move",
        "target end": "ank",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #pass
tList6D19 = {
    "con" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "bla",        
        "target end": "ank",             
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bla" : {
        "nation": "russia",
        "order": "move",
        "target end": "ank",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "smy" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "ank",        
        "target end": "con",          
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ank" : {
        "nation": "turkey",
        "order": "move",
        "target end": "con",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #passs
tList6D20 = {
    "lon" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "nth",        
        "target end": "eng",             
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nth" : {
        "nation": "england",
        "order": "move",
        "target end": "eng",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "yor" : {
        "nation": "england",
        "order": "move",
        "target end": "lon",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "eng" : {
        "nation": "france",
        "order": "hold",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #PASS!
tList6D21 = {
    "tri" : {
        "nation": "austria",
        "order": "hold",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ven" : {
        "nation": "italy",
        "order": "move",
        "target end": "tri",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "tyr" : {
        "nation": "italy",
        "order": "support",
        'support type': "move support",
        "target start": "ven",        
        "target end": "tri",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "mun" : {
        "nation": "germany",
        "order": "move",
        "target end": "tyr",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "sil" : {
        "nation": "russia",
        "order": "move",
        "target end": "mun",        
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ber" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "sil",        
        "target end": "mun",             
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    } 
} #Pass!
tList6D33 = {
    "ser" : {
        "nation": "austria",
        "order": "move",
        "target end": "bud",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "vie" : {
        "nation": "austria",
        "order": "move",
        "target end": "bud",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "gal" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "ser",        
        "target end": "bud",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bul" : {
        "nation": "turkey",
        "order": "move",
        "target end": "ser",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #Pass!
tList6E1 = {
    "ber" : {
        "nation": "germany",
        "order": "move",
        "target end": "pru",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "germany",
        "order": "move",
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "sil" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "ber",        
        "target end": "pru",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "pru" : {
        "nation": "russia",
        "order": "move",
        "target end": "ber",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #PASS
tList6E2 = {
    "ber" : {
        "nation": "germany",
        "order": "move",
        "target end": "kie",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "germany",
        "order": "move",
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "mun" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "ber",        
        "target end": "kie",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #PASS
tList6E3 = {
    "ber" : {
        "nation": "germany",
        "order": "move",
        "target end": "kie",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "england",
        "order": "move",
        "target end": "ber",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "mun" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "kie",        
        "target end": "ber",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #PASS
tList6E4 = {
    "hol" : {
        "nation": "germany",
        "order": "move",
        "target end": "nth",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "hel" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "hol",        
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ska" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "hol",        
        "target end": "nth",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nth" : {
        "nation": "france",
        "order": "move",
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bel" : {
        "nation": "france",
        "order": "support",
        'support type': "move support",
        "target start": "nth",        
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "edi" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "nwg",        
        "target end": "nth",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "yor" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "nwg",        
        "target end": "nth",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nwg" : {
        "nation": "england",
        "order": "move",
        "target end": "nth",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "ruh",        
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ruh" : {
        "nation": "austria",
        "order": "move",
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #PASS
tList6E5 = {
    "hol" : {
        "nation": "germany",
        "order": "move",
        "target end": "nth",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "hel" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "hol",        
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ska" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "hol",        
        "target end": "nth",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nth" : {
        "nation": "france",
        "order": "move",
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bel" : {
        "nation": "france",
        "order": "support",
        'support type': "move support",
        "target start": "nth",        
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "edi" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "nwg",        
        "target end": "nth",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "yor" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "nwg",        
        "target end": "nth",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "lon" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "nwg",        
        "target end": "nth",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nwg" : {
        "nation": "england",
        "order": "move",
        "target end": "nth",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "ruh",        
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ruh" : {
        "nation": "austria",
        "order": "move",
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #Pass with flying fuckin' carpets
tList6E6 = {
    "hol" : {
        "nation": "germany",
        "order": "move",
        "target end": "nth",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "hel" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "hol",        
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nth" : {
        "nation": "france",
        "order": "move",
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bel" : {
        "nation": "france",
        "order": "support",
        'support type': "move support",
        "target start": "nth",        
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "eng" : {
        "nation": "france",
        "order": "support",
        'support type': "move support",
        "target start": "hol",        
        "target end": "nth",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "ruh",        
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ruh" : {
        "nation": "austria",
        "order": "move",
        "target end": "hol",     
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #Pass
tList6E7 = {
    "nth" : {
        "nation": "england",
        "order": "hold",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "yor" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "nor",        
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "hol" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "hel",        
        "target end": "nth",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "hel" : {
        "nation": "germany",
        "order": "move",    
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ska" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "nor",        
        "target end": "nth",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nor" : {
        "nation": "russia",
        "order": "move",    
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #pass
tList6E8 = {
    "nth" : {
        "nation": "england",
        "order": "move",    
        "target end": "nor",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "yor" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "nor",        
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "hol" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "hel",        
        "target end": "nth",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "hel" : {
        "nation": "germany",
        "order": "move",    
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ska" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "nor",        
        "target end": "nth",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nor" : {
        "nation": "russia",
        "order": "move",    
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #pass
tList6E9 = {
    "nth" : {
        "nation": "england",
        "order": "move",    
        "target end": "nwg",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "yor" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "nor",        
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "hol" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "hel",        
        "target end": "nth",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "hel" : {
        "nation": "germany",
        "order": "move",    
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ska" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "nor",        
        "target end": "nth",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nor" : {
        "nation": "russia",
        "order": "move",    
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #pass
tList6E10 = {
    "nth" : {
        "nation": "england",
        "order": "move",    
        "target end": "den",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "yor" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "nor",        
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "hol" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "hel",        
        "target end": "nth",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "hel" : {
        "nation": "germany",
        "order": "move",    
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "den" : {
        "nation": "germany",
        "order": "move",    
        "target end": "hel",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ska" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "nor",        
        "target end": "nth",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nor" : {
        "nation": "russia",
        "order": "move",    
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #pass
tList6E12 = {
    "bud" : {
        "nation": "austria",
        "order": "move",    
        "target end": "rum",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "ser" : {
        "nation": "austria",
        "order": "support",
        'support type': "move support",
        "target start": "vie",        
        "target end": "bud",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "vie" : {
        "nation": "italy",
        "order": "move",    
        "target end": "bud",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "gal" : {
        "nation": "germany",
        "order": "move",    
        "target end": "bud",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "rum" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "gal",        
        "target end": "bud",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #pass
tList6E13 = {
    "edi" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "yor",        
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },   
    "yor" : {
        "nation": "england",
        "order": "move",    
        "target end": "nth",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "bel" : {
        "nation": "france",
        "order": "move",    
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "eng" : {
        "nation": "france",
        "order": "support",
        'support type': "move support",
        "target start": "bel",        
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "nth" : {
        "nation": "germany",
        "order": "hold",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nwg" : {
        "nation": "russia",
        "order": "move",    
        "target end": "nth",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "nor" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "nwg",        
        "target end": "nth",   
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #pass
tList6E15 = {
    "hol" : {
        "nation": "england",
        "order": "support",
        'support type': "move support",
        "target start": "ruh",        
        "target end": "kie",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },   
    "ruh" : {
        "nation": "england",
        "order": "move",    
        "target end": "kie",
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "kie" : {
        "nation": "france",
        "order": "move",    
        "target end": "ber",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "mun" : {
        "nation": "france",
        "order": "support",
        'support type': "move support",
        "target start": "kie",        
        "target end": "ber",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "sil" : {
        "nation": "france",
        "order": "support",
        'support type': "move support",
        "target start": "kie",        
        "target end": "ber",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "ber" : {
        "nation": "germany",
        "order": "move",    
        "target end": "kie",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },
    "den" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "ber",        
        "target end": "kie",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "hel" : {
        "nation": "germany",
        "order": "support",
        'support type': "move support",
        "target start": "ber",        
        "target end": "kie",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "bal" : {
        "nation": "russia",
        "order": "support",
        'support type': "move support",
        "target start": "pru",        
        "target end": "ber",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    },    
    "pru" : {
        "nation": "russia",
        "order": "move",    
        "target end": "ber",    
        "outcome": 'undecided',
        'dislodge status': 'undecided'
    }
} #pass

#defunct move code
''' if movelist.get(targetArea) != None and (movelist.get(targetArea,{}).get("order") == "move" and movelist.get(targetArea,{}).get("target end") == unit): #head to head
        if attackStrengthMin(unit, targetArea, movelist) > defendStrengthMax(targetArea, unit, movelist) and attackStrengthMin(unit, targetArea, movelist) > largestPreventMax:
            return "moves"
        elif attackStrengthMax(unit, targetArea, movelist) <= defendStrengthMin(targetArea, unit, movelist):
            return "fails"
    elif attackStrengthMin(unit, targetArea, movelist) > holdStrengthMax(targetArea, movelist) and attackStrengthMin(unit, targetArea, movelist) > largestPreventMax:
        return "moves"
    elif attackStrengthMax(unit, targetArea, movelist) <= holdStrengthMin(targetArea, movelist) or attackStrengthMax(unit, targetArea, movelist) <= largestPreventMin:
        return "fails"
    else:
        return "undecided"'''
#defunct adjudicate code
'''def adjudicate(turnMoves, turnOutcomes):

    for m in turnMoves:     #add all hold and move orders to turnOutcomes
        if turnMoves[m]["order"] in ("hold" , "move" ,"move via convoy"):
            turnOutcomes[m] = turnMoves[m]
            turnOutcomes[m]["support"] = 0
            turnOutcomes[m].pop("target start")

    for n in turnMoves:     #add all supports to existing moves TODO: add hold support to attacking units
        if turnMoves[n]["order"] == "support":
            for match in turnOutcomes:
                if turnMoves[n]["target start"] == match and turnMoves[n]["target end"] == turnOutcomes[match]["target end"]:
                    turnOutcomes[match]["support"] += 1
    

    unitsList = {}
    for x in turnmoves:
        append x to unitslist
    '''