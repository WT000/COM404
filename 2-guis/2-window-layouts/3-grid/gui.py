# Importing GUI code
from tkinter import *

# class Gui Inherits from Tk
class Gui(Tk):
    def __init__(self): # Init is a constructor
        super().__init__() # Super means that it inherits from Tk

        # Set window attributes
        self.geometry("390x120")
        self.title("Newsletter")

        # Add window components REMEMBER TO KEEP THESE IN ORDER OF APPERANCE
        self.__add_heading_label()
        self.__add_message_label()       
        self.__add_email_frame()  
        self.__add_email_label() 
        self.__add_input_entry()    
        self.__add_submit_button()

    # Window component functions
    def __add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2) #sticky can keep it N, E, S or W
        # style
        self.heading_label.configure(font="Arial 20", 
                                     text="RECIEVE OUR NEWSLETTER")
        # events

    def __add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.grid(row=2, column=0, columnspan=2)
    
    def __add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        self.email_label.configure(font="Arial 11",
                                     text="Email:")
    
    def __add_input_entry(self):
        self.input_entry = Entry(self.email_frame)
        self.input_entry.pack(side=RIGHT)

    def __add_message_label(self):
        self.message_label = Label()
        self.message_label.grid(row=1, column=0, columnspan=2)
        self.message_label.configure(font="Arial 11",
                                     text="Please enter your email below to recieve our newsletter.")

    def __add_submit_button(self):
        self.submit_button = Button()
        self.submit_button.grid(row=3, column=0, columnspan=2)
        self.submit_button.configure(font="Arial 11",
                                     text="Subscribe",
                                     width="40")