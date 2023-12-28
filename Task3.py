'''
Task 3
A password generator is a useful tool that generates strong andrandom passwords for users.
This project aims to create a password generator application using Python,
allowing users to specify the length and complexity of the password.
User Input: Prompt the user to specify the desired length of the password.
Generate Password: Use a combination of random characters to generate a password of the specified length.
Display the Password: Print the generated password on the screen.
'''

import string
import random

if __name__=="__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    plen = int(input("Enter password length\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)
    print("Your password is:")
    print( "".join(s[0:plen]))
