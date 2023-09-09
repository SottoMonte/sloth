# --------------------------------------------------------------------------------------
#                               GRAMMAR
# --------------------------------------------------------------------------------------
TYPETOKEN = { "ID","OP","KEYWORD","STRING","INTEGER","NUMBER","NATURAL","DATA" }
PERMISSION_INTEGER_OP = { "=",":=","+=","-=","*=","/=","%=","^=","++","--" }

KEYWORD_SET = { "SET","TUPLE","LIST","DICT","NATURAL","INTEGER","RATIONAL","REAL","COMPLEX","STRING","BOOL","BYTE","SECURE","TRUE","FALSE","AND","OR" }

LOWER = { "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z" }
UPPER = { "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" } 
LETTER_SET = LOWER.union(UPPER)

CLOSURE = { "\"","(",")","<",">","[","]","{","}" }
SEPARATOR_SET = { ",","|","::",":",";"," ","\n","" }
OTHER = { ".","...","?"}


SYMBOL = { }

ARITHMETIC = { "+","-","*","/","%","++","--" }
ASSIGNMENT = { "=",":=","+=","-=","*=","/=","%=","^=" }
COMPARISON = { "==","!=",">","<",">=","<=" }
LOGICAL = { "&&","||","!" }

OPERATOR_SET = LOGICAL.union(ASSIGNMENT,ARITHMETIC,COMPARISON)



DIGIT = {"0","1","2","3","4","5","6","7","8","9"}

TYPETOKEN = { "ID","OP","KEYWORD","STRING","INTEGER","NUMBER","NATURAL","DATA" }

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# SINTASSI
PERMISSION_INTEGER_OP = { "=",":=","+=","-=","*=","/=","%=","^=","++","--" }

# --------------------------------------------------------------------------------------
#                                GENEREIC FUNC
# --------------------------------------------------------------------------------------


def OR(TARGET,CHECK):
    bool_check = 0
    bool_name = []
    false_name = []
    for T in TARGET:
        for C in CHECK:
            #print(T,C.__name__)
            if C(T)  == True:
                #print(C.__name__)
                bool_name.append(C.__name__)
                bool_check += 1
                continue
            else:
                false_name.append(C.__name__)
    #print(len(TARGET),bool_check)
    print(bool_name)
    if len(TARGET) <= bool_check:
        print("vero")
        return tuple((True,bool_name))
    else:
        #print("falso")
        return tuple((False,[]))

def SPLIT(TARGET,SEPARETOR,LOCK,UNLOCK):
    DIVIDED = []
    job = ""
    lock = False
    for T in TARGET:
        if T == LOCK:
            lock = True
        if T == UNLOCK:
            lock = False

        if (T == SEPARETOR) & (lock == False):
            DIVIDED.append(job)
            job = ""
        else:
            job += T
        print(job)
    if job != "": DIVIDED.append(job)
    return DIVIDED

def TEST_ARITHMETIC(X):
    if FOUND_ALL(X,arithmetic) == True:
        return tuple((True,["ARITHMETIC"]))
    else:
        return tuple((False,[]))

def TEST_EXPRESSION_ARITHMETIC(X):
    A = TEST_OR(X,[TEST_BINARY,TEST_ARITHMETIC])
    if A[0] == True:
        return tuple((True,A[1]))
    else:
        return tuple((False,[]))

def TEST_EXPRESSION_ARITHMETIC_AST(X):
    SPEED = {"+": 3,"-": 3,"/": 4,"*": 5,}
    S = 5
    TREE = []
    if TEST_EXPRESSION_ARITHMETIC(X)[0] == True:
        while S >= 0:
            for P in X:
                if P in SPEED:
                    PX = X.index(P)
                    print(P,X.index(P))
                    if SPEED[P] == S:
                        print(X,len(X),PX)
                        if len(X) != 3:
                            TREE.append((X[PX],X[PX-1],X[PX+1]))
                            X = X[:PX-1] + [(X[PX],X[PX-1],X[PX+1])] + X[PX+2:]
                        else:
                            TREE.append((X[1],X[0],X[2]))
                            #X = X[0] + [(X[PX],X[PX-1],X[PX+1])] + X[PX+2:]
                        
                        
                            
                        
            S -= 1
    else:
        print("ERRORE")
    return TREE[len(TREE)-1]

