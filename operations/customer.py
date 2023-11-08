import json
from users.customer import Customer
from users.employee import Employee
from users.user import User
from .operation import Operation


class Save(Operation):
    """Save all bank customers"""

    def summary(self) -> str:
        return "Save customer data"

    def execute(self, user: User, users: dict[str, User]) -> User:
        # customers is a new dict that contains only instances of Customer
        customers = {k: v.save_as_dict()[k] for k, v in users.items() if isinstance(v, Customer)}

        with open('customers.json', 'w', encoding='utf-8') as f:
            json.dump(customers, f, ensure_ascii=False)
        return user


class Create(Save):
    """Create new bank customer"""

    def summary(self) -> str:
        return "Create customer account"

    def execute(self, user: Employee, users: dict[str, User]) -> User:
        for _ in range(3):
            username = input("Username: ")
            if username == "":
                print("Username must not be empty.")
            elif username in users:
                print("Username already exists. Please try another one.")
            else:
                break
        else:
            print("Operation canceled. Invalid input for 3 times.")
            return user

        for _ in range(3):
            password = input("Password: ")
            if password == "":
                print("Password must not be empty.")
                continue

            password_repeat = input("Repeat Password: ")
            if password != password_repeat:
                print("Passwords are different. Please try again.")
            else:
                break
        else:
            print("Operation canceled. Invalid input for 3 times.")
            return user

        for _ in range(3):
            try:
                balance = float(input("Starting Balance: "))
                users[username] = Customer(username, password=password, balance=balance)
                break
            except ValueError:
                print("Balance is not a valid number!")
            except AssertionError:
                print("That's not a valid number!")
        else:
            print("Operation canceled. Invalid input for 3 times.")
            return user

        return super().execute(user, users)


class Remove(Save):
    """Create remove bank customer"""

    def summary(self) -> str:
        return "Remove customer account"

    def execute(self, user: Employee, users: dict[str, User]) -> User:
        for _ in range(3):
            username = input("Username: ")
            if username in users and isinstance(users[username], Customer):
                balance = users[username].balance  # type: ignore
                if balance == 0.0:
                    del users[username]
                    print(f"Customer {username} removed.")
                    return super().execute(user, users)
                else:
                    print(f"Customer was not removed. Balance {balance}$ needs to be removed.")
                break
            else:
                print(f"Customer {username} is not existing.")
        else:
            print("Operation canceled. Invalid input for 3 times.")
        return user
