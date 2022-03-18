class Case:
    
    def __init__(self, position, aspect):
        
        self.__position = position
        self.__aspect = aspect
        
    def getCase(self):
        return [self.__position, self.__aspect, 0]