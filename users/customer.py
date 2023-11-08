from operations.operation import Operation
from .user import User


class Customer(User):
    """Special class for bank customers with their operations"""
    _poweruser = False
    menu_options: dict[str, Operation] = {}

    def __init__(self, username, password, balance: float):
        super().__init__(username, password)
        self.balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, new_balance: float):
        assert (new_balance >= 0.0)
        self._balance = new_balance

    def save_as_dict(self):
        user = super().save_as_dict()
        user[self._username]["balance"] = self._balance
        return user
