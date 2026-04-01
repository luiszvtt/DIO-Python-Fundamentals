#Verificação de vogais -> aplicando estudo de operadores

frase = "Olá, esse é o meu contador de vogais."
vogais = "aeiouAEIOU" #definindo as vogais

total = sum(1 for char in frase if char in vogais) #soma 1 ao total se os caracteres da frase estiverem dentro de vogais

print(total)




    