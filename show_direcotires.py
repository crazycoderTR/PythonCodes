#coding:utf-8
import os
from functools import reduce

def show_Dr(grap_dir = 0, grap_files = 1,directory = "", index = 0):
    oopok = "┣━"
    oopno = "┗━"
    oopcontinue = " ┃  "
    maindr = list(os.listdir("/"))
    if index == len(maindr):
        return 1
    else:
        if directory != "":
            for top, dirs, files in list(os.walk(directory)):
                grap_dir = len(top.split("/")) - 2 #dizinlerin soldan-sağa kaç birim öteleneceği
                print(oopcontinue*(grap_dir),oopno,top)
                grap_files = len(top.split("/")) - 1 #alt dizinlerin soldan-sağa kaç birim öteleneceği
                for file in files:
                    print(oopcontinue*(grap_files),oopok,file)
        show_Dr(grap_dir, grap_files, "/"+maindr[index], index+1)
def main():
    show_Dr()
main()
