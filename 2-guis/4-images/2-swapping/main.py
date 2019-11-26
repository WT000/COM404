from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        # Load resources
        self.cactus1_img = PhotoImage(file="U:/com404/COM404/2-guis/4-images/2-swapping/cactus1.gif")
        self.cactus2_img = PhotoImage(file="U:/com404/COM404/2-guis/4-images/2-swapping/cactus2.gif")

        # Window attributes
        self.title("Cactus Leaves")
        self.configure(padx=10, pady=5)

        # Components
        self.__add_header_label()
        self.__add_cactus_img_label()
        self.__add_flip_button()

    def __add_header_label(self):
        self.header_label = Label()
        self.header_label.grid(row=0, column=0)
        self.header_label.configure(font="Arial 20", 
                                    text="Cactus Leaves")

    def __add_cactus_img_label(self):
        self.cactus_img_label = Label()
        self.cactus_img_label.grid(row=1, column=0)
        self.cactus_img_label.configure(image=self.cactus1_img,
                                           height=150,
                                           width=250)

    def __add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=0, pady=5)
        self.flip_button.configure(font="Arial 15",
                                     text="Flip",
                                     width="10")
        self.flip_button.bind("<ButtonRelease-1>", self.__left_clicked_flip_button)
        self.flip_button.bind("<ButtonRelease-3>", self.__right_clicked_flip_button)

    def __left_clicked_flip_button(self, event):
        self.cactus_img_label.configure(image = self.cactus2_img)

    def __right_clicked_flip_button(self, event):
        self.cactus_img_label.configure(image = self.cactus1_img)

# This means that two files are not required
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()