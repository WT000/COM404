from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        # Load resources
        self.map_img = PhotoImage(file="U:/com404/COM404/2-guis/4-images/3-positioning/map.gif")
        self.character_img = PhotoImage(file="U:/com404/COM404/2-guis/4-images/3-positioning/dragonborn.gif")
        
        # Window attributes
        self.title("Skyrim Journey")
        self.geometry("1200x930")

        # Components
        self.__add_header_label()
        self.__map_frame()
        self.__add_map_img_label()
        self.__add_character_img_label()

    def __add_header_label(self):
        self.header_label = Label()
        self.header_label.place(x=450)
        self.header_label.configure(font="Arial 20", 
                                    text="Fast travel simulator")

    def __map_frame(self):
        self.map_frame = Frame()
        self.map_frame.place(x=0, y=30)
        self.map_frame.configure(height=900,
                                 width=1200)
    
    def __add_map_img_label(self):
        self.map_img_label = Label(self.map_frame)
        self.map_img_label.place(x=0, y=0)
        self.map_img_label.configure(image=self.map_img,
                                           height=900,
                                           width=1200)

    def __add_character_img_label(self):
        self.character_img_label = Label(self.map_frame)
        self.character_img_label.place(x=600, y=500)
        self.character_img_label.configure(image=self.character_img,
                                           height=56,
                                           width=58)
        self.character_img_label.bind("<B1-Motion>", self.__character_move)

    def __character_move(self, event):
        self.character_img_label.place(x=event.x, y=event.y) 

# This means that two files are not required
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()