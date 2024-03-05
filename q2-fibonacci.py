'''

Author: Raphael Pereira
Data: 04/03/2024
Descrição: Verifica se um numero inteiro pertence a seq. de fibonacci.
Entrada: um número inteiro
Saída: texto informando se o numero está na sequencia

'''
nterms = int(input("Insira um numero inteiro!! "))

n1, n2, valid, count = 0, 1, 0, 0
fibAr = [0]

if nterms <= 0:
   print("Inteiro maior que zero por favor!!")

elif nterms == 1:
   print(n1, "Pertence a sequencia")

else:
   
   while count < nterms or nterms > n2:
       fibAr.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
 
for x in range(1, len(fibAr)):
    if fibAr[x] == nterms:
        print("o elemento pertence")
        valid = x

print("elemento nao encontrado") if valid == 0 else print("encontrado no index: ", valid)
