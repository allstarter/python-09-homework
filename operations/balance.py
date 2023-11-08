from reportlab.pdfgen import canvas
from users.customer import Customer
from users.employee import Employee
from users.user import User
from .operation import Operation
from .customer import Save


class Show(Operation):
    """Show balance operation of a customer"""

    def summary(self) -> str:
        return "Check Balance"

    def execute(self, user: Customer, users: dict[str, User]) -> Customer:
        print(f"Your balance is {user.balance}!")
        return user


class PdfReport(Operation):
    """Generate PDF Reort"""

    def summary(self) -> str:
        return "Export PDF Reort"

    def execute(self, user: User, users: dict[str, User]) -> User:
        # create a Canvas object with a filename
        c = canvas.Canvas("rl-hello_again.pdf", pagesize=(595.27, 841.89))  # A4 pagesize
        # draw a string at x=100, y=800 points
        # point ~ standard desktop publishing (72 DPI)
        # coordinate system:
        #   y
        #   |
        #   |   page
        #   |
        #   |
        #   0-------x
        c.drawString(50, 780, "Hello Again")
        # finish page
        c.showPage()
        # construct and save file to .pdf
        c.save()
        return user


class Report(Operation):
    """Show balance operation of a customer"""

    def summary(self) -> str:
        return "Generate Bank Report"

    def execute(self, user: Employee, users: dict[str, User]) -> User:
        sum = 0.0
        number = 0
        print("List of accounts:")
        for username in users:
            if isinstance(users[username], Customer):
                balance = users[username].balance  # type: ignore
                number += 1
                sum += balance
                print(f"{balance}$ of {username}")
        print(f"{sum}$ overall balance of {number} customers")
        return user


class Deposit(Save):
    """Deposit money from a costumer"""

    def summary(self) -> str:
        return "Deposit money"

    def execute(self, user: Employee, users: dict[str, User], negative=False) -> User:
        customer = input("Customer: ")
        if customer in users and isinstance(users[customer], Customer):
            try:
                amount = float(input("Amount: "))
                if amount < 0.0:
                    raise ValueError
                if negative:
                    users[customer].balance -= amount  # type: ignore
                else:
                    users[customer].balance += amount  # type: ignore
                super().execute(user, users)
            except ValueError:
                print("Oops! That was no valid positive number.")
            except AssertionError:
                print(f"Not enough balance to cash-out {users[customer].balance}.")  # type: ignore
        else:
            print(f"Customer {customer} is not existing.")
        return user


class Cashout(Deposit):
    """Cash-out balance to a costumer"""

    def summary(self) -> str:
        return "Cash-out balance"

    def execute(self, user: Employee, users: dict[str, User]) -> User:
        return super().execute(user, users, True)


class Transfer(Save):
    """Transfer balance of a costumer"""

    def summary(self) -> str:
        return "Transfer balance"

    def execute(self, user: Customer, users: dict[str, User]) -> User:
        receiver = input("Receiver: ")
        if receiver in users and isinstance(users[receiver], Customer):
            try:
                amount = float(input("Amount: "))
                if amount < 0.0:
                    raise ValueError
                user.balance -= amount
                users[receiver].balance += amount  # type: ignore
                super().execute(user, users)
            except ValueError:
                print("Oops! That was no valid positive number.")
            except AssertionError:
                print(f"Not enough balance to tranfer {user.balance}.")
        else:
            print(f"Receiver {receiver} is not existing.")
        return user
