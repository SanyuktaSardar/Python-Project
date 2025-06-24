import random
print("Welcome to the PyPassword Generator!")
logo = '''

██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                    
'''
print(logo)
file_path = 'Password.txt'
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','[',']']
choice = input("If you want detect password strength type 'd' and If you want to Computer to create password type 'c': ")
if choice == 'c':
    letters_password = int(input("How many letters would you like in your password?"))
    symbol_password = int(input("How many symbol would you like?"))
    numbers_password = int(input("How many numbers would you like?"))

    password_user= []
    for i in range(0,letters_password):
        letter = random.choice(letters)
        password_user.append(letter)

    for i in range(0,symbol_password):
        symbol = random.choice(symbols)
        password_user.append(symbol)

    for i in range(0,numbers_password):
        number = random.choice(numbers)
        password_user.append(number)

    random.shuffle(password_user)

    password = ''
    for item in password_user:
        password += item
    print(f"Your password is: {password}")

    with open(file_path,'a') as  file:
        file.write(password+"\n")
elif choice == 'd':
    your_password = input("Enter your password: ")
    letter_present = False
    number_present = False
    symbol_present = False
    for i in your_password:
        if i in letters:
            letter_present = True
        elif i in numbers:
            number_present = True
        else:
            symbol_present = True
    if (letter_present == True) and (number_present== True) and (symbol_present== True):
        print('Strong Password Strength🎉. You can keep it as a password')
        want_store = input("Do you want to store the password? type 'yes' or 'no'").lower()
        if want_store == 'yes':
            with open(file_path, 'a') as file:
                file.write(your_password + "\n")
    elif ((letter_present == False) and (number_present==True) and (symbol_present==True)) or ((letter_present == True) and (number_present==False) and (symbol_present==True)) or ((letter_present == True) and (number_present==True) and (symbol_present==False)):
        print('Medium Password Strength😒! ')
        if (letter_present == False) and (number_present==True) and (symbol_present==True):
            print('Add Letter to Make Strong Password💪')
        elif (letter_present == True) and (number_present==False) and (symbol_present==True):
            print("Add Number to Make Strong Password💪")
        else:
            print('Add Symbol to Make Strong Password💪')
    else:
        print("Weak Password!! Your password should contain letters, numbers and symbols to make a strong password 💪.")



