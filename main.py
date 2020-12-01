from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.form = "0"
        self.lbl = Label(text=self.form,
                         font=(21), bg="#555",
                         foreground="#FFF")
        self.lbl.place(x=11, y=50)

        buttons = [
            "%", "CE", "C", "DEL",
            "1/x", "X^2", "2√x", "*",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "+/-", "0", ",", "="
        ]

        x = 10
        y = 140
        for button in buttons:
            com = lambda x=button: self.logicalc(x)
            Button(text=button,
                   bg="#790",
                   font=(15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.form = ""
        elif operation == "DEL":
            self.form = self.form[0:-1]
        elif operation == "X^2":
            self.form = str(eval(self.form)**2)
        elif operation == "2√x":
            self.form = str(eval(self.form)**0.5)
        elif operation == "1/x":
            self.form = str(1/(eval(self.form)))
        elif operation == "=":
            self.form = str(eval(self.form))
        elif operation == ",":
            self.form = str(eval(self.form)*10/10)
        elif operation == "+/-":
            self.form = str(eval(self.form)*(-1))
        else:
            if self.form == "0":
                self.form = ""
            self.form += operation
        self.update()

    def update(self):
        if self.form == "":
            self.form = "0"
        self.lbl.configure(text=self.form)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#555"
    root.geometry("485x630")
    root.title("Калькулятор")
    app = Main(root)
    app.pack()
    root.mainloop()