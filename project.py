import random
import os

u_pwd = input("Enter a password: ")

pwd = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

pw = ""

while pw != u_pwd:
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[random.randint(0, 9)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("Cracking password...")
        os.system("cls")

print("Your password is: ", pw)
