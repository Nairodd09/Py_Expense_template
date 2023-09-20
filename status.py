from PyInquirer import prompt
from utils import useful_functions as utils

def status():
    list_expense = utils.getAllExpenseJSON("expense_report.csv")
    users = utils.getAllUsers("users.csv")
    debt = []
    for i in range(1, len(list_expense)):
        endebted = []
        list = utils.convert(list_expense[i][3]) # is expected to convert a string to list
        for e in list:
            if e != list_expense[i][2]:
                endebted.append(e)
        
        debt.append((list_expense[i][2], int(list_expense[i][0]) / len(users), endebted))

    print(debt)
        
    return
