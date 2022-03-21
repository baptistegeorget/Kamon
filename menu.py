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
        self.__themeActuel = self.__themeByScott
        
        #------------------------------------ 
        # Le canvas
        #------------------------------------ 
        
        self.__canvasConfig = [720, 450]
        self.__canvas = Canvas(self.__root, width=1440, height=900, highlightthickness=0)
        self.__canvas.place(x=self.__canvasConfig[0], y=self.__canvasConfig[1], anchor="center")
        
        #------------------------------------ 
        # Le background
        #------------------------------------ 
        
        self.__canvas.create_image(self.__canvasConfig[0], self.__canvasConfig[1], image = self.__themeActuel[0], anchor = "center") 
        
        #------------------------------------ 
        # Le logo
        #------------------------------------ 
        self.__logoConfig = [720, 200]
        self.__logoImage = self.image("assets/logo/logo.png", 700, 180)
        self.__canvas.create_image(self.__logoConfig[0], self.__logoConfig[1], anchor="center", image=self.__logoImage)
        
        #------------------------------------ 
        # L'objet gameTurn
        #------------------------------------ 
        
        self.__turn = None
        self.__boardSize = None
        self.__rayon = None
        
        #------------------------------------ 
        # Styles
        #------------------------------------ 
        
        self.__fgColor = "black"
        self.__bgColor = "white"
        self.__bdColor = "black"
        self.__bdSize = 3
        self.__fontButton = ("Courier", 24, "bold")
        self.__fontLabel = ("Courier", 70, "bold")
        self.__fontEntry = ("Helvetica", 24, "bold")
        self.__heightSmall = 50
        self.__heightLarge = 2
        self.__widthSmall = 50
        self.__widthLarge = 20
        self.__widthMedium = 13
        
        #------------------------------------ 
        # Les widgets
        #------------------------------------ 
        
        self.__button1vs1 = Button(self.__root, text='1 vs 1', command=lambda: self.changeDisplay(self.__pageSizeBoard, self.__pageSizeBoardConfig), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vs1Config = [720, 400]
        self.__button1vsBot = Button(self.__root, text='1 vs ordi', command=lambda: self.changeDisplay(self.__pageSizeBoard, self.__pageSizeBoardConfig), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vsBotConfig = [720, 500]
        self.__button1vs1online = Button(self.__root, text='1 vs 1 en ligne', command=lambda: self.changeDisplay(self.__pageOnline, self.__pageOnlineConfig), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vs1onlineConfig = [720, 600]
        self.__buttonSettings = Button(self.__root, bitmap="assets/logo/parametre.png", command=lambda: self.changeDisplay(self.__pageSettings, self.__pageSettingsConfig), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightSmall, width=self.__widthSmall, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonSettingsConfig = [1300, 100]
        self.__buttonQuitGame = Button(self.__root, text='Quitter le jeu', command=lambda: self.__root.destroy(), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonQuitGameConfig = [720, 700]
        self.__buttonBack = Button(self.__root, bitmap="assets/logo/retour.png", command=lambda: self.changeDisplay(self.__pageBack, self.__pageBackConfig), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightSmall, width=self.__widthSmall, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonBackConfig = [140, 100]
        self.__buttonJoin = Button(self.__root, text='Rejoindre', command=lambda: self.getJoinText(), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthMedium, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonJoinConfig = [550, 400]
        self.__buttonCreate = Button(self.__root, text='Créer', command=lambda: self.getCreateText(), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthMedium, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonCreateConfig = [550, 500]
        self.__buttonBreak = Button(self.__root, bitmap="assets/logo/pause.png", command=lambda: [self.changeDisplay(self.__pageBreak, self.__pageBreakConfig), self.pause()], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightSmall, width=self.__widthSmall, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonBreakConfig = [1300, 100]
        self.__buttonResume = Button(self.__root, text='Reprendre', command=lambda: [self.changeDisplay(self.__pageGame, self.__pageGameConfig), self.pause(), self.__turn.displayBoard()], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonResumeConfig = [720, 400]
        self.__buttonRestart = Button(self.__root, text='Recommencer', command=lambda: [self.changeDisplay(self.__pageGame, self.__pageGameConfig), self.startGame(self.__boardSize, self.__rayon)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonRestartConfig = [720, 500]
        self.__buttonSaveGame = Button(self.__root, text='Sauvegarder et quitter', font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonSaveGameConfig = [720, 600]
        self.__buttonQuit = Button(self.__root, text='Quitter la partie', command=lambda: self.changeDisplay(self.__pageAccueil, self.__pageAccueilConfig), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonQuitConfig = [720, 700]
        self.__buttonPetit = Button(self.__root, text='Petit', command=lambda: [self.changeDisplay(self.__pageGame, self.__pageGameConfig), self.startGame(37, 65)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonPetitConfig = [720, 400]
        self.__buttonMoyen = Button(self.__root, text='Moyen', command=lambda: [self.changeDisplay(self.__pageGame, self.__pageGameConfig), self.startGame(61, 50)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonMoyenConfig = [720, 500]
        self.__buttonGrand = Button(self.__root, text='Grand', command=lambda: [self.changeDisplay(self.__pageGame, self.__pageGameConfig), self.startGame(91, 40)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonGrandConfig = [720, 600]
        self.__buttonAstro = Button(self.__root, text='Theme Astro', command=lambda: [self.changeTheme(self.__themeAstro), self.changeDisplay(self.__pageBack, self.__pageBackConfig)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthMedium, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonAstroConfig = [450, 300]
        self.__buttonByScott = Button(self.__root, text='Theme ByScott', command=lambda: [self.changeTheme(self.__themeByScott), self.changeDisplay(self.__pageBack, self.__pageBackConfig)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthMedium, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonByScottConfig = [700, 300]
        self.__buttonClassique = Button(self.__root, text='Theme Classique', command=lambda: [self.changeTheme(self.__themeClassique), self.changeDisplay(self.__pageBack, self.__pageBackConfig)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthMedium, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonClassiqueConfig = [950, 300]
        
        self.__labelBreak = Label(self.__root, text="PAUSE", font=self.__fontLabel, fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelBreakConfig = [720, 200]
        self.__labelSettings = Label(self.__root, text="PARAMETRE", font=self.__fontLabel, fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelSettingsConfig = [720, 200]
        self.__labelOnline = Label(self.__root, text="PARTIE PRIVEE", font=self.__fontLabel, fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelOnlineConfig = [720, 200]
        self.__labelPlateau = Label(self.__root, text="PLATEAU", font=self.__fontLabel, fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelPlateauConfig = [720, 200]
        
        self.__joinEntryArea = Entry(self.__root, font=self.__fontEntry, fg=self.__fgColor, bg=self.__bgColor, width=25, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor, relief=FLAT)
        self.__joinEntryAreaConfig = [850, 400]
        self.__createEntryArea = Entry(self.__root, font=self.__fontEntry, fg=self.__fgColor, bg=self.__bgColor, width=25, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor, relief=FLAT)
        self.__createEntryAreaConfig = [850, 500]
        
        #------------------------------------ 
        # Pages et configuration
        #------------------------------------ 
        
        self.__pageAccueil = [self.__button1vs1, self.__button1vsBot, self.__button1vs1online, self.__buttonSettings, self.__buttonQuitGame]
        self.__pageAccueilConfig =  [self.__button1vs1Config, self.__button1vsBotConfig, self.__button1vs1onlineConfig, self.__buttonSettingsConfig, self.__buttonQuitGameConfig]
        
        self.__pageSettings = [self.__labelSettings, self.__buttonBack, self.__buttonAstro, self.__buttonClassique, self.__buttonByScott]
        self.__pageSettingsConfig = [self.__labelSettingsConfig, self.__buttonBackConfig, self.__buttonAstroConfig, self.__buttonClassiqueConfig, self.__buttonByScottConfig]
        
        self.__pageSizeBoard = [self.__buttonBack, self.__buttonPetit, self.__buttonMoyen, self.__buttonGrand, self.__labelPlateau]
        self.__pageSizeBoardConfig = [self.__buttonBackConfig, self.__buttonPetitConfig, self.__buttonMoyenConfig, self.__buttonGrandConfig, self.__labelPlateauConfig]
        
        self.__pageGame = [self.__buttonBreak]
        self.__pageGameConfig = [self.__buttonBreakConfig]
        
        self.__pageBreak = [self.__labelBreak, self.__buttonRestart, self.__buttonSaveGame, self.__buttonQuit, self.__buttonResume]
        self.__pageBreakConfig = [self.__labelBreakConfig, self.__buttonRestartConfig, self.__buttonSaveGameConfig, self.__buttonQuitConfig, self.__buttonResumeConfig]
        
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
            
    def delDisplay(self):
        for i in range(len(self.__pageActuel)):
            self.__pageActuel[i].place_forget()
        self.__canvas.delete(ALL)
        self.__canvas.create_image(self.__canvasConfig[0], self.__canvasConfig[1], image = self.__themeActuel[0], anchor = "center") 
        
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
        self.__boardSize = boardSize
        self.__rayon = rayon
        self.__turn = GameTurn(self.__canvas, self.__canvasConfig, boardSize, rayon, self.__themeActuel[2], self.__themeActuel[1], self.__colorBoard, self.__colorPlayer1, self.__colorPlayer2, self.__bgCase, self.__themeActuel[0])
        self.__turn.displayBoard()
    
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
        
    #------------------------------------   
    # Met le jeu sur pause
    #------------------------------------ 
    
    def pause(self):
        self.__turn.setPause()
    
menu = Menu()
menu.startKamon()