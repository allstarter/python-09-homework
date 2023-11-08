import json
from simple_term_menu import TerminalMenu
from operations import user, balance, customer
from operations.operation import Operation
from users.customer import Customer
from users.employee import Employee
from users.user import User

# getting application data in new shape
employees = json.loads(open("employees.json", "r").read())
customers = json.loads(open("customers.json", "r").read())

users: dict[str, User] = {}

# the ** operator does a cool trick for us ..
for username in employees:
    users[username] = Employee(username, **employees[username])

for username in customers:
    users[username] = Customer(username, **customers[username])

for username in users:
    print(f"User {username} is {users[username].__class__}")

start_options: dict[str, Operation] = {
            "1": user.Login(),
            "2": user.Goodbye(),
        }

Customer.menu_options = {
    "1": balance.Show(),
    "2": balance.Transfer(),
    "3": user.Logout()
}

Employee.menu_options = {
    "1": balance.Report(),
    "2": balance.Deposit(),
    "3": balance.Cashout(),
    "4": customer.Create(),
    "5": customer.Remove(),
    "6": user.Logout()
}

user = None
while True:
    menu_options: dict[str, Operation] = user.menu_options if user else start_options

    # Start here, using TerminalMenu
    # Follow examle at https://pypi.org/project/simple-term-menu/
    #
    # options = ["entry 1", "entry 2", "entry 3"]
    # terminal_menu = TerminalMenu(options)
    # menu_entry_index = terminal_menu.show()
    # print(f"You have selected {options[menu_entry_index]}!")

    for key in menu_options.keys():
        print(f"{key}. {menu_options[key].summary()}")

    user_input = input("> ")
    if user_input in menu_options:
        user = menu_options[user_input].execute(user, users)
    else:
        valid_keys = list(menu_options.keys())
        last_key = valid_keys.pop()
        print(f"Wrong option, please use {', '.join(valid_keys)} or {last_key}.")
