from operations.operation import Operation
from .user import User


class Employee(User):
    """Special class for bank employees that internal service operations"""
    _poweruser = True
    menu_options: dict[str, Operation] = {}

    def __init__(self, username, password):
        super().__init__(username, password)
