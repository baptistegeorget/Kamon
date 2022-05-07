import PIL.Image, PIL.ImageTk
from tkinter import Tk, Button, Canvas, Entry, Label, FLAT
from gameTurn import Game
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
        # L'objet représentant une partie
        self.__game = None
        #--------------------------------------------------------------------------------------------------------------------#
        # Paramètrage des widget et du board
        self.__hlt_widget = 0
        self.__hlb_widget = "dark slate blue"
        self.__hlc_widget = "dark slate blue"
        self.__fg_widget = "dark slate blue"
        self.__bg_widget = "white"
        self.__relief_widget = FLAT
        self.__board_color_outline = "black"
        self.__board_color = "#555"
        self.__font_helvetica_24_bold = ("Helvetica", 24, "bold")
        self.__font_courier_120_bold = ("Courier", 120, "bold")
        self.__width_50_px = 50
        self.__height_50_px = 50
        self.__height_2 = 2
        self.__width_20 = 20
        self.__width_13 = 13
        self.__anchor = "center"
        #--------------------------------------------------------------------------------------------------------------------#
        # Les emplacements des widgets
        self.__canvas_p = [self.__screen[0]*50/100, self.__screen[1]*50/100]
        self.__logo_p = [self.__screen[0]*50/100, self.__screen[1]*20/100]
        self.__button_player_vs_player_p = [self.__screen[0]*50/100, self.__screen[1]*40/100]
        self.__button_player_vs_ordi_p = [self.__screen[0]*50/100, self.__screen[1]*50/100]
        self.__button_player_vs_player_online_p = [self.__screen[0]*50/100, self.__screen[1]*60/100]
        self.__button_quit_kamon_p = [self.__screen[0]*50/100, self.__screen[1]*70/100]
        self.__button_settings_p = [self.__screen[0]*90/100, self.__screen[1]*10/100]
        self.__button_back_p = [self.__screen[0]*10/100, self.__screen[1]*10/100]
        self.__button_join_p = [self.__screen[0]*30/100, self.__screen[1]*40/100]
        self.__button_create_p = [self.__screen[0]*30/100, self.__screen[1]*60/100]
        self.__button_break_p = [self.__screen[0]*90/100, self.__screen[1]*10/100]
        self.__button_resume_p = [self.__screen[0]*50/100, self.__screen[1]*40/100]
        self.__button_restart_p = [self.__screen[0]*50/100, self.__screen[1]*50/100]
        self.__button_save_game_p = [self.__screen[0]*50/100, self.__screen[1]*60/100]
        self.__button_quit_game_p = [self.__screen[0]*50/100, self.__screen[1]*70/100]
        self.__button_small_board_p = [self.__screen[0]*50/100, self.__screen[1]*40/100]
        self.__button_medium_board_p = [self.__screen[0]*50/100, self.__screen[1]*50/100]
        self.__button_large_board_p = [self.__screen[0]*50/100, self.__screen[1]*60/100]
        self.__button_theme_astro_p = [450, 300]
        self.__button_theme_imaginary_p = [700, 300]
        self.__button_theme_classique_p = [950, 300]
        self.__button_croix_p = [self.__screen[0]*90/100, self.__screen[1]*10/100]
        self.__item_title_break_p = [self.__screen[0]*50/100, self.__screen[1]*20/100]
        self.__item_title_settings_p = [self.__screen[0]*50/100, self.__screen[1]*20/100]
        self.__item_title_online_p = [self.__screen[0]*50/100, self.__screen[1]*20/100]
        self.__item_title_board_size_p = [self.__screen[0]*50/100, self.__screen[1]*20/100]
        self.__entry_join_p = [self.__screen[0]*60/100, self.__screen[1]*40/100]
        self.__entry_create_p = [self.__screen[0]*60/100, self.__screen[1]*60/100]
        #--------------------------------------------------------------------------------------------------------------------#
        # Les widgets
        self.__canvas = Canvas(self.__root, width=self.__screen[0], height=self.__screen[1], highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_player_vs_player = Button(self.__root, text='1 vs 1', command=lambda: self.change_display(self.__page_board_size), font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_player_vs_ordi = Button(self.__root, text='1 vs IA', command=lambda: self.change_display(self.__page_board_size), font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_player_vs_player_online = Button(self.__root, text='1 vs 1 en ligne', command=lambda: self.change_display(self.__page_online), font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_quit_kamon = Button(self.__root, text='Quitter le jeu', command=lambda: self.__root.destroy(), font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_settings = Button(self.__root, bitmap="assets/logo/parametre.png", command=lambda: self.change_display(self.__page_settings), font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_50_px, width=self.__width_50_px, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_back = Button(self.__root, bitmap="assets/logo/retour.png", command=lambda: self.change_display(self.__page_back), font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_50_px, width=self.__width_50_px, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_join = Button(self.__root, text='Rejoindre', command=lambda: self.__get_entry_join(), font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_13, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_create = Button(self.__root, text='Créer', command=lambda: self.__get_entry_create(), font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_13, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_break = Button(self.__root, bitmap="assets/logo/pause.png", command=lambda: [self.change_display(self.__page_break), self.pause(True)], font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_50_px, width=self.__width_50_px, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_resume = Button(self.__root, text='Reprendre', command=lambda: [self.change_display(self.__page_game), self.pause(False), self.__game.displayBoard()], font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_restart = Button(self.__root, text='Recommencer', command=lambda: [self.change_display(self.__page_game), self.start_game(self.__game.get_board_size(), self.__game.get_rayon())], font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_save_game = Button(self.__root, text='Sauvegarder et quitter', font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_quit_game = Button(self.__root, text='Quitter la partie', command=lambda: self.change_display(self.__page_accueil), font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_small_board = Button(self.__root, text='Petit', command=lambda: [self.change_display(self.__page_game), self.start_game(37, 65)], font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_medium_board = Button(self.__root, text='Moyen', command=lambda: [self.change_display(self.__page_game), self.start_game(61, 50)], font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_large_board = Button(self.__root, text='Grand', command=lambda: [self.change_display(self.__page_game), self.start_game(91, 40)], font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_20, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_theme_astro = Button(self.__root, text='Theme Astro', command=lambda: [self.change_theme(self.__theme_astro)], font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_13, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_theme_imaginary = Button(self.__root, text='Theme ByScott', command=lambda: [self.change_theme(self.__theme_imaginary)], font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_13, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_theme_classique = Button(self.__root, text='Theme Classique', command=lambda: [self.change_theme(self.__theme_classique)], font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_2, width=self.__width_13, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__button_croix = Button(self.__root, bitmap="assets/logo/croix.png", command=lambda: [self.change_display(self.__page_accueil)], font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, height=self.__height_50_px, width=self.__width_50_px, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, highlightcolor=self.__hlc_widget)
        self.__entry_join = Entry(self.__root, font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, width=25, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, relief=self.__relief_widget, highlightcolor=self.__hlc_widget)
        self.__entry_create = Entry(self.__root, font=self.__font_helvetica_24_bold, fg=self.__fg_widget, bg=self.__bg_widget, width=25, highlightthickness=self.__hlt_widget, highlightbackground=self.__hlb_widget, relief=self.__relief_widget, highlightcolor=self.__hlc_widget)
        self.__canvas.place(x=self.__canvas_p[0], y=self.__canvas_p[1], anchor=self.__anchor)
        #--------------------------------------------------------------------------------------------------------------------#
        # Les codes pour les parties en réseaux
        self.__entry_join_code = None
        self.__entry_create_code = None
        #--------------------------------------------------------------------------------------------------------------------#
        # Les items
        self.__item_logo = None
        self.__item_title_board_size = None
        self.__item_title_break = None
        self.__item_title_online = None
        self.__item_title_settings = None
        self.__item_bg = self.__canvas.create_image(self.__canvas_p[0], self.__canvas_p[1], image = self.image(self.__theme_actuel["bg"], self.__screen[0], self.__screen[1]), anchor= self.__anchor)
        #--------------------------------------------------------------------------------------------------------------------#
        # Les pages
        self.__page_accueil = [[self.__button_player_vs_player, self.__button_player_vs_ordi, self.__button_player_vs_player_online, self.__button_settings, self.__button_quit_kamon], [self.__button_player_vs_player_p, self.__button_player_vs_ordi_p, self.__button_player_vs_player_online_p, self.__button_settings_p, self.__button_quit_kamon_p]]
        self.__page_settings = [[self.__button_back, self.__button_theme_astro, self.__button_theme_classique, self.__button_theme_imaginary], [self.__button_back_p, self.__button_theme_astro_p, self.__button_theme_classique_p, self.__button_theme_imaginary_p]]
        self.__page_board_size = [[self.__button_back, self.__button_small_board, self.__button_medium_board, self.__button_large_board], [self.__button_back_p, self.__button_small_board_p, self.__button_medium_board_p, self.__button_large_board_p]]
        self.__page_game = [[self.__button_break], [self.__button_break_p]]
        self.__page_break = [[self.__button_restart, self.__button_save_game, self.__button_quit_game, self.__button_resume], [self.__button_restart_p, self.__button_save_game_p, self.__button_quit_game_p, self.__button_resume_p]]
        self.__page_online = [[self.__button_back, self.__button_join, self.__button_create, self.__entry_join, self.__entry_create], [self.__button_back_p, self.__button_join_p, self.__button_create_p, self.__entry_join_p, self.__entry_create_p]]
        self.__page_actuel = None
        self.__page_back = None
        #--------------------------------------------------------------------------------------------------------------------#
        if __name__ == "__main__":
            self.change_display(self.__page_accueil)
            self.__root.mainloop()

    def image(self, image, width, height):
        image = PIL.Image.open(image)
        image = image.resize((width, height), PIL.Image.ANTIALIAS)
        image = PIL.ImageTk.PhotoImage(image)
        label = Label(self.__root, image=image)
        label.img=image
        return image
            
    def change_display(self, page):
        self.__page_back = self.__page_actuel
        if self.__page_actuel != None:
            for i in range(len(self.__page_actuel[0])):
                self.__page_actuel[0][i].place_forget()
        for i in range(len(page[0])):
            page[0][i].place(x=page[1][i][0], y=page[1][i][1], anchor=self.__anchor)
        if page == self.__page_accueil:
            self.__item_logo = self.__canvas.create_image(self.__logo_p[0], self.__logo_p[1], anchor=self.__anchor, image=self.image(Themes().get_logo(), 700, 180))
        if page != self.__page_accueil:
            self.__canvas.delete(self.__item_logo)
        if page == self.__page_break:
            self.__item_title_break = self.__canvas.create_text(self.__item_title_break_p[0], self.__item_title_break_p[1], text="Pause", font=self.__font_courier_120_bold, fill=self.__fg_widget)
        if page != self.__page_break:
            self.__canvas.delete(self.__item_title_break)
        if page == self.__page_online:
            self.__item_title_online = self.__canvas.create_text(self.__item_title_online_p[0], self.__item_title_online_p[1], text="Online", font=self.__font_courier_120_bold, fill=self.__fg_widget)
        if page != self.__page_online:
            self.__canvas.delete(self.__item_title_online)
        if page == self.__page_settings:
            self.__item_title_settings = self.__canvas.create_text(self.__item_title_settings_p[0], self.__item_title_settings_p[1], text="Settings", font=self.__font_courier_120_bold, fill=self.__fg_widget)
        if page != self.__page_settings:
            self.__canvas.delete(self.__item_title_settings)
        if page == self.__page_board_size:
            self.__item_title_board_size = self.__canvas.create_text(self.__item_title_board_size_p[0], self.__item_title_board_size_p[1], text="Plateaux", font=self.__font_courier_120_bold, fill=self.__fg_widget)
        if page != self.__page_board_size:
            self.__canvas.delete(self.__item_title_board_size)
        self.__page_actuel = page
        self.__root.update()
         
    def __get_entry_join(self):
        self.__entry_join_code = self.__entry_join.get()
        
    def __get_entry_create(self):
        self.__entry_create_code = self.__entry_create.get()
        
    def start_game(self, board_size, rayon):
        self.__game = Game(self.__theme_actuel, self.image, self.__canvas, self.__canvas_p, board_size, rayon, self.__board_color_outline, self.__board_color, self.__button_croix, self.__button_croix_p)
    
    def change_theme(self, theme):
        self.__canvas.delete(self.__item_bg, self.__item_title_settings)
        self.__item_bg = self.__canvas.create_image(self.__canvas_p[0], self.__canvas_p[1], image = self.image(theme["bg"], self.__screen[0], self.__screen[1]), anchor= self.__anchor)
        self.__item_title_settings = self.__canvas.create_text(self.__item_title_settings_p[0], self.__item_title_settings_p[1], text="Settings", font=self.__font_courier_120_bold, fill=self.__fg_widget)
        self.__theme_actuel = theme
        
    def pause(self, set):
        self.__game.setPause(set)
        
Menu()