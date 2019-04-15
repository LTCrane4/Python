from tkinter import *


class Calculator2:
    def __init__(self, master):
        self.master = master
        self.master.title = 'Calculator'
        
        self.reg_x = 0  # bottom register
        self.reg_y = 0  # top register
        
        # X register labels
        self.reg_x_text = IntVar()
        self.reg_x_text.set(self.reg_x)
        self.reg_x_label = Label(master, textvariable=self.reg_x_text)
        
        # Y register labels
        self.reg_y_text = IntVar()
        self.reg_y_text.set(self.reg_y)
        self.reg_y_label = Label(master, textvariable=self.reg_y_text)
        
        # informational labels for registers
        self.reg_x_id = Label(master, text="X: ")
        self.reg_y_id = Label(master, text="Y: ")
        
        # input handling wrapping
        cmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(cmd, "%P"), justify=RIGHT)  # dunno what this does tbh
        
        # set buttons
        self.add_button = Button(master, text="+", command=lambda: self.update('add'))
        self.sub_button = Button(master, text="-", command=lambda: self.update('sub'))
        self.mult_button = Button(master, text="*", command=lambda: self.update('times'))
        self.div_button = Button(master, text='/', command=lambda: self.update('div'))
        self.enter_button = Button(master, text="Enter", command=lambda: self.update('enter'))
        
        # set layout
        self.reg_x_id.grid(row=1, column=0, columnspan=2, sticky=W)
        self.reg_y_id.grid(row=0, column=0, columnspan=2, sticky=W)
        self.entry.grid(row=1, column=2, columnspan=2, sticky=E)
        self.reg_y_label.grid(row=0, column=2, columnspan=2, sticky=W + E)
        self.
    
    def validate(self, new_text) -> bool:
        return True
    
    def update(self, method: str) -> None:
        """Updates the registers in the calculator.  """
        if method == 'add':
            self.reg_x += self.reg_y
            self.reg_y = 0
        elif method == 'sub':
            self.reg_x -= self.reg_y
            self.reg_y = 0
        elif method == 'times':
            self.reg_x *= self.reg_y
            self.reg_y = 0
        elif method == 'div':
            if self.reg_y != 0:
                self.reg_x /= self.reg_y
                self.reg_y = 0
        elif method == 'enter':
            self.reg_y = self.entry_value
        else:
            self.reg_x = 0
            self.reg_y = 0


root = Tk()
root.geometry("300x300")
my_gui = Calculator2(root)
root.mainloop()
