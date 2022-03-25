class Player:
    
    #------------------------------------
    # Constructeur
    #------------------------------------
    
    def __init__(self, numeroJoueur):
        self.__color = ["white", "black"]
        self.__numeroJoueur = numeroJoueur
        
    #------------------------------------
    # Renvoie l'objet joueur
    #------------------------------------
        
    def getPlayer(self):
        return [self.__numeroJoueur, self.__color[self.__numeroJoueur-1]]