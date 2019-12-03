from tkinter import *
# Time imported
import time

class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        # Load resources
        self.umbrella_image = PhotoImage(file="U:/com404/COM404/2-guis/5-animations/1-single-object/umbrella.gif")
        
        # Window attributes
        self.title("Umbrella Animation")
        self.configure(height="300",
                       width="300")

        # Animation attributes (variables)
        self.umbrella_x_pos = 130
        self.umbrella_x_change = 2

        self.umbrella_y_pos = 60
        self.umbrella_y_change = 2
        
        # Components
        self.__umbrella_image_label()

        # Start the timer
        self.__tick()

    def __tick(self):
        self.umbrella_x_pos = self.umbrella_x_pos + self.umbrella_x_change
        if (self.umbrella_x_pos > 260):
            self.umbrella_x_change = -2
        elif (self.umbrella_x_pos < 0):
            self.umbrella_x_change = 2
    
        self.umbrella_y_pos = self.umbrella_y_pos + self.umbrella_y_change
        if (self.umbrella_y_pos > 260):
            self.umbrella_y_change = -2
        elif (self.umbrella_y_pos < 0):
            self.umbrella_y_change = 2

        self.umbrella_image_label.place(x=self.umbrella_x_pos, 
                                        y=self.umbrella_y_pos)
        self.after(10, self.__tick)
    
    def __umbrella_image_label(self):
        self.umbrella_image_label = Label()
        self.umbrella_image_label.place(x=self.umbrella_x_pos, 
                                        y=self.umbrella_y_pos)
        self.umbrella_image_label.configure(image=self.umbrella_image)

# This means that two files are not required
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()