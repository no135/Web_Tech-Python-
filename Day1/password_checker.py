print('Password Checker')

password = input('please enter password : ')

if password.isupper():
    print('not correct password')
    if password.islower():
        print('not correct password')
        if password.isalpha():
            print('not correct password')
            if password.isdigit():
                print('not correct password')
else:
    print('correct password')

