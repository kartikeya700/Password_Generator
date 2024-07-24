def main():
    print("Welcome to the PyPassword Generator!")
    import random
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    Letters = int(input("How many letters would you like in your password?\n"))
    Symbols = int(input("How many symbols would you like in your password?\n"))
    Numbers = int(input("How many numbers would you like in your password?\n"))
    characters = Letters + Symbols + Numbers
    pwd_letters = random.choices(letters, k = Letters)
    pwd_numbers = random.choices(numbers, k = Numbers)
    pwd_symbols = random.choices(symbols, k =Symbols)
    pwd = pwd_letters + pwd_numbers + pwd_symbols
    random.shuffle(pwd)
    password = ""
    for char in pwd:
        password += char
    print(f"Your password is : {password}")      
main()