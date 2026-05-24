# Age eligibility checker

age = '8'
if age < 12:
    print('You are a child.')
elif age < 18:
    print('You are a teenager.')
else:
    print('You are an adult.')

# Password Validator

password = '1234'
if len(password) >= 5:
    print('Password is strong.')
else:    print('Password is weak. Please use at least 5 characters.')

# Grade classification

score = 15
total = 20
if score < 10:
    print('You failed the test, grade C.')
elif score < 15:
    print('You passed the test, grade B.')
else:
    print('You passed the test, grade A.')

# Multiplication table

number = 2
for number in range(1,12):
    print('{number} x {i} = {number*i}')

# Number guessing game

secret_number = 7
user_guess = int(input('Guess the secret number: '))
if user_guess == secret_number:
    print('Congratulations! You guessed the secret number.')
else:
    print('Sorry, that's not the secret number.')

# Countdown timer

 t = 2
for t in range (10, 0, -2):
    print(i)

# ATM withdrawal simulations

Account_balance = 120000.00
withdraw = 5000.00
if withdraw > Account_balance:
    print('Insufficient funds')
else:
    Account_balance <= withdraw
    print('Withdrawal successful}')

# Login system

  username = 'isauraetiendem'
password = '12345'
if username == 'isauraetiendem' and password == '12345':
    print('Login successful!')
else:    print('Login failed. Please check your username and password.')


