from tkinter import *
# Time imported
import time

class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        # Load resources
        self.rball_image = PhotoImage(file="U:/com404/COM404/2-guis/5-animations/2-multiple-components/rball.gif")
        self.bball_image = PhotoImage(file="U:/com404/COM404/2-guis/5-animations/2-multiple-components/bball.gif")
        
        # Window attributes
        self.title("Ball Animation")
        self.configure(height="300",
                       width="300")

        # Animation attributes (variables)
        self.rball_x_pos = 180
        self.rball_x_change = -2
        self.rball_y_pos = 30
        self.rball_y_change = -2
        
        self.bball_x_pos = 130
        self.bball_x_change = 2
        self.bball_y_pos = 60
        self.bball_y_change = 2
        
        # Components
        self.__red_ball_image_label()
        self.__blue_ball_image_label()

        # Start the timer
        self.__tick()

    def __tick(self):
        # -----------------------------------------------------------
        self.rball_x_pos = self.rball_x_pos + self.rball_x_change
        if (self.rball_x_pos > 270):
            self.rball_x_change = -2
        elif (self.rball_x_pos < 0):
            self.rball_x_change = 2
    
        self.rball_y_pos = self.rball_y_pos + self.rball_y_change
        if (self.rball_y_pos > 270):
            self.rball_y_change = -2
        elif (self.rball_y_pos < 0):
            self.rball_y_change = 2

        self.red_ball_image_label.place(x=self.rball_x_pos, 
                                         y=self.rball_y_pos)
        # -----------------------------------------------------------
        self.bball_x_pos = self.bball_x_pos + self.bball_x_change
        if (self.bball_x_pos > 270):
            self.bball_x_change = -2
        elif (self.bball_x_pos < 0):
            self.bball_x_change = 2
    
        self.bball_y_pos = self.bball_y_pos + self.bball_y_change
        if (self.bball_y_pos > 270):
            self.bball_y_change = -2
        elif (self.bball_y_pos < 0):
            self.bball_y_change = 2

        self.blue_ball_image_label.place(x=self.bball_x_pos, 
                                         y=self.bball_y_pos)
        # -----------------------------------------------------------
        self.after(10, self.__tick)
    
    def __red_ball_image_label(self):
        self.red_ball_image_label = Label()
        self.red_ball_image_label.place(x=self.rball_x_pos,
                                        y=self.rball_y_pos)
        self.red_ball_image_label.configure(image=self.rball_image)
    
    def __blue_ball_image_label(self):
        self.blue_ball_image_label = Label()
        self.blue_ball_image_label.place(x=self.bball_x_pos, 
                                         y=self.bball_y_pos)
        self.blue_ball_image_label.configure(image=self.bball_image)

# This means that two files are not required
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()