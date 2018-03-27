#coding:utf-8
import generate_password
import string
passwords = generate_password.generate_password()

def passcontrol(passwords):
    correct = []
    incorrect = []
    for i in range(len(passwords)):
        control = 0
        for a in range (0,10):
            for m in range (0,8):
                value = passwords[i][m]
                if value in string.punctuation or value in string.ascii_letters:
                    control = 0
                else:
                    value = passwords[i][m]
                    if value in string.digits:
                        control += 1
                    else:
                        control = 0
        if control > 1:
            incorrect.append(passwords[i])
        else:
            correct.append(passwords[i])
    print("Hatalı Şifreler: ",incorrect)
    print("Hatasız Şifreler: ",correct)

passcontrol(passwords)                 
