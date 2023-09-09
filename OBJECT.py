from sys import getsizeof
#import numpy as np
import time
import inspect
from operator import eq

def OR(TARGET,TEST):
    bool_check = 0
    bool_name = []
    false_name = []
    for T in TARGET:
        for C in TEST:
            #print(T,C.__name__)
            if C(T[0],T[1])  == True:
                #print(C.__name__)
                bool_name.append(C.__name__)
                bool_check += 1
                
            else:
                false_name.append(C.__name__)
    #print(len(TARGET),bool_check)
    print(bool_name)
    if len(TARGET) <= bool_check:
        print("vero")
        return tuple((True,bool_name))
    else:
        #print("falso")
        return tuple((False,false_name))

def ARGS(TARGET,TEST):
    #print(self["ARGS"])
    #print(check)
    #print(len(TARGET["ARGS"]),TARGET["ARGS"])
    for idx in range(len(TARGET)):
        print(type(TARGET[idx]),type(TEST[idx]))
        if (type(TARGET[idx]) != type(TEST[idx])):return False
    return True

def FORBIDDEN(TARGET,TEST):
    return False
# ########################################################## METHOD ###########################################################
class OBJECT:
    __OPERATORS = dict()
    __PROPERTY = dict()
    def __CALLBOUND(self,NAME,ARGS):
        if NAME in self.__PROPERTY:
            for ITEMS in self.__PROPERTY[NAME]:
                if ITEMS[2] == None:
                    CHECK = OR([tuple((ARGS,ITEMS[0]))],[ITEMS[1]])
                else:
                    CHECK = OR([tuple((ARGS[ITEMS[2]],ITEMS[0]))],[ITEMS[1]])
                
                if CHECK[0] == True:
                    print("vero")
                else:
                    print(CHECK,"ERRORE non",ARGS,ITEMS[0])
                    exit(1)
        #print("------->DETRO",NAME,self.__PROPERTY)
    def __CALLEVENT(self,NAME):
        '''try:
            for key in self.EVENT[NAME]:
                key(self)
        except KeyError as ke:
            print('Key Not Found in Employee Dictionary:', ke)'''
    def __SIGNAL(self):
        return ""
    def __CALL_METHOD(foo):
        def call(self,*ARGS):
            print("##### STARTED ############################################################  ",foo.__name__,"  ###########################################################")
            saved_args = locals()
            print("[0|ARGS:", saved_args,"]")
            self.ARGS = saved_args
            this_function_name = foo.__name__
            self.__CALLBOUND(this_function_name,ARGS)
            foo(self,*ARGS)
            print("##### FINISHED ###########################################################  ",foo.__name__,"  ###########################################################")
        return call