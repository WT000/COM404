from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        # Load resources
        self.correct_img = PhotoImage(file="C:/Users/Will/Desktop/COM404/COM404/2-guis/4-images/4-hiding-and-showing/correct.png")
        self.incorrect_img = PhotoImage(file="C:/Users/Will/Desktop/COM404/COM404/2-guis/4-images/4-hiding-and-showing/incorrect.png")
        self.invisible_img = PhotoImage(file="C:/Users/Will/Desktop/COM404/COM404/2-guis/4-images/4-hiding-and-showing/invisible.png")
        
        # Window attributes
        self.title("Hotel GUI")
        self.configure(padx=10, pady=10)

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

        self.__add_check_in_button()

# --------------------------------------------

    def __add_header_label(self):
        self.header_label = Label()
        self.header_label.grid(row=0, column=0, columnspan=3, pady=0)
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
        self.name_entry.bind("<FocusOut>", self.__complete_name_entry)

    def __add_name_img_label(self):
        self.name_img_label = Label()
        self.name_img_label.grid(row=1, column=2, padx=5)
        self.name_img_label.configure(image=self.invisible_img)

    def __complete_name_entry(self, event):
        entered_name = (self.name_entry.get())
        if (entered_name == ""):
            messagebox.showerror("ERROR", "Please enter your name.")
            self.name_img_label.configure(image=self.incorrect_img)

        elif entered_name.isnumeric():
            messagebox.showerror("ERROR", "Please use your real name.")
            self.name_img_label.configure(image=self.incorrect_img)

        else:
            self.name_img_label.configure(image=self.correct_img)

# --------------------------------------------

    def __add_pnumber_label(self):
        self.pnumber_label = Label()
        self.pnumber_label.grid(row=2, column=0, pady=5, sticky=W)
        self.pnumber_label.configure(font="Arial 13", 
                                    text="Passport Number:")

    def __add_pnumber_entry(self):
        self.pnumber_entry = Entry()
        self.pnumber_entry.grid(row=2, column=1, sticky=E + W)
        self.pnumber_entry.bind("<FocusOut>", self.__complete_pnumber_entry)

    def __add_pnumber_img_label(self):
        self.pnumber_img_label = Label()
        self.pnumber_img_label.grid(row=2, column=2, padx=5)

    def __complete_pnumber_entry(self, event):
        entered_pnumber = (self.pnumber_entry.get())
        entered_pnumber_length = len(self.pnumber_entry.get())
        if (entered_pnumber == ""):
            messagebox.showerror("ERROR", "Please enter your passport number.")
            self.pnumber_img_label.configure(image=self.incorrect_img)

        elif not entered_pnumber.isdigit():
            messagebox.showerror("ERROR", "Please enter a real passport number.")
            self.pnumber_img_label.configure(image=self.incorrect_img)

        elif (entered_pnumber_length < 6) or (entered_pnumber_length > 6):
            messagebox.showerror("ERROR", "Please enter an appropriate passport number. It should have 6 numbers.")
            self.pnumber_img_label.configure(image=self.incorrect_img)

        else:
            self.pnumber_img_label.configure(image=self.correct_img)

# --------------------------------------------

    def __add_nights_label(self):
        self.nights_label = Label()
        self.nights_label.grid(row=3, column=0, pady=5, sticky=W)
        self.nights_label.configure(font="Arial 13", 
                                    text="No. of nights:")

    def __add_nights_entry(self):
        self.nights_entry = Entry()
        self.nights_entry.grid(row=3, column=1, sticky=E + W)
        self.nights_entry.bind("<FocusOut>", self.__complete_nights_entry)

    def __add_nights_img_label(self):
        self.nights_img_label = Label()
        self.nights_img_label.grid(row=3, column=2, padx=5)

    def __complete_nights_entry(self, event):
        entered_nights_number = int(self.nights_entry.get())

        if (entered_nights_number < 1):
            messagebox.showerror("ERROR", "It's not possible to stay here for zero or negative nights.")
            self.nights_img_label.configure(image=self.incorrect_img)

        elif (entered_nights_number > 365):
            messagebox.showerror("ERROR", "It's not possible to stay here for longer than a year.")
            self.nights_img_label.configure(image=self.incorrect_img)

        else:
            self.nights_img_label.configure(image=self.correct_img)

# --------------------------------------------

    def __add_check_in_button(self):
        self.check_in_button = Button()
        self.check_in_button.grid(row=4, column=0, columnspan=3)
        self.check_in_button.configure(font="Arial 13",
                                       text="Check In",
                                       width="13")
        self.check_in_button.bind("<ButtonRelease-1>", self.__clicked_complete_button)

    def __clicked_complete_button(self, event):
            messagebox.showinfo("COMPLETE", "You've successfully checked in!")


# This means that two files are not required
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()