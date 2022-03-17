from board import Board
from tkinter import *
import math
from math import *
 
class GameTurn:
    
    #------------------------------------   
    # Constructeur
    #------------------------------------  
    
    def __init__(self, canvas, canvasConfig, boardSize, rayon, listSymb, listColor, colorBoard, colorPlayer1, colorPlayer2, bgCase):
        
        # Le canvas
        self.__canvasBoard = canvas
        self.__canvasBoard.bind('<Button-1>', self.gameTurn)
        
        # Objet board
        self.__bgCase = bgCase
        self.__rayon = rayon
        self.__borderdWidth = 5
        self.__board = Board(rayon, boardSize, canvasConfig[0], canvasConfig[1], listSymb, listColor)
        self.__dic = self.__board.getDic()
        self.__ring = self.__board.getRing()
        self.__colorBoard = colorBoard
        
        # Dernier coups joué
        self.__lastHit = ()
        
        # Joueur actuel
        self.__player1 = 1
        self.__player2 = 2
        self.__colorPlayer1 = colorPlayer1
        self.__colorPlayer2 = colorPlayer2
        self.__player = self.__player1
        self.__colorPlayer = self.__colorPlayer1
        
    #------------------------------------   
    # Affichage du plateau
    #------------------------------------  
    
    def displayBoard(self):
        self.__canvasBoard.delete(ALL)
        for value in self.__dic.values():
            listCoordCorner = self.__board.generateCoordCorner(value[0][0], value[0][1], self.__rayon)
            listCoordCircle = self.__board.generateCoordCircle(value[0][0], value[0][1], self.__rayon)
            self.__canvasBoard.create_polygon(listCoordCorner, fill=self.__bgCase, outline=self.__colorBoard, width=self.__borderdWidth)
            self.__canvasBoard.create_oval(listCoordCircle, fill=value[1][1], width=0)
            self.__canvasBoard.create_image(value[0][0], value[0][1], image=value[1][0])
            self.__canvasBoard.create_polygon(listCoordCorner, fill="", outline=self.__colorBoard, width=self.__borderdWidth, activeoutline="yellow")
        self.__canvasBoard.update()
    
    #------------------------------------   
    # Tours de jeu
    #------------------------------------ 
        
    def gameTurn(self, event):
        key = self.where(event.x, event.y)
        if key != "no":
            value = self.__dic[key]
            if self.startOrPossible(key, self.__ring):
                self.put(value)
                self.changePlayer()
    
    #------------------------------------   
    # Premier coup ou possible
    #------------------------------------ 
    
    def startOrPossible(self, key, ring):
        if self.__lastHit == ():
            return ((key[0] == ring or key[0] == -ring) and (key[1] != ring or key[1] != -ring) and (key[2] != ring or key[2] != -ring)) ^ ((key[1] == ring or key[1] == -ring) and (key[2] != ring or key[2] != -ring) and (key[0] != ring or key[0] != -ring)) ^ ((key[2] == ring or key[2] == -ring) and (key[1] != ring or key[1] != -ring) and (key[0] != ring or key[0] != -ring))
        if self.__lastHit != ():
            return self.possible(key)
        
    #------------------------------------   
    # Possible ?
    #------------------------------------ 
    
    def possible(self, key):
        value = self.__dic[key]
        if value[1][0] != "":
            if value[2] == "vide":
                if self.__lastHit == () or self.__lastHit[0] == value[1][0] or self.__lastHit[1] == value[1][1]:
                    return True
        return False
                
    #------------------------------------   
    # Quel hexagone ?
    #------------------------------------ 
                
    def where(self, x, y):
        for value in self.__dic.values():
            if math.sqrt((value[0][0] - x)*(value[0][0] - x) + (value[0][1] - y)*(value[0][1] - y)) < self.__board.getHeight()/2:
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
        value[2] = self.__colorPlayer
        self.__lastHit = (value[1][0], value[1][1])
        listCoordCorner = self.__board.generateCoordCorner(value[0][0], value[0][1], self.__rayon*0.9)
        listCoordCircle = self.__board.generateCoordCircle(value[0][0], value[0][1], self.__rayon*1.2)
        self.__canvasBoard.create_polygon(listCoordCorner, fill="", outline=self.__colorPlayer, width=0.2*self.__rayon)
        self.__canvasBoard.create_oval(listCoordCircle, fill="", outline=self.__colorPlayer, width=0.25*self.__rayon)
        
    #------------------------------------   
    # Changement de joueur
    #------------------------------------  
        
    def changePlayer(self):
        if self.__player == self.__player1:
            self.__player = self.__player2
            self.__colorPlayer = self.__colorPlayer2
        else:
            self.__player = self.__player1
            self.__colorPlayer = self.__colorPlayer1