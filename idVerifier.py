user_input = input("Enter your ID number: ")

try:
    user_id = int(user_input)
    print('Access Granted!')
except ValueError:
    print(f"Sorry, '{user_input}' is not a valid whole number.")
    user_id = None