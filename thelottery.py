#coding:utf-8
import random

def fill_estimate():
    estimates = []
    for i in range(6):
        estimates.append(input("Sayı giriniz: "))
    lottery_check(estimates)

def lottery_check(estimates):
    lottery = []
    for i in range(6):
        lottery.append(random.randint(1,49))
    control(estimates,lottery)

def control(estimates,lottery):
    true_known = []
    for i in range(6):
        if estimates[i] == lottery[i]:
            true_known.append(i)
    print("Tahminleriniz: ",estimates)
    print("Sayısal Loto: ",lottery)
    print("Doğru Bilinenler: ",true_known)

fill_estimate()
