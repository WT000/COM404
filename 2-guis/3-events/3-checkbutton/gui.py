from tkinter import *
from tkinter import messagebox

# Setting the GUI Class
class Gui(Tk):

    def __init__(self):
        super().__init__()

        # Window attributes
        self.title("Passport Check")
        self.configure(padx=10, pady=5)

        # GUI Components
        self.__add_header_label()
        self.__add_q1_label()
        self.__add_q1_y_checkbutton()
        self.__add_q1_n_checkbutton()
        self.__add_q2_label()
        self.__add_q2_y_checkbutton()
        self.__add_q2_n_checkbutton()
        self.__add_q3_label()
        self.__add_q3_y_checkbutton()
        self.__add_q3_n_checkbutton()
        self.__add_complete_button()

    def __add_header_label(self):
        self.header_label = Label()
        self.header_label.grid(row=0, column=0, columnspan=2)
        self.header_label.configure(font="Arial 20",
                                    text="Passport Checker",
                                    bg="#eee")

# ------------------------------------------------------

    def __add_q1_label(self):
        self.q1_label = Label()
        self.q1_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.q1_label.configure(font="Arial 11",
                                    text="1. Photo matches face?",
                                    bg="#eee")

    def __add_q1_y_checkbutton(self):
        self.q1_y_value = IntVar()
        self.q1_y_checkbutton = Checkbutton(variable=self.q1_y_value)
        self.q1_y_checkbutton.grid(row=2, column=1)
        self.q1_y_checkbutton.configure(text="Yes")

    def __add_q1_n_checkbutton(self):
        self.q1_n_checkbutton = Checkbutton()
        self.q1_n_checkbutton.grid(row=2, column=1, sticky=E)
        self.q1_n_checkbutton.configure(text="No")

# ------------------------------------------------------

    def __add_q2_label(self):
        self.q2_label = Label()
        self.q2_label.grid(row=3, column=0, columnspan=2, sticky=W)
        self.q2_label.configure(font="Arial 11",
                                    text="2. Passport has at least 6 months validity?",
                                    bg="#eee")

    def __add_q2_y_checkbutton(self):
        self.q2_y_value = IntVar()
        self.q2_y_checkbutton = Checkbutton(variable=self.q2_y_value)
        self.q2_y_checkbutton.grid(row=4, column=1)
        self.q2_y_checkbutton.configure(text="Yes")

    def __add_q2_n_checkbutton(self):
        self.q2_n_checkbutton = Checkbutton()
        self.q2_n_checkbutton.grid(row=4, column=1, sticky=E)
        self.q2_n_checkbutton.configure(text="No")

# ------------------------------------------------------

    def __add_q3_label(self):
        self.q3_label = Label()
        self.q3_label.grid(row=5, column=0, columnspan=2, sticky=W)
        self.q3_label.configure(font="Arial 11",
                                    text="3. Visa, if required, is valid? (leave blank if not required)",
                                    bg="#eee")

    def __add_q3_y_checkbutton(self):
        self.q3_y_value = IntVar()
        self.q3_y_checkbutton = Checkbutton(variable=self.q3_y_value)
        self.q3_y_checkbutton.grid(row=6, column=1)
        self.q3_y_checkbutton.configure(text="Yes")

    def __add_q3_n_checkbutton(self):
        self.q3_n_value = IntVar()
        self.q3_n_checkbutton = Checkbutton(variable=self.q3_n_value)
        self.q3_n_checkbutton.grid(row=6, column=1, sticky=E)
        self.q3_n_checkbutton.configure(text="No")

# ------------------------------------------------------

    def __add_complete_button(self):
        self.complete_button = Button()
        self.complete_button.grid(row=7, column=0, columnspan=2)
        self.complete_button.configure(font="Arial 11",
                                     text="Check",
                                     width="10")
        self.complete_button.bind("<ButtonRelease-1>", self.__clicked_complete_button)

    def __clicked_complete_button(self, event):
        q1_complete = int(self.q1_y_value.get())
        q2_complete = int(self.q2_y_value.get())
        q3_complete = int(self.q3_y_value.get())
        q3_complete2 = int(self.q3_n_value.get())

        if ((q1_complete == 1) and (q2_complete == 1) and (q3_complete2 == 0)) or ((q1_complete == 1) and (q2_complete == 1) and q3_complete == 1):
            messagebox.showinfo("CHECK COMPLETE", "Your Passport is genuine, you may continue.")
        
        else:
            messagebox.showerror("CHECK COMPLETE", "Your Passport is not genuine, please wait here for assistance.")