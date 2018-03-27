#coding:utf-8
import datetime
import locale
locale.setlocale(locale.LC_ALL,"")
print(datetime.date.today().strftime("%d-%B-%A:%y"))
