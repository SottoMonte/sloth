import DATA

def OR(TARGET,TEST):
    bool_check = 0
    bool_name = []
    false_name = []
    for T in TARGET:
        for C in TEST:
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

class BOOLEAN(DATA.VARIABLE):
    def __init__(self, VALUE,PROPERTY=dict()):
        self.__VALUE = VALUE
        self.__TYPE = type(VALUE)
        self.__CARDINALITY = 1
        self.__PROPERTY = PROPERTY

    def AND(self,IN):
        print(IN[""], "evaluates to", eval(IN[""]))
        return eval(IN[""])
    def OR(self,IN):
        print(IN[""], "evaluates to", eval(IN[""]))
        return eval(IN[""])
    def NOT(self,IN):
        print(IN[""], "evaluates to", eval(IN[""]))
        return eval(IN[""])