def TEST_CALCOLA(X):
    print("----------- CALCOLA -------------------")
    A = 0
    B = 0
    if type(X[1]) == type((1,2,3)):
        A = int(TEST_CALCOLA(X[1]))
        print(A)
    else:
        A=int(X[1])
        print(A)

    if type(X[2]) == type((1,2,3)):
        
        B = int(TEST_CALCOLA(X[2]))
        print(B)
    else:
        B=int(X[2])
        print(B)
    print("----------- CALCOLA ------------------- END")
    if X[0] == "*":
        return A * B
    if X[0] == "+":
        return A + B
    if X[0] == "-":
        return A - B
    if X[0] == "/":
        return A / B

class AST_TREE:
    def __init__(self,TYPE,ID,VALUE):
        self.TYPE = TYPE
        self.ID = ID
        self.VALUE = VALUE

def TEST_INSTRUCTION_DECLARATION(X,Y,Z): 
    if (PAIR_KEY_ID(X) & (":=" == Y) & (OR(Z,[BINARY,STRING,IDENTIFIER]))) == True:
        return AST_TREE(GET_PAIR(X)[0],GET_PAIR(X)[1],Z)
    else:
        return False
def TEST_INSTRUCTION_ASSIGNMENT(X,Y,Z): return (IDENTIFIER(X) & ("=" == Y) & (OR(Z,[BINARY,STRING,IDENTIFIER])))

def GET_SET(X):
    R = []
    IN = []
    for Z in X[1:len(X)-1]:
        if Z == ';':
            R = IN
            IN = []
            continue
        IN.append(Z)
    R += IN
    return R

def INSTRUCTION_DECLARATION(X):
    
    if TEST_INSTRUCTION_BLOCK_PAIR(X)  : return tuple((True,[]))
    else:return tuple((False,[]))

def SET_NEW(X):
    # X[0] X[END]
    if FOUND(X,"{",0) & FOUND(X,"}",len(X)-1) & (X.count("{") == X.count("}")):
        return TEST_OR(SPLIT(X[1:len(X)-1],';',"{","}"),[SET_NEW,TEST_BINARY])
    else:
        return tuple((False,[]))

def NOT(CHECK,VALUE,P):
    if len(CHECK) < P:
        if VALUE == CHECK[P]:
            return False
        else:
            return True
    return True

def FOUND(VALUE,CHECK,INDEX):
    try:
        if CHECK == VALUE[INDEX]:
            return True
        else:
            return False
    except IndexError:
        return False

def FOUND_ALL(VALUE,CHECK):
    for X in VALUE:
        for Y in CHECK:
            if X==Y: return True
    return False

def GET_PAIR(X): return X[1:len(X)-1].split(":")
def EQL(X,Y): return X == Y

def CHECK_KEY(key, list_of_dicts):
    try:
        for i in list_of_dicts.keys():
            if i == key : return True
        return False
    except Exception as e:
        print("KEYYYYYYYYYYYYYYYYYY")
        return False;

def CHANGE(word,char,new):
    for letter in word:
        if letter == char:
            word = word.replace(letter,new)
    return word

def DATA_GET(X): return OR([X],[NATURAL,STRING,PAIR,TUPLE])

# --------------------------------------------------------------------------------------
#                                ANALIZZATORE
# --------------------------------------------------------------------------------------

# NUMERI
def BINARY(X): return (X.isdigit())
def NATURAL(X): return (X.isdigit() & NOT(X,"0",0))
def INTEGER(X): return (NATURAL(X))
def NUMBER(X): return  (BINARY(X)|NATURAL(X))
def LETTER(X): return X.isalpha()

