class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def say_name(self):
        return self.name


lima = User('Lima', 'joao@gmail.com', '@secret')
print(lima)
print(lima.name)
print(lima.email)
print(lima.password)
print(lima.say_name())
