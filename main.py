from classes.book import Book
import os
import json

user_list = [
    {
        "name": "Ashkan",
        "phone": "09123456701",
        "password": "ashkan 123",
    },
    {
        "name": "Parsa",
        "phone": "09123456702",
        "password": "pass1",
    },
    {
        "name": "AmirHossain",
        "phone": "09123456703",
        "password": "pass2",
    },
]

book_list = []

cart_list = []
####################################################################### Constant Variables #############################
BOOK_JSON_FILE_PATH = "database_files/books.json"
USER_JSON_FILE_PATH = "database_files/user.json"
CART_JSON_FILE_PATH = "database_files/cart.json"


####################################################################### Load database ##################################
# Load books
def load_books_from_database():
    with open(BOOK_JSON_FILE_PATH, 'r') as file:
        # Load json array in data variable
        data = json.load(file)

        # Creating book object form the class and save in list
        for book in data:
            book_list.append(
                Book(
                    uid=book.get("uid"),
                    title=book.get("title"),
                    author=book.get("author"),
                    pages=book.get("pages"),
                    price=book.get("price"),
                    discount_price=book.get("discount_price"),
                    category=book.get("category"),
                    published_date=book.get("published_date"),
                )
            )


####################################################################### Functions ######################################
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def user_checker():
    the_user = None

    entry_phone = input("Phone number >>> ")
    for temp_user in user_list:
        if temp_user.get("phone") == entry_phone:
            the_user = temp_user
            break

    # The user with that phone number is not exists
    if the_user is None:
        return None

    else:
        # Clear screen
        clear_screen()

        print(f'Hello {the_user.get("name")}')
        print("Please enter your password to login :)")

        entry_password = input("Password >>> ")
        while entry_password != the_user.get("password"):
            clear_screen()

            print(f'Dear {the_user.get("name")},\nyou entered the wrong password.')
            print("Please enter the correct password to login :)")
            entry_password = input("Password >>> ")

        return the_user


def waiting_function():
    print()
    print()
    input("Please press 'enter' to continue ...")


def main_function_show_all_the_books():
    # Showing table
    print("##################################################################################################")
    print("Book id \t Price \t\t\t Discount \t\t Book title ")
    print("##################################################################################################")

    # Show each item in book list
    for item in book_list:
        # Calculating discount price
        discount_price = item.getter_discount_price() if item.getter_discount_price() != 0 else "----"

        # Showing each book info
        print(f"{item.getter_uid()} \t\t {item.getter_price()} $ \t\t {discount_price} $ \t\t {item.getter_title()}")


def main_function_show_the_book_details():
    print("Show the book details")
    try:
        # Getting the book id
        book_id = int(input("Enter the book id >>> "))

        founded_book = None

        # Searching for the book
        for the_book in book_list:
            if the_book.getter_uid() == book_id:
                founded_book = the_book
                break

        # Here we founded the book
        if founded_book is not None:
            print(f'📚 Book name : {founded_book.getter_title()}')
            print(f'🗿 Author : {founded_book.getter_author()}')
            print(f'📄 Pages : {founded_book.getter_pages()}')
            print(f'💸 Price : {founded_book.getter_price()}')
            print(f'🤑 Discount Price : {founded_book.getter_discount_price() if founded_book.getter_discount_price == 0.0 else "---"}')
            print(f'📅 Published date : {founded_book.getter_published_date()}')

            print("""
            [Book Title] is a compelling work by the talented author [Author Name], published in [Year of Publication]. Presented in a [Cover Type] format, this book spans [Number of Pages] pages filled with rich content that invites readers into a thoughtful and immersive journey through the author's world.
Priced at [Price] USD, this book reflects the value of its content and the quality of its production. With artistic design, high-end printing, and carefully selected materials, it stands as a distinguished cultural product.
More than just a literary work, [Book Title] offers a reflective and aesthetic experience—one that encourages deeper understanding, contemplation, and a fresh perspective on the world around us.
            """)

        # The book not exists in our database
        else:
            clear_screen()
            print("There is no book exists with this id!")
            print("Please enter a valid book id :)")

    except ValueError:
        clear_screen()
        print("Please enter a number\nNot a string !")
        print("Try again :)")


####################################################################### Main Part ######################################

clear_screen()

# Loading files
load_books_from_database()

print("""Hello dear user!
Welcome to Computech Book Store !
""")

print("Please enter your phone")
user = user_checker()
while user is None:
    clear_screen()
    print("Sorry this phone number is not exists :(")
    print("Please enter a valid phone number")
    user = user_checker()

# Now we can continue with the detected user

# Defining the Menu
menu = '''Choose one of the following options : 
1) Show the all books
2) Show the book details
3) Show the cart
4) Remove item form cart
5) Add item to cart
6) Deposit 
7) To pay
8) Exit
>>> '''

while True:
    # To clear screen
    clear_screen()

    choice = input(menu)

    # Clear menu screen
    clear_screen()

    if choice == "1":
        main_function_show_all_the_books()
    elif choice == "2":
        main_function_show_the_book_details()
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        pass
    elif choice == "8":
        # Showing the suitable message
        print("Thank you for using Computech Book Store!")
        print("Have a nice time ! :)")
        print("Programmed by : Computech Team !")

        # Exit from loop
        break
    else:
        print("Invalid option")
        print("Please try again and select one of the options :)")

    # Waiting for user to press enter to continue
    waiting_function()
