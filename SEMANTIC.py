# --------------------------------------------------------------------------------------
#                                GENERATOR
# --------------------------------------------------------------------------------------


def OP_ASSIGNMENT_NEW(a):
    return f"{a.ID} = int({a.VALUE})\n"
def OP_ASSIGNMENT_NEW_INTEGER(a):
    return f"{a.ID} = int({a.VALUE})\n"
def OP_ASSIGNMENT_NEW_NATURAL(a):
    return f"{a.ID} = int({a.VALUE})\n"
def OP_ASSIGNMENT_NEW_STRING(a):
    return f"{a.ID} = {a.VALUE}\n"
def OP_ASSIGNMENT_NEW_PAIR(a):
    B = CHANGE(a.VALUE,":",",")
    return f"{a.ID} = tuple({B})\n"
def OP_ASSIGNMENT_NEW_TUPLE(a):
    B = CHANGE(a.VALUE,",",",")
    return f"{a.ID} = tuple({B})\n"
def OP_ASSIGNMENT_EQUAL(a):
    return f"{a.ID} = int({a.VALUE})\n"
def OP_ASSIGNMENT_INCREASE(a):
    return f"{a.ID}++"
def OP_ASSIGNMENT_DECREASE(a):
    return f"{a.ID}--"

def OP_CALL_METHOD(a):
    
    B = a.ID.replace("::",".")
    return f"{B}{a.VALUE}\n"
# ID + OP + ID|NUMBER|DATA
def GRAMMAR_ASSIGNMENT(a):
    return f"{a.ID} = int({a.VALUE})"
# ID... + OP + ID|DATA  | ID... + OP + ID|DATA...
def GRAMMAR_ASSIGNMENT_MULTI(a):
    return f"{a.ID} = int({a.VALUE})"

# PRENDE AST come parametro 
def GENERATOR(self):

    global ALL_VAR

    IN = ""
    IN = self.TUBO[0].recv()
    print(IN)
    if IN != None:
        TT = IN
        code = ""
        
        
        f = open("CODE.py", "a+")

        if "INSTRUCTION_DECLARATION" == TT.INSTUC:
            print("INSTRUCTION_DECLARATION - START")
            if TT.VALUE in ALL_VAR.keys():
                TT.VALUE = ALL_VAR[TT.VALUE].VALUE
            else:
                print("variabile non esiste:",TT.VALUE)

            print(ALL_VAR)

            if GRAMMAR.EQL(TT.TYPE,GRAMMAR.NEW_DATA(TT.VALUE)[0]):
                if "STRING" == TT.TYPE:
                    code = GRAMMAR.OP_ASSIGNMENT_NEW_STRING(TT)
                elif "NATURAL" == TT.TYPE:
                    code = GRAMMAR.OP_ASSIGNMENT_NEW_NATURAL(TT)
                elif "PAIR" == TT.TYPE:
                    code = GRAMMAR.OP_ASSIGNMENT_NEW_PAIR(TT)
                elif "TUPLE" == TT.TYPE:
                    code = GRAMMAR.OP_ASSIGNMENT_NEW_TUPLE(TT)
                ALL_VAR[TT.ID] = TT
            else:
                print("ERRORE TYPE",TT.TYPE,"!=",GRAMMAR.NEW_DATA(TT.VALUE)[0])
                
        if "INSTRUCTION_ASSIGNMENT" == TT.INSTUC: 
            if TT.VALUE in ALL_VAR.keys():
                TT.VALUE = ALL_VAR[TT.VALUE].VALUE
            else:
                print("||||||||||||||||||||||||| ERRORE VARIABILE NON ESISTE")
            print(ALL_VAR)
            print("---------->>",ALL_VAR[TT.ID].TYPE,GRAMMAR.NEW_DATA(TT.VALUE)[0])
            if GRAMMAR.EQL(ALL_VAR[TT.ID].TYPE,GRAMMAR.NEW_DATA(TT.VALUE)[0]):
                if "STRING" == ALL_VAR[TT.ID].TYPE:
                    code = GRAMMAR.OP_ASSIGNMENT_NEW_STRING(TT)
                elif "NATURAL" == ALL_VAR[TT.ID].TYPE:
                    code = GRAMMAR.OP_ASSIGNMENT_NEW_NATURAL(TT)
                elif "PAIR" == ALL_VAR[TT.ID].TYPE:
                    code = GRAMMAR.OP_ASSIGNMENT_NEW_PAIR(TT)
                elif "TUPLE" == ALL_VAR[TT.ID].TYPE:
                    code = GRAMMAR.OP_ASSIGNMENT_NEW_TUPLE(TT)
                ALL_VAR[TT.ID].VALUE = TT.VALUE
            else:
                print("ERRORE TYPE",TT.TYPE,"!=",GRAMMAR.NEW_DATA(TT.VALUE)[0])
        
        if "INSTRUCTION_CALL" == TT.INSTUC:
            print(TT.VALUE,TT.ID)
            code = GRAMMAR.OP_CALL_METHOD(TT)
                
        
        
        f.write(code)
        f.close()
        #CC.remove(TT)
    #print(TYPETOKEN[1])