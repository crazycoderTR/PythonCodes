#coding:utf-8
class Programmer():
    def __init__(self,name,sname,salary,languages):
        self.name = name
        self.sname = sname
        self.salary = salary
        self.languages = languages
    def showInformation(self):
        print("""
        Yazılımcı objesinin özellikleri

        İsim = {}

        Soyisim = {}

        Maaş = {}

        Bildiği Diller = {}
        
        """.format(self.name,self.sname,self.salary,self.languages))
    def addLang(self,language):
        self.languages.append(language)
programmer = Programmer("Mesut","KILINCASLAN",10000,["java","C#","javascript","Python"])
programmer.addLang("Ruby")
programmer.showInformation()
