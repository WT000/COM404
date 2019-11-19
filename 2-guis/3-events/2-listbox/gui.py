from tkinter import *

# Setting the GUI Class
class Gui(Tk):

    def __init__(self):
        super().__init__()

        # Window attributes
        self.geometry("230x150")
        self.title("Song Maker")

        # GUI Components
        self.__add_header_label()
        self.__add_lyric_label()
        self.__add_lyric_entry()
        self.__add_total_lyrics_label()
        self.__add_lyrics_listbox()

    def __add_header_label(self):
        pass

    def __add_lyric_label(self):
        pass

    def __add_lyric_entry(self):
        pass

    def __add_total_lyrics_label(self):
        pass

    def __add_lyrics_listbox(self):
        pass