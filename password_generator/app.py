#!/usr/bin/env python3.10
import random

simple_passwd_list = ['a', 'e', 'i', 'o', 'u', 'k', 'b', 'p']

medium_passwd_list = ['a','b','c','d','e','f','g','h','i','j',
    'l','m','n','o','p','q','r','s','t','u',
    'v','w','x','y','z', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]

complex_passwd_list = [
    'a','b','c','d','e','f','g','h','i','j',
    'l','m','n','o','p','q','r','s','t','u',
    'v','w','x','y','z', '1', '2', '3', '4',
    '5', '6', '7', '8', '9','0', '&', '%', 
    '_', ' '
]

passwd_len = int(input("Enter password length: "))
password_complexity = int(input("Choose password complexity\n1: simple\
\n2: medium\n3: hard\n\n"))
if password_complexity == 1:
    for i in range(0, passwd_len):
        random_char = random.choice(simple_passwd_list)
        password = random_char

        print(password, end='')
elif password_complexity == 2:
    for i in range(0, passwd_len):
        random_char = random.choice(medium_passwd_list)
        password = random_char

        print(password, end='')
elif password_complexity == 3:
    for i in range(0, passwd_len):
        random_char = random.choice(complex_passwd_list)
        password = random_char

        print(password, end='')
else:
    print("Please Enter a valid number :) ")