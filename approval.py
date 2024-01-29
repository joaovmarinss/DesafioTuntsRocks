import quickstart
import math
def main():
    
    

    main()

def avarege_calc(noteP1,noteP2,noteP3):
    return (noteP1 + noteP2 + noteP3)/3

def notefinal_calc(avarage):
    finalnote = 0
    for i in range(11):
        if 5 <= (avarage + i)/2:
            finalnote = i   

def situation(avarage):
    if avarage <5: return "Reprovado por Nota"
    elif 5<= avarage < 7: 
        notefinal_calc(avarage)
        return "Exame Final" 
    else : return "Aprovado"

    