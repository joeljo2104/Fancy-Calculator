''''
C#0028ffits:

Developed by James George

This is a Fancy calculator performing the basic mathematical operations made using Tkinter module using OOP principles of the python programming language did as part of my self made projects.'''


from tkinter import Button, Label, Entry, Tk


class Calculator:

    # Constructor or the initializer method which is automatically called when this class is instantiated or when an instance / object is created

    def __init__(self, master):

        # List to be accessible everywhere.

        self.list = []

        # Global variable i which tracks the index position of elements within the list.

        self.i = -1

        # The final result.

        self.result = 0

        # Building up the UI part.

        # Setting the title which appears on the title bar of the window
        master.title('Calculator')

        # Setting both the width and height to 400 pixels
        master.geometry('400x400')

        # Setting background colour of the whole window
        master.config(bg='#24009c')

        # Preventing the windows from being resized.
        master.resizable(False, False)

        # Title
        self.heading_label = Label(
            text="Calculator", font='times 45 bold', fg='white', bg='#24009c')
        self.heading_label.grid(row=0, column=0, columnspan=4)


        # TextField where the operations performed will appear
        self.textfield = Entry(font='times 35 bold', background="#021759",
                               width=16, relief='flat')
        self.textfield.grid(row=2, column=0, columnspan=4)

        # Buttons being instantiated from the Button class by passing the requried parameters and placing them in order using the grid() method

        # First row

        self.seven = Button(text="7", font='times 25 bold', relief='flat',
                            width=4,   fg='#10eaf0', bg='#0028ff', command=self.seven_clicked)
        self.seven.grid(row=3, column=0)

        self.eigth = Button(text="8", font='times 25 bold', relief='flat',
                            width=4,   fg='#10eaf0', bg='#0028ff', command=self.eight_clicked)
        self.eigth.grid(row=3, column=1)

        self.nine = Button(text="9", font='times 25 bold', relief='flat',
                           width=4,   fg='#10eaf0', bg='#0028ff', command=self.nine_clicked)
        self.nine.grid(row=3, column=2)

        self.addition = Button(text="+", font='times 25 bold', relief='flat',
                               width=4,   fg='#24009c', bg='#10eaf0', command=self.add)
        self.addition.grid(row=3, column=3)

        # Second row

        self.four = Button(text="4", font='times 25 bold', relief='flat',
                           width=4,   fg='#10eaf0', bg='#0028ff', command=self.four_clicked)
        self.four.grid(row=4, column=0)

        self.five = Button(text="5", font='times 25 bold', relief='flat',
                           width=4,   fg='#10eaf0', bg='#0028ff', command=self.five_clicked)
        self.five.grid(row=4, column=1)

        self.six = Button(text="6", font='times 25 bold', relief='flat',
                          width=4,   fg='#10eaf0', bg='#0028ff', command=self.six_clicked)
        self.six.grid(row=4, column=2)

        self.subtraction = Button(text="-", font='times 25 bold', relief='flat',
                                  width=4,   fg='#24009c', bg='#10eaf0', command=self.subtract)
        self.subtraction.grid(row=4, column=3)

        # Third row

        self.one = Button(text="1", font='times 25 bold', relief='flat',
                          width=4,   fg='#10eaf0', bg='#0028ff', command=self.one_clicked)
        self.one.grid(row=5, column=0)

        self.two = Button(text="2", font='times 25 bold', relief='flat',
                          width=4,   fg='#10eaf0', bg='#0028ff', command=self.two_clicked)
        self.two.grid(row=5, column=1)

        self.three = Button(text="3", font='times 25 bold', relief='flat',
                            width=4,   fg='#10eaf0', bg='#0028ff', command=self.three_clicked)
        self.three.grid(row=5, column=2)

        self.multiplication = Button(text="*", font='times 25 bold', relief='flat',
                                     width=4,   fg='#24009c', bg='#10eaf0', command=self.multiply)
        self.multiplication.grid(row=5, column=3)

        # Fourth row

        self.negation = Button(text="+/-", font='times 25 bold', relief='flat',
                               width=4,   fg='#0028ff', bg='#10eaf0', command=self.negate)
        self.negation.grid(row=6, column=0)

        self.ans = Button(text="=", font='times 25 bold', relief='flat',
                          width=4,   fg='#0028ff', bg='#10eaf0', command=self.equals)
        self.ans.grid(row=6, column=1)

        self.delete = Button(text="DEL", font='times 25 bold', relief='flat',
                             width=4,   fg='#0028ff', bg='#10eaf0', command=self.clear)
        self.delete.grid(row=6, column=2)

        self.division = Button(text="/", font='times 25 bold', relief='flat',
                               width=4,   fg='#24009c', bg='#10eaf0', command=self.divide)
        self.division.grid(row=6, column=3)

    # These functions are invoked when buttons from 1-9 are tapped

    def one_clicked(self):
        self.textfield.insert(16, "1")

    def two_clicked(self):
        self.textfield.insert(16, "2")

    def three_clicked(self):
        self.textfield.insert(16, "3")

    def four_clicked(self):
        self.textfield.insert(16, "4")

    def five_clicked(self):
        self.textfield.insert(16, "5")

    def six_clicked(self):
        self.textfield.insert(16, "6")

    def seven_clicked(self):
        self.textfield.insert(16, "7")

    def eight_clicked(self):
        self.textfield.insert(16, "8")

    def nine_clicked(self):
        self.textfield.insert(16, "9")

    # Mathematical operations performed by these functions are invoked by their respective button clicks.

    def add(self):

        self.i += 1

        try:

            self.list.append(int(self.textfield.get()))

        except:

            self.list.append(0)

        self.btn_clicked = 'addition'

        if self.i is 0:

            self.textfield.delete(0, 16)
            self.result = self.list[self.i]

        else:

            self.textfield.delete(0, 16)

            if self.list[self.i] is not self.result:

                self.result += self.list[self.i]

    def subtract(self):

        self.i += 1

        try:

            self.list.append(int(self.textfield.get()))

        except:

            self.list.append(0)

        self.btn_clicked = 'subtraction'

        print(self.list, ", ", self.result, ", ", self.list[self.i])

        if self.i is 0:

            self.textfield.delete(0, 16)
            self.result = self.list[self.i]

        else:

            self.textfield.delete(0, 16)

            if self.list[self.i] is not self.result:

                self.result -= self.list[self.i]

    def multiply(self):

        self.i += 1

        try:

            self.list.append(int(self.textfield.get()))

        except:

            self.list.append(0)

        self.btn_clicked = 'multiplication'

        if self.i is 0:

            self.textfield.delete(0, 16)

            self.result = self.list[self.i]

        else:

            self.textfield.delete(0, 16)

            if self.list[self.i] is not self.result:

                self.result *= self.list[self.i]

    def divide(self):

        self.i += 1

        try:

            self.list.append(int(self.textfield.get()))

        except:

            self.list.append(0)

        self.btn_clicked = 'division'

        if self.i is 0:

            self.result = self.list[self.i]

            self.textfield.delete(0, 16)

        else:

            try:
                if self.list[self.i] is not self.result:

                    self.result //= self.list[self.i]

            except ZeroDivisonError:

                self.messagebox.showwarning(
                    "warning", "Division by zero is not possible!")

            self.textfield.delete(0, 16)

    def negate(self):

        self.textfield.delete(0, 16)

        try:

            self.element = int(self.textfield.get())

            print(self.element)

            self.textfield.insert(16, self.element*-1)

        except:

            print('Exception')

    def equals(self):

        try:

            self.list.append(int(self.textfield.get()))

            if self.btn_clicked is 'addition':

                self.result += int(self.textfield.get())

            elif self.btn_clicked is 'subtraction':

                self.result -= int(self.textfield.get())

            elif self.btn_clicked is 'multiplication':

                self.result *= int(self.textfield.get())

            else:

                self.result //= int(self.textfield.get())

            self.textfield.delete(0, 16)

            self.textfield.insert(16, self.result)

        except:

            pass

    def clear(self):

        print(self.result)
        print(self.list)

        self.i = -1

        self.list = []

        self.result = 0

        self.textfield.delete(0, 20)


if __name__ == '__main__':

    root = Tk()
    gui = Calculator(root)
    root.mainloop()
