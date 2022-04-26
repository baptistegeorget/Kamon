from board import Board
from tkinter import *
import math
from math import *
from player import Player
import copy
from winScreen import WinScreen
 
class GameTurn:
    
    #------------------------------------   
    # Constructeur
    #------------------------------------  
    
    def __init__(self, canvas, canvasConfig, boardSize, rayon, listSymb, listColor, colorBoard, bgCase, backgroundImage, buttonBreak, buttonBreakConfig):
        # Le canvas
        self.__canvas = canvas
        self.__canvas.bind('<Button-1>', self.gameTurn)
        self.__backgroundImage = backgroundImage
        self.__canvasConfig = canvasConfig
        self.__pause = False
        self.__buttonBreak = buttonBreak
        self.__buttonBreakConfig = buttonBreakConfig
        
        # Objet 
        self.__bgCase = bgCase
        self.__rayon = rayon
        self.__borderdWidth = 5
        self.__board = Board(rayon, boardSize, canvasConfig[0], canvasConfig[1], listSymb, listColor)
        self.__dic = self.__board.getDic()
        self.__ring = self.__board.getRing()
        self.__height = self.__board.getHeight()
        self.__colorBoard = colorBoard
        self.__listColor = listColor
        
        # Dernier coups joué
        self.__lastHit = ()
        
        # Joueur actuel
        self.__player1 = Player(1).getPlayer()
        self.__player2 = Player(2).getPlayer()
        self.__playerActuel = self.__player1 
                
    #------------------------------------   
    # Met le jeu en pause
    #------------------------------------  
        
    def setPause(self, set):
        self.__pause = set
        
    #------------------------------------   
    # Affichage du plateau
    #------------------------------------  
    
    def displayBoard(self):
        self.__canvas.delete(ALL)
        self.__canvas.create_image(self.__canvasConfig[0], self.__canvasConfig[1], image = self.__backgroundImage, anchor = "center")
        for key in self.__dic:
            value = self.__dic[key]
            listCoordCorner = self.__board.generateCoordCorner(value[0][0], value[0][1], self.__rayon)
            listCoordCircle = self.__board.generateCoordCircle(value[0][0], value[0][1], self.__rayon*0.6)
            self.__canvas.create_polygon(listCoordCorner, fill=self.__bgCase, outline=self.__colorBoard, width=self.__borderdWidth)
            self.__canvas.create_oval(listCoordCircle, fill=value[1][1], width=0)
            self.__canvas.create_image(value[0][0], value[0][1], image=value[1][0])
            self.__canvas.create_polygon(listCoordCorner, fill="", outline="", width=self.__borderdWidth, activeoutline="yellow")
            if value[2] != 0:
                listCoordCorner = self.__board.generateCoordCorner(value[0][0], value[0][1], self.__rayon*0.9)
                listCoordCircle = self.__board.generateCoordCircle(value[0][0], value[0][1], self.__rayon*0.7)
                self.__canvas.create_polygon(listCoordCorner, fill="", outline=self.colorPlayer(value[2]), width=0.2*self.__rayon)
                self.__canvas.create_oval(listCoordCircle, fill="", outline=self.colorPlayer(value[2]), width=0.25*self.__rayon)
        self.__canvas.update()
    
    #------------------------------------   
    # Renvoie la couleur de pion des joueurs
    #------------------------------------ 
    
    def colorPlayer(self, value):
        if value == self.__player1[0]:
            return self.__player1[1]
        else:
            return self.__player2[1]
    
    #------------------------------------   
    # Tours de jeu
    #------------------------------------ 
        
    def gameTurn(self, event):
        key = self.where(event.x, event.y)
        if key != "no" and self.__pause != True:
            value = self.__dic[key]
            if self.startOrPossible(key, self.__ring):
                self.put(value)
                self.displayBoard()
                if (self.verifSide() or self.verifTrap() or self.verifAgainPlayer() == False):
                    self.__pause = True
                    winScreen = WinScreen(self.__canvas, self.__canvasConfig, self.__playerActuel[0], self.__backgroundImage, self.__buttonBreak, self.__buttonBreakConfig, "win")
                    winScreen.displayWinScreen()
                elif self.verifEgal():
                    self.__pause = True
                    winScreen = WinScreen(self.__canvas, self.__canvasConfig, self.__playerActuel[0], self.__backgroundImage, self.__buttonBreak, self.__buttonBreakConfig, "egal")
                    winScreen.displayWinScreen()
                self.changePlayer()
    
    #------------------------------------   
    # Premier coup ou possible
    #------------------------------------ 
    
    def startOrPossible(self, key, ring):
        if self.__lastHit == ():
            return self.possible(key) and (((key[0] == ring or key[0] == -ring) and (key[1] != ring or key[1] != -ring) and (key[2] != ring or key[2] != -ring)) ^ ((key[1] == ring or key[1] == -ring) and (key[2] != ring or key[2] != -ring) and (key[0] != ring or key[0] != -ring)) ^ ((key[2] == ring or key[2] == -ring) and (key[1] != ring or key[1] != -ring) and (key[0] != ring or key[0] != -ring)))
        else:
            return self.possible(key)
        
    #------------------------------------   
    # Possible ?
    #------------------------------------ 
    
    def possible(self, key):
        value = self.__dic[key]
        if value[1][1] != self.__listColor[0]:
            if value[2] == 0:
                if self.__lastHit == () or self.__lastHit[0] == value[1][0] or self.__lastHit[1] == value[1][1]:
                    return True
        return False
                
    #------------------------------------   
    # Quel hexagone ?
    #------------------------------------ 
                
    def where(self, x, y):
        for value in self.__dic.values():
            if math.sqrt((value[0][0] - x)*(value[0][0] - x) + (value[0][1] - y)*(value[0][1] - y)) < self.__height/2:
                key = self.getKey(value)
                return key
        return "no"
    
    #------------------------------------   
    # Trouve la clé avec sa valeur
    #------------------------------------ 
    
    def getKey(self, val):
        for key, value in self.__dic.items():
            if val == value:
                return key
     
    #------------------------------------   
    # Ajoute un pion et enregistre le coup
    #------------------------------------  
           
    def put(self, value):
        value[2] = self.__playerActuel[0]
        self.__lastHit = (value[1][0], value[1][1])
        
    #------------------------------------   
    # Changement de joueur
    #------------------------------------  
        
    def changePlayer(self):
        if self.__playerActuel == self.__player1:
            self.__playerActuel = self.__player2
        else:
            self.__playerActuel = self.__player1
            
    def keyDeplacement(self, axe, deplacement, cle):
        key = copy.deepcopy(cle)
        if axe == "q":
            key[0] = key[0]+deplacement
            key[1] = key[1]-deplacement
            return key
        if axe == "r":
            key[1] = key[1]+deplacement
            key[2] = key[2]-deplacement
            return key
        if axe == "s":
            key[2] = key[2]+deplacement
            key[0] = key[0]-deplacement
            return key
    
    #verifier si toute les cases sont jouées
    def verifEgal(self):
        for value in self.__dic.values():
            if value[1][1] != self.__listColor[0] and value[2] == 0:
                return False 
        return True
    
    #verifier si le joueur peut jouer
    def verifAgainPlayer(self):
        for value in self.__dic.values():
            if value[1][0] == self.__lastHit[0] or value[1][1] == self.__lastHit[1]:
                return True
        return False
    
    #verifier si les cases rejoignent deux bords
    def verifSide(self):
        side = False
        for key in self.__dic:
            if self.__dic[key][2] == self.__playerActuel[0] and (abs(key[0]) == self.__ring or abs(key[1]) == self.__ring or abs(key[2]) == self.__ring):
                listKey = []
                if self.voisinSide(list(key), listKey, list(key)) == True:
                    side = True
        return side
    
    def voisinSide(self, key, listKey, saveKey):
        if (key not in listKey) and (tuple(key) in self.__dic) and (self.__dic[tuple(key)][2] == self.__playerActuel[0]) and (abs(saveKey[0]) == self.__ring and saveKey[0] == -key[0]) or (abs(saveKey[1]) == self.__ring and saveKey[1] == -key[1]) or (abs(saveKey[2]) == self.__ring and saveKey[2] == -key[2]):
            return True
        listKey.append(key)
        dep1 = ["r", "q", "s", "r", "q", "s"]
        dep2 = [-1, 1, -1, 1, -1, 1]
        for i in range(6):                                       
            func = self.keyDeplacement(dep1[i], dep2[i], key)
            if (tuple(func) in self.__dic) and (func not in listKey) and (self.__dic[tuple(func)][2] == self.__playerActuel[0]):
                if self.voisinSide(func, listKey, saveKey) == True:
                    return True
        
    #verifier si les cases emprisonnent une case adverse
    def verifTrap(self):
        trap = False
        for key in self.__dic:
            if self.__dic[key][2] != self.__playerActuel[0] and (key[0] != abs(self.__ring) and key[1] != abs(self.__ring) and key[2] != abs(self.__ring)):
                listKey = []
                if self.voisinTrap(list(key), listKey) != False:
                    trap = True
        return trap
        
    def voisinTrap(self, key, listKey):
        listKey.append(key)
        dep1 = ["r", "q", "s", "r", "q", "s"]
        dep2 = [-1, 1, -1, 1, -1, 1]
        for i in range(6):
            func = self.keyDeplacement(dep1[i], dep2[i], key)
            if (tuple(func) in self.__dic) and (func not in listKey) and (self.__dic[tuple(func)][2] != self.__playerActuel[0]) and (func[0] == abs(self.__ring) or func[1] == abs(self.__ring) or func[2] == abs(self.__ring)):
                return False
            elif (tuple(func) in self.__dic) and (func not in listKey) and (self.__dic[tuple(func)][2] != self.__playerActuel[0]):
                if self.voisinTrap(func, listKey) == False:
                    return False