# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages


# # Create an object (a real book)
# book1 = Book("Python Basics", "John Doe", 250)

# # Access the title using dot notation
# print(book1.title)

class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance


# Create two accounts
john = BankAccount("John", "1234567890", 25000)
mary = BankAccount("Mary", "9876543210", 150000)

# Print balances
print(john.balance)
print(mary.balance)

# Update John's balance
john.balance = 40000

# Print updated balance
print(john.balance)