age = input("Enter your age: ")
if age <= 2:
    status = 'Baby'
elif age <= 8:
    status = 'Toddler'
elif age <= 12:
    status = 'Adolescent'
elif age < 18:
    status = 'Teenager'
else:
    status = 'Adult'
if status[0] == 'A' or 'E' or 'I' or 'O' or 'U':
    print('You are an', status)