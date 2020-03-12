import tkinter as tk
import traceback
from tkinter import *
from tkinter import messagebox

from Budget import Budget


# TODO: create GUI for budgets after creation
# TODO: functionality for entering paycheck
# TODO: delete budget
class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()

        self.lbl_hello = tk.Label(text="Welcome to the Budget Console")
        self.lbl_name = tk.Label(text="Name")
        self.lbl_type = tk.Label(text="Type")
        self.lbl_amount = tk.Label(text="Amount")
        self.lbl_field_name = tk.Label(text="Name")
        self.lbl_field_saved = tk.Label(text="Saved")
        self.lbl_field_amount = tk.Label(text="Amount")
        self.lbl_field_type = tk.Label(text="Type")
        self.lbl_paycheck = tk.Label(text="Paycheck")

        self.txt_name = tk.Entry()
        self.txt_amount = tk.Entry()
        self.txt_paycheck = tk.Entry()

        self.types = StringVar()
        self.types.set("Amount")
        self.opt_type = tk.OptionMenu(self.master, self.types, "Amount", "Percentage")

        self.btn_create = tk.Button(text="Create Budget", command=lambda: self.create_budget())
        self.btn_print = tk.Button(text="Print Budgets", command=lambda: self.print_budgets())
        self.btn_calculate = tk.Button(text="Calculate", command=lambda: self.insert_calculations())

        self.budgets = []
        self.budget_fields = [[]]

        self.create_widgets()

    def create_widgets(self):
        self.lbl_hello.grid(row=0)
        self.btn_print.grid(row=0, column=3)
        self.lbl_name.grid(row=1)
        self.txt_name.grid(row=1, column=1)
        self.lbl_type.grid(row=2)
        self.opt_type.grid(row=2, column=1)
        self.lbl_amount.grid(row=3)
        self.txt_amount.grid(row=3, column=1)
        self.lbl_paycheck.grid(row=3, column=2)
        self.txt_paycheck.grid(row=3, column=3)
        self.btn_create.grid(row=4, column=1)
        self.btn_calculate.grid(row=4, column=3)

        self.lbl_field_name.grid(row=5)
        self.lbl_field_saved.grid(row=5, column=1)
        self.lbl_field_amount.grid(row=5, column=2)
        self.lbl_field_type.grid(row=5, column=3)

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
            # traceback.print_exc(file=sys.stdout)

    # TODO: switch to local gui fields. no tkinter in Budget
    def insert_budget_field(self):
        num = len(self.budgets)
        print(num)
        budget = self.budgets[num-1]
        row = num + 6
        budget_name = tk.Label(text=budget.get_name())
        budget_save = tk.Entry()
        budget_amount = tk.Entry()
        if budget.is_fixed():
            budget_amount.insert(0, budget.get_amount())
        else:
            budget_amount.insert(0, budget.get_percentage())
        budget_type = tk.Label(text=budget.get_type())

        self.budget_fields.append([])
        self.budget_fields[num-1].append(budget_name)
        self.budget_fields[num-1].append(budget_save)
        self.budget_fields[num-1].append(budget_amount)
        self.budget_fields[num-1].append(budget_type)

        for i in range(0, len(self.budget_fields[num-1])):
            self.budget_fields[num-1][i].grid(row=row, column=i)

    # TODO: Exceptions
    def insert_calculations(self):
        paycheck = float(self.txt_paycheck.get())

        print(paycheck)

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

