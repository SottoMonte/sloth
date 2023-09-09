import OBJECT
import TYPE
import NATIVE
# ------------------------------------------------------------------------------
#   Un dato è caratterizzato da 3 proprietà fondamentali: tipo, cardinalità e valore.
# ------------------------------------------------------------------------------
def HOMOGENEOUS(TARGET): return (X.isdigit())
def HETEROGENEOUS(TARGET): return (X.isdigit())

def EQUAL(TARGET,TEST):
    if (TARGET == TEST):
        return True
    else:
        return False
def GREATER(TARGET,TEST):
    if (TARGET > TEST):
        return False
    else:
        return True
def GREATER_EQUAL(TARGET,TEST):
    if (TARGET >= TEST):
        return False
    else:
        return True
def LESS(TARGET,TEST):
    if (TARGET < TEST):
        return False
    else:
        return True
def LESS_EQUAL(TARGET,TEST):
    if (TARGET <= TEST):
        return False
    else:
        return True   
# ########################################################## OBJECT ###########################################################
class VARIABLE(OBJECT.OBJECT):
    __TYPE = None
    __VALUE = None
    __CARDINALITY = None
    def __init__(self, TYPE, VALUE, CARDINALITY):
        self.__TYPE = type(VALUE)
        self.__VALUE = VALUE
        self.__CARDINALITY = CARDINALITY
        # OP ########################################
        self.__OPERATORS['='] = self.SET
        self.__OPERATORS['=='] = self.EQUAL
        self.__OPERATORS['>'] = self.GREATER
        self.__OPERATORS['>='] = self.GREATER_EQUAL
        self.__OPERATORS['<'] = self.LESS
        self.__OPERATORS['<='] = self.LESS_EQUAL
    # ########################################################## METHOD ###########################################################
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def ECHO(self):
        print(f"{NATIVE.COLORS.WARNING}Value:{self.__VALUE}|Type:{self.__TYPE}|{NATIVE.COLORS.ENDC}")
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def CARD(self):
        return 0
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def SET(self,VALUE):
        self.__VALUE = VALUE
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def GET(self):
        return self.VALUE
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def EQUAL(self,check):
        if (self.__VALUE == check):
            return True
        else:
            return False
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def GREATER(self,check):
        if (self.__VALUE > check):
            return False
        else:
            return True
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def GREATER_EQUAL(self,check):
        if (self.__VALUE >= check):
            return False
        else:
            return True
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def LESS(self,check):
        if (self.__VALUE < check):
            return False
        else:
            return True
    @OBJECT.OBJECT._OBJECT__CALL_METHOD
    def LESS_EQUAL(self,check):
        if (self.__VALUE <= check):
            return False
        else:
            return True

class CONSTANT(VARIABLE):
    __TYPE = None
    __VALUE = None
    __CARDINALITY = None
    _OBJECT__PROPERTY = {'SET':[tuple(([set()],OBJECT.FORBIDDEN,None))]}
    def __init__(self, TYPE, VALUE, CARDINALITY):
        self.__TYPE = type(VALUE)
        self.__VALUE = VALUE
        self.__CARDINALITY = CARDINALITY