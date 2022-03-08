import math
from math import *
import random

class Board: 
     
    #------------------------------------   
    # Constructeur
    #------------------------------------   
    
    def __init__(self, rayon, boardSize, centerX, centerY, listSymb, listColor):
        
        # Hexagone
        self.__rayon = rayon
        self.__height = math.sqrt(3)*rayon
        
        # Plateau
        self.__boardSize = boardSize
        self.__centerX = centerX
        self.__centerY = centerY
        self.__ring = self.ring()
        
        # Case
        self.__dic = self.createDic(listSymb, listColor)
    
    #------------------------------------   
    # Les getter
    #------------------------------------
    
    def getDic(self):
        return self.__dic
    
    def getHeight(self):
        return self.__height
    
    def getRayon(self):
        return self.__rayon
    
    def getRing(self):
        return self.__ring
    
    #------------------------------------
    # Anneaux
    #------------------------------------
    
    def ring(self):
        x = 1
        ring = 1
        while x != self.__boardSize:
            x += 6*ring
            ring += 1
        return ring
    
    #------------------------------------
    # Dictionnaire de cases
    #------------------------------------
    
    # Création des clés et des coordonnées
    def generateCoord(self):
        dic = {}
        position = (self.__centerX, self.__centerY)
        coordKey = [0, 0, 0]
        self.addDic(dic, coordKey, position)
        for i in range(1, self.__ring):
            for _ in range(i):
                coordKey[1] -= 1
                coordKey[2] += 1
                position = self.axeDeplacement("r", -1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            for _ in range(i):
                coordKey[2] -= 1
                coordKey[0] += 1
                position = self.axeDeplacement("s", -1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            for _ in range(i):
                coordKey[2] -= 1
                coordKey[1] += 1
                position = self.axeDeplacement("r", 1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            for _ in range(i):
                coordKey[0] -= 1
                coordKey[1] += 1
                position = self.axeDeplacement("q", -1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            for _ in range(i):
                coordKey[0] -= 1
                coordKey[2] += 1
                position = self.axeDeplacement("s", 1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            for _ in range(i):
                coordKey[1] -= 1
                coordKey[2] += 1
                position = self.axeDeplacement("r", -1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            if i > 1:
                for _ in range(i-1):
                    coordKey[1] -= 1
                    coordKey[0] += 1
                    position = self.axeDeplacement("q", 1, position[0], position[1])
                    self.addDic(dic, coordKey, position)
            position = (self.__centerX, self.__centerY)
            coordKey = [0, 0, 0]
        return dic
    
    # Ajouts des clés et des coordonnées
    def addDic(self, dic, coordKey, position):
        coordKey = tuple(coordKey)
        dic[coordKey] = [position]
        coordKey = list(coordKey)
    
    # Création des couleurs et des symboles
    def colorSymb(self, listSymb, listColor):
        case = []
        symb = listSymb
        for i in range(1, 7):
            for j in range((self.__boardSize-1)//6):
                case += [(symb[i], listColor[j+1])]
        case += [(symb[0], listColor[0])]
        return case
    
    # Ajouts des couleurs et des symboles   
    def addColorSymb(self, listSymb, dic, listColor):
        case = self.colorSymb(listSymb, listColor)
        listKey = []
        for key in dic:
            listKey.append(key)
        random.shuffle(listKey)
        x = 0
        for i in range(len(listKey)):
            dic[listKey[i]] += [case[x]]
            x += 1
    
    # Ajouts de l'état des cases
    def addState(self, dic):
        for value in dic.values():
            value += ["vide"]
            
    # Création du dictionnaire
    def createDic(self, listSymb, listColor):
        dic = self.generateCoord()
        self.addColorSymb(listSymb, dic, listColor)
        self.addState(dic)
        return dic
            
    #------------------------------------
    # Coordonnées des coins d'un hexagone
    #------------------------------------
    
    def generateCoordCorner(self, x, y, rayon):
        return [(x+rayon, y), 
                (rayon*math.cos(pi/3)+x, rayon*math.sin(pi/3)+y), 
                (-(rayon*math.cos(pi/3))+x, rayon*math.sin(pi/3)+y), 
                (x-rayon, y), 
                (-(rayon*math.cos(pi/3))+x, -(rayon*math.sin(pi/3))+y), 
                (rayon*math.cos(pi/3)+x, -(rayon*math.sin(pi/3))+y)]
        
    #------------------------------------
    # Coordonnées d'un cercle
    #------------------------------------
        
    def generateCoordCircle(self, x, y):
        return [(x-0.65*self.__rayon, y-0.65*self.__rayon), (x+0.65*self.__rayon, y+0.65*self.__rayon)]
    
    #------------------------------------
    # Deplacement de case en case
    #------------------------------------
    
    def axeDeplacement(self, axe, deplacement, x, y):
        if axe == "q":
            return (self.__rayon*1.5*deplacement+x, -(self.__height/2)*deplacement+y)
        if axe == "r":
            return (x, self.__height*deplacement+y)
        if axe == "s":
            return (-(self.__rayon*1.5)*deplacement+x, -(self.__height/2)*deplacement+y)