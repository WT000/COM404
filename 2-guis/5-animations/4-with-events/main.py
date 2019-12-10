from tkinter import *
import time

class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        # Load resources
        self.ufo_image = PhotoImage(file="U:/com404/COM404/2-guis/5-animations/4-with-events/UFO.gif")
        
        # Window attributes
        self.title("UFO Animation")
        self.configure(height="500",
                       width="500",
                       bg="#000")

        # Animation attributes (variables)
        self.ufo_x_pos = 0
        self.ufo_x_change = 2
        self.ufo_y_pos = 215
        self.ufo_y_change = 0
        
        # Components
        self.__ufo_image_label()
        self.__add_up_button()
        self.__add_down_button()

        # Start the timer
        self.__tick()

    def __tick(self):
        if (self.ufo_x_pos > 400):
            self.ufo_x_change = -1

        if (self.ufo_x_pos < 0):
            self.ufo_x_change = 1

        # Movement
        self.ufo_x_pos = self.ufo_x_pos + self.ufo_x_change
        self.ufo_y_pos = self.ufo_y_pos + self.ufo_y_change
        self.ufo_image_label.place(x=self.ufo_x_pos,
                                   y=self.ufo_y_pos)
        # Tick
        self.after(8, self.__tick)

    def __ufo_image_label(self):
        self.ufo_image_label = Label()
        self.ufo_image_label.place(x=self.ufo_x_pos,
                                   y=self.ufo_y_pos)
        self.ufo_image_label.configure(image=self.ufo_image)

    def __add_up_button(self):
        self.up_button = Button()
        self.up_button.place(x=100, y=450)
        self.up_button.configure(font="Arial 13",
                                 text="Up",
                                 width="13")
        # Events
        self.up_button.bind("<ButtonRelease-1>", self.__up_button_active)

    def __up_button_active(self, event):
        self.ufo_y_change = -1

    def __add_down_button(self):
        self.down_button = Button()
        self.down_button.place(x=250, y=450)
        self.down_button.configure(font="Arial 13",
                                   text="Down",
                                   width="13")
        # Events
        self.down_button.bind("<ButtonRelease-1>", self.__down_button_active)

    def __down_button_active(self, event):
        self.ufo_y_change = 1

# This means that two files are not required
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()