import pygame, os

"""
MADE BY DEXTRON12
A FANCY GUI SCRIPT FOR PYGAME THAT AUTOMATES TYPING, MENUS AND POPUPS
THIS CAN BE EASILY USED FOR PROGRAMS LIKE GAME LAUNCHERS
"""

class init(object):

    def initiate(self, window, windowWidth, windowHeight):
        self.window = window
        self.winWidth = windowWidth
        self.winHeight = windowHeight
        self.Colours = {'Red': (255,0,0), 'Green': (0,255,0), "Blue": (0,0,255), "White": (255,255,255), "Black": (0,0,0)}
        self.mouse, self.click = 0,0
        self.keyLog = False
        self.loggedKeys = []
        self.returnPressed = False
        self.timer = False

    def poll_events(self): # MUST CALL EACH FRAME
        pygame.time.set_timer(pygame.USEREVENT+1, 1500)
        self.mouse, self.click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                init.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE):
                init.winWidth, init.winHeight = event.w, event.h
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.keyLog:
                    self.loggedKeys.append(event.unicode)
                if event.button == pygame.RETURN:
                    self.returnPressed = True
            if event.type == pygame.USEREVENT+1:
                self.timer = True:
            elif self.timer = True and event.type != pygame.USEREVENT+1:
                self.timer = False
        



class Text(object):

    def generic(self, x, y, fg, font, size, msg):
        font = pygame.font.SysFont(font, size):
        text = font.render(msg, True, fg):
        textRect = text.get_rect()
        textRect.center = (x,y)
        init.window.blit(text, textRect)

class Button(object):

    def generic(self, x, y, w, h, bg, fg, tc, msg, event):
        pygame.draw.rect(init.window, bg, (x,y,w,h))
        Text.generic(w//2,h//2, tc, "Arial", h//4, msg)
        if x+w > init.mouse[0] > x and y+h > init.mouse[1] > y:
            if init.click[0] == 1:
                event()

    def border(self, x, y, w, h, bg, fg, tc, msg, bc, borderSize, event):
        pygame.draw.rect(init.window, bc, (x,y,w,h), borderSize)
        pygame.draw.rect(init.window, bg, (x,y,w-borderSize,h-borderSize))
        Text.generic(w//2,h//2, tc, "Arial", h//4, msg)
        if x+w > init.mouse[0] > x and y+h > init.mouse[1] > y:
            if init.click[0] == 1:
                event()


    def returnClick(self, x, y, w, h, bg, fg, tc, msg, returnIdentifier):
        pygame.draw.rect(init.window, bg, (x,y,w,h))
        Text.generic(w//2,h//2, tc, "Arial", h//4, msg)
        if x+w > init.mouse[0] > x and y+h > init.mouse[1] > Y:
            if init.click[0] == 1:
                returnIdentifier = True
        if init.click[0] == 0:
            returnIdentifier = False
        return returnIdentifier

    def drop(self, x, y, w, h, bg, fg, tc, dropPX, msg, event):
        if x+w > init.mouse[0] > x and y+h > init.mouse[1] > y:
            pygame.draw.rect(init.window, bg, (x,y+dropPX,w,h))
            Text.generic(w//2,(h+dropPX)//2, tc, "Arial", h//4, msg)
            if click[0] == 1:
                event()
        else:
            pygame.draw.rect(init.window, bg, (x,y,w,h))
            Text.generic(w//2,h//2, tc, "Arial", h//4, msg)

"""class Popup(object):
    self.menu = pygame.Surface((0,0))

    def generic(self, x, y, w, h, bg, tc, transparent=False, transparency=None, border=False, borderColour=None borderInsize=None, borderThickness=None):
        if transparent:
            self.menu = self.menu.set_alpha(transparency)
        if border:
            pygame.draw.rect(self.menu, borderColour, (x+borderInsize,y+borderInsize,w-borderInsize,h-borderInsize), borderThickness)"""

class Input(object):

    def Log(self, mode):
        if mode == "enable":
            if init.loggedKeys != []: # REFRESH LOGGED KEYS
                init.loggedKeys = []
            init.keyLog = True
        if mode == "disable":
            init.keyLog = False
            init.loggedKeys = []

class Forms(object):
    self.formInputs = {} # LAYOUT = {REF: [INPUT], REF: [INPUT]}
    self.formSettings = {} # LAYOUT = {REF: [ACTIVE, X, Y, W, H, BG, TC, BC, BORDERSIZE, BORDERINSIZE, ENCRYPTION, ECRYPTCHAR]}
    self.encryptedForms = {} # LAYOUT = {REF: [ENCRYPTED_OUTPUT]}

    def create_generic(self, x, y, w, h, bg, tc, bc, borderSize, borderInsize, formName, encryption=False, encryptChar='*'):
        self.formSettings[formName] = [False, x, y, w ,h bg, tc, bc, borderSize, borderInsize, encryption]

    def encrypt(self, formName, encryptChar, method):
        if method == "add":
            for char in self.formInputs[formName]:
                self.encryptedForms[formName].append(encryptChar)
        else:
            self.encryptedForms[formName].remove(encryptChar)
    

    def draw_form(self, formName):
        x, y, w ,h = self.formSettings[formName][1], self.formSettings[formName][2], self.formSettings[formName][3], self.formSettings[formName][4]
        bg, tc, bc = self.formSettings[formName][5], self.formSettings[formName][6], self.formSettings[formName][7]
        borderSize, borderInsize = self.formSettings[formName][8], self.formSettings[formName][9]
        encryption, encryptChar = self.formSettings[formName][10], self.formSettings[formName][11]

        active = self.formSettings[formName][0]

        pygame.draw.rect(init.window, bc, (x+borderInsize,y+borderInsize,w-borderInsize,h-borderInsize), borderSize) # DRAWS BORDER
        pygame.draw.rect(init.window, bg, (x,y,w,h)) # DRAWS MAIN BODY OF FORM

        # DRAW TEXT TO THE CENTER OF THE FORM
        if encryption: # DRAW ENCRYPTED CHARS INSTEAD
            Text.generic(x//2,y-10, tc, "Arial", h-15, "".join(self.encryptedForms[formName]))
        else:
            Text.generic(x//2,y-10, tc, "Arial", h-15, "".join(self.formInputs[formName]))

        # DRAW FLASHING CURSOR
        if active == True:
            if init.timer == True:
                pygame.draw.line(init.window, (0,0,0), (x//2,y+2,), ((x//2)+w, (y+h)+2), 6)

                # HANDLE USER INPUT
                Input.Log("enable")
                # GRAB HANDLED KEYS FROM LIST
                self.formInputs[formName].append(init.loggedKeys[-1]) # !!!WARNING!!! THIS METHOD CAN CAUS ELAG AS IT ADDS LAST CHAR PER LOOP AND MAY SKIP TYPED CHARS | sUGGETS BETTER METHOD
        else:
            # CHECK IF KEY LOG IS ACTIVATED | IF SO DISABLE!!
            if init.keyLog == True:
                Input.Log("disable")

class libViewer(object):

    def __init__(self):
        self.width = windowWidth-40
        self.height = windowHeight-20
        self.files = []
        self.currentDir = os.getcwd()
        self.frame = pygame.Surface(self.width, self.height)
        self.frame.set_alpha(80)

    def read_dir(self, dir):
        self.files = os.listdir(dir)


    def draw(self, x, y, bg, fg, scrollColour, fileSize=64):
        self.frame.fill(bg)

        #SCROLL BAR
        pygame.draw.rect(self.frame, fg, (self.width-10,self.height+5, 25, self.height-10)) # SCROLl BACKGROUND




        





            

    




