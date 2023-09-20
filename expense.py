from PyInquirer import prompt
from utils import useful_functions as utils

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": utils.getAllUsers("users.csv"),   # CRASH if users file is empty at the start of the main
    },
    {
        "type":"checkbox",
        "name":"payback",
        "message":"New Expense - List of Users involved: ",
        "choices": utils.getAllUsersJSON("users.csv"),   # spender has to be checked by default
    },
]

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    utils.write_info("expense_report.csv", infos, 'w', fields = ["amount", "label", "spender", "payback"])
    print("Expense Added !")
    return True
