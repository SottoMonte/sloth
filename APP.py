import WORKER
import OBJECT
import STRING

import flet as flt

def GUI(page: flt.Page):
    page.theme_mode = flt.ThemeMode.LIGHT
    page.window_height = 1500
    page.window_width = 1000

    NOME = STRING.STRING("NOME", "######", {"SET":[],"":[(["CAZZO","HITLET"], STRING.BOUND_EQL, "questa stringa non è permessa"),(9, STRING.BOUND_SIZE, "size superato")]}, {"SET":[]})

    def textbox_changed(e):
        #text.value = e.control.value
        print(type(text.value))
        NOME.SET(text.value)
        page.update()

    text = flt.TextField(
        label="Introductory Text",
        value="This App is made using Flet",
        on_change=textbox_changed
    )
  
    page.add(text)
  
    page.title = 'GeeksApp using Flet'
  
    page.update()

INTERFACE = {'API':'API','CLI':'CLI','GUI':'GUI'}
PLATFORM = {'WEB':'WEB','NATIVE':'NATIVE'}
TARGET = {'MOBILE':'MOBILE','BROWSER':'BROWSER','DESKTOP':'DESKTOP','SERVER':'SERVER'}
TYPE = {'INTERPRETED':'INTERPRETED', 'COMPILED':'COMPILED', 'HYBRID':'HYBRID'}
LANGUAGES = {'PHP','PYTHON','RUST','SQL','C','JAVASCRIPT','GO'}
FRAMEWORK = {'FLUTTER','GTK4','LARAVEL','PANDA'}

# WEB PHP
# API PY
# 

class APP(OBJECT.OBJECT):
    WORKERS = []
    ARGS = []
    IDENTIFIER = ""
    def __init__(self, IDENTIFIER,INTERFACE=INTERFACE['CLI'],PLATFORM=PLATFORM['NATIVE'],TARGET=TARGET['DESKTOP'],TYPE=TYPE['INTERPRETED'],ARGS=[]):
        self.IDENTIFIER = IDENTIFIER
        self.INTERFACE = INTERFACE
        self.PLATFORM = PLATFORM
        self.TARGET = TARGET
        self.TYPE = TYPE
        self.ARGS = ARGS

    def ADD(self,FUNC,ARGS,CHANNEL):
        self.WORKERS.append(WORKER.WORKER(FUNC,ARGS,CHANNEL))

    def RUN(self):
        for i in self.WORKERS:
            i.p.start()
        for i in self.WORKERS:
            i.p.join()
        if self.INTERFACE == 1:
            flt.app(target=GUI)