class EmptyValueError(Exception):
    def __init__(self, value='The value'):
        self.message = f'"{value}" cannot be empty.'

    def __str__(self):
        return self.message


class UserTypeError(Exception):
    def __init__(self, message):
        self.message = f'Invalid user type: {message}'

    def __str__(self):
        return self.message


class PasswordCheckError(Exception):
    def __init__(self):
        self.message = 'Password check field is not equal to password.'

    def __str__(self):
        return self.message


class ModelDoesNotExistError(Exception):
    def __init__(self, model='The model'):
        self.message = f'"{model}" does not exist.'

    def __str__(self):
        return self.message

