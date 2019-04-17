from enum import Enum
from tkinter import *


class Action(Enum):
    ADD = 1
    SUB = 2
    MULT = 3
    DIV = 4
    SWAP = 5
    DECIMAL = 6
    SET = 7
    RESET = 9


class Calculator2:
    def __init__(self, master):
        # dunno what master is
        self.master = master
        self.master.title = "Calculator v2"
        
        # entries
        self.entry_value = 0  # Serves as X value
        self.y_value = 0  # acts as a total tracker.  will implement full RPN functionality later
        
        # labels
        self.y_label = Label(master, text="Y: ", anchor=W)
        
        self.y_entry_text = IntVar()
        self.y_entry_text.set(self.y_value)
        self.y_entry = Label(master, textvariable=self.y_entry_text)
        
        self.x_label = Label(master, text="X: ", anchor=W)
        
        vcmd = master.register(self.validate)
        self.x_entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'), justify=RIGHT)
        
        # Operation Buttons
        self.add_button = Button(master, text=" + ", command=lambda: self.update(Action.ADD))
        self.sub_button = Button(master, text=" - ", command=lambda: self.update(Action.SUB))
        self.mult_button = Button(master, text=" * ", command=lambda: self.update(Action.MULT))
        self.div_button = Button(master, text=" \u00F7 ", command=lambda: self.update(Action.DIV))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update(Action.RESET))
        self.button_enter = Button(master, text="Enter", command=lambda: self.update(Action.SET))
        # Number buttons
        # First row
        self.button_7 = Button(master, text="7", command=lambda: self.numbers(7))
        self.button_8 = Button(master, text="8", command=lambda: self.numbers(8))
        self.button_9 = Button(master, text="9", command=lambda: self.numbers(9))
        
        # Second row
        self.button_4 = Button(master, text="4", command=lambda: self.numbers(4))
        self.button_5 = Button(master, text="5", command=lambda: self.numbers(5))
        self.button_6 = Button(master, text="6", command=lambda: self.numbers(6))
        
        # Third row
        self.button_1 = Button(master, text="1", command=lambda: self.numbers(1))
        self.button_2 = Button(master, text="2", command=lambda: self.numbers(2))
        self.button_3 = Button(master, text="3", command=lambda: self.numbers(3))
        
        # Bottom row
        self.button_reg_swap = Button(master, text="Swap", command=lambda: self.update(Action.SWAP))
        self.button_decimal_point = Button(master, text=" . ", command=lambda: self.update(Action.DECIMAL))
        
        # Layout
        self.y_label.grid(row=0, sticky=W + E)
        self.y_entry.grid(row=0, column=2, columnspan=3, sticky=W)
        
        self.x_label.grid(row=1, sticky=W + E)
        self.x_entry.grid(row=1, column=1, columnspan=3)
        
        # Operation button layout
        self.add_button.grid(row=2, column=5, sticky=W + E)
        self.sub_button.grid(row=3, column=5, sticky=W + E)
        self.mult_button.grid(row=4, column=5, sticky=W + E)
        self.div_button.grid(row=5, column=5, sticky=W + E)
        self.reset_button.grid(row=2, column=6, sticky=W + E)
        self.button_enter.grid(row=2, column=0, rowspan=2, sticky=N + S)
        
        # Number button layout
        self.button_7.grid(row=2, column=1, sticky=W + E)
        self.button_8.grid(row=2, column=2, sticky=W + E)
        self.button_9.grid(row=2, column=3, sticky=W + E)
        
        self.button_4.grid(row=3, column=1, sticky=W + E)
        self.button_5.grid(row=3, column=2, sticky=W + E)
        self.button_6.grid(row=3, column=3, sticky=W + E)
        
        self.button_1.grid(row=4, column=1, sticky=W + E)
        self.button_2.grid(row=4, column=2, sticky=W + E)
        self.button_3.grid(row=4, column=3, sticky=W + E)
    
    def validate(self, new_text) -> bool:
        """Validates entry to ensure that the only things that are being entered into the calculator are integers"""
        if not new_text:
            self.entry_value = 0
            return True
        try:
            self.entry_value = int(new_text)
            return True
        except ValueError:
            return False
    
    def update(self, action: Action):
        if action == Action.ADD:
            self.y_value += self.entry_value
            self.entry_value = 0
        elif action == Action.SUB:
            self.y_value -= self.entry_value
            self.entry_value = 0
        elif action == Action.MULT:
            self.y_value *= self.entry_value
            self.entry_value = 0
        elif action == Action.DIV:
            try:
                self.y_value /= self.entry_value
                self.entry_value = 0
            except ZeroDivisionError:
                return
        elif action == Action.SWAP:
            temp = self.entry_value
            self.entry_value = self.y_value
            self.y_value = temp
        elif action == Action.DECIMAL:
            self.x_entry.insert(END, ".")
        elif action == Action.SET:
            self.y_value = self.entry_value
        elif action == Action.RESET:
            self.y_value = 0
            self.entry_value = 0
        
        self.y_entry_text.set(self.y_value)
        self.x_entry.delete(0, END)
    
    def numbers(self, number: int):
        self.x_entry.insert(END, number)


root = Tk()
root.geometry("230x200")
gui = Calculator2(root)
root.mainloop()
