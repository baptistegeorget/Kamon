import math
from math import *
import random
from case import Case

class Board: 
     
    def __init__(self, rayon, board_size, center_x, center_y, list_symb, list_color, func_image):
        
        self.__func_image = func_image
        self.__rayon = rayon
        self.__height = math.sqrt(3)*rayon
        self.__board_size = board_size
        self.__center_x = center_x
        self.__center_y = center_y
        self.__ring = self.ring()
        self.__list_symb = list_symb
        self.__list_color = list_color
    
    def get_dic(self):
        return self.create_dic(self.__list_symb, self.__list_color)
    
    def get_height(self):
        return self.__height
    
    def get_ring(self):
        return self.__ring
    
    def ring(self):
        if self.__board_size == 37:
            return 3
        if self.__board_size == 61:
            return 4
        if self.__board_size == 91:
            return 5
    
    def list_coord_key(self):
        list_coord_key = []
        coord_key = [0, 0, 0]
        self.add_list(list_coord_key, coord_key)
        for i in range(1, self.__ring+1):
            for _ in range(i):
                coord_key[1] -= 1
                coord_key[2] += 1
            self.add_list(list_coord_key, coord_key)
            for _ in range(i):
                coord_key[2] -= 1
                coord_key[0] += 1
                self.add_list(list_coord_key, coord_key)
            for _ in range(i):
                coord_key[2] -= 1
                coord_key[1] += 1
                self.add_list(list_coord_key, coord_key)
            for _ in range(i):
                coord_key[0] -= 1
                coord_key[1] += 1
                self.add_list(list_coord_key, coord_key)
            for _ in range(i):
                coord_key[0] -= 1
                coord_key[2] += 1
                self.add_list(list_coord_key, coord_key)
            for _ in range(i):
                coord_key[1] -= 1
                coord_key[2] += 1
                self.add_list(list_coord_key, coord_key)
            if i > 1:
                for _ in range(i-1):
                    coord_key[1] -= 1
                    coord_key[0] += 1
                    self.add_list(list_coord_key, coord_key)
            coord_key = [0, 0, 0]
        return list_coord_key
    
    def add_list(self, list_coord_key, coord_key):
        coord_key = tuple(coord_key)
        list_coord_key.append(coord_key)
        coord_key = list(coord_key)
    
    def list_aspect(self, list_symb, list_color):
        list_aspect = []
        list_random_symb = self.random_symb(list_symb)
        for i in range(1, 7):
            for j in range((self.__board_size-1)//6):
                list_aspect += [(list_random_symb[i], list_color[j+1])]
        list_aspect += [(list_random_symb[0], list_color[0])]
        random.shuffle(list_aspect)
        return list_aspect
    
    def random_symb(self, list_symb):
        random.shuffle(list_symb)
        seven_symb = [""]
        for i in range(6):
            seven_symb.append(self.__func_image(list_symb[i], round((self.__center_x+0.60*self.__rayon)-(self.__center_x-0.60*self.__rayon)), round((self.__center_y+0.60*self.__rayon)-(self.__center_y-0.60*self.__rayon))))
        return seven_symb
    
    def list_position(self):
        list_position = []
        position = (self.__center_x, self.__center_y)
        list_position.append(position)
        for i in range(1, self.__ring+1):
            for _ in range(i):
                position = self.axe_deplacement("r", -1.1, position[0], position[1])
            list_position.append(position)
            for _ in range(i):
                position = self.axe_deplacement("s", -1.1, position[0], position[1])
                list_position.append(position)
            for _ in range(i):
                position = self.axe_deplacement("r", 1.1, position[0], position[1])
                list_position.append(position)
            for _ in range(i):
                position = self.axe_deplacement("q", -1.1, position[0], position[1])
                list_position.append(position)
            for _ in range(i):
                position = self.axe_deplacement("s", 1.1, position[0], position[1])
                list_position.append(position)
            for _ in range(i):
                position = self.axe_deplacement("r", -1.1, position[0], position[1])
                list_position.append(position)
            if i > 1:
                for _ in range(i-1):
                    position = self.axe_deplacement("q", 1.1, position[0], position[1])
                    list_position.append(position)
            position = (self.__center_x, self.__center_y)
        return list_position
    
    def create_dic(self, list_symb, list_color):
        dic = {}
        list_aspect = self.list_aspect(list_symb, list_color)
        list_position = self.list_position()
        list_coord_key = self.list_coord_key()
        for i in range(self.__board_size):
            case = Case(list_position[i], list_aspect[i])
            dic[list_coord_key[i]] = case.get_case()
        return dic
            
    def generate_coord_corner(self, x, y, rayon):
        return [(x+rayon, y), 
                (rayon*math.cos(pi/3)+x, rayon*math.sin(pi/3)+y), 
                (-(rayon*math.cos(pi/3))+x, rayon*math.sin(pi/3)+y), 
                (x-rayon, y), 
                (-(rayon*math.cos(pi/3))+x, -(rayon*math.sin(pi/3))+y), 
                (rayon*math.cos(pi/3)+x, -(rayon*math.sin(pi/3))+y)]
        
    def generate_coord_circle(self, x, y, rayon):
        return [(x-rayon, y-rayon), (x+rayon, y+rayon)]
    
    def axe_deplacement(self, axe, deplacement, x, y):
        if axe == "q":
            return (round(self.__rayon*1.5*deplacement+x), round(-(self.__height/2)*deplacement+y))
        if axe == "r":
            return (round(x), round(self.__height*deplacement+y))
        if axe == "s":
            return (round(-(self.__rayon*1.5)*deplacement+x), round(-(self.__height/2)*deplacement+y))