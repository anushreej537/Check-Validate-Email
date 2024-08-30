import re

check_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
User_email = input('Enter your Email')

if re.search(check_condition , User_email):
    print('Correct Email')
else:
    print('Incorrect Email')