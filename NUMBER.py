from sys import getsizeof
#import numpy as np
import time
import inspect
from operator import eq


class NUMBER(MATTER):
    def ADD(self,VALUE):
        print("NON DEFINITA")
    def SUB(self,VALUE):
        print("NON DEFINITA")
    def MUL(self,VALUE):
        print("NON DEFINITA")
    def DIV(self,VALUE):
        print("NON DEFINITA")
    def EXP(self,VALUE):
        print("NON DEFINITA")

    def ODD(self,check):
        if (self.VALUE % 2) == 0:
            return False
        else:
            return True
