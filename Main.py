from tkinter import *

root = Tk()


class Calculate:

    # ListOfString -> String
    # puts the individual nums together into one num and clears the list

    def __init__(self):
        self.s = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "="
        self.num_list = []
        self.add_list = []
        self.add = 0
        self.x = None

    def merge_nums(self):
        self.x = ""
        for i in self.num_list:
            self.x += str(i)
        self.num_list.clear()
        self.add_list.append(self.x)

    # ListOfString -> Integer
    # Assume it is all numbers meant to be added
    # takes the all items in the ListOfString and adds them together to produce the answer

    def add_input(self):
        self.merge_nums()
        for i in self.add_list:
            self.add += int(i)
        self.add_list.clear()
        return self.add

    # String -> Integer
    # Assume all Inputs are [0-9], +, and "="
    # Takes the Input from num_pad() and produces the answer\

    def command(self, s):
        if s == "+":
            self.merge_nums()
        elif s == "=":
            try:
                label = Label(root, text=self.add_input())
                label.grid(row=0, column=3)
                self.add = 0
            except ValueError:
                self.add_list = []
        else:
            self.num_list.append(s)


# These are for executing the Buttons and calling the function command with argument
    def execute1(self):
        self.command(self.s[1])

    def execute2(self):
        self.command(self.s[2])

    def execute3(self):
        self.command(self.s[3])

    def execute4(self):
        self.command(self.s[4])

    def execute5(self):
        self.command(self.s[5])

    def execute6(self):
        self.command(self.s[6])

    def execute7(self):
        self.command(self.s[7])

    def execute8(self):
        self.command(self.s[8])

    def execute9(self):
        self.command(self.s[9])

    def execute0(self):
        self.command(self.s[0])

    def execute_plus(self):
        self.command(self.s[10])

    def execute_equal(self):
        self.command(self.s[11])

    def execute_clear(self):
        self.command(self.s[12])


# produces Nums at the correct point

def num_pad(s, row, column, c):
    button1 = Button(root, text=s, padx=50, pady=50, command=c)
    button1.grid(row=row, column=column)


calculate = Calculate()
e = Entry(root)

num_pad("1", 1, 1, calculate.execute1)
num_pad("2", 1, 2, calculate.execute2)
num_pad("3", 1, 3, calculate.execute3)
num_pad("4", 2, 1, calculate.execute4)
num_pad("5", 2, 2, calculate.execute5)
num_pad("6", 2, 3, calculate.execute6)
num_pad("7", 3, 1, calculate.execute7)
num_pad("8", 3, 2, calculate.execute8)
num_pad("9", 3, 3, calculate.execute9)
num_pad("+", 4, 1, calculate.execute_plus)
num_pad("0", 4, 2, calculate.execute0)
num_pad("=", 4, 3, calculate.execute_equal)
root.mainloop()
