
from multiprocessing import Process, Pipe
import os
import asyncio



class WORKER:
    STATE = True
    EVENTS = dict()
    def __init__(self,FUNC,ARGS,PIPE):
        self.CICLO = 1
        self.QUEUE = FUNC
        self.CICLO = ARGS
        self.TUBO = PIPE
        self.p = Process(target=self.RUN, args=(self,))
        
        #self.p.start()
        #self.p.join()
    # ESEGUE TUTTI I TASK
    def RUN(self,A):
        while self.STATE:
            #self.QUEUE(self)
            asyncio.run(self.QUEUE(self))
            #self.info(self.CICLO)

    def INFO(self):
        print('module name:', __name__)
        print('parent process:', os.getppid())
        print('process id:', os.getpid())
           
    async def FOREACH(self,VALUE,FUNC):
        for x in VALUE:
            task_2 = asyncio.create_task(FUNC(self,x))
            price = await task_2