class ValidationRegex():
    def __init__(self):
        self.__email = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

    def regex_code_email(self):
        return self.__email
