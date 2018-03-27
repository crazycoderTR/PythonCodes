#coding:utf-8
def switch(value):
    case = {}
    try:
        case = {
                0:'Case 0\'ın degeri', #Birinci secenek
                1:'Case 1\'ın değeri', #İkinci seçenek
                2: 'Case 2\'ın değeri',#Üçüncü seçenek
                3: 'Case 3\'ın değeri',#Dördüncü seçenek
                4: 'Case 4\'ın değeri', #Beşinci seçenek
                'default':'Yanlış bir değer girdiniz!' # diğer dillerde olduğu gibi default case değerini oluşturma
            }
        return (case[value])  # parametreden gelen değeri ana fonksiyona geri dönderiyoruz
    except KeyError:
        return (case['default']) #hatalı giriş olduğu anda default değeri ana fonksiyona geri dönderiyoruz .

def main(): 
    while True:
      try:
         value = int(input("Lütfen bir tam sayı girin ... : "))
         answer = switch(value) #switch fonksiyonumuzu çağırıyoruz .
         print(answer) #dönen yanıtı ekrana yazdırıyoruz
         break #programın döngüden çıkmasını sağlıyoruz
      except ValueError:
         print("Girdiğiniz değer bir tam sayı değil")
         continue
main() #main fonksiyonumuzu çağırıyoruz   