# INTERNI
def OPERATOR(X): return (FOUND_ALL([X],OPERATOR_SET))
def KEYWORD(X): return (FOUND_ALL([X],KEYWORD_SET))
def SEPARATOR(X): return (FOUND_ALL([X],SEPARATOR_SET))
def CLOSE(X): return (FOUND_ALL([X],CLOSURE))
## CICLO INFINITO CHIAMATE
def IDENTIFIER(X): return  (  (X[len(X)-2:] == "::") | X.isalpha() |  (OR(X.split("::"),[LETTER]))[0])

# CONTENITORI
def EXPRESSION(X): return ( True )
#STR "STRINGA"
def STRING(X): return ( FOUND(X,"\"",0) & (1 != len(X)) & FOUND(X,"\"",len(X)-1) )
#LIST [1,2,3]
# PAIR (1:1)
def PAIR(X): return (FOUND(X,"(",0) & (2 == len(X.split(":"))) & (AND(X[1:len(X)-1].split(":"),[BINARY,STRING,IDENTIFIER]))  & FOUND(X,")",len(X)-1) | (2 == len(X.split(":"))) & (AND(X.split(":"),[BINARY,STRING,IDENTIFIER])))
#TUPLE (1:2:3)
def TUPLE(X): return (FOUND(X,"(",0) & (AND(X[1:len(X)-1].split(","),[BINARY,STRING,IDENTIFIER]))  & FOUND(X,")",len(X)-1))
#SET { 1;2;3 }
def SET(X): return (FOUND(X,"{",0) & (AND(X[1:len(X)-1].split(";"),[BINARY,STRING,IDENTIFIER]))  & FOUND(X,"}",len(X)-1) & (X.count("{") == X.count("}")))
def TEST_SET(X): 
    if SET(X):return tuple((True,['SET']))
    else:return tuple((False,[]))
#DICT <"A":0;"B":1>
def DICT(X): return (NOT(X,"{",0) & AND(X.split(";"),[PAIR]) & NOT(X,"}",len(X)-1) | AND(X.split(";"),[PAIR]))

def DATA(X): return (NUMBER(X) | PAIR(X) | SET(X))

def PAIR_KEY_ID(X): return (FOUND(X,"(",0) & (2 == len(X.split(":"))) & (AND(X[1:len(X)-1].split(":"),[KEYWORD,IDENTIFIER]))  & FOUND(X,")",len(X)-1) | (2 == len(X.split(":"))) & (AND(X.split(":"),[KEYWORD,IDENTIFIER])))

# --------------------------------------------------------------------------------------
#                                SYNTAX
# --------------------------------------------------------------------------------------

def INSTRUCTION(X): return ""

def INSTRUCTION_BLOCK_SET(X): 
    return tuple((False,[]))
def INSTRUCTION_BLOCK_TUPLE(X): return ""
def INSTRUCTION_BLOCK_COUPLE(X): return ""
def INSTRUCTION_BLOCK_LIST(X): return ""
def INSTRUCTION_BLOCK_DICT(X): return ""
def INSTRUCTION_BLOCK(X): return ""

def INSTRUCTION_EXPRESSION_ARITHMETIC(X): return ""
def INSTRUCTION_EXPRESSION_BOOLEAN(X): return ""
def INSTRUCTION_EXPRESSION_CALL(X): return ""
def INSTRUCTION_EXPRESSION(X): return ""

# INT:ANNO OP:= DATA
def INSTRUCTION_DECLARATION(X,Y,Z): return (PAIR_KEY_ID(X) & (":=" == Y) & (OR(Z,[BINARY,STRING,IDENTIFIER])))
def INSTRUCTION_ASSIGNMENT(X,Y,Z): return (IDENTIFIER(X) & ("=" == Y) & (OR(Z,[BINARY,STRING,IDENTIFIER])))
def INSTRUCTION_CALL(X,Y,Z): return (IDENTIFIER(X) | IDENTIFIER(X) & IDENTIFIER(Y) & TUPLE(Z))
def INSTRUCTION_NAMESPACE(X): return ""
# --------------------------------------------------------------------------------------
#                                TEST
# --------------------------------------------------------------------------------------
TEST_ALL = {
    
}