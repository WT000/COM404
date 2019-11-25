from tkinter import *

# Setting the GUI Class
class Gui(Tk):

    def __init__(self):
        super().__init__()

        # Window attributes
        self.title("Song Maker")
        self.configure(padx=10, pady=5)

        # GUI Components
        self.__add_header_label()
        self.__add_lyric_label()
        self.__add_lyric_entry()
        self.__add_lyric_button()
        self.__add_total_lyrics_label()
        self.__add_lyrics_listbox()

    def __add_header_label(self):
        self.header_label = Label()
        self.header_label.grid(row=0, column=0, columnspan=2)
        self.header_label.configure(font="Arial 20",
                                    text="Song Maker",
                                    bg="#eee")

    def __add_lyric_label(self):
        self.header_label = Label()
        self.header_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.header_label.configure(font="Arial 13",
                                    text="Lyric to add:",
                                    bg="#eee")

    def __add_lyric_entry(self):
        self.lyric_entry = Entry()
        self.lyric_entry.grid(row=2, column=0)
        self.lyric_entry.configure(width=20)

    def __add_lyric_button(self):
        self.lyric_button = Button()
        self.lyric_button.grid(row=2, column=1, sticky=E)
        self.lyric_button.configure(text="Add", width=6)
        self.lyric_button.bind("<ButtonRelease-1>", self.__lyric_button_clicked)

    def __add_total_lyrics_label(self):
        self.header_label = Label()
        self.header_label.grid(row=3, column=0, columnspan=2, sticky=W)
        self.header_label.configure(font="Arial 13",
                                    text="Lyrics:",
                                    bg="#eee")

    def __lyric_button_clicked(self, event):
        new_lyric = self.lyric_entry.get()
        self.lyrics_listbox.insert(END, new_lyric)

    def __add_lyrics_listbox(self):
        self.lyrics_listbox = Listbox()
        self.lyrics_listbox.grid(row=4, column=0, columnspan=2)
        self.lyrics_listbox.configure(height=4, width=30)