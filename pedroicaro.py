# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date 
Hoje = date.today()
Anoatual = Hoje.year
IdadeMaior = print ("")
IdadeMenor = print ("")
for I in range(8):
    Nascimento =  int(input("digite seu ano de nascimento: "))
    if Anoatual - Nascimento >= 18:
        IdadeMaior.append(Nascimento)
    else:
        IdadeMenor.append(Nascimento)
print(f"As pessoa que nasceram em {IdadeMaior}, ja atingiram a maior idade.")
print(f"As pessoa que nasceram em {IdadeMenor}, ainda nâo atingiram a maior idade.")