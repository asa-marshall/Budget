import tkinter as tk


class Budget(object):

    # TODO: Exceptions for Constructor
    def __init__(self, budget_name="", budget_type="", budget_percentage=0.0, budget_amount=0.0):
        self.budget_name = budget_name
        self.budget_type = budget_type
        self.budget_percentage = budget_percentage
        self.budget_amount = budget_amount
        self.lbl_name = tk.Label(text=budget_name)

    def calculate_budget(self, paycheck):
        if paycheck is None or not isinstance(paycheck, float):
            raise ValueError("Invalid Paycheck Amount")
        if self.is_percentage():
            return paycheck * self.budget_percentage
        elif self.is_fixed():
            return self.budget_amount
        else:
            return 0

    def is_percentage(self):
        if self.budget_type == "Percentage":
            return True
        return False

    def is_fixed(self):
        if self.budget_type == "Amount":
            return True
        return False

    def get_name(self):
        return self.budget_name

    def get_type(self):
        return self.budget_type

    def get_percentage(self):
        return self.budget_percentage

    def get_amount(self):
        return self.budget_amount

    def get_lbl_name(self):
        return self.lbl_name

    def set_name(self, name):
        if not isinstance(name, str) or name == "":
            raise TypeError("Invalid Name Type")
        self.budget_name = name
        self.lbl_name.config(text=name)

    def set_type(self, budget_type):
        if not budget_type == "Percentage" and not budget_type == "Amount":
            raise TypeError("Invalid Budget Type")
        self.budget_type = budget_type

    def set_percentage(self, percentage):
        if not isinstance(percentage, float):
            raise ValueError("Invalid Percentage Value")
        self.budget_percentage = percentage

    def set_amount(self, amount):
        if not isinstance(amount, float):
            raise ValueError("Invalid Amount Value")
        self.budget_amount = amount

    def __repr__(self):
        return "Name:\t\t" + self.budget_name + "\nType:\t\t" + self.budget_type + "\nPercentage:\t" +\
               str(self.budget_percentage) + "\nAmount:\t\t" + str(self.budget_amount)
