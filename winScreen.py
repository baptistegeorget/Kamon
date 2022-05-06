from tkinter import *
class WinScreen:
    
    def __init__(self, canvas, canvasConfig, winner, bgImage, buttonBreak, buttonBreakConfig, result):
        self.__canvas = canvas
        self.__canvasConfig = canvasConfig
        self.__buttonBreak = buttonBreak
        self.__buttonBreakConfig = buttonBreakConfig
        self.__textWin = "Partie terminé !\nLe gagnant est Player "+str(winner)
        self.__textEgal = "Partie terminé !\nEgalité"
        self.__result = result
        
    def displayWinScreen(self):
        self.__canvas.delete(ALL)
        self.__buttonBreak.place(x=self.__buttonBreakConfig[0], y=self.__buttonBreakConfig[1], anchor="center")
        if self.__result == "win":
            self.__canvas.create_text(self.__canvasConfig[0], self.__canvasConfig[1], fill="black", font=("Courier", 90, "bold"), justify="center", text=self.__textWin)
        elif self.__result == "egal":
            self.__canvas.create_text(self.__canvasConfig[0], self.__canvasConfig[1], fill="black", font=("Courier", 90, "bold"), justify="center", text=self.__textEgal)
        self.__canvas.update()