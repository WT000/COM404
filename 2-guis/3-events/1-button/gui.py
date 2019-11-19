# Importing tkinter and message box
from tkinter import *
from tkinter import messagebox

# Setting the GUI Class
class Gui(Tk):

    def __init__(self):
        super().__init__()

        # Window attributes
        self.geometry("230x150")
        self.title("Tickets")

        # GUI Components
        self.__add_header_label()
        self.__add_ticket_label()
        self.__add_ticket_entry()
        self.__add_buy_button()

    def __add_header_label(self):
        self.header_label = Label()
        self.header_label.grid(row=0, column=0)
        self.header_label.configure(font="Arial 25",
                                    text="Entrance Ticket",
                                    bg="#eee")

    def __add_ticket_label(self):
        self.ticket_label = Label()
        self.ticket_label.grid(row=1, column=0, sticky=N)
        self.ticket_label.configure(font="Arial 11",
                                    text="How many tickets are needed?")

    def __add_ticket_entry(self):
        self.ticket_entry = Entry()
        self.ticket_entry.grid(row=2, column=0, pady=6)
        self.ticket_entry.configure(width="30")

    def __add_buy_button(self):
        #create
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0, pady=6)
        #styles
        self.buy_button.configure(font="Arial 13",
                                  text="Buy",
                                  width="10",
                                  bg="#fcc")
        #events
        self.buy_button.bind("<ButtonRelease-1>", self.__clicked_buy_button)

    def __clicked_buy_button(self, event):
        if (int(self.ticket_entry.get()) == 1):
            messagebox.showinfo("Complete!", "You have purchased 1 ticket!")
        elif (int(self.ticket_entry.get()) >= 1):
            messagebox.showinfo("Complete!", "You have purchased " + self.ticket_entry.get() + " tickets!")
        else:
            messagebox.showerror("ERROR", "You entered an invalid number of tickets.")