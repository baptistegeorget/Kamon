from tkinter import *
from PIL import Image, ImageTk
from gameTurn import GameTurn

class Menu: 
    
    def __init__(self):
        
        #------------------------------------ 
        # Tkinter root
        #------------------------------------ 
        
        self.__root = Tk(className=" KAMON GAME")
        self.__root.geometry("1440x900")
        self.__root.attributes('-fullscreen', True)
        
        #------------------------------------ 
        # Liste des background par theme
        #------------------------------------ 
        
        self.__bgAstro = self.image("assets/background/astro.png", 1440, 900)
        self.__bgClassique = self.image("assets/background/classique.png", 1440, 900)
        self.__bgByScott = self.image("assets/background/byscott.png", 1440, 900)
        
        #------------------------------------ 
        # Liste des png par theme
        #------------------------------------ 
        
        self.__listAstro = ["assets/symbole/astro/balance.png",
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
        
        self.__listClassique = ["assets/symbole/classique/bird.png",
                                "assets/symbole/classique/butterfly.png",
                                "assets/symbole/classique/door.png",
                                "assets/symbole/classique/fan.png",
                                "assets/symbole/classique/fish.png",
                                "assets/symbole/classique/mountain.png"]
        
        self.__listByScott = ["assets/symbole/byscott/cascade.png",
                                "assets/symbole/byscott/eau.png",
                                "assets/symbole/byscott/foudre.png",
                                "assets/symbole/byscott/herbe.png",
                                "assets/symbole/byscott/neige.png",
                                "assets/symbole/byscott/pluie.png",
                                "assets/symbole/byscott/son.png",
                                "assets/symbole/byscott/terre.png",
                                "assets/symbole/byscott/vent.png"]
        
        #------------------------------------ 
        # Liste des couleurs par theme
        #------------------------------------ 
        
        self.__listColorAstro = ["red",
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
        
        self.__listColorClassique = ["light slate gray",
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
        
        self.__listColorByScott = ["maroon1",
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
        
        #------------------------------------ 
        # Themes
        #------------------------------------ 
        
        self.__themeAstro = (self.__bgAstro, self.__listColorAstro, self.__listAstro)
        self.__themeByScott = (self.__bgByScott, self.__listColorByScott, self.__listByScott)
        self.__themeClassique = (self.__bgClassique, self.__listColorClassique, self.__listClassique)
        self.__themeActuel = self.__themeClassique
        
        #------------------------------------ 
        # Le canvas
        #------------------------------------ 
        
        self.__canvas = Canvas(self.__root, width=1440, height=900, highlightthickness=0)
        self.__canvas.place(x=0, y=0)
        self.__centerBoard = [720, 450]
        
        #------------------------------------ 
        # Le background
        #------------------------------------ 
        
        self.__canvas.create_image(0, 0, image = self.__themeActuel[0], anchor = "nw") 
        
        #------------------------------------ 
        # Le logo
        #------------------------------------ 
        
        self.__logoImage = self.image("assets/logo/logo.png", 700, 180)
        self.__canvas.create_image(720, 200, anchor="center", image=self.__logoImage)
        
        #------------------------------------ 
        # Styles
        #------------------------------------ 
        
        self.__fgColor = "#404040"
        self.__bgColor = "white"
        self.__bdSize = 5
        self.__bdColor = "#404040"
        
        #------------------------------------ 
        # Les widgets
        #------------------------------------ 
        
        self.__button1vs1 = Button(self.__root, text='1 vs 1', command=lambda: [self.changeDisplay(self.__pageGame, self.__pageGameConfig), self.startGame(37, 65)], font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vs1Config = [720, 400]
        self.__button1vsBot = Button(self.__root, text='1 vs Bot', command=lambda: self.changeDisplay(self.__pageSizeBoard, self.__pageSizeBoardConfig), font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vsBotConfig = [720, 500]
        self.__button1vs1online = Button(self.__root, text='1 vs 1 Online', command=lambda: self.changeDisplay(self.__pageOnline, self.__pageOnlineConfig), font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vs1onlineConfig = [720, 600]
        self.__buttonSettings = Button(self.__root, text='Settings', command=lambda: self.changeDisplay(self.__pageSettings, self.__pageSettingsConfig), font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=2, width=6, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonSettingsConfig = [1300, 100]
        self.__buttonQuitGame = Button(self.__root, text='Quit Game', command=lambda: self.__root.destroy(), font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonQuitGameConfig = [720, 700]
        self.__buttonBack = Button(self.__root, text='Back', command=lambda: self.changeDisplay(self.__pageBack, self.__pageBackConfig), font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=2, width=3, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonBackConfig = [100, 100]
        self.__buttonJoin = Button(self.__root, text='Join', command=lambda: self.getJoinText(), font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=1, width=10, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonJoinConfig = [550, 400]
        self.__buttonCreate = Button(self.__root, text='Create', command=lambda: self.getCreateText(), font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=1, width=10, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonCreateConfig = [550, 450]
        self.__buttonBreak = Button(self.__root, text='⎥⎪', command=lambda: self.changeDisplay(self.__pageBreak, self.__pageBreakConfig), font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=2, width=3, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonBreakConfig = [1300, 100]
        #####################################
        self.__buttonRestart = Button(self.__root, text='Restart', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonRestartConfig = [720, 400]
        self.__buttonSaveGame = Button(self.__root, text='Save and quit Game', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonSaveGameConfig = [720, 500]
        ########################################
        self.__buttonQuit = Button(self.__root, text='Quit', command=lambda: self.changeDisplay(self.__pageAccueil, self.__pageAccueilConfig), font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonQuitConfig = [720, 600]
        
        self.__labelBreak = Label(self.__root, text="BREAK", font=("Helvetica", 44, "bold"), fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelBreakConfig = [720, 200]
        self.__labelSettings = Label(self.__root, text="SETTINGS", font=("Helvetica", 44, "bold"), fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelSettingsConfig = [720, 200]
        self.__labelOnline = Label(self.__root, text="ONLINE", font=("Helvetica", 44, "bold"), fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelOnlineConfig = [720, 200]
        
        self.__joinEntryArea = Entry(self.__root, font=("Helvetica", 20, "bold"), fg="black", bg="white", width=25, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor, relief=FLAT)
        self.__joinEntryAreaConfig = [850, 400]
        self.__createEntryArea = Entry(self.__root, font=("Helvetica", 20, "bold"), fg="black", bg="white", width=25, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor, relief=FLAT)
        self.__createEntryAreaConfig = [850, 450]
        
        #------------------------------------ 
        # Pages et configuration
        #------------------------------------ 
        
        self.__pageAccueil = [self.__button1vs1, self.__button1vsBot, self.__button1vs1online, self.__buttonSettings, self.__buttonQuitGame]
        self.__pageAccueilConfig =  [self.__button1vs1Config, self.__button1vsBotConfig, self.__button1vs1onlineConfig, self.__buttonSettingsConfig, self.__buttonQuitGameConfig]
        
        self.__pageSettings = [self.__labelSettings, self.__buttonBack]
        self.__pageSettingsConfig = [self.__labelSettingsConfig, self.__buttonBackConfig]
        
        self.__pageSizeBoard = []
        self.__pageSizeBoardConfig = []
        
        self.__pageGame = [self.__buttonBreak]
        self.__pageGameConfig = [self.__buttonBreakConfig]
        
        self.__pageBreak = [self.__labelBreak, self.__buttonBack, self.__buttonSettings, self.__buttonRestart, self.__buttonSaveGame, self.__buttonQuit]
        self.__pageBreakConfig = [self.__labelBreakConfig, self.__buttonBackConfig, self.__buttonSettingsConfig, self.__buttonRestartConfig, self.__buttonSaveGameConfig, self.__buttonQuitConfig]
        
        self.__pageOnline = [self.__labelOnline, self.__buttonBack, self.__buttonJoin, self.__buttonCreate, self.__joinEntryArea, self.__createEntryArea]
        self.__pageOnlineConfig = [self.__labelOnlineConfig, self.__buttonBackConfig, self.__buttonJoinConfig, self.__buttonCreateConfig, self.__joinEntryAreaConfig, self.__createEntryAreaConfig]
        
        self.__pageActuel = self.__pageAccueil
        self.__pageActuelConfig = self.__pageAccueilConfig
        
        self.__pageBack = self.__pageAccueil
        self.__pageBackConfig = self.__pageAccueilConfig


        self.__colorBoard = "black"
        self.__bgCase = "#404040"
        self.__colorPlayer1 = "white"
        self.__colorPlayer2 = "black"
        
        self.__joinCode = None
        self.__createCode = None

    #------------------------------------   
    # Fonction pour utiliser un png
    #------------------------------------  

    def image(self, image, width, height):
        file = Image.open(image)
        file = file.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(file)
    
    #------------------------------------   
    # Change de page
    #------------------------------------ 
            
    def changeDisplay(self, newPage, newPageConfig):
        self.__pageBack = self.__pageActuel
        self.__pageBackConfig = self.__pageActuelConfig
        self.delDisplay()
        self.__pageActuel = newPage
        self.__pageActuelConfig = newPageConfig
        self.display()
        
    def display(self):
        for j in range(len(self.__pageActuel)):
            self.__pageActuel[j].place(x=self.__pageActuelConfig[j][0], y=self.__pageActuelConfig[j][1], anchor="center")
        if self.__pageActuel == self.__pageAccueil:
            self.__canvas.create_image(720, 200, anchor="center", image=self.__logoImage)
        if self.__pageActuel == self.__pageGame:
            self.startGame(37, 65)
            
    def delDisplay(self):
        for i in range(len(self.__pageActuel)):
            self.__pageActuel[i].place_forget()
        if self.__pageActuel == self.__pageAccueil or self.__pageActuel == self.__pageGame:
            self.__canvas.delete(ALL)
            self.__canvas.create_image(0, 0, image = self.__themeActuel[0], anchor = "nw") 
        
    #------------------------------------   
    # Récupère les codes 
    #------------------------------------ 
         
    def getJoinText(self):
        self.__joinCode = self.__joinEntryArea.get()
        
    def getCreateText(self):
        self.__createCode = self.__createEntryArea.get()
        
    #------------------------------------   
    # Lance une partie
    #------------------------------------  
        
    def startGame(self, boardSize, rayon):
        turn = GameTurn(self.__canvas, self.__centerBoard, boardSize, rayon, self.__themeActuel[2], self.__themeActuel[1], self.__colorBoard, self.__colorPlayer1, self.__colorPlayer2, self.__bgCase, self.__themeActuel[0])
        turn.displayBoard()
    
    #------------------------------------   
    # Change le theme
    #------------------------------------ 
    
    def changeTheme(self, theme):
        self.__themeActuel = theme
       
    #------------------------------------   
    # Lance Kamon
    #------------------------------------ 
        
    def startKamon(self):
        self.display()
        self.__root.mainloop()
    
menu = Menu()
menu.startKamon()