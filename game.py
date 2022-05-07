from board import Board
import math
from player import Player
import copy
 
class Game:
    
    def __init__(self, theme, func_image, canvas, canvas_p, board_size, rayon, board_color_outline, board_color, board_border, board_hlc):

        self.__func_image = func_image
        self.__theme = theme
        self.__canvas = canvas
        self.__canvas.bind('<Button-1>', self.game_turn)
        self.__canvas_p = canvas_p
        self.__board_size = board_size
        self.__rayon = rayon
        self.__board_color = board_color
        self.__board_color_outline = board_color_outline
        self._board_border = board_border
        self.__board_hlc = board_hlc
        self.__pause = False
        self.__board = Board(self.__rayon, self.__board_size, self.__canvas_p[0], self.__canvas_p[1], self.__theme["list_png"], self.__theme["list_color"], self.__func_image)
        self.__dic = self.__board.get_dic()
        self.__ring = self.__board.get_ring()
        self.__height = self.__board.get_height()
        self.__last_hit = ()
        self.__player_1 = Player(1).get_player()
        self.__player_2 = Player(2).get_player()
        self.__player_actuel = self.__player_1
        self.__dic__item = {}
        self.display_board()  
                
    def set_pause(self, set):
        self.__pause = set
        
    def get_board_size(self):
        return self.__board_size
        
    def get_rayon(self):
        return self.__rayon
    
    def get_dic_item(self):
        return self.__dic__item
    
    def display_board(self):
        for value in self.__dic__item.values():
            self.__canvas.delete(value)
        for value in self.__dic.values():
            list_coord_corner = self.__board.generate_coord_corner(value[0][0], value[0][1], self.__rayon)
            list_coord_circle = self.__board.generate_coord_circle(value[0][0], value[0][1], self.__rayon*0.6)
            self.__dic__item["polygon_"+str(value)] = self.__canvas.create_polygon(list_coord_corner, fill=self.__board_color, outline=self.__board_color_outline, width=self._board_border)
            self.__dic__item["oval_"+str(value)] = self.__canvas.create_oval(list_coord_circle, fill=value[1][1], width=0)
            self.__dic__item["image_"+str(value)] = self.__canvas.create_image(value[0][0], value[0][1], image=value[1][0])
            self.__dic__item["outline_"+str(value)] = self.__canvas.create_polygon(list_coord_corner, fill="", outline="", width=self._board_border, activeoutline=self.__board_hlc)
            if value[2] != 0:
                list_coord_corner = self.__board.generate_coord_corner(value[0][0], value[0][1], self.__rayon*0.9)
                list_coord_circle = self.__board.generate_coord_circle(value[0][0], value[0][1], self.__rayon*0.7)
                self.__dic__item["pion_polygon_"+str(value)] = self.__canvas.create_polygon(list_coord_corner, fill="", outline=self.color_player(value[2]), width=0.2*self.__rayon)
                self.__dic__item["pion_oval_"+str(value)] = self.__canvas.create_oval(list_coord_circle, fill="", outline=self.color_player(value[2]), width=0.25*self.__rayon)
        self.__canvas.update()
    
    def color_player(self, value):
        if value == self.__player_1[0]:
            return self.__player_1[1]
        else:
            return self.__player_2[1]
    
    def game_turn(self, event):
        if self.__pause == False:
            key = self.where(event.x, event.y)
            if key != "no":
                value = self.__dic[key]
                if self.start_or_possible(key, self.__ring):
                    self.put(value)
                    self.display_board()
                    if self.verif_side() == True or self.verif_trap() == True or self.verif_again_player() == False:
                        self.__pause = True
                    elif self.verif_egal():
                        self.__pause = True
                    self.change_player()
    
    def start_or_possible(self, key, ring):
        if self.__last_hit == ():
            return self.possible(key) and (((key[0] == ring or key[0] == -ring) and (key[1] != ring or key[1] != -ring) and (key[2] != ring or key[2] != -ring)) ^ ((key[1] == ring or key[1] == -ring) and (key[2] != ring or key[2] != -ring) and (key[0] != ring or key[0] != -ring)) ^ ((key[2] == ring or key[2] == -ring) and (key[1] != ring or key[1] != -ring) and (key[0] != ring or key[0] != -ring)))
        else:
            return self.possible(key)
        
    def possible(self, key):
        value = self.__dic[key]
        if value[1][1] != self.__theme["list_color"][0]:
            if value[2] == 0:
                if self.__last_hit == () or self.__last_hit[0] == value[1][0] or self.__last_hit[1] == value[1][1]:
                    return True
        return False
                
    def where(self, x, y):
        for value in self.__dic.values():
            if math.sqrt((value[0][0] - x)*(value[0][0] - x) + (value[0][1] - y)*(value[0][1] - y)) < self.__height/2:
                key = self.get_key(value)
                return key
        return "no"
    
    def get_key(self, val):
        for key, value in self.__dic.items():
            if val == value:
                return key
     
    def put(self, value):
        value[2] = self.__player_actuel[0]
        self.__last_hit = (value[1][0], value[1][1])
        
    def change_player(self):
        if self.__player_actuel == self.__player_1:
            self.__player_actuel = self.__player_2
        else:
            self.__player_actuel = self.__player_1
            
    def key_deplacement(self, axe, deplacement, cle):
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
    
    def verif_egal(self):
        for value in self.__dic.values():
            if value[1][1] != self.__theme["list_color"][0] and value[2] == 0:
                return False 
        return True
    
    def verif_again_player(self):
        for value in self.__dic.values():
            if (value[1][0] == self.__last_hit[0] or value[1][1] == self.__last_hit[1]) and value[2] == 0:
                return True
        self.change_player()
        return False
    
    def verif_side(self):
        side = False
        for key in self.__dic:
            if self.__dic[key][2] == self.__player_actuel[0] and (abs(key[0]) == self.__ring or abs(key[1]) == self.__ring or abs(key[2]) == self.__ring):
                list_key = []
                if self.voisin_side(list(key), list_key, list(key)) == True:
                    side = True
        return side
    
    def voisin_side(self, key, list_key, save_key):
        if (key not in list_key) and (tuple(key) in self.__dic) and (self.__dic[tuple(key)][2] == self.__player_actuel[0]) and (abs(save_key[0]) == self.__ring and save_key[0] == -key[0]) or (abs(save_key[1]) == self.__ring and save_key[1] == -key[1]) or (abs(save_key[2]) == self.__ring and save_key[2] == -key[2]):
            return True
        list_key.append(key)
        dep1 = ["r", "q", "s", "r", "q", "s"]
        dep2 = [-1, 1, -1, 1, -1, 1]
        for i in range(6):                                       
            func = self.key_deplacement(dep1[i], dep2[i], key)
            if (tuple(func) in self.__dic) and (func not in list_key) and (self.__dic[tuple(func)][2] == self.__player_actuel[0]):
                if self.voisin_side(func, list_key, save_key) == True:
                    return True
        
    def verif_trap(self):
        trap = False
        for key in self.__dic:
            if self.__dic[key][2] != self.__player_actuel[0] and (key[0] != abs(self.__ring) and key[1] != abs(self.__ring) and key[2] != abs(self.__ring)):
                list_key = []
                if self.voisin_trap(list(key), list_key) != False:
                    trap = True
        return trap
        
    def voisin_trap(self, key, list_key):
        list_key.append(key)
        dep1 = ["r", "q", "s", "r", "q", "s"]
        dep2 = [-1, 1, -1, 1, -1, 1]
        for i in range(6):
            func = self.key_deplacement(dep1[i], dep2[i], key)
            if (tuple(func) in self.__dic) and (func not in list_key) and (self.__dic[tuple(func)][2] != self.__player_actuel[0]) and (func[0] == abs(self.__ring) or func[1] == abs(self.__ring) or func[2] == abs(self.__ring)):
                return False
            elif (tuple(func) in self.__dic) and (func not in list_key) and (self.__dic[tuple(func)][2] != self.__player_actuel[0]):
                if self.voisin_trap(func, list_key) == False:
                    return False