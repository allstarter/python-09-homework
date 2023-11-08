class User():
    """Basic class for bank application user that handle login and logout"""
    menu_options = {}

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._loggedin = False

    @property
    def username(self):
        return self._username

    def login(self, password):
        if self._password == password:
            self._loggedin = True
        else:
            self._loggedin = False
        return self._loggedin

    def save_as_dict(self):
        return {self._username: {"password": self._password}}

    def logout(self):
        self._loggedin = False
