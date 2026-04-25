import secrets

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special_char = '@!()&.'

characters = letters + numbers + special_char
password = ''

for i in range(10):
    password += secrets.choice(characters)

print(password)