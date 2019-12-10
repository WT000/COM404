from tkinter import *
# Time imported
import time

class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        # Load resources
        self.redman_image = PhotoImage(file="U:/com404/COM404/2-guis/5-animations/3-varying-ticks/redman.gif")
        self.redmanleft_image = PhotoImage(file="U:/com404/COM404/2-guis/5-animations/3-varying-ticks/redmanleft.gif")

        self.blueman_image = PhotoImage(file="U:/com404/COM404/2-guis/5-animations/3-varying-ticks/blueman.gif")
        self.bluemanleft_image = PhotoImage(file="U:/com404/COM404/2-guis/5-animations/3-varying-ticks/bluemanleft.gif")
        
        # Window attributes
        self.title("Walking Animation")
        self.configure(height="300",
                       width="300")

        # Animation attributes (variables)
        self.redman_x_pos = 1
        self.redman_x_change = 2
        
        self.blueman_x_pos = 220
        self.blueman_x_change = 2
        
        # Components
        self.__redman_image_label()
        self.__blueman_image_label()

        # Tick number
        self.__num_tick = 0
        
        # Start the timer
        self.__tick()

    def __tick(self):
        # Tick counter
        self.__num_tick = self.__num_tick + 1
        
        # Redman
        # -----------------------------------------------------------
        if (self.__num_tick % 2 == 0):
        
            if (self.redman_x_pos > 220):
                self.redman_x_change = -1
                self.redman_image_label.configure(image=self.redmanleft_image)
            
            elif (self.redman_x_pos < 0):
                self.redman_x_change = 1
                self.redman_image_label.configure(image=self.redman_image)

            self.redman_x_pos = self.redman_x_pos + self.redman_x_change
            self.redman_image_label.place(x=self.redman_x_pos)
        
        # Blueman
        # -----------------------------------------------------------
        if (self.__num_tick % 4 == 0):
        
            if (self.blueman_x_pos > 220):
                self.blueman_x_change = -1
                self.blueman_image_label.configure(image=self.bluemanleft_image)
            
            elif (self.blueman_x_pos < 0):
                self.blueman_x_change = 1
                self.blueman_image_label.configure(image=self.blueman_image)

            self.blueman_x_pos = self.blueman_x_pos + self.blueman_x_change
            self.blueman_image_label.place(x=self.blueman_x_pos)
        # -----------------------------------------------------------
        self.after(5, self.__tick)
    
    def __redman_image_label(self):
        self.redman_image_label = Label()
        self.redman_image_label.place(x=self.redman_x_pos,
                                      y=15)
        self.redman_image_label.configure(image=self.redman_image)
    
    def __blueman_image_label(self):
        self.blueman_image_label = Label()
        self.blueman_image_label.place(x=self.blueman_x_pos,
                                       y=170)
        self.blueman_image_label.configure(image=self.bluemanleft_image)

# This means that two files are not required
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()