from tkinter import *
from tkinter import messagebox as msg

# globals variables
players: list = []

top = Tk()
top.geometry("400x550")
top.resizable(False, False)
top.title("KENKAN-Claculater")

header_frame = Frame(top)
header_frame.pack(side=TOP, pady=10)

headings_frame = Frame(top, bg="gray")
headings_frame.columnconfigure(index=(0, 1, 2, 3), weight=1, uniform='equal')
headings_frame.pack(side=TOP, fill=X, pady=(10, 0))

bottom_frame = Frame(top)
bottom_frame.pack(side=BOTTOM, fill=X, pady=10, padx=10)


class Player:

    def __init__(self, name: str):
        self.point = 0
        self.name = name

        self.e_point = StringVar()
        self.e_point.set('0')
        self.e_total = IntVar()
        self.e_total.set(0)
        self.e_last_point = IntVar()
        self.e_last_point.set(0)
        self.last_point = 0
        self.total = 0
        self.row()

    def calculate(self) -> None:
        self.point = self.e_point.get()
        if self.point != '' and is_digits(self.point):
            self.total += int(self.point)
            self.last_point = int(self.point)
            self.e_point.set('0')
            self.e_total.set(self.total)
            self.e_last_point.set(self.last_point)
        elif self.point == '':
            self.e_point.set('0')
            self.point = 0
        else:
            msg.showerror('Error', 'Integer only!!')

    def row(self):
        frame = Frame(top)
        frame.columnconfigure(index=(0, 1, 2, 3), weight=1, uniform='equal')

        label_name = Label(frame, text=f'{self.name}', font=("Times New Roman", 10), bg='gray')
        label_name.grid(row=0, column=0, pady=2, padx=2, ipady=2, sticky=NSEW)

        entry_point = Entry(frame, textvariable=self.e_point, justify=CENTER, font=("Times New Roman", 10))
        entry_point.grid(row=0, column=1, pady=2, padx=2, ipady=2, sticky=NSEW)

        label_total = Label(frame, textvariable=self.e_total, font=("Times New Roman", 10), bg='gray')
        label_total.grid(row=0, column=2, pady=2, padx=2, ipady=2, sticky=NSEW)

        label_last_point = Label(frame, textvariable=self.e_last_point, font=("Times New Roman", 10), bg='gray')
        label_last_point.grid(row=0, column=3, pady=2, padx=2, ipady=2, sticky=NSEW)
        frame.pack(fill=X)

    def __repr__(self) -> str:
        return f"Player(name:{self.name}, point:{self.point}, total:{self.total}, last_point:{self.last_point})"


def is_valid(text: str):
    if len(text) < 3:
        msg.showerror("Name", "The name must be at least 3 characters long.")
    elif len(text) > 8:
        msg.showerror("Name", "The name must not exceed 8 characters long.")
    elif len(text) == 0:
        msg.showerror("Name", 'You must enter a neme.')
    else:
        return True


def is_digits(text: str) -> bool:
    if len(text) == 1:
        if text == '+' or text == '-':
            return False

    for i in text:
        if i not in '1234567890+-':
            return False

    for i in text[1:]:
        if i in '+-':
            return False
    return True


def get_name():
    global players
    player_name = e_name.get().strip()
    if is_valid(player_name):
        player = Player(player_name.title().strip())
        players.append(player)
        e_name.set('')


def calculate_func():
    global players
    for player in players:
        player.calculate()
        print(player)


e_name = StringVar()
e_name.set('')

entry_name = Entry(header_frame, textvariable=e_name, font=("Times New Roman", 12), borderwidth=2)
entry_name.grid(row=0, column=0, columnspan=3)

add_btn = Button(header_frame, bd=1, text='ADD', font=("Times New Roman", 8, 'bold'), command=get_name)
add_btn.grid(row=0, column=4, padx=(5, 0), ipadx=4)

label1 = Label(headings_frame, text="Name", font=("Times New Roman", 10, 'bold'))
label1.grid(row=0, column=0, padx=5, pady=5, ipadx=2, ipady=2, sticky=NSEW)

label2 = Label(headings_frame, text="Point", font=("Times New Roman", 10, 'bold'))
label2.grid(row=0, column=1, padx=5, pady=5, ipadx=2, ipady=2, sticky=NSEW)

label3 = Label(headings_frame, text="Total", font=("Times New Roman", 10, 'bold'))
label3.grid(row=0, column=2, padx=5, pady=5, ipadx=2, ipady=2, sticky=NSEW)

label3 = Label(headings_frame, text="Last point", font=("Times New Roman", 10, 'bold'))
label3.grid(row=0, column=3, padx=5, pady=5, ipadx=2, ipady=2, sticky=NSEW)

calc_btn = Button(bottom_frame, bd=1, text='Calculate', font=("Times New Roman", 10, 'bold'), command=calculate_func)
calc_btn.pack(pady=10)

top.mainloop()
