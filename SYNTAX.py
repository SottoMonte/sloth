import GRAMMAR
import time

def AST_GEX(ROOT,STREE):
    ALL = []
    print("::::::::::::::| Root ",ROOT)
    if type(STREE) == type((1,2)):
        return STREE
    else:
        if GRAMMAR.TEST_OR([STREE],[GRAMMAR.TEST_SET])[0] == True:
            for X in GRAMMAR.GET_SET(STREE):
                ALL.append(AST_GEX(ROOT+1,X))
            return tuple(("BLOCK",ALL))
        if GRAMMAR.TEST_OR([STREE],[GRAMMAR.TEST_BINARY])[0] == True:
            return tuple(("NUMBER",STREE))
        if GRAMMAR.TEST_OR([STREE],[GRAMMAR.TEST_IDENTIFIER])[0] == True:
            return tuple(("ID",STREE))
    


# prende TOKEN CONTROLLA LA SINTASSI IL CODICE SE E SCRITTO BENE
def ANALYSIS(self):
    print("-------------------------------- SYNTAX ----------------------------------------------")
    # DOVE SALVA I RISULTATI PER IL GENERATORE
    global ALL
    # RICEVE DAL LEXER I TOKEN
    
    IN = self.TUBO[0].recv()[2]
    print("[SYNTAX]:",IN)
    if IN != "\n" and IN != " ": 
        self.JOB += IN
        ALL.append(IN)
    print(f"[JOB|{self.JOB}]")
    CHECK = GRAMMAR.TEST_OR([self.JOB],[GRAMMAR.TEST_IDENTIFIER])
    if CHECK[0] == True:
        if len(CHECK[1])==1:
            self.LAST = CHECK[1][0]
        else:
            print("dentro")
    elif (self.JOB != "") & (self.LAST != ""):
        self.JOB = ""
        print("ST",self.LAST)
        self.LAST = ""
    else:
        print(CHECK[1])

    

    print(ALL)