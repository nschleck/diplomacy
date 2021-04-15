#
#
#

territories = {             #dictionary containing all initial conditions of the map territories
    "adr" : {
        "name": "Adriatic Sea",
        "type": "sea",
        "country": "",
        "supplyCenter":False,
        "borders": ["ion","apu","ven","tri","alb"],
        "occupied": False
    },
    "aeg" : {
        "name": "Aegean Sea",
        "type": "sea",
        "country": "",
        "supplyCenter":False,
        "borders": ["ion","gre","bul","con","smy","eas"],
        "occupied": False
    },
    "alb" : {
        "name": "Albania",
        "type": "coast",
        "country": "",
        "supplyCenter":False,
        "borders": ["ion","adr","tri","ser","gre"],
        "occupied": False
    },
    "ank" : {
        "name": "Ankara",
        "type": "coast",
        "country": "turkey",
        "homeCenter": "turkey",
        "supplyCenter":True,
        "borders": ["smy","con","bla","arm"],
        "occupied": True
    },
    "apu" : {
        "name": "Apulia",
        "type": "coast",
        "country": "italy",
        "supplyCenter":False,
        "borders": ["ion","adr","nap","rom","ven"],
        "occupied": False
    },
    "arm" : {
        "name":"Armenia",
        "type": "coast",
        "country": "turkey",
        "supplyCenter":False,
        "borders": ["syr","smy","ank","bla","sev"],
        "occupied": False
    },
    "bal" : {
        "name":"Baltic Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["bot", "den", "kie","ber","pru","lvn","swe"],
        "occupied":False,
    },
    "bar" : {
        "name":"Barents Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["stp","nwg","nwy"],
        "occupied":False,
    },
    "bel" : {
        "name":"Belgium",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["pic","eng","bur","ruh","hol","nth"],
        "occupied":False,
    },
    "ber" : {
        "name":"Berlin",
        "type":"coast",
        "country":"germany",
        "homeCenter": "germany",
        "supplyCenter":True,
        "borders":["kie","mun","sil","pru","bal"],
        "occupied":True,
    },
    "bla" : {
        "name":"Black Sea",
        "type": "sea",
        "country": "",
        "supplyCenter":False,
        "borders": ["rum","bul","ank","con","sev","arm"],
        "occupied": False
    },
    "boh" : {
        "name":"Bohemia",
        "type":"land",
        "country":"austria",
        "supplyCenter":False,
        "borders":["sil","mun","tyr","vie","gal"],
        "occupied":False,
    },
    "bre" : {
        "name":"Brest",
        "type":"coast",
        "country":"france",
        "homeCenter": "france",
        "supplyCenter":True,
        "borders":["pic","par","gas","mid","eng"],
        "occupied":True,
    },
    "bud" : {
        "name":"Budapest",
        "type":"land",
        "country":"austria",
        "homeCenter": "austria",
        "supplyCenter":True,
        "borders":["vie","gal","rum","ser","tri"],
        "occupied":True,
    },
    "bul" : {
        "name":"Bulgaria",
        "type": "coast",
        "country": "",
        "supplyCenter":True,
        "borders": ["rum","bla","ser","con","gre","aeg"],
        "occupied": False
    },
    "bur" : {
        "name":"Burgundy",
        "type":"land",
        "country":"france",
        "supplyCenter":False,
        "borders":["mar","gas","par","pic","bel","ruh","mun"],
        "occupied":False,
    },
    "cly" : {
        "name":"Clyde",
        "type":"coast",
        "country":"england",
        "supplyCenter":False,
        "borders":["edi","lvp","nat","nwg"],
        "occupied":False,
    },
    "con" : {
        "name": "Constantinople",
        "type": "coast",
        "country": "turkey",
        "homeCenter": "turkey",
        "supplyCenter":True,
        "borders": ["bla","ank","smy","aeg","bul"],
        "occupied": True
    },
    "den" : {
        "name":"Denmark",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["kie","swe","bal","ska","hel","nth"],
        "occupied":False,
    },
    "eas" : {
        "name":"Eastern Mediterranean",
        "type": "sea",
        "country": "",
        "supplyCenter":False,
        "borders": ["syr","smy","aeg","ion"],
        "occupied": False
    },
    "edi" : {
        "name":"Edinburgh",
        "type": "coast",
        "country": "england",
        "homeCenter": "england",
        "supplyCenter":True,
        "borders": ["cly","nwg","nth","yor","lvp"],
        "occupied": True
    },
    "eng" : {
        "name":"English Channel",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["mid","bre","pic","bel","nth","lon","wal","iri"],
        "occupied":False,
    },
    "fin" : {
        "name":"Finland",
        "type":"coast",
        "country":"russia",
        "supplyCenter":False,
        "borders":["swe","nwy","stp","bot"],
        "occupied":False,
    },
    "gal" : {
        "name":"Galicia",
        "type":"land",
        "country":"austria",
        "supplyCenter":False,
        "borders":["war","ukr","rum","bud","vie","boh","sil"],
        "occupied":False,
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
    },
    "bot" : {
        "name":"Gulf of Bothnia",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["fin","stp","lvn","bal","swe"],
        "occupied":False,
    },
    "lyo" : {
        "name":"Gulf of Lyon",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["wes","tyn","spa","mar","pie","tus"],
        "occupied":False,
    },
    "hel" : {
        "name":"Helgoland Bight",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["nth","den","kie","hol"],
        "occupied":False,
    },
    "hol" : {
        "name":"Holland",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["hel","nth","bel","ruh","kie"],
        "occupied":False,
    },
    "ion" : {
        "name":"Ionian Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["tun","tyn","nap","apu","adr","alb","gre","aeg","eas"],
        "occupied":False,
    },
    "iri" : {
        "name":"Irish Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["nat","mid","eng","wal","lvp"],
        "occupied":False,
    },
    "kie" : {
        "name":"Kiel",
        "type":"coast",
        "country":"germany",
        "homeCenter": "germany",
        "supplyCenter":True,
        "borders":["hel","hol","ruh","mun","ber","bal","den"],
        "occupied":True,
    },
    "lvp" : {
        "name":"Liverpool",
        "type":"coast",
        "country":"england",
        "homeCenter": "england",
        "supplyCenter":True,
        "borders":["iri","nat","cly","edi","yor","wal"],
        "occupied":True,
    },
    "lvn" : {
        "name":"Livonia",
        "type":"coast",
        "country":"russia",
        "supplyCenter":False,
        "borders":["bot","bal","pru","war","mos","stp"],
        "occupied":False,
    },
    "lon" : {
        "name":"London",
        "type":"coast",
        "country":"england",
        "homeCenter": "england",
        "supplyCenter":True,
        "borders":["wal","yor","nth","eng"],
        "occupied":True,
    },
    "mar" : {
        "name":"Marseilles",
        "type":"coast",
        "country":"france",
        "homeCenter": "france",
        "supplyCenter":True,
        "borders":["lyo","spa","gas","pie","bur"],
        "occupied":True,
    },
    "mid" : {
        "name":"Mid Atlantic Ocean",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["naf","por","spa","gas","bre","eng","iri","nat"],
        "occupied":False,
    },
    "mos" : {
        "name":"Moscow",
        "type":"land",
        "country":"russia",
        "homeCenter": "russia",
        "supplyCenter":True,
        "borders":["sev","ukr","war","stp","lvn"],
        "occupied":True,
    },
    "mun" : {
        "name":"Munich",
        "type":"land",
        "country":"germany",
        "homeCenter": "germany",
        "supplyCenter":True,
        "borders":["bur","ruh","kie","ber","sil","boh","tyr"],
        "occupied":True,
    },
    "nap" : {
        "name":"Naples",
        "type":"coast",
        "country":"italy",
        "homeCenter": "italy",
        "supplyCenter":True,
        "borders":["tyn","ion","apu","rom"],
        "occupied":True,
    },
    "naf" : {
        "name":"North Africa",
        "type":"coast",
        "country":"",
        "supplyCenter":False,
        "borders":["tun","mid","wes"],
        "occupied":False,
    },
    "nat" : {
        "name":"North Atlantic Ocean",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["mid","iri","cly","nwg","lvp"],
        "occupied":False,
    },
    "nth" : {
        "name":"North Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["nwg","ska","hel","eng","edi","yor","lon","bel","hol","nwy","den"],
        "occupied":False,
    },
    "nwy" : {
        "name":"Norway",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["swe","fin","bar","nwg","nth","ska","stp"],
        "occupied":False,
    },
    "nwg" : {
        "name":"Norwegian Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["nwy","cly","edi","nat","bar","nth"],
        "occupied":False,
    },
    "par" : {
        "name":"Paris",
        "type":"land",
        "country":"france",
        "homeCenter": "france",
        "supplyCenter":True,
        "borders":["pic","bre","bur","gas"],
        "occupied":True,
    },
    "pic" : {
        "name":"Picardy",
        "type":"coast",
        "country":"france",
        "supplyCenter":False,
        "borders":["eng","bel","bre","par","bur"],
        "occupied":False,
    },
    "pie" : {
        "name":"Piedmont",
        "type":"coast",
        "country":"italy",
        "supplyCenter":False,
        "borders":["mar","lyo","tus","ven","tyr"],
        "occupied":False,
    },
    "por" : {
        "name":"Portugal",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["spa","mid"],
        "occupied":False,
    },
    "pru" : {
        "name":"Prussia",
        "type":"coast",
        "country":"germany",
        "supplyCenter":False,
        "borders":["ber","sil","war","lvn","bal"],
        "occupied":False,
    },
    "rom" : {
        "name":"Rome",
        "type":"coast",
        "country":"italy",
        "homeCenter": "italy",
        "supplyCenter":True,
        "borders":["tus","ven","apu","nap","tyn"],
        "occupied":True,
    },
    "ruh" : {
        "name":"Ruhr",
        "type":"land",
        "country":"germany",
        "supplyCenter":False,
        "borders":["kie","bel","hol","bur","mun"],
        "occupied":False,
    },
    "rum" : {
        "name":"Rumania",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["bla","sev","ukr","gal","bud","ser","bul"],
        "occupied":False,
    },
    "stp" : {
        "name":"St Petersburg",
        "type":"coast",
        "country":"russia",
        "homeCenter": "russia",
        "supplyCenter":True,
        "borders":["bar","fin","nwy","bot","lvn","mos"],
        "occupied":True,
    },
    "ser" : {
        "name":"Serbia",
        "type":"land",
        "country":"",
        "supplyCenter":True,
        "borders":["tri","bud","rum","bul","gre","alb"],
        "occupied":False,
    },
    "sev" : {
        "name":"Sevastapol",
        "type":"coast",
        "country":"russia",
        "homeCenter": "russia",
        "supplyCenter":True,
        "borders":["ukr","mos","bla","rum","arm"],
        "occupied":True,
    },
    "sil" : {
        "name":"Silessia",
        "type":"land",
        "country":"germany",
        "supplyCenter":False,
        "borders":["ber","pru","mun","war","boh","gal"],
        "occupied":False,
    },
    "ska" : {
        "name":"Skaggerack",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["nwy","swe","den","nth"],
        "occupied":False,
    },
    "smy" : {
        "name":"Smyrna",
        "type": "coast",
        "country": "turkey",
        "homeCenter": "turkey",
        "supplyCenter":True,
        "borders": ["syr","eas","aeg","con","ank","arm"],
        "occupied": True
    },
    "spa" : {
        "name":"Spain",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["por","gas","mar","mid","wes","lyo"],
        "occupied":False,
    },
    "swe" : {
        "name":"Sweden",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["nwy","ska","fin","den","bal","bot"],
        "occupied":False,
    },
    "syr" : {
        "name":"Syria",
        "type": "coast",
        "country": "turkey",
        "supplyCenter":False,
        "borders": ["smy","eas","arm"],
        "occupied": False
    },
    "tri" : {
        "name":"Trieste",
        "type":"coast",
        "country":"austria",
        "homeCenter": "austria",
        "supplyCenter":True,
        "borders":["tyr","vie","bud","ser","alb","adr","ven"],
        "occupied":True,
    },
    "tun" : {
        "name":"Tunisia",
        "type":"coast",
        "country":"",
        "supplyCenter":True,
        "borders":["naf","ion","tyn","wes"],
        "occupied":False,
    },
    "tus" : {
        "name":"Tuscany",
        "type":"coast",
        "country":"italy",
        "supplyCenter":False,
        "borders":["pie","ven","rom","lyo","tyn"],
        "occupied":False,
    },
    "tyr" : {
        "name":"Tyrolia",
        "type":"land",
        "country":"austria",
        "supplyCenter":False,
        "borders":["boh","vie","tri","mun","ven","pie"],
        "occupied":False,
    },
    "tyn" : {
        "name":"Tyrrhenian Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["tus","rom","nap","tun","wes","lyo","ion"],
        "occupied":False,
    },
    "ukr" : {
        "name":"Ukraine",
        "type":"land",
        "country":"russia",
        "supplyCenter":False,
        "borders":["war","mos","sev","gal","rum"],
        "occupied":False,
    },
    "ven" : {
        "name":"Venice",
        "type":"coast",
        "country":"italy",
        "homeCenter": "italy",
        "supplyCenter":True,
        "borders":["pie","tus","rom","apu","adr","tri","tyr"],
        "occupied":True,
    },
    "vie" : {
        "name":"Vienna",
        "type":"land",
        "country":"austria",
        "homeCenter": "austria",
        "supplyCenter":True,
        "borders":["tyr","boh","gal","tri","bud"],
        "occupied":True,
    },
    "wal" : {
        "name":"Wales",
        "type":"coast",
        "country":"england",
        "supplyCenter":False,
        "borders":["lvp","yor","lon","eng","iri"],
        "occupied":False,
    },
    "war" : {
        "name":"Warsaw",
        "type":"land",
        "country":"russia",
        "homeCenter": "russia",
        "supplyCenter":True,
        "borders":["lvn","mos","ukr","pru","sil","gal"],
        "occupied":True,
    },
    "wes" : {
        "name":"Western Mediterranean Sea",
        "type":"sea",
        "country":"",
        "supplyCenter":False,
        "borders":["spa","naf","tun","lyo","tyn"],
        "occupied":False,
    },
    "yor" : {
        "name":"York",
        "type":"coast",
        "country":"england",
        "supplyCenter":False,
        "borders":["edi","lvp","wal","lon","nth"],
        "occupied":False,
    }
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

#testTypes(territories)
#testCountries(territories)
#listSuppliers(territories)
#testBorders(territories)


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
    }
}
