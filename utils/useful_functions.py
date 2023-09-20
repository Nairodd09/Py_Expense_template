import csv

def write_info(file, data, mode, fields):
    expense_report = open(file, mode, newline="")
    writer = csv.DictWriter(expense_report, fieldnames=fields)
    if mode == 'w':
        writer.writeheader()
    writer.writerow(data)
    expense_report.close()

def getAllUsers(file):
    users = open(file, 'r')
    users_list = []
    for e in users:
        users_list.append(e.strip())
    users.close()
    return users_list

def getAllUsersJSON(file):
    users = open(file, 'r')
    users_list = []
    for e in users:
        users_list.append({'name': e.strip()})
    users.close()
    return users_list

def getAllExpenseJSON(file):
    expenses = open(file, 'r')
    csvreader = csv.reader(expenses)
    expenses_list = []
    for row in csvreader:
        expenses_list.append(row)
    expenses.close()
    return expenses_list

def convert(string):
    out = list(string.split(" []"))
    return out