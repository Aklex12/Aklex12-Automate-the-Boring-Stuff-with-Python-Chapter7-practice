import re

passwordRegex = re.compile(r'[a-zA-Z0-9._]{8,12}')
password = input("Enter your password: ")

while passwordRegex.search(password) == None:
    if passwordRegex.search(password) == None:
        print("Password must be 8 to 12 characters long and must have: upper and lower case letters, numbers, periods and underscores.")
        password = input("Enter new password: ")

print("Excelent, you created your password: ", password)
