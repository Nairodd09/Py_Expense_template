from PyInquirer import prompt
from utils import useful_functions as utils

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"Name: ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    utils.write_info("users.csv", infos, 'a', fields = ["name"])
    return