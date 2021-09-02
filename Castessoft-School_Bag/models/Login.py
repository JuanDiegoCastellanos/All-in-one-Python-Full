from tests.mocks import Users

class Login:
    def __init__(self) -> None:
        self.user_name = ''
        self.password = ''
    def __init__(self, user_name, password) -> None:
        self.user_name = user_name
        self.password = password

    def validation(self):
        for key,value in Users.users_logins.items:
            if self.user_name == key and self.password == value:
                print('LOGIN SUCESSFULL')
            else:
                print('LOGIN ERROR')

login = Login('Juan Diego Castellanos','123456A')





