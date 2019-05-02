def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


numero = int(input("Informe um número: "))
if numero<0:
    print("Valor inválido!")
else:
    print(fatorial(numero))
