class User:
    ###############
    # Magic methods
    ###############
    def __init__(self, name, age, phone, password, balance):
        self.__name = name
        self.__age = age
        self.__phone = phone
        self.__password = password
        self.__balance = balance

    def __str__(self):
        return self.__name

    #####################
    # Getters and Setters
    #####################
    # Name
    def getter_name(self):
        return self.__name

    def setter_name(self, new_name):
        self.__name = new_name

    # Age
    def getter_age(self):
        return self.__age

    def setter_age(self, new_age):
        self.__age = new_age

    # Phone
    def getter_phone(self):
        return self.__phone

    def setter_phone(self, new_phone):
        self.__phone = new_phone

    # Password
    def getter_password(self):
        return self.__password

    def setter_password(self, new_password):
        self.__password = new_password

    # Balance
    def getter_balance(self):
        return self.__balance

    def setter_balance(self, new_balance):
        self.__balance = new_balance

    ######################
    # Defining our methods
    ######################
    def dictionary_info(self):
        return {
            'name': self.__name,
            'age': self.__age,
            'phone': self.__phone,
            'password': self.__password,
            'balance': self.__balance
        }

    def show_user_info(self):
        return {
            'name': self.__name,
            'age': self.__age,
            'phone': self.__phone,
        }

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            return None
