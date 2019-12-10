# notes to help
# when wanting to change a label or message make sure to use self.name_label.configure(text="")

# use .format, it's in 1-classes-and-objects

# tick always goes before anything

# layout:
############################
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
############################

    def __add_original_option_menu(self):
        self.SelectionVar = StringVar()
        self.SelectionVar.set("GBP")
        self.original_option_menu = Spinbox(self.outer_frame, textvariable=self.SelectionVar, values=("GBP", "Euro"))
        self.original_option_menu(row=x, column=x, columnspan=x) # could have sticky too
        self.original_option_menu(e.g. bd, bg, colour, width, height)

later on...

    def __whatever(self, event):
        original_value = self.original_option_menu.get()
        when getting am amount make sure to do int
        amount = int(amount_entry)

!= means not equal to
== means equal to