import fileinput
import GRAMMAR
import time

#LEXICAL
def  LEXER(WORKER):
    SOURCE = open('sorgente.go', 'r').read()
    def TOKENIZER(self,VALUE):
        print("+++++++>|JOB|",self.JOB,"|V|",VALUE)
        if GRAMMAR.OR([self.JOB + VALUE],[GRAMMAR.IDENTIFIER,GRAMMAR.NUMBER,GRAMMAR.CLOSE,GRAMMAR.SEPARATOR,GRAMMAR.OPERATOR])[0] == True:
            self.JOB += VALUE
            self.CONSUME()
            self.COL += 1
        elif GRAMMAR.OR([self.JOB + VALUE + self.PEEK()],[GRAMMAR.IDENTIFIER,GRAMMAR.NUMBER,GRAMMAR.CLOSE,GRAMMAR.SEPARATOR,GRAMMAR.OPERATOR])[0] == True:
            print(self.JOB + VALUE + self.PEEK())
            self.JOB += VALUE
            self.CONSUME()
        
        else:
            #print("-->",self.JOB)
            print("TOKEN",self.JOB)
            self.JOB = VALUE
            self.CONSUME()
        if (VALUE == "\n"):
                self.LINE += 1
                self.COL = 1
                print("----------------------------------------------- LINE ",self.LINE)
        time.sleep(1)
    WORKER.READER(SOURCE,TOKENIZER)
    

    self.STATE = False