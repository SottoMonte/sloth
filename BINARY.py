from sys import getsizeof
#import numpy as np
import time
import inspect
from operator import eq
import CONSTANT

class BOUND:
    def __init__(self, VALUE, FN, ERROR):
        self.VALUE = VALUE
        self.FN = FN
        self.ERROR = ERROR

    def LOGIC(self,IN):
        print(IN[""], "evaluates to", eval(IN[""]))
        return eval(IN[""])

    def EQL(self,check):
        if (self.VALUE == check):
            return False
        else:
            return True

    def FORBIDDEN(self,check):
        return True

def ODD(self,check):
    if (self.VALUE % 2) == 0:
        return False
    else:
        return True

def EQL(self,check):
    if (self.VALUE == check):
        return False
    else:
        return True

def TYPE(self,check):
    print(type(self.ARGS["ARGS"][0]))
    print(type(check))
    if (self.TYPE == type(self.ARGS["ARGS"][0])):
        return False
    else:
        return True

def FORBIDDEN(self,check):
    return True

class BASE:
    VALUE = ""
    ARGS = []
    #BOUND = (1,2,3)
    CASE = ("",None)
    CONSTANT = BOUND(10, FORBIDDEN, "è una constante")

class WORKER(BOUND):
    STATE = False
    CICLO = 0
    def __init__(self):
        self.CICLO = 1
    
    def my_function(self):
        frame = inspect.currentframe()
        msg = 'We are on file {0.f_code.co_filename} and line {0.f_lineno}'.format(frame)
        current_state = frame.f_locals
        print(current_state)

    def FOREACH(self,VALUE,FUNC):
        for x in VALUE:
            FUNC(x)
        return False
    def MATCH(self,CHECK,*CASE:BASE.CASE):
        for x in CASE:
            if CHECK == x[0]:
                print(x)
                x[1](self)
                return 
    def SECURE(self,CHECK,SAFE,UNSAFE):
        #self.my_function()
        if(CHECK):
            print("SAFE")
            SAFE(self)
            return True
        else:
            print("UNSAFE")
            UNSAFE(self)
            return False
    

class OBJECT:
    ARGS = []
    WORKER = WORKER()
    def __init__(self, IDENTIFIER, TRAIT, PROPERTY, EVENT):
        self.IDENTIFIER = IDENTIFIER
        self.TRAIT = TRAIT
        self.EVENT = EVENT
    # TEST
    def CALLBOUND(self,NAME,ARGS):
        print(NAME)
        try:
            for i in self.TRAIT[NAME]:
                if(False != i.FN(self,i.VALUE)):
                    print("!OK")
                    print(i.ERROR)
                    exit(1)
                else:
                    print("OK")
        except KeyError as ke:
            print('Key Not Found in Employee Dictionary:', ke)

    def _callback_event(foo):
        def call(self,*ARGS):
            print("[")
            saved_args = locals()
            print("saved_args is", saved_args)
            self.ARGS = saved_args
            this_function_name = foo.__name__
            self.CALLBOUND("",saved_args)
            self.CALLBOUND(this_function_name,saved_args)
            foo(self,ARGS)
            
            self.CALLEVENT(this_function_name)
            print("]"+this_function_name)
        return call
    
    def CALLEVENT(self,NAME):
        try:
            for key in self.EVENT[NAME]:
                key(self)
        except KeyError as ke:
            print('Key Not Found in Employee Dictionary:', ke)

class MATTER(OBJECT):
    def __init__(self, TYPE, VALUE, SIZE):
        self.TYPE = TYPE
        self.VALUE = VALUE
        self.SIZE = SIZE
    @OBJECT._callback_event
    def SET(self,VALUE):
        self.VALUE = VALUE

class DATA(MATTER):
    def ECHO(self,ARGS):
        print(ARGS)
        print(f"{CONSTANT.bcolors.WARNING}Value:{self.VALUE}|Type:{self.TYPE}|{CONSTANT.bcolors.ENDC}")


def UNIQUE(self,check):
    for idx, item in enumerate(self.VALUE):
        for c in self.VALUE[idx+1:]:
            #print(c,item)
            if (c == item):
                return True
    return False

class SET(DATA):
    def __init__(self, IDENTIFIER, VALUE, TRAIT, EVENT):
        self.IDENTIFIER = IDENTIFIER
        self.TRAIT = TRAIT
        self.TYPE = type(VALUE)
        self.SIZE = len(VALUE)
        self.VALUE = VALUE
        self.EVENT = EVENT
        #self.SET(VALUE)
        self.CALLBOUND("",[])
    @OBJECT._callback_event
    def SET(self,VALUE):
        self.SIZE = len(self.VALUE)
        self.VALUE.append(VALUE)
    @OBJECT._callback_event
    def ADD(self,VALUE):
        self.SET(VALUE)
    @OBJECT._callback_event
    def SUB(self,VALUE):
        self.VALUE -= VALUE

def MAKE_SET(VALUE=[],TRAIT={"":[BOUND([], UNIQUE, "valore presente")]},EVENT={"":[]}):
    return SET("SSS",VALUE,TRAIT,EVENT)
