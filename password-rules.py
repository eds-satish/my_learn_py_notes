while True:
    uid = input('Enter uid: ')
    if uid.isalpha():
        while True:
            pwd = input('Enter password: ')
            if pwd.isalnum():
                print('Access granted')
                break
            else:
                continue
        break
    else:
        continue

