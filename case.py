class Case:
    
    def __init__(self, position, aspect):
        
        self.__position = position
        self.__aspect = aspect
        
    def get_case(self):
        return [self.__position, self.__aspect, 0]