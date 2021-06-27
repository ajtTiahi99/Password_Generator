#Password Generator Project
import random
import data

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=[]
for _ in range(nr_letters):
  password.append(data.letters[random.randint(0,26)])
for _ in range(nr_symbols):
  password.append(data.symbols[random.randint(0,8)])
for _ in range(nr_numbers):
  password.append(data.numbers[random.randint(0,9)])
random.shuffle(password)
print("Your Generated Password is:- ")
print(*password,sep="")


