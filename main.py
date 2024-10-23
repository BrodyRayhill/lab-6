#Brody Rayhill's main and encoder functions
#Ryan Rupp will push the decoder function

def displayMenu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    return

def main():
    while True:
        displayMenu()
        user_input = input("Please enter an option: ")
        if int(user_input) == 1:
            encoded_password = encode()
        elif int(user_input) == 2:
            decode(encoded_password)
        elif int(user_input) == 3:
            exit()
        else:
            print("Invalid option.")
            print()

def encode():
    pass_check = False
    while pass_check == False: # Checks for valid password input
        password = input("Please enter your password to encode: ")
        if len(password) == 8: # Make sure password is 8 chars long
            count = 0
            for i in password:
                if i.isdigit(): # Make sure each digit of password is an integer
                    count += 1
                    if count == 8:
                        pass_check = True
                else:
                    print("Invalid password.")
                    count = 0
                    break
        else:
            print("Invalid password.")
    password_list = []
    for i in password:
        num = int(i)
        password_list.append(num)
    for i in range(len(password_list)):
        password_list[i] = str(password_list[i] + 3)
    encoded_password = ''.join(password_list)
    print("Your password has been encoded and stored!")
    print()
    return encoded_password

def decode(encoded_password): # Ryan's implementation of decode()
    encoded_password_list = []
    for i in range(len(encoded_password)):
        encoded_password_list.append(int(encoded_password[i]))
        encoded_password_list[i] = str(encoded_password_list[i] - 3)
    decoded_password = ''.join(encoded_password_list)
    print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
    print()
    return

if __name__ == "__main__":
    main()
