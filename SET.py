import DATA
import OBJECT


def INFINITE(TARGET):
    if TARGET.VALUE == None:return False 
    else:return True
def FINITE(TARGET): 
    if TARGET.VALUE == None:return False 
    else:return True
def UNIQUE(TARGET,TEST):
    for VALUE in TARGET:
        for CHECK in TEST:
            if VALUE == CHECK:
                return False
    return True
def UNION(TARGET,VALUE):
    for keyX, valueX in VALUE.items():
            for keyY, valueY in TARGET.items():
                if keyX == keyY:
                    for X in valueX:
                        valueY.append(X)

#VARIABLE CONSTANT 
class VARIABLE(DATA.VARIABLE):
    def __init__(self, VALUE,PROPERTY=dict()):
        self.__TYPE = type(set())
        UNION_DICT = {
            'SET':[tuple(([set()],OBJECT.ARGS,None))],
            'UNION':[tuple(([set()],OBJECT.ARGS,None))],
            'INTERSECTION':[tuple(([set()],OBJECT.ARGS,None))],
            'DIFFERENCE':[tuple(([set()],OBJECT.ARGS,None))],
            'PRODUCT':[tuple(([set()],OBJECT.ARGS,None))],
        }
        for keyX, valueX in PROPERTY.items():
            for keyY, valueY in UNION_DICT.items():
                if keyX == keyY:
                    for X in valueX:
                        valueY.append(X)
        self._OBJECT__PROPERTY = UNION_DICT
        self.SET(VALUE)
        # OP ########################################
        self._OBJECT__OPERATORS['='] = self.SET
        self._OBJECT__OPERATORS['+='] = self.UNION
        self._OBJECT__OPERATORS['-='] = self.DIFFERENCE
        self._OBJECT__OPERATORS['%='] = self.INTERSECTION
        self._OBJECT__OPERATORS['*='] = self.PRODUCT

    def UNION(SET):
        self.__VALUE.union(SET)
    def INTERSECTION(SET):
        self.__VALUE.intersection(SET)
    def DIFFERENCE(SET):
        self.__VALUE.difference(SET)
    def PRODUCT(SET):
        self.__VALUE.difference(SET)

class CONSTANT(DATA.CONSTANT):
    def __init__(self, VALUE,PROPERTY=dict()):
        self.__TYPE = type(set())
        self.SET(VALUE)
        UNION_DICT = {
            'SET':[tuple(([set()],OBJECT.FORBIDDEN,None))],
        }
        for keyX, valueX in PROPERTY.items():
            for keyY, valueY in UNION_DICT.items():
                if keyX == keyY:
                    for X in valueX:
                        valueY.append(X)
        self._OBJECT__PROPERTY = UNION_DICT