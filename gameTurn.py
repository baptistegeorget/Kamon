from board import Board
from tkinter import *
import math
from math import *
from player import Player
 
class GameTurn:
    
    #------------------------------------   
    # Constructeur
    #------------------------------------  
    
    def __init__(self, canvas, canvasConfig, boardSize, rayon, listSymb, listColor, colorBoard, bgCase, backgroundImage):
        
        # Le canvas
        self.__canvas = canvas
        self.__canvas.bind('<Button-1>', self.gameTurn)
        self.__backgroundImage = backgroundImage
        self.__canvasConfig = canvasConfig
        self.__pause = False
        
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
        
    def setPause(self):
        if self.__pause == True:
            self.__pause = False
        else:
            self.__pause = True
        
    #------------------------------------   
    # Affichage du plateau
    #------------------------------------  
    
    def displayBoard(self):
        self.__canvas.delete(ALL)
        self.__canvas.create_image(self.__canvasConfig[0], self.__canvasConfig[1], image = self.__backgroundImage, anchor = "center")
        for value in self.__dic.values():
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
                self.changePlayer()
                print(self.__dic)
    
    #------------------------------------   
    # Premier coup ou possible
    #------------------------------------ 
    
    def startOrPossible(self, key, ring):
        if self.__lastHit == ():
            return self.possible(key) and (((key[0] == ring or key[0] == -ring) and (key[1] != ring or key[1] != -ring) and (key[2] != ring or key[2] != -ring)) ^ ((key[1] == ring or key[1] == -ring) and (key[2] != ring or key[2] != -ring) and (key[0] != ring or key[0] != -ring)) ^ ((key[2] == ring or key[2] == -ring) and (key[1] != ring or key[1] != -ring) and (key[0] != ring or key[0] != -ring)))
        if self.__lastHit != ():
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