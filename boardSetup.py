#
#


territories = {             #dictionary containing all initial conditions of the map territories
    "adr" : {
        "name": "Adriatic Sea",
        "type": "sea",
        "country": "",
        "supplyCenter":False,
        "borders": ["ion","apu","ven","tri","alb"],
        "occupied": False,
        "x_coord": 615,
        "y_coord":775
    },
    "aeg" : {
        "name": "Aegean Sea",
        "type": "sea",
        "country": "",
        "supplyCenter":False,
        "borders": ["ion","gre","bul","con","smy","eas"],
        "occupied": False,
        "x_coord": 810,
        "y_coord": 925
    },
    "alb" : {
        "name": "Albania",
        "type": "coast",
        "country": "",
        "supplyCenter":False,
        "borders": ["ion","adr","tri","ser","gre"],
        "occupied": False,
        "x_coord": 700,
        "y_coord": 830
    },
    "ank" : {
        "name": "Ankara",
        "type": "coast",
        "country": "turkey",
        "homeCenter": "turkey",
        "supplyCenter":True,
        "borders": ["smy","con","bla","arm"],
        "occupied": True,
        "x_coord": 970,
        "y_coord": 820
    },
    "apu" : {
        "name": "Apulia",
        "type": "coast",
        "country": "italy",
        "supplyCenter":False,
        "borders": ["ion","adr","nap","rom","ven"],
        "occupied": False,
        "x_coord": 610,
        "y_coord": 820
    },
    "arm" : {
        "name":"Armenia",
        "type": "coast",
        "country": "turkey",
        "supplyCenter":False,
        "borders": ["syr","smy","ank","bla","sev"],
        "occupied": False,
        "x_coord": 1130,
        "y_coord": 820
    },
    "bal" : {
        "name":"Baltic Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["bot", "den", "kie","ber","pru","lvn","swe"],
        "occupied":False,
        "x_coord": 650,
        "y_coord": 450
    },
    "bar" : {
        "name":"Barents Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["stp","nwg","nwy"],
        "occupied":False,
        "x_coord": 860,
        "y_coord": 50
    },
    "bel" : {
        "name":"Belgium",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["pic","eng","bur","ruh","hol","nth"],
        "occupied":False,
        "x_coord": 440,
        "y_coord": 555
    },
    "ber" : {
        "name":"Berlin",
        "type":"coast",
        "country":"germany",
        "homeCenter": "germany",
        "supplyCenter":True,
        "borders":["kie","mun","sil","pru","bal"],
        "occupied":True,
        "x_coord": 590,
        "y_coord": 520
    },
    "bla" : {
        "name":"Black Sea",
        "type": "sea",
        "country": "",
        "supplyCenter":False,
        "borders": ["rum","bul","ank","con","sev","arm"],
        "occupied": False,
        "x_coord": 960,
        "y_coord": 750
    },
    "boh" : {
        "name":"Bohemia",
        "type":"land",
        "country":"austria",
        "supplyCenter":False,
        "borders":["sil","mun","tyr","vie","gal"],
        "occupied":False,
        "x_coord": 605,
        "y_coord": 600
    },
    "bre" : {
        "name":"Brest",
        "type":"coast",
        "country":"france",
        "homeCenter": "france",
        "supplyCenter":True,
        "borders":["pic","par","gas","mid","eng"],
        "occupied":True,
        "x_coord": 320,
        "y_coord": 590
    },
    "bud" : {
        "name":"Budapest",
        "type":"land",
        "country":"austria",
        "homeCenter": "austria",
        "supplyCenter":True,
        "borders":["vie","gal","rum","ser","tri"],
        "occupied":True,
        "x_coord": 710,
        "y_coord": 675
    },
    "bul" : {
        "name":"Bulgaria",
        "type": "coast",
        "country": "",
        "supplyCenter":True,
        "borders": ["rum","bla","ser","con","gre","aeg"],
        "occupied": False,
        "coasts": ["east","south"],
        "east borders": ["rum","bla","con"],
        "south borders": ["con","gre","aeg"],
        "x_coord": 800,
        "y_coord": 790
    },
    "bur" : {
        "name":"Burgundy",
        "type":"land",
        "country":"france",
        "supplyCenter":False,
        "borders":["mar","gas","par","pic","bel","ruh","mun"],
        "occupied":False,
        "x_coord": 425,
        "y_coord": 640
    },
    "cly" : {
        "name":"Clyde",
        "type":"coast",
        "country":"england",
        "supplyCenter":False,
        "borders":["edi","lvp","nat","nwg"],
        "occupied":False,
        "x_coord": 345,
        "y_coord": 360
    },
    "con" : {
        "name": "Constantinople",
        "type": "coast",
        "country": "turkey",
        "homeCenter": "turkey",
        "supplyCenter":True,
        "borders": ["bla","ank","smy","aeg","bul"],
        "occupied": True,
        "x_coord": 870,
        "y_coord": 840
    },
    "den" : {
        "name":"Denmark",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["kie","swe","bal","ska","hel","nth"],
        "occupied":False,
        "x_coord": 545,
        "y_coord": 430
    },
    "eas" : {
        "name":"Eastern Mediterranean",
        "type": "sea",
        "country": "",
        "supplyCenter":False,
        "borders": ["syr","smy","aeg","ion"],
        "occupied": False,
        "x_coord": 920,
        "y_coord": 970
    },
    "edi" : {
        "name":"Edinburgh",
        "type": "coast",
        "country": "england",
        "homeCenter": "england",
        "supplyCenter":True,
        "borders": ["cly","nwg","nth","yor","lvp"],
        "occupied": True,
        "x_coord": 370,
        "y_coord": 370
    },
    "eng" : {
        "name":"English Channel",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["mid","bre","pic","bel","nth","lon","wal","iri"],
        "occupied":False,
        "x_coord": 310,
        "y_coord": 545
    },
    "fin" : {
        "name":"Finland",
        "type":"coast",
        "country":"russia",
        "supplyCenter":False,
        "borders":["swe","nwy","stp","bot"],
        "occupied":False,
        "x_coord": 770,
        "y_coord": 270
    },
    "gal" : {
        "name":"Galicia",
        "type":"land",
        "country":"austria",
        "supplyCenter":False,
        "borders":["war","ukr","rum","bud","vie","boh","sil"],
        "occupied":False,
        "x_coord": 760,
        "y_coord": 610
    },
    "gas" : {
        "name":"Gascony",
        "type":"coast",
        "country":"france",
        "supplyCenter":False,
        "borders":["spa","mid","bre","par","bur","mar"],
        "occupied":False,
    },
    "gre" : {
        "name":"Greece",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["ion","aeg","bul","ser","alb"],
        "occupied":False,
        "x_coord": 740,
        "y_coord": 880
    },
    "bot" : {
        "name":"Gulf of Bothnia",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["fin","stp","lvn","bal","swe"],
        "occupied":False,
        "x_coord": 715,
        "y_coord": 350
    },
    "lyo" : {
        "name":"Gulf of Lyon",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["wes","tyn","spa","mar","pie","tus"],
        "occupied":False,
        "x_coord": 430,
        "y_coord": 800
    },
    "hel" : {
        "name":"Helgoland Bight",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["nth","den","kie","hol"],
        "occupied":False,
        "x_coord": 490,
        "y_coord": 460
    },
    "hol" : {
        "name":"Holland",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["hel","nth","bel","ruh","kie"],
        "occupied":False,
        "x_coord": 470,
        "y_coord": 520
    },
    "ion" : {
        "name":"Ionian Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["tun","tyn","nap","apu","adr","alb","gre","aeg","eas"],
        "occupied":False,
        "x_coord": 670,
        "y_coord": 930
    },
    "iri" : {
        "name":"Irish Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["nat","mid","eng","wal","lvp"],
        "occupied":False,
        "x_coord": 250,
        "y_coord": 490
    },
    "kie" : {
        "name":"Kiel",
        "type":"coast",
        "country":"germany",
        "homeCenter": "germany",
        "supplyCenter":True,
        "borders":["hel","hol","ruh","mun","ber","bal","den"],
        "occupied":True,
        "x_coord": 530,
        "y_coord": 510
    },
    "lvp" : {
        "name":"Liverpool",
        "type":"coast",
        "country":"england",
        "homeCenter": "england",
        "supplyCenter":True,
        "borders":["iri","nat","cly","edi","yor","wal"],
        "occupied":True,
        "x_coord": 355,
        "y_coord": 440
    },
    "lvn" : {
        "name":"Livonia",
        "type":"coast",
        "country":"russia",
        "supplyCenter":False,
        "borders":["bot","bal","pru","war","mos","stp"],
        "occupied":False,
        "x_coord": 770,
        "y_coord": 430
    },
    "lon" : {
        "name":"London",
        "type":"coast",
        "country":"england",
        "homeCenter": "england",
        "supplyCenter":True,
        "borders":["wal","yor","nth","eng"],
        "occupied":True,
        "x_coord": 380,
        "y_coord": 500
    },
    "mar" : {
        "name":"Marseilles",
        "type":"coast",
        "country":"france",
        "homeCenter": "france",
        "supplyCenter":True,
        "borders":["lyo","spa","gas","pie","bur"],
        "occupied":True,
        "x_coord": 420,
        "y_coord": 720
    },
    "mid" : {
        "name":"Mid Atlantic Ocean",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["naf","por","spa","gas","bre","eng","iri","nat"],
        "occupied":False,
        "x_coord": 90,
        "y_coord": 650
    },
    "mos" : {
        "name":"Moscow",
        "type":"land",
        "country":"russia",
        "homeCenter": "russia",
        "supplyCenter":True,
        "borders":["sev","ukr","war","stp","lvn"],
        "occupied":True,
        "x_coord": 900,
        "y_coord": 470
    },
    "mun" : {
        "name":"Munich",
        "type":"land",
        "country":"germany",
        "homeCenter": "germany",
        "supplyCenter":True,
        "borders":["bur","ruh","kie","ber","sil","boh","tyr"],
        "occupied":True,
        "x_coord": 530,
        "y_coord": 610
    },
    "nap" : {
        "name":"Naples",
        "type":"coast",
        "country":"italy",
        "homeCenter": "italy",
        "supplyCenter":True,
        "borders":["tyn","ion","apu","rom"],
        "occupied":True,
        "x_coord": 600,
        "y_coord": 850
    },
    "naf" : {
        "name":"North Africa",
        "type":"coast",
        "country":"",
        "supplyCenter":False,
        "borders":["tun","mid","wes"],
        "occupied":False,
        "x_coord": 300,
        "y_coord": 940
    },
    "nat" : {
        "name":"North Atlantic Ocean",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["mid","iri","cly","nwg","lvp"],
        "occupied":False,
        "x_coord": 180,
        "y_coord": 280
    },
    "nth" : {
        "name":"North Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["nwg","ska","hel","eng","edi","yor","lon","bel","hol","nwy","den"],
        "occupied":False,
        "x_coord": 450,
        "y_coord": 360
    },
    "nwy" : {
        "name":"Norway",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["swe","fin","bar","nwg","nth","ska","stp"],
        "occupied":False,
        "x_coord": 550,
        "y_coord": 305
    },
    "nwg" : {
        "name":"Norwegian Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["nwy","cly","edi","nat","bar","nth"],
        "occupied":False,
        "x_coord": 500,
        "y_coord": 190
    },
    "par" : {
        "name":"Paris",
        "type":"land",
        "country":"france",
        "homeCenter": "france",
        "supplyCenter":True,
        "borders":["pic","bre","bur","gas"],
        "occupied":True,
        "x_coord": 380,
        "y_coord": 620
    },
    "pic" : {
        "name":"Picardy",
        "type":"coast",
        "country":"france",
        "supplyCenter":False,
        "borders":["eng","bel","bre","par","bur"],
        "occupied":False,
        "x_coord": 400,
        "y_coord": 570
    },
    "pie" : {
        "name":"Piedmont",
        "type":"coast",
        "country":"italy",
        "supplyCenter":False,
        "borders":["mar","lyo","tus","ven","tyr"],
        "occupied":False,
        "x_coord": 490,
        "y_coord": 710
    },
    "por" : {
        "name":"Portugal",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["spa","mid"],
        "occupied":False,
        "x_coord": 135,
        "y_coord": 790
    },
    "pru" : {
        "name":"Prussia",
        "type":"coast",
        "country":"germany",
        "supplyCenter":False,
        "borders":["ber","sil","war","lvn","bal"],
        "occupied":False,
        "x_coord": 660,
        "y_coord": 500
    },
    "rom" : {
        "name":"Rome",
        "type":"coast",
        "country":"italy",
        "homeCenter": "italy",
        "supplyCenter":True,
        "borders":["tus","ven","apu","nap","tyn"],
        "occupied":True,
        "x_coord": 560,
        "y_coord": 800
    },
    "ruh" : {
        "name":"Ruhr",
        "type":"land",
        "country":"germany",
        "supplyCenter":False,
        "borders":["kie","bel","hol","bur","mun"],
        "occupied":False,
        "x_coord": 490,
        "y_coord": 570
    },
    "rum" : {
        "name":"Rumania",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["bla","sev","ukr","gal","bud","ser","bul"],
        "occupied":False,
        "x_coord": 830,
        "y_coord": 720
    },
    "stp" : {
        "name":"St Petersburg",
        "type":"coast",
        "country":"russia",
        "homeCenter": "russia",
        "supplyCenter":True,
        "borders":["bar","fin","nwy","bot","lvn","mos"],
        "occupied":True,
        "coasts": ["north","south"],
        "north borders": ["bar","nwy"],
        "south borders": ["fin","bot","lvn"],
        "x_coord": 860,
        "y_coord": 300
    },
    "ser" : {
        "name":"Serbia",
        "type":"land",
        "country":"",
        "supplyCenter":True,
        "borders":["tri","bud","rum","bul","gre","alb"],
        "occupied":False,
        "x_coord": 710,
        "y_coord": 880
    },
    "sev" : {
        "name":"Sevastapol",
        "type":"coast",
        "country":"russia",
        "homeCenter": "russia",
        "supplyCenter":True,
        "borders":["ukr","mos","bla","rum","arm"],
        "occupied":True,
        "x_coord": 945,
        "y_coord": 650
    },
    "sil" : {
        "name":"Silessia",
        "type":"land",
        "country":"germany",
        "supplyCenter":False,
        "borders":["ber","pru","mun","war","boh","gal"],
        "occupied":False,
        "x_coord": 635,
        "y_coord": 560
    },
    "ska" : {
        "name":"Skaggerack",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["nwy","swe","den","nth"],
        "occupied":False,
        "x_coord": 560,
        "y_coord": 370
    },
    "smy" : {
        "name":"Smyrna",
        "type": "coast",
        "country": "turkey",
        "homeCenter": "turkey",
        "supplyCenter":True,
        "borders": ["syr","eas","aeg","con","ank","arm"],
        "occupied": True,
        "x_coord": 900,
        "y_coord": 910
    },
    "spa" : {
        "name":"Spain",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["por","gas","mar","mid","wes","lyo"],
        "occupied":False,
        "coasts": ["north","south"],
        "north borders": ["por","gas","mid"],
        "south borders": ["por","mar","mid","wes","lyo"],
        "x_coord": 270,
        "y_coord": 770
    },
    "swe" : {
        "name":"Sweden",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["nwy","ska","fin","den","bal","bot"],
        "occupied":False,
        "x_coord": 620,
        "y_coord": 380
    },
    "syr" : {
        "name":"Syria",
        "type": "coast",
        "country": "turkey",
        "supplyCenter":False,
        "borders": ["smy","eas","arm"],
        "occupied": False,
        "x_coord": 1080,
        "y_coord": 920
    },
    "tri" : {
        "name":"Trieste",
        "type":"coast",
        "country":"austria",
        "homeCenter": "austria",
        "supplyCenter":True,
        "borders":["tyr","vie","bud","ser","alb","adr","ven"],
        "occupied":True,
        "x_coord": 640,
        "y_coord": 730
    },
    "tun" : {
        "name":"Tunisia",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["naf","ion","tyn","wes"],
        "occupied":False,
        "x_coord": 480,
        "y_coord": 950
    },
    "tus" : {
        "name":"Tuscany",
        "type":"coast",
        "country":"italy",
        "supplyCenter":False,
        "borders":["pie","ven","rom","lyo","tyn"],
        "occupied":False,
        "x_coord": 530,
        "y_coord": 765
    },
    "tyr" : {
        "name":"Tyrolia",
        "type":"land",
        "country":"austria",
        "supplyCenter":False,
        "borders":["boh","vie","tri","mun","ven","pie"],
        "occupied":False,
        "x_coord": 550,
        "y_coord": 670
    },
    "tyn" : {
        "name":"Tyrrhenian Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["tus","rom","nap","tun","wes","lyo","ion"],
        "occupied":False,
        "x_coord": 530,
        "y_coord": 850
    },
    "ukr" : {
        "name":"Ukraine",
        "type":"land",
        "country":"russia",
        "supplyCenter":False,
        "borders":["war","mos","sev","gal","rum"],
        "occupied":False,
        "x_coord": 840,
        "y_coord": 580
    },
    "ven" : {
        "name":"Venice",
        "type":"coast",
        "country":"italy",
        "homeCenter": "italy",
        "supplyCenter":True,
        "borders":["pie","tus","rom","apu","adr","tri","tyr"],
        "occupied":True,
        "x_coord": 540,
        "y_coord": 720
    },
    "vie" : {
        "name":"Vienna",
        "type":"land",
        "country":"austria",
        "homeCenter": "austria",
        "supplyCenter":True,
        "borders":["tyr","boh","gal","tri","bud"],
        "occupied":True,
        "x_coord": 640,
        "y_coord": 640
    },
    "wal" : {
        "name":"Wales",
        "type":"coast",
        "country":"england",
        "supplyCenter":False,
        "borders":["lvp","yor","lon","eng","iri"],
        "occupied":False,
        "x_coord": 330,
        "y_coord": 500
    },
    "war" : {
        "name":"Warsaw",
        "type":"land",
        "country":"russia",
        "homeCenter": "russia",
        "supplyCenter":True,
        "borders":["lvn","mos","ukr","pru","sil","gal"],
        "occupied":True,
        "x_coord": 730,
        "y_coord": 550
    },
    "wes" : {
        "name":"Western Mediterranean Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["spa","naf","tun","lyo","tyn"],
        "occupied":False,
        "x_coord": 380,
        "y_coord": 880
    },
    "yor" : {
        "name":"York",
        "type":"coast",
        "country":"england",
        "supplyCenter":False,
        "borders":["edi","lvp","wal","lon","nth"],
        "occupied":False,
        "x_coord": 380,
        "y_coord": 450
    }
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

###############TESTING FUNCTIONS###############################################################################################

def testTypes(terrs):
    sea = 0
    coast = 0
    land = 0
    tot = 0
    properTypes = ["sea","coast","land"]
    for x in terrs:
        if terrs[x]["type"] not in properTypes:
            print (x)
        if terrs[x]["type"] == "sea":
            sea += 1
        elif terrs[x]["type"] == "coast":
            coast += 1
        elif terrs[x]["type"] == "land":
            land += 1
        tot += 1
    print("total: " + str(tot))    
    print("sea: " + str(sea))
    print("land: " + str(land))    
    print("coast: " + str(coast))    
def testCountries(terrs):
    properCounts = ["england","france","germany","russia","turkey","austria","italy",""]
    for x in terrs:
        if terrs[x]["country"] not in properCounts:
            print (x)
def listSuppliers(terrs):
    print("Home Country supply centers:")
    for x in terrs:
        if terrs[x]["supplyCenter"] and terrs[x]["occupied"]:
            print (terrs[x]["name"])
    print("up for grabs SCs:")
    for x in terrs:
        if terrs[x]["supplyCenter"] and not terrs[x]["occupied"]:
            print (terrs[x]["name"])
def testBorders(terrs):
    for area in terrs:
        for adj in terrs[area]["borders"]:
            if adj not in terrs:
                print(str(area) + " border is not in territories list: " + str(adj))
            if area not in terrs[adj]["borders"]:
                print(str(area) + " is not connected properly to " + str(adj))


unitsTurkey = {             #dictionary containing all initial conditions of the map territories
    "smy" : {
        "type": "army",
    },
    "ank" : {
        "type": "fleet",
    },
    "con" : {
        "type": "army",
    }
}
unitsItaly = {
    "nap" : {
        "type": "fleet",
    },
    "ven" : {
        "type": "army",
    },
    "rom" : {
        "type": "army",
    }
}
unitsFrance = {
    "par" : {
        "type": "army",
    },
    "bre" : {
        "type": "fleet",
    },
    "mar" : {
        "type": "army",
    }
}
unitsEngland = {
    "edi" : {
        "type": "fleet",
    },
    "lon" : {
        "type": "fleet",
    },
    "lvp" : {
        "type": "army",
    }
}
unitsGermany = {
    "ber" : {
        "type": "army",
    },
    "kie" : {
        "type": "fleet",
    },
    "mun" : {
        "type": "army",
    }
}
unitsAustria = {
    "vie" : {
        "type": "army",
    },
    "tri" : {
        "type": "fleet",
    },
    "bud" : {
        "type": "army",
    }
}
unitsRussia = {
    "mos" : {
        "type": "army",
    },
    "war" : {
        "type": "army",
    },
    "sev" : {
        "type": "fleet",
    },
    "stp" : {
        "type": "fleet",
        "coast": "south"
    }
}

################ Setup Functions #####################################################################

def setupUnits():
    allUnits = {
        'austria' : {},
        "england" : {},
        'france' :  {},
        'germany' :  {},
        'italy' : {},
        'russia' :  {},
        'turkey' : {},
    }


    #Gametype input loop
    while True:
        setupInput = input("Do you want to start a standard game of Diplomacy, or custom scenario? (Please answer \"standard\" or \"custom\")\n\t")
        if setupInput.lower() == "standard":
            print("Standard game selected")
            allUnits = {
                'austria' : unitsAustria,
                "england" : unitsEngland,
                'france' :  unitsFrance,
                'germany' :  unitsGermany,
                'italy' : unitsItaly,
                'russia' :  unitsRussia,
                'turkey' : unitsTurkey,
            }
            return allUnits
        elif setupInput.lower() == "custom":
            print("Custom game selected\n")
            break
        else:
            print("Gametype not recognized\n")
    
    ##Custom Setup:
    def setupBuild(nation):
        while True:
            buildOrder = input("\tPlease specify a build order (Press enter to end builds for this nation):\n\t\t")
            #sanitize buildOrder input
            if buildOrder == '':
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
            if unitType not in ["army", "fleet"] or unitArea not in territories.keys():
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
            unitCoastStr = ''
            if unitType == "fleet":
                if territories[unitArea]["type"] == "land":
                    print("\tYou cannot build a fleet on land, dumb dumb.")
                    continue
                elif unitArea in ["bul",'spa',"stp"]:
                    try:
                        unitCoast = buildOrder[2]
                        if unitCoast in territories[unitArea]["coasts"]:
                            unitCoastStr = ', ' + unitCoast + ' coast'
                        else:
                            print("\t\tPlease specify a valid coast for a fleet build in this territory. e.g. F bul south")
                            continue     
                    except:
                        print("\t\tPlease specify a coast for a fleet build in this territory. e.g. F bul south")
                        continue                        

            #check for valid fleet build
            if unitType == "army" and territories[unitArea]["type"] == "sea":
                print("\tYou cannot build an army on water, dumb dumb.")
                continue


            #Valid Build
            print("\t\t" + (str(unitType)).capitalize() + " built in " + str(territories[unitArea]["name"]) + unitCoastStr)
            allUnits[nation][unitArea] = {"type" : unitType}
            if unitCoastStr != '':
                allUnits[nation][unitArea]["coast"] = unitCoast

        return allUnits[nation]        
            
    for nation in allUnits.keys():
        print(nationality[nation][nation] + " initial units:")
        allUnits[nation] = setupBuild(nation)

    return allUnits