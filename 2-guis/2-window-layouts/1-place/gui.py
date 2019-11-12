# Importing GUI code
from tkinter import *

# class Gui Inherits from Tk
class Gui(Tk):
    def __init__(self): # Init is a constructor
        super().__init__() # Super means that it inherits from Tk

        # Set window attributes
        self.geometry("450x180")
        self.title("Newsletter")

        # Add window components
        self.__add_heading_label()
        self.__add_input_entry()
        self.__add_email_label()
        self.__add_message_label()
        self.__add_submit_button()

    # Window component functions
    def __add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.place(x=30, y=10)
        # style
        self.heading_label.configure(font="Arial 20", 
                                     text="RECIEVE OUR NEWSLETTER")
        # events

    def __add_email_label(self):
        self.email_label = Label()
        self.email_label.place(x=110, y=99)
        self.email_label.configure(font="Arial 11",
                                     text="Email:")
    
    def __add_input_entry(self):
        self.input_entry = Entry()
        self.input_entry.place(x=160, y=102)

    def __add_message_label(self):
        self.message_label = Label()
        self.message_label.place(x=40, y=60)
        self.message_label.configure(font="Arial 11",
                                     text="Please enter your email below to recieve our newsletter.")

    def __add_submit_button(self):
        self.submit_button = Button()
        self.submit_button.place(x=43, y=140)
        self.submit_button.configure(font="Arial 11",
                                     text="Subscribe",
                                     width="40")