from tkinter import *


class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
        ]
    
    def __init__(self, master):
        self.master = master
        self.master.title = "Calculator"
        
        self.total = 0  # Output value for calculation
        self.entered_number = 0  # track entry value
        
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        
        self.label = Label(master, text="Total: ")
        
        vcmd = master.register(self.validate)  # something about wrapping the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        
        # LAYOUT
        
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=3, sticky=E)
        
        self.entry.grid(row=1, column=0)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2)
        
        # END TUTORIAL STUFF HERE
        
    def validate(self, new_text) -> bool:
        if not new_text:
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
    
    def update(self, method: str):
        if method == 'add':
            self.total += self.entered_number
        elif method == 'subtract':
            self.total -= self.entered_number;
        else:
            self.total = 0
        
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
