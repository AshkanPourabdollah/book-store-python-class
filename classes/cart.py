from classes.book import Book
from classes.user import User


class Cart:
    ###############
    # Magic methods
    ###############
    def __init__(self, uid, book: Book, user: User):
        self.__uid = uid
        self.__book = book
        self.__user = user

    def __str__(self):
        return f'{self.__book} --> {self.__user}'

    #####################
    # Getters and Setters
    #####################
    # Uid
    def getter_uid(self):
        return self.__uid

    # Book
    def getter_book(self):
        return self.__book

    def setter_book(self, new_book):
        self.__book = new_book

    # User
    def getter_user(self):
        return self.__user

    def setter_user(self, new_user):
        self.__user = new_user

    ######################
    # Defining our methods
    ######################
    def dictionary_info(self):
        return {
            "uid": self.__uid,
            "book": self.__book.dictionary_info(),
            "user": self.__user.show_user_info(),
        }
