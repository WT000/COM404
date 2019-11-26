from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        # Load resources
        self.ambulance_img = PhotoImage(file="U:/com404/COM404/2-guis/4-images/1-loading/ambulance.gif")
        self.bike_img = PhotoImage(file="U:/com404/COM404/2-guis/4-images/1-loading/bike.gif")
        self.plane_img = PhotoImage(file="U:/com404/COM404/2-guis/4-images/1-loading/plane.gif")
        
        # Window attributes
        self.title("Transportation")

        # Components
        self.__add_header_label()
        self.__add_ambulance_img_label()
        self.__add_bike_img_label()
        self.__add_plane_img_label()

    def __add_header_label(self):
        self.header_label = Label()
        self.header_label.grid(row=0, column=0, columnspan=3)
        self.header_label.configure(font="Arial 20", 
                                    text="TRANSPORT")
    
    def __add_ambulance_img_label(self):
        self.ambulance_img_label = Label()
        self.ambulance_img_label.grid(row=1, column=0)
        self.ambulance_img_label.configure(image=self.ambulance_img,
                                           height=60,
                                           width=60)

    def __add_bike_img_label(self):
        self.bike_img_label = Label()
        self.bike_img_label.grid(row=1, column=1)
        self.bike_img_label.configure(image=self.bike_img,
                                           height=60,
                                           width=60)

    def __add_plane_img_label(self):
        self.plane_img_label = Label()
        self.plane_img_label.grid(row=1, column=2)
        self.plane_img_label.configure(image=self.plane_img,
                                           height=60,
                                           width=60)

# This means that two files are not required
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()