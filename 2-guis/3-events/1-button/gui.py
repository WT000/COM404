# Importing tkinter
from tkinter import *

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
        #create
        self.header_label = Label()
        self.header_label.grid(row=0, column=0)
        #style
        self.header_label.configure(font="Arial 25",
                                   text="Entrance Ticket")

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
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0, pady=6)
        self.buy_button.configure(font="Arial 13",
                                  text="Buy",
                                  width="10")