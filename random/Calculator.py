from tkinter import *


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.master.title = "Calculator"
        
        self.total = 0  # Output value for calculation
        self.entry_value = 0  # track entry value
        
        # label for total
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        
        self.entry_label_text = IntVar()
        self.entry_label_text.set(self.entry_value)
        self.entry_label = Label(master, textvariable=self.entry_value)
        
        self.label = Label(master, text="Total: ")
        
        vcmd = master.register(self.validate)  # something about wrapping the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        
        # LAYOUT
        
        # OPERATIONS BUTTONS
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.multiplication_button = Button(master, text="*", command=lambda: self.update("mult"))
        self.division_button = Button(master, text="/", command=lambda: self.update("div"))
        
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        
        # GRID LAYOUT
        self.label.grid(row=0, column=0, columnspan=2, sticky=N)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=S)
        
        self.entry.grid(row=1, column=0)
        self.add_button.grid(row=2, column=0, columnspan=2, sticky=W + E)
        self.subtract_button.grid(row=2, column=2, columnspan=2, sticky=W + E)
        self.multiplication_button.grid(row=2, column=4, columnspan=2, sticky=W + E)
        self.division_button.grid(row=2, column=6, columnspan=2, sticky=W + E)
        self.reset_button.grid(row=2, column=8, columnspan=2, sticky=W + E)
    
    # END TUTORIAL STUFF HERE
    
    def validate(self, new_text) -> bool:
        if not new_text:
            self.entry_value = 0
            return True
        try:
            self.entry_value = int(new_text)
            return True
        except ValueError:
            return False
    
    def update(self, method: str) -> None:
        if method == 'add':
            self.total += self.entry_value
        elif method == 'subtract':
            self.total -= self.entry_value
        elif method == 'mult':
            self.total *= self.entry_value
        elif method == 'div':
            if self.entry_value != 0:
                self.total /= self.entry_value
        elif method == 'enter':
            self.total = self.entry_value
        else:
            self.total = 0
        
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)


root = Tk()
root.geometry('300x300')

my_gui = MyFirstGUI(root)
root.mainloop()
