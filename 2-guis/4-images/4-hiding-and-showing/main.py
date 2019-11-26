from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        # Load resources
        self.correct_img = PhotoImage(file="U:/com404/COM404/2-guis/4-images/1-loading/ambulance.gif")
        self.incorrect_img = PhotoImage(file="U:/com404/COM404/2-guis/4-images/1-loading/bike.gif")
        
        # Window attributes
        self.title("Hotel GUI")
        self.configure(padx=10, pady=5)

        # Components
        self.__add_header_label()

        self.__add_name_label()
        self.__add_name_entry()
        self.__add_name_img_label()

        self.__add_pnumber_label()
        self.__add_pnumber_entry()
        self.__add_pnumber_img_label()

        self.__add_nights_label()
        self.__add_nights_entry()
        self.__add_nights_img_label()

# --------------------------------------------

    def __add_header_label(self):
        self.header_label = Label()
        self.header_label.grid(row=0, column=0, columnspan=3, pady=5)
        self.header_label.configure(font="Arial 20", 
                                    text="Hotel Check In")

# --------------------------------------------

    def __add_name_label(self):
        self.name_label = Label()
        self.name_label.grid(row=1, column=0, pady=5, sticky=W)
        self.name_label.configure(font="Arial 13", 
                                    text="Name:")

    def __add_name_entry(self):
        self.name_entry = Entry()
        self.name_entry.grid(row=1, column=1, sticky=E + W)

    def __add_name_img_label(self):
        pass
# def image_correct... do this twice

# --------------------------------------------

    def __add_pnumber_label(self):
        self.pnumber_label = Label()
        self.pnumber_label.grid(row=2, column=0, pady=5, sticky=W)
        self.pnumber_label.configure(font="Arial 13", 
                                    text="Passport Number:")

    def __add_pnumber_entry(self):
        self.pnumber_entry = Entry()
        self.pnumber_entry.grid(row=2, column=1, sticky=E + W)

    def __add_pnumber_img_label(self):
        pass

# --------------------------------------------

    def __add_nights_label(self):
        self.nights_label = Label()
        self.nights_label.grid(row=3, column=0, pady=5, sticky=W)
        self.nights_label.configure(font="Arial 13", 
                                    text="No. of nights:")

    def __add_nights_entry(self):
        self.nights_entry = Entry()
        self.nights_entry.grid(row=3, column=1, sticky=E + W)

    def __add_nights_img_label(self):
        pass

# --------------------------------------------

# This means that two files are not required
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()