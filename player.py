class Player:
    
    def __init__(self, numero_joueur):
        self.__color = ["white", "black"]
        self.__numero_joueur = numero_joueur
        
    def get_player(self):
        return [self.__numero_joueur, self.__color[self.__numero_joueur-1]]