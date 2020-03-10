import tkinter as tk
from tkinter import *
from tkinter import messagebox

from Budget import Budget


# TODO: create GUI for budgets after creation
# TODO: functionality for entering paycheck
class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()

        self.lbl_hello = tk.Label(text="Welcome to the Budget Console")
        self.lbl_name = tk.Label(text="Name")
        self.lbl_type = tk.Label(text="Type")
        self.lbl_amount = tk.Label(text="Amount")

        self.txt_name = tk.Entry()
        self.txt_amount = tk.Entry()

        self.types = StringVar()
        self.types.set("Amount")
        self.opt_type = tk.OptionMenu(self.master, self.types, "Amount", "Percentage")

        self.btn_create = tk.Button(text="Create Budget", command=lambda: self.create_budget())
        self.btn_print = tk.Button(text="Print Budgets", command=lambda: self.print_budgets())

        self.budgets = []

        self.create_widgets()

    def create_widgets(self):
        self.lbl_hello.grid(row=0)
        self.lbl_name.grid(row=1)
        self.txt_name.grid(row=1, column=1)
        self.lbl_type.grid(row=2)
        self.opt_type.grid(row=2, column=1)
        self.lbl_amount.grid(row=3)
        self.txt_amount.grid(row=3, column=1)
        self.btn_create.grid(row=4)
        self.btn_print.grid(row=4, column=1)

    def create_budget(self):
        budget = Budget()
        try:
            budget_name = str(self.txt_name.get())
            budget.set_name(budget_name)
            try:
                budget_type = self.types.get()
                budget.set_type(budget_type)
                if budget.is_fixed():
                    budget.set_amount(float(self.txt_amount.get()))
                else:
                    budget.set_percentage(float(self.txt_amount.get()))
                self.budgets.append(budget)
                self.insert_budget_field()
                self.clear_create_fields()
            except ValueError:
                messagebox.showwarning("Invalid Fields", "Amount field must be a decimal value.")
        except TypeError:
            self.txt_name.insert(0, "Enter Name Here")

    def insert_budget_field(self):
        budget = self.budgets[len(self.budgets)-1]
        row = len(self.budgets) + 5
        budget.lbl_name.grid(row)
        print(budget)

    def clear_create_fields(self):
        self.txt_name.delete(0, END)
        self.txt_amount.delete(0, END)
        self.types.set("Amount")

    def print_budgets(self):
        for budget in self.budgets:
            print(budget)
            print()


def main_window():
    root = Tk()
    root.title("Budget Console")
    gui = GUI(master=root)
    gui.mainloop()

