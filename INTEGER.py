import BINARY


class INTEGER(BINARY.DATA):
    def __init__(self, IDENTIFIER, TRAIT:BINARY.BOUND, PROPERTY, TYPE, VALUE, SIZE, EVENT):
        self.IDENTIFIER = IDENTIFIER
        self.TRAIT = TRAIT
        self.PROPERTY = PROPERTY
        self.TYPE = TYPE
        self.VALUE = VALUE
        self.SIZE = SIZE
        self.EVENT = EVENT
        self.CALLBOUND("",[])
    @BINARY.OBJECT._callback_event
    def ADD(self,VALUE):
        self.VALUE += VALUE
    @BINARY.OBJECT._callback_event
    def SUB(self,VALUE):
        self.VALUE -= VALUE
        
