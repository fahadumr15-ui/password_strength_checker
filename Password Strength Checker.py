import re
def check_password_strength(password):

    if len(password)<8:
        return "weak :passowrd must be at least 8 characters"
    if not any(char.isdigit() for char in password):
        return "weak:password must contain a digit"
    if not any(char.isupper() for char in password):
        return "weak:passowrd must contain upper case"
    if not any(char.islower()for char in password):
        return "weak:passowrd must contain lower case"
    if not re.search(r'[!@#$%^&*?{}.,]',password):
        return "medium:password must contain special character"
    return "Strong.Your password is secured"
def password_checker():
    print("Welcome to the password strength checker")
while True:
    password=input("Enter your password (or type 'exit' to quit):")
    if password.lower()== 'exit':
        print("Thanks for using this!")
        break 
    result=check_password_strength(password)
    print(result)
    if __name__== "__main__":
        password_checker()