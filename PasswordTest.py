print('This project will determine the strength of your password.')

while True:
    UsersPassword = input("Enter your password: ")
    lower = 0
    upper = 0
    alphanum = 0
    numbers = 0

    for c in UsersPassword:
        if c.isupper():
            upper += 1
        if c.islower():
            lower += 1
        if c.isdigit():
            numbers += 1
        if c.isalnum():
            alphanum += 1

    total_length = len(UsersPassword)
    nonalphanum_chars = total_length - alphanum

    if len(UsersPassword) < 5:
        print('Password must be at least 5 characters.')
    elif upper > 0 and lower > 0 and numbers > 0 and nonalphanum_chars > 0:
        print('This is a strong password.')
    elif upper > 0 and lower > 0:
        print('This is a good password.')
    elif lower > 0:
        print('This is a weak password.')
    else:
        print('Invalid password entry.')
    break  
