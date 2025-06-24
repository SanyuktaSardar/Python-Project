import random
print("Welcome to the PyPassword Generator!")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','[',']']

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

file_path = 'Password.txt'
with open(file_path,'a') as  file:
    file.write(password+"\n")



