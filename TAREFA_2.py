#2)Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
#  sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5,
#  8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
#  informado um número, ele calcule a sequência de Fibonacci e retorne
#  uma mensagem avisando se o número informado pertence ou não a
#  sequência.


numeroInformado = int(input("Informe um valor para verificar se faz parte da sequência de Fibonacci: "))
num1 = 0
num2 = 1
resultado = False
while num1 <= numeroInformado:
    if num2 == numeroInformado:
        resultado = True
        break
    num1,num2 = num2, num1+num2
if resultado :
    print(f" O valor informado, {numeroInformado}, faz parte da sequência de Fibonacci")
else:
    print(f"O valor informado, {numeroInformado}, não faz parte da sequência de Fibonacci")

