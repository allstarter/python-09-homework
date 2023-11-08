from users.user import User
from abc import ABC, abstractmethod


# That is how abstract base class work in Python
class Operation(ABC):
    """Abstract Base Class to implement special operation execute() methods"""
    @abstractmethod
    def summary(self) -> str:
        pass

    @abstractmethod
    def execute(self, user: User, users: dict[str, User]) -> User:
        pass
