import DATA
import TYPE
import OBJECT

def SIZE(TARGET,TEST):
    if (len(self.VALUE) <= check):
        return False
    else:
        return True

def EQUAL(TARGET,TEST):
    for CHECK in TEST:
        print(TARGET,CHECK)
        if (TARGET == CHECK):return True
    return False

def CHAR(TARGET,TEST):
    for CHECK in TEST:
        for VALUE in TARGET:
            print(VALUE,CHECK)
            if (VALUE == CHECK):return True
    return False

def BOUND_CHARACTER(TARGET,TEST):
    for item in self.VALUE:
        for c in check.VALUE:
            if (c == item):
                return True
    return False

def FOUND_CHARACTER(TARGET,TEST):
    if B == A[P]:
        return False
    else:
        return True

class VARIABLE(DATA.VARIABLE):
    def __init__(self,VALUE,PROPERTY=dict()):
        # INIT ######################################
        self.__TYPE = type("")
        #tuple(('',TYPE.EQUAL))
        UNION_DICT = {'SET':[tuple(([''],OBJECT.ARGS,None))]}
        for keyX, valueX in PROPERTY.items():
            for keyY, valueY in UNION_DICT.items():
                if keyX == keyY:
                    for X in valueX:
                        valueY.append(X)
        self._OBJECT__PROPERTY = UNION_DICT
        self.SET(VALUE)
        # OP ########################################
        self._OBJECT__OPERATORS['='] = self.SET
        self._OBJECT__OPERATORS['=='] = self.EQUAL
        self._OBJECT__OPERATORS['>'] = self.GREATER
        self._OBJECT__OPERATORS['>='] = self.GREATER_EQUAL
        self._OBJECT__OPERATORS['<'] = self.LESS
        self._OBJECT__OPERATORS['<='] = self.LESS_EQUAL
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def SET(self,VALUE):
        self.__VALUE = VALUE
        self.__CARDINALITY = len(VALUE)
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def ADD(self,VALUE):
        self.__VALUE += VALUE
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def SUB(self,VALUE):
        self.__VALUE -= VALUE
    # VALUE,DIVISORE
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def SPLITT(self,VALUE,DIVISORE):
        self.__VALUE -= VALUE
        
class CONSTANT(DATA.CONSTANT):
    def __init__(self,VALUE,PROPERTY=dict()):
        # INIT ######################################
        self.__TYPE = type("")
        self.SET(VALUE)
        #tuple(('',TYPE.EQUAL))
        UNION_DICT = {'SET':[tuple(([''],OBJECT.ARGS,None))]}
        for keyX, valueX in PROPERTY.items():
            for keyY, valueY in UNION_DICT.items():
                if keyX == keyY:
                    for X in valueX:
                        valueY.append(X)
        self._OBJECT__PROPERTY = UNION_DICT