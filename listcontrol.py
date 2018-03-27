#coding:utf-8
import string
def control_firstletter(letter):
    return letter[0].istitle()
values = ["Python","Ruby","PHP","jAVA","scala","go"]
print(list(filter(control_firstletter,values)))


def control_fullletter(character):
    return character.isupper()
print(list(filter(control_fullletter,values)))
