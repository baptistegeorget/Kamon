import PIL.Image, PIL.ImageTk
from tkinter import *
from gameTurn import GameTurn
from themes import Themes
import os
import AppKit
import ctypes

class Menu: 
    
    def __init__(self):
        
        #--------------------------------------------------------------------------------------------------------------------#
        # Choix de l'OS
        if os.name == "posix": # Macos, Linux
            self.__screen = (round(AppKit.NSScreen.screens()[0].frame().size.width), round(AppKit.NSScreen.screens()[0].frame().size.height))
        elif os.name == "nt": # Windows
            self.__screen = (round(ctypes.windll.user32.GetSystemMetrics(0)), round(ctypes.windll.user32.GetSystemMetrics(1)))
        else: # Inconnu
            self.__screen = (1920, 1080)
            print("Error: Votre OS n'est pas reconnu.")
        #--------------------------------------------------------------------------------------------------------------------#
        # Fenêtre Tkinter #
        self.__root = Tk(className = " Kamon")
        self.__root.geometry(str(self.__screen[0])+"x"+str(self.__screen[1]))
        self.__root.attributes('-fullscreen', True)
        self.__root.resizable(False, False)
        #--------------------------------------------------------------------------------------------------------------------#
        # Thèmes
        self.__theme_astro = Themes().get_themes()[0]
        self.__theme_imaginary = Themes().get_themes()[1]
        self.__theme_classique = Themes().get_themes()[2]
        self.__theme_actuel = self.__theme_classique
        #--------------------------------------------------------------------------------------------------------------------#
        self.__turn = None
        self.__boardSize = None
        self.__rayon = None
        #--------------------------------------------------------------------------------------------------------------------#
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
        #--------------------------------------------------------------------------------------------------------------------#
        self.__canvasConfig = [720, 450]
        self.__canvas = Canvas(self.__root, width=1440, height=900, highlightthickness=0, background="white")
        self.__canvas.place(x=self.__canvasConfig[0], y=self.__canvasConfig[1], anchor="center")
        self.__canvas.create_image(self.__canvasConfig[0], self.__canvasConfig[1], image = self.image(self.__theme_actuel["bg"], self.__screen[0], self.__screen[1]), anchor = "center") 
        self.__logoConfig = [720, 200]
        self.__logoImage = self.image("assets/logo/logo.png", 700, 180)
        self.__canvas.create_image(self.__logoConfig[0], self.__logoConfig[1], anchor="center", image=self.__logoImage)
        
        self.__button1vs1 = Button(self.__root, text='1 vs 1', command=lambda: self.changeDisplay(self.__pageSizeBoard, self.__pageSizeBoardConfig), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vs1Config = [720, 400]
        self.__button1vsIA = Button(self.__root, text='1 vs IA', command=lambda: self.changeDisplay(self.__pageSizeBoard, self.__pageSizeBoardConfig), font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vsIAConfig = [720, 500]
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
        self.__buttonBreak = Button(self.__root, bitmap="assets/logo/pause.png", command=lambda: [self.changeDisplay(self.__pageBreak, self.__pageBreakConfig), self.pause(True)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightSmall, width=self.__widthSmall, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonBreakConfig = [1300, 100]
        self.__buttonResume = Button(self.__root, text='Reprendre', command=lambda: [self.changeDisplay(self.__pageGame, self.__pageGameConfig), self.pause(False), self.__turn.displayBoard()], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthLarge, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
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
        self.__buttonAstro = Button(self.__root, text='Theme Astro', command=lambda: [self.changeTheme(self.__theme_astro), self.changeDisplay(self.__pageBack, self.__pageBackConfig)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthMedium, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonAstroConfig = [450, 300]
        self.__buttonByScott = Button(self.__root, text='Theme ByScott', command=lambda: [self.changeTheme(self.__theme_imaginary), self.changeDisplay(self.__pageBack, self.__pageBackConfig)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthMedium, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonByScottConfig = [700, 300]
        self.__buttonClassique = Button(self.__root, text='Theme Classique', command=lambda: [self.changeTheme(self.__theme_classique), self.changeDisplay(self.__pageBack, self.__pageBackConfig)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightLarge, width=self.__widthMedium, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonClassiqueConfig = [950, 300]
        self.__buttonWinScreen = Button(self.__root, bitmap="assets/logo/croix.png", command=lambda: [self.changeDisplay(self.__pageAccueil, self.__pageAccueilConfig)], font=self.__fontButton, fg=self.__fgColor, bg=self.__bgColor, height=self.__heightSmall, width=self.__widthSmall, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonWinScreenConfig = [1300, 100]
        
        self.__labelBreak = Label(self.__root, text="PAUSE", font=self.__fontLabel, fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelBreakConfig = [720, 200]
        self.__labelSettings = Label(self.__root, text="PARAMETRES", font=self.__fontLabel, fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
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
        
        self.__pageAccueil = [self.__button1vs1, self.__button1vsIA, self.__button1vs1online, self.__buttonSettings, self.__buttonQuitGame]
        self.__pageAccueilConfig =  [self.__button1vs1Config, self.__button1vsIAConfig, self.__button1vs1onlineConfig, self.__buttonSettingsConfig, self.__buttonQuitGameConfig]
        
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
        self.__bgCase = "#636262"
        
        self.__joinCode = None
        self.__createCode = None
        
        if __name__ == "__main__":
            self.startKamon()

    #------------------------------------   
    # Fonction pour utiliser un png
    #------------------------------------  

    def image(self, image, width, height):
        image = PIL.Image.open(image)
        image = image.resize((width, height), PIL.Image.ANTIALIAS)
        image = PIL.ImageTk.PhotoImage(image)
        label = Label(self.__root, image=image)
        label.img=image
        return image
    
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
        self.__buttonWinScreen.place_forget()
        self.__canvas.delete(ALL)
        self.__canvas.create_image(self.__canvasConfig[0], self.__canvasConfig[1], image = self.image(self.__theme_actuel["bg"], self.__screen[0], self.__screen[1]), anchor = "center") 
        
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
        self.__turn = GameTurn(self.image, self.__canvas, self.__canvasConfig, boardSize, rayon, self.__theme_actuel["list_png"], self.__theme_actuel["list_color"], self.__colorBoard, self.__bgCase, self.__theme_actuel["bg"], self.__buttonWinScreen, self.__buttonWinScreenConfig)
        self.__turn.displayBoard()
    
    #------------------------------------   
    # Change le theme
    #------------------------------------ 
    
    def changeTheme(self, theme):
        self.__theme_actuel = theme
       
    #------------------------------------   
    # Lance Kamon
    #------------------------------------ 
        
    def startKamon(self):
        self.display()
        self.__root.mainloop()
        
    #------------------------------------   
    # Met le jeu sur pause
    #------------------------------------ 
    
    def pause(self, set):
        self.__turn.setPause(set)
        
Menu()