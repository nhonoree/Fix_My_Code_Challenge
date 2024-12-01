#!/usr/bin/python3

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def is_valid_password(self, password):
        return self.password == password

if __name__ == "__main__":
    user = User('Test User', 'password123')
    print(user.is_valid_password('password123'))  # Should return True
