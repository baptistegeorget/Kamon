from PIL import Image, ImageTk

class Themes:
    
    def __init__(self):
        
        self.__bg_astro = "assets/background/astro.png"
        self.__bg_classique = "assets/background/classique.png"
        self.__bg_imaginary = "assets/background/byscott.png"
        
        self.__list_png_astro = ["assets/symbole/astro/balance.png",
                            "assets/symbole/astro/bélier.png",
                            "assets/symbole/astro/cancer.png",
                            "assets/symbole/astro/capricorne.png",
                            "assets/symbole/astro/gémeaux.png",
                            "assets/symbole/astro/lion.png",
                            "assets/symbole/astro/poisson.png",
                            "assets/symbole/astro/sagittaire.png",
                            "assets/symbole/astro/scorpion.png",
                            "assets/symbole/astro/taureau.png",
                            "assets/symbole/astro/verseau.png",
                            "assets/symbole/astro/vierge.png"]
        
        self.__list_png_classique = ["assets/symbole/classique/bird.png",
                                "assets/symbole/classique/butterfly.png",
                                "assets/symbole/classique/door.png",
                                "assets/symbole/classique/fan.png",
                                "assets/symbole/classique/fish.png",
                                "assets/symbole/classique/mountain.png"]
        
        self.__list_png_imaginary = ["assets/symbole/byscott/cascade.png",
                              "assets/symbole/byscott/eau.png",
                              "assets/symbole/byscott/foudre.png",
                              "assets/symbole/byscott/herbe.png",
                              "assets/symbole/byscott/neige.png",
                              "assets/symbole/byscott/pluie.png",
                              "assets/symbole/byscott/son.png",
                              "assets/symbole/byscott/terre.png",
                              "assets/symbole/byscott/vent.png"]
        
        self.__list_color_astro = ["red",
                                 "DarkGoldenrod2",
                                 "CadetBlue2",
                                 "DarkOliveGreen3",
                                 "DarkOrange1",
                                 "DarkOrchid3",
                                 "DarkSeaGreen3",
                                 "DeepSkyBlue3",
                                 "HotPink2",
                                 "MediumOrchid1",
                                 "MediumPurple3",
                                 "OliveDrab4",
                                 "coral1",
                                 "DarkSlateGray4",
                                 "RoyalBlue2",
                                 "aquamarine2"]
        
        self.__list_color_classique = ["light slate gray",
                                     "red",
                                     "hot pink",
                                     "light sky blue",
                                     "orange",
                                     "chartreuse4",
                                     "yellow2",
                                     "HotPink3",
                                     "DodgerBlue3",
                                     "SlateBlue3",
                                     "goldenrod3",
                                     "PaleGreen2",
                                     "orchid4",
                                     "magenta4",
                                     "tan4",
                                     "sea green"]
        
        self.__list_color_imaginary = ["maroon1",
                                   "coral2",
                                   "dark orange",
                                   "goldenrod1",
                                   "NavajoWhite3",
                                   "dodger blue",
                                   "azure4",
                                   "firebrick3",
                                   "LightSteelBlue3",
                                   "SkyBlue2",
                                   "DarkOlivegreen2",
                                   "salmon3",
                                   "HotPink2",
                                   "red",
                                   "cyan2",
                                   "DeepSkyBlue3"]
        
        self.__theme_astro = {"bg":self.__bg_astro, "list_color":self.__list_color_astro, "list_png":self.__list_png_astro}
        self.__theme_imaginary = {"bg":self.__bg_imaginary, "list_color":self.__list_color_imaginary, "list_png":self.__list_png_imaginary}
        self.__theme_classique = {"bg":self.__bg_classique, "list_color":self.__list_color_classique, "list_png":self.__list_png_classique}
        
    def get_themes(self):
        return self.__theme_astro, self.__theme_imaginary, self.__theme_classique