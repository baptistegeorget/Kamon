from tkinter import *
from PIL import Image, ImageTk
from gameTurn import GameTurn

class Menu: 
    
    def __init__(self):
        
        ########## Fenêtre ##########
        self.__root = Tk(className=" KAMON GAME")
        self.__root.geometry("1440x900")
        
        ########## Styles ##########
        self.__fgColor = "orange"
        self.__bgColor = "white"
        self.__bdSize = 5
        self.__bdColor = "orange"
        
        ########## Codes ##########
        self.__joinCode = ""
        self.__createCode = ""
        
        ########## Background ##########
        self.__bg = Canvas(self.__root, width=1440, height=900, bg="#404040")
        self.__bg.place(x=720, y=450, anchor="center")
        self.__bgImage = self.image("assets/background/naruto.jpg", 1440, 900)
        self.__bg.create_image(720, 450, image = self.__bgImage) 
         
        ########## Label Kamon ##########
        self.__labelKamon = Label(self.__root, text="KAMON", font=("Helvetica", 70, "bold"), fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelKamon.place(x=720, y=200, anchor="center")
        self.__labelKamonConfig = [720, 200]
        ########## Boutton 1vs1 ##########
        self.__button1vs1 = Button(self.__root, text='1 vs 1', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: [self.changeDisplay([self.__labelKamon, self.__button1vs1, self.__button1vsBot, self.__button1vs1online, self.__buttonSettingsKamon, self.__buttonQuitGame], [self.__canvasBoard, self.__buttonBreak], [self.__canvasBoardConfig, self.__buttonBreakConfig]), self.startGame(91, 40)], pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vs1.place(x=720, y=400, anchor="center")
        self.__button1vs1Config = [720, 400]
        ########## Boutton 1vsBot ##########
        self.__button1vsBot = Button(self.__root, text='1 vs Bot', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelKamon, self.__button1vs1, self.__button1vsBot, self.__button1vs1online, self.__buttonSettingsKamon, self.__buttonQuitGame], [self.__canvasBoard, self.__buttonBreak], [self.__canvasBoardConfig, self.__buttonBreakConfig]), pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vsBot.place(x=720, y=500, anchor="center")
        self.__button1vsBotConfig = [720, 500]
        ########## Boutton 1vs1 Online ##########
        self.__button1vs1online = Button(self.__root, text='1 vs 1 Online', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelKamon, self.__button1vs1, self.__button1vsBot, self.__button1vs1online, self.__buttonSettingsKamon, self.__buttonQuitGame], [self.__labelOnline, self.__buttonBackOnline, self.__buttonJoin, self.__buttonCreate, self.__joinEntryArea, self.__createEntryArea], [self.__labelOnlineConfig, self.__buttonBackOnlineConfig, self.__buttonJoinConfig, self.__buttonCreateConfig, self.__joinEntryAreaConfig, self.__createEntryAreaConfig]), pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__button1vs1online.place(x=720, y=600, anchor="center")
        self.__button1vs1onlineConfig = [720, 600]
        ########## Boutton Settings Kamon ##########
        self.__buttonSettingsKamon = Button(self.__root, text='Settings', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelKamon, self.__button1vs1, self.__button1vsBot, self.__button1vs1online, self.__buttonSettingsKamon, self.__buttonQuitGame], [self.__labelSettingsMenu, self.__buttonBackSettingsMenu], [self.__labelSettingsMenuConfig, self.__buttonBackSettingsMenuConfig]), pady=1, height=2, width=6, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonSettingsKamon.place(x=1300, y=100, anchor="center")
        self.__buttonSettingsKamonConfig = [1300, 100]
        ########## Boutton Quit Game ##########
        self.__buttonQuitGame = Button(self.__root, text='Quit Game', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.__root.destroy(), pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonQuitGame.place(x=720, y=700, anchor="center")
        self.__buttonQuitGameConfig = [720, 700]
        
        ########## Label Online ##########
        self.__labelOnline = Label(self.__root, text="ONLINE", font=("Helvetica", 44, "bold"), fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelOnlineConfig = [720, 200]
        ########## Boutton Retour Online ##########
        self.__buttonBackOnline = Button(self.__root, text='Back', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelOnline, self.__buttonBackOnline, self.__buttonJoin, self.__buttonCreate, self.__joinEntryArea, self.__createEntryArea], [self.__labelKamon, self.__button1vs1, self.__button1vsBot, self.__button1vs1online, self.__buttonSettingsKamon, self.__buttonQuitGame], [self.__labelKamonConfig, self.__button1vs1Config, self.__button1vsBotConfig, self.__button1vs1onlineConfig, self.__buttonSettingsKamonConfig, self.__buttonQuitGameConfig]), pady=1, height=2, width=3, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonBackOnlineConfig = [100, 100]
        ########## Bouton Join ##########
        self.__buttonJoin = Button(self.__root, text='Join', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.getJoinText(), pady=1, height=1, width=10, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonJoinConfig = [550, 400]
        ########## Boutton Create ##########
        self.__buttonCreate = Button(self.__root, text='Create', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.getCreateText(), pady=1, height=1, width=10, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonCreateConfig = [550, 450]
        ########## Entrée Join ##########
        self.__joinEntryArea = Entry(self.__root, font=("Helvetica", 20, "bold"), fg="black", bg="white", width=25, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor, relief=FLAT)
        self.__joinEntryArea.insert(0, "(Enter the code!)")
        self.__joinEntryAreaConfig = [850, 400]
        ########## Entrée Create ##########
        self.__createEntryArea = Entry(self.__root, font=("Helvetica", 20, "bold"), fg="black", bg="white", width=25, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor, relief=FLAT)
        self.__createEntryArea.insert(0, "(Enter the code!)")
        self.__createEntryAreaConfig = [850, 450]
        
        ########## Boutton Break ##########
        self.__buttonBreak = Button(self.__root, text='⎥⎪', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__buttonBreak, self.__canvasBoard], [self.__labelBreak, self.__buttonBackBreak, self.__buttonSettingsBreak, self.__buttonRestart, self.__buttonSaveGame, self.__buttonQuit], [self.__labelBreakConfig, self.__buttonBackBreakConfig, self.__buttonSettingsBreakConfig, self.__buttonRestartConfig, self.__buttonSaveGameConfig, self.__buttonQuitConfig]), pady=1, height=2, width=3, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonBreakConfig = [1300, 100]
        ########## Board Game ##########
        self.__canvasBoard = Canvas(self.__root, width=1200, height=890, highlightthickness=0, highlightbackground=self.__bdColor, bg="#404040")
        self.__canvasBoardConfig = [605, 450]
        
        ########## Label Break ##########
        self.__labelBreak = Label(self.__root, text="BREAK", font=("Helvetica", 44, "bold"), fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelBreakConfig = [720, 200]
        ########## Boutton Retour Break ##########
        self.__buttonBackBreak = Button(self.__root, text='Back', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelBreak, self.__buttonBackBreak, self.__buttonSettingsBreak, self.__buttonRestart, self.__buttonSaveGame, self.__buttonQuit], [self.__buttonBreak, self.__canvasBoard], [self.__buttonBreakConfig, self.__canvasBoardConfig]), pady=1, height=2, width=3, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonBackBreakConfig = [100, 100]
        ########## Boutton Settings Break ##########
        self.__buttonSettingsBreak = Button(self.__root, text='Settings', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelBreak, self.__buttonBackBreak, self.__buttonSettingsBreak, self.__buttonRestart, self.__buttonSaveGame, self.__buttonQuit], [self.__labelSettingsBreak, self.__buttonBackSettingsBreak], [self.__labelSettingsBreakConfig, self.__buttonBackSettingsBreakConfig]), pady=1, height=2, width=6, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonSettingsBreakConfig = [1300, 100]
        ########## Boutton Restart ##########
        self.__buttonRestart = Button(self.__root, text='Restart', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelBreak, self.__buttonBackBreak, self.__buttonSettingsBreak, self.__buttonRestart, self.__buttonSaveGame, self.__buttonQuit], [self.__buttonBreak, self.__canvasBoard], [self.__buttonBreakConfig, self.__canvasBoardConfig]), pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonRestartConfig = [720, 400]
        ########## Boutton Save Game ##########
        self.__buttonSaveGame = Button(self.__root, text='Save and quit Game', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelBreak, self.__buttonBackBreak, self.__buttonSettingsBreak, self.__buttonRestart, self.__buttonSaveGame, self.__buttonQuit], [self.__labelKamon, self.__button1vs1, self.__button1vsBot, self.__button1vs1online, self.__buttonSettingsKamon, self.__buttonQuitGame], [self.__labelKamonConfig, self.__button1vs1Config, self.__button1vsBotConfig, self.__button1vs1onlineConfig, self.__buttonSettingsKamonConfig, self.__buttonQuitGameConfig]), pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonSaveGameConfig = [720, 500]
        ########## Boutton Quit ##########
        self.__buttonQuit = Button(self.__root, text='Quit', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelBreak, self.__buttonBackBreak, self.__buttonSettingsBreak, self.__buttonRestart, self.__buttonSaveGame, self.__buttonQuit], [self.__labelKamon, self.__button1vs1, self.__button1vsBot, self.__button1vs1online, self.__buttonSettingsKamon, self.__buttonQuitGame], [self.__labelKamonConfig, self.__button1vs1Config, self.__button1vsBotConfig, self.__button1vs1onlineConfig, self.__buttonSettingsKamonConfig, self.__buttonQuitGameConfig]), pady=1, height=2, width=20, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonQuitConfig = [720, 600]
        
        ########## Label Settings Break ##########
        self.__labelSettingsBreak = Label(self.__root, text="SETTINGS", font=("Helvetica", 44, "bold"), fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelSettingsBreakConfig = [720, 200]
        ########## Boutton Retour Settings Break ##########
        self.__buttonBackSettingsBreak = Button(self.__root, text='Back', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelSettingsBreak, self.__buttonBackSettingsBreak], [self.__labelBreak, self.__buttonBackBreak, self.__buttonSettingsBreak, self.__buttonRestart, self.__buttonSaveGame, self.__buttonQuit], [self.__labelBreakConfig, self.__buttonBackBreakConfig, self.__buttonSettingsBreakConfig, self.__buttonRestartConfig, self.__buttonSaveGameConfig, self.__buttonQuitConfig]), pady=1, height=2, width=3, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonBackSettingsBreakConfig = [100, 100]
        
        ########## Label Settings Menu ##########
        self.__labelSettingsMenu = Label(self.__root, text="SETTINGS", font=("Helvetica", 44, "bold"), fg=self.__fgColor, bg=self.__bgColor, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__labelSettingsMenuConfig = [720, 200]
        ########## Boutton Retour Settings Menu ##########
        self.__buttonBackSettingsMenu = Button(self.__root, text='Back', font=("Helvetica", 24, "bold"), fg=self.__fgColor, bg=self.__bgColor, command=lambda: self.changeDisplay([self.__labelSettingsMenu, self.__buttonBackSettingsMenu], [self.__labelKamon, self.__button1vs1, self.__button1vsBot, self.__button1vs1online, self.__buttonSettingsKamon, self.__buttonQuitGame], [self.__labelKamonConfig, self.__button1vs1Config, self.__button1vsBotConfig, self.__button1vs1onlineConfig, self.__buttonSettingsKamonConfig, self.__buttonQuitGameConfig]), pady=1, height=2, width=3, highlightthickness=self.__bdSize, highlightbackground=self.__bdColor)
        self.__buttonBackSettingsMenuConfig = [100, 100]
        
        # Liste de symboles
        self.__listSymb1 = ["",
                            self.image("assets/symbole/astro/bélier.png", 100, 100),
                            self.image("assets/symbole/astro/cancer.png", 100, 100),
                            self.image("assets/symbole/astro/capricorne.png", 100, 100),
                            self.image("assets/symbole/astro/gémeaux.png", 100, 100),
                            self.image("assets/symbole/astro/lion.png", 100, 100),
                            self.image("assets/symbole/astro/balance.png", 100, 100)]
        
        self.__listSymb2 = ["",
                            self.image("assets/symbole/classique/bird.png", 80, 80),
                            self.image("assets/symbole/classique/butterfly.png", 80, 80),
                            self.image("assets/symbole/classique/door.png", 80, 80),
                            self.image("assets/symbole/classique/fan.png", 80, 80),
                            self.image("assets/symbole/classique/fish.png", 80, 80),
                            self.image("assets/symbole/classique/mountain.png", 80, 80)]
        
        self.__listSymb3 = ["",
                            self.image("assets/symboleNoir/naruto/cascade.png", 80, 80),
                            self.image("assets/symboleNoir/naruto/eau.png", 80, 80),
                            self.image("assets/symboleNoir/naruto/feu.png", 80, 80),
                            self.image("assets/symboleNoir/naruto/herbe.png", 80, 80),
                            self.image("assets/symboleNoir/naruto/neige.png", 80, 80),
                            self.image("assets/symboleNoir/naruto/son.png", 80, 80)]
        
        self.__listColor1 = ["red",
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
        
        self.__listColor2 = ["light slate gray",
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
        
        self.__listColor3 = ["",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             ""]
        
        self.__colorBoard = "black"
        self.__colorPlayer1 = "yellow"
        self.__colorPlayer2 = "black"
        
        self.__root.mainloop()

    #------------------------------------   
    # Changer la taille d'une image
    #------------------------------------  

    def image(self, image, width, height):
        file = Image.open(image)
        file = file.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(file)
    
    #------------------------------------   
    # Changer de fenetre dans le menu
    #------------------------------------  
    
    def changeDisplay(self, listSupp, listAdd, listConfig):
        for i in range(len(listSupp)):
            listSupp[i].place_forget()
        for j in range(len(listAdd)):
            listAdd[j].place(x=listConfig[j][0], y=listConfig[j][1], anchor="center")
                
    #------------------------------------   
    # Récupère les codes 
    #------------------------------------ 
         
    # Code pour rejoindre       
    def getJoinText(self):
        self.__joinCode = self.__joinEntryArea.get()
        
    # Code pour créer
    def getCreateText(self):
        self.__createCode = self.__createEntryArea.get()
        
    #------------------------------------   
    # Lance une partie
    #------------------------------------  
        
    def startGame(self, boardSize, rayon):
        turn = GameTurn(self.__canvasBoard, self.__canvasBoardConfig, boardSize, rayon, self.__listSymb2, self.__listColor2, self.__colorBoard, self.__colorPlayer1, self.__colorPlayer2)
        turn.displayBoard()
    
Menu()