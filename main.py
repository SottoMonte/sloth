#import BINARY
#import STRING
import sys

import WORKER
import LEXICAL
import SYNTAX
import APP
import GRAMMAR
import BOOLEAN
import SECURE
import SET
import DATA
import TYPE
import STRING
import OBJECT
import asyncio

async def show_message(TXT):
    print(TXT)

async def SHOW(self,TXT):
    await asyncio.sleep(1)
    print(TXT)

async def SHOW2(self,TXT):
    await asyncio.sleep(2)
    print(TXT)


async def W2(self):
    message_task = asyncio.create_task(
    show_message("W2")
    )
    #await asyncio.sleep(4)
    await self.FOREACH('CIAO',SHOW)
    self.STATE = False
    self.INFO()
    return False

async def W1(self):
    message_task = asyncio.create_task(
    show_message("W1")
    )
    #await asyncio.sleep(4)
    await self.FOREACH('CIAO',SHOW2)
    self.INFO()
    self.STATE = False
    return False

if __name__ == "__main__":
    print(sys.path)
    print(sys.executable)
    parent_conn, child_conn = WORKER.Pipe()

    MAIN = APP.APP("COMPILATORE.COM",sys.argv)
    MAIN.ADD(W1,None,parent_conn)
    MAIN.ADD(W2,None,parent_conn)
    MAIN.RUN()
    
    #NOME = STRING.VARIABLE('1',{'SET':[(['1','2'],STRING.EQUAL,0)]})
    #NOME.ECHO()
    #NOMI = SET.VARIABLE({1,2,3})

    #INV = SET.CONSTANT({1,2,3,3,3})
    #INV.ECHO()
    #INV.SET({1})
    '''
    parent_conn, child_conn = WORKER.Pipe()
    parent_conn_2, child_conn_2 = WORKER.Pipe()
    TOPAZ = APP.APP("COMPILATORE.COLOSSO.IT",0,sys.argv)
    TOPAZ.ADD(LEXICAL.LEXER,None,parent_conn)
    #TOPAZ.ADD(SYNTAX.ANALYSIS,None,parent_conn)
    #TOPAZ.ADD(SYNTAX,None,[child_conn,parent_conn_2])
    #TOPAZ.ADD(GENERATOR,None,[child_conn_2])
    TOPAZ.RUN()'''