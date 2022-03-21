import math
from math import *
import random
from PIL import Image, ImageTk
from case import Case

class Board: 
     
    #------------------------------------   
    # Constructeur
    #------------------------------------   
    
    def __init__(self, rayon, boardSize, centerX, centerY, listSymb, listColor):
        
        self.__rayon = rayon
        self.__height = math.sqrt(3)*rayon
        self.__boardSize = boardSize
        self.__centerX = centerX
        self.__centerY = centerY
        self.__ring = self.ring()
        self.__listSymb = listSymb
        self.__listColor = listColor
    
    #------------------------------------   
    # Renvoie les données du plateau
    #------------------------------------
    
    def getDic(self):
        return self.createDic(self.__listSymb, self.__listColor)
    
    def getHeight(self):
        return self.__height
    
    def getRing(self):
        return self.__ring
    
    #------------------------------------
    # Calcule le nombre d'anneaux
    #------------------------------------
    
    def ring(self):
        if self.__boardSize == 37:
            return 3
        if self.__boardSize == 61:
            return 4
        if self.__boardSize == 91:
            return 5
    
    #------------------------------------
    # Créer une liste de clés pour le dictionnaire
    #------------------------------------
    
    def listCoordKey(self):
        listCoordKey = []
        coordKey = [0, 0, 0]
        self.addList(listCoordKey, coordKey)
        for i in range(1, self.__ring+1):
            for _ in range(i):
                coordKey[1] -= 1
                coordKey[2] += 1
            self.addList(listCoordKey, coordKey)
            for _ in range(i):
                coordKey[2] -= 1
                coordKey[0] += 1
                self.addList(listCoordKey, coordKey)
            for _ in range(i):
                coordKey[2] -= 1
                coordKey[1] += 1
                self.addList(listCoordKey, coordKey)
            for _ in range(i):
                coordKey[0] -= 1
                coordKey[1] += 1
                self.addList(listCoordKey, coordKey)
            for _ in range(i):
                coordKey[0] -= 1
                coordKey[2] += 1
                self.addList(listCoordKey, coordKey)
            for _ in range(i):
                coordKey[1] -= 1
                coordKey[2] += 1
                self.addList(listCoordKey, coordKey)
            if i > 1:
                for _ in range(i-1):
                    coordKey[1] -= 1
                    coordKey[0] += 1
                    self.addList(listCoordKey, coordKey)
            coordKey = [0, 0, 0]
        return listCoordKey
    
    def addList(self, listCoordKey, coordKey):
        coordKey = tuple(coordKey)
        listCoordKey.append(coordKey)
        coordKey = list(coordKey)
    
    #------------------------------------
    # Creer une liste d'aspect pour le dictionnaire
    #------------------------------------
    
    def listAspect(self, listSymb, listColor):
        listAspect = []
        listRandomSymb = self.randomSymb(listSymb)
        for i in range(1, 7):
            for j in range((self.__boardSize-1)//6):
                listAspect += [(listRandomSymb[i], listColor[j+1])]
        listAspect += [(listRandomSymb[0], listColor[0])]
        random.shuffle(listAspect)
        return listAspect
    
    def randomSymb(self, listSymb):
        random.shuffle(listSymb)
        sevenSymb = [""]
        for i in range(6):
            sevenSymb.append(self.image(listSymb[i], round((self.__centerX+0.60*self.__rayon)-(self.__centerX-0.60*self.__rayon)), round((self.__centerY+0.60*self.__rayon)-(self.__centerY-0.60*self.__rayon))))
        return sevenSymb
    
    #------------------------------------
    # Creer une liste de position pour le dictionnaire
    #------------------------------------
    
    def listPosition(self):
        listPosition = []
        position = (self.__centerX, self.__centerY)
        listPosition.append(position)
        for i in range(1, self.__ring+1):
            for _ in range(i):
                position = self.axeDeplacement("r", -1.1, position[0], position[1])
            listPosition.append(position)
            for _ in range(i):
                position = self.axeDeplacement("s", -1.1, position[0], position[1])
                listPosition.append(position)
            for _ in range(i):
                position = self.axeDeplacement("r", 1.1, position[0], position[1])
                listPosition.append(position)
            for _ in range(i):
                position = self.axeDeplacement("q", -1.1, position[0], position[1])
                listPosition.append(position)
            for _ in range(i):
                position = self.axeDeplacement("s", 1.1, position[0], position[1])
                listPosition.append(position)
            for _ in range(i):
                position = self.axeDeplacement("r", -1.1, position[0], position[1])
                listPosition.append(position)
            if i > 1:
                for _ in range(i-1):
                    position = self.axeDeplacement("q", 1.1, position[0], position[1])
                    listPosition.append(position)
            position = (self.__centerX, self.__centerY)
        return listPosition
    
    #------------------------------------
    # Créer un dictionnaire
    #------------------------------------
    
    def createDic(self, listSymb, listColor):
        dic = {}
        listAspect = self.listAspect(listSymb, listColor)
        listPosition = self.listPosition()
        listCoordKey = self.listCoordKey()
        for i in range(self.__boardSize):
            case = Case(listPosition[i], listAspect[i])
            dic[listCoordKey[i]] = case.getCase()
        return dic
            
    #------------------------------------
    # Calcule les coordonnées des coins d'un hexagone
    #------------------------------------
    
    def generateCoordCorner(self, x, y, rayon):
        return [(x+rayon, y), 
                (rayon*math.cos(pi/3)+x, rayon*math.sin(pi/3)+y), 
                (-(rayon*math.cos(pi/3))+x, rayon*math.sin(pi/3)+y), 
                (x-rayon, y), 
                (-(rayon*math.cos(pi/3))+x, -(rayon*math.sin(pi/3))+y), 
                (rayon*math.cos(pi/3)+x, -(rayon*math.sin(pi/3))+y)]
        
    #------------------------------------
    # Calcule les coordonnées pour tracer un cercle
    #------------------------------------
        
    def generateCoordCircle(self, x, y, rayon):
        return [(x-rayon, y-rayon), (x+rayon, y+rayon)]
    
    #------------------------------------
    # Calcule un déplacement sur les vecteurs (q, r, s)
    #------------------------------------
    
    def axeDeplacement(self, axe, deplacement, x, y):
        if axe == "q":
            return (self.__rayon*1.5*deplacement+x, -(self.__height/2)*deplacement+y)
        if axe == "r":
            return (x, self.__height*deplacement+y)
        if axe == "s":
            return (-(self.__rayon*1.5)*deplacement+x, -(self.__height/2)*deplacement+y)
        
    #------------------------------------   
    # Fonction pour utiliser un png
    #------------------------------------  

    def image(self, image, width, height):
        file = Image.open(image)
        file = file.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(file)