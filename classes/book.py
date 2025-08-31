class Book:
    ###############
    # Magic methods
    ###############
    def __init__(self, uid, title, author, pages, price, discount_price, category, published_date):
        self.__uid = uid
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__price = price
        self.__discount_price = discount_price
        self.__category = category
        self.__published_date = published_date

    def __str__(self):
        return self.__title

    #####################
    # Getters and Setters
    #####################

    # UID
    def getter_uid(self):
        return self.__uid

    # Title
    def getter_title(self):
        return self.__title

    def setter_title(self, new_title):
        self.__title = new_title

    # Author
    def getter_author(self):
        return self.__author

    def setter_author(self, new_author):
        self.__author = new_author

    # Pages
    def getter_pages(self):
        return self.__pages

    def setter_pages(self, new_pages):
        self.__pages = new_pages

    # Price
    def getter_price(self):
        return self.__price

    def setter_price(self, new_price):
        self.__price = new_price

    # Discount price
    def getter_discount_price(self):
        return self.__discount_price

    def setter_discount_price(self, new_discount_price):
        self.__discount_price = new_discount_price

    # Category
    def getter_category(self):
        return self.__category

    def setter_category(self, new_category):
        self.__category = new_category

    # Published date
    def getter_published_date(self):
        return self.__published_date

    def setter_published_date(self, new_published_date):
        self.__published_date = new_published_date

    ######################
    # Defining our methods
    ######################
    def dictionary_info(self):
        return {
                "uid": self.__uid,
                "title": self.__title,
                "author": self.__author,
                "pages": self.__pages,
                "price": self.__price,
                "discount_price": self.__discount_price,
                "category": self.__category,
                "published_date": self.__published_date,
            }

    def show_info_by_id(self, id):
        if self.__uid == id:
            return self.dictionary_info()
        else:
            return None
