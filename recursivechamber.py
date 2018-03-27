#coding:utf-8
import string
def plenty(divided, dividing, result = 0, answer = "", decimal = 0, step = 0):
    if divided < dividing:
        if divided <= 0:
            if answer == "":
                answer = str(float(result))
            return answer
        else:
            if step == 0:
                answer += str(result) + str(",")
                step += 1
            elif step <10:
                answer += str(decimal)
                step += 1   
                decimal = 0
            else:
                return answer  
            return plenty((divided*10)-dividing, dividing, result, answer, decimal+1, step)
    else:
        if "," in answer:
            return plenty(divided-dividing, dividing, result, answer, decimal+1, step)
        else:
            return plenty(divided-dividing, dividing, result+1, answer, decimal, step)
print(plenty(22,7))
