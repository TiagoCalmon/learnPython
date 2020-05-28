#Programa Simulador de Dados
#exibe um número aleatório entre 1 e 6 a cada interação
#AUTHOR: TIAGO CALMON
#DATA 15-04-2020

import random
random.seed(a=None, version=2)
a=1
b=6
print(random.randint(a, b))
print(1 // 2 * 3)
while(int(input("vc deseja rodar novamente(1,0)"))==0):
    print(random.randint(a, b))