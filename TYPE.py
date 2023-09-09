from enum import Enum

def EQUAL(TARGET,TEST):
    if (type(TARGET) == type(TEST)):
        return True
    else:
        return False

'''class TYPE(Enum):
    SET
    TUPLE
    LIST
    DICT
    SINGLETON
    MATRIX
    RECORD
    OBJECT
    VECTOR
    PAIR
    # NUMRI
    NATURAL
    INTEGER
    RATIONAL
    REAL
    COMPLEX
    # ALTRO
    STRING
    BOOLEAN
    PROPERTY
    BYTE
    SECURE
    def __init__(self, IDENTIFIER, TRAIT, PROPERTY, TYPE, VALUE, SIZE, EVENT):
        self.IDENTIFIER = IDENTIFIER
        self.TRAIT = TRAIT
        self.PROPERTY = PROPERTY
        self.TYPE = TYPE
        self.VALUE = VALUE
        self.SIZE = SIZE
        self.EVENT = EVENT

    @OBJECT._decorator
    def saluta(self):
        print("BYTE ")
        print(type(self))
        print(getsizeof(self))'''
