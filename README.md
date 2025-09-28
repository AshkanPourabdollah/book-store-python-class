# 📚 Computech Book Store

A simple **Command-Line Interface (CLI)** application that simulates a book store.  
Users can log in, browse books, view details, manage their cart, deposit balance, and proceed with payments.  
All data is stored and managed in **JSON files**.

---

## ✨ Features
- User authentication with phone number and password  
- View all available books with price and discount  
- Show detailed information about a specific book (author, pages, price, published date, etc.)  
- Manage shopping cart (add/remove items, view total price)  
- Deposit balance into user account  
- Persistent data storage using JSON files  

---

## 🗂 Project Structure
```
project/
│
├── classes/
│   ├── book.py      # Book class to manage book information
│   ├── user.py      # User class to manage user information
│   └── cart.py      # Cart class to manage cart items
│
├── database_files/
│   ├── books.json   # Books database
│   ├── users.json   # Users database
│   └── cart.json    # Cart database
│
├── main.py          # Main entry point of the program
└── README.md        # Project documentation
```

---

## ⚙️ How to Run
1. Make sure you have **Python 3** installed on your system.  
2. Clone the repository:
   git clone https://github.com/AshkanPourabdollah/book-store-python-class.git
   cd computech-book-store
   
3. Run the program:
   python main.py
   

---

## 📖 Menu Options
Once logged in, you’ll see the following menu:
```
1) Show all books
2) Show book details
3) Show cart
4) Remove item from cart
5) Add item to cart
6) Deposit balance
7) Pay
8) Exit
```

---

## 📌 Requirements
- Python 3.x  
- Built-in Python libraries:  
  - `os`  
  - `json`
  - `uuid`

---

## 👨‍💻 Developer
Created with ❤️ by **Computech Team** 🚀  
