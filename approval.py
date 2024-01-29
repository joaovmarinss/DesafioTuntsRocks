import math
def avarege_calc(noteP1,noteP2,noteP3):
    return (noteP1 + noteP2 + noteP3)/3

def notefinal_calc(avarage):
    for i in range(1,101):
        if ((i+avarage)/2) >= 50:
            return i
            break
              


def situation(avarage):
    if avarage < 50 : return "Reprovado por Nota"
    elif 50<= avarage < 70: 
        notefinal_calc(avarage)
        return "Exame Final" 
    else : return "Aprovado"

def presence(fouls):
    if (((60 - fouls)/60)*100 < 75):
        return True

def situation_pres(fouls):
    if(presence(fouls)):
        return False , "Reprovado por Falta"
    else : 
        return True, "x"

