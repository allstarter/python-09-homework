from users.user import User
from .operation import Operation


class Login(Operation):
    """Handle login of an user"""

    def summary(self) -> str:
        return "Login"

    def execute(self, user: User, users: dict[str, User]):
        username = input("Username: ")
        password = input("Password: ")

        if username in users:
            if users[username].login(password):
                return users[username]
        print("Wrong credentials.")


class Logout(Operation):
    """Log out the current user"""

    def summary(self) -> str:
        return "Log off"

    def execute(self, user: User, users: dict[str, User]):
        print(f"Goodbye {user.username}!")
        user.logout()


class Goodbye(Operation):
    """Exit of the application"""

    def summary(self) -> str:
        return "Exit"

    def execute(self, user: User, users: dict[str, User]):
        print("Thanks for using our Bank!")
        exit()
