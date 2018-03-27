#coding:utf-8
import random
import string

def encryption():
    pass_k = ""
    for i in range(0,8):
        key = random.randint(1,4)
        pass_k += str(key)
    return pass_k

def generate_password():
    control = False
    passwords = []
    pass_k = ""
    password = ""
    data = {1:string.ascii_uppercase,2:string.ascii_lowercase,3:"!%?*#",4:string.digits}
    
    for a in range(100):
        password = ""
        pass_k = ""
        pass_k = encryption()
        i = 1
        while i<5:
            for m in range(0,8):
                if int(pass_k[m]) == i:
                    control = True
                    break
                else:
                    control = False
            if control == False:
                pass_k = encryption()
                i = 0
            i += 1
        if control == True:
            for i in range(0,8):
                password += str(random.choice(data[int(pass_k[i])])) 
        passwords.append(password)
    return passwords
passwords = generate_password()
print(passwords)
