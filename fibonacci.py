iloscLiczb = int(input("Ile liczb fibonacciego chcesz uzyskac: "))
lista = []
num1 = 0
num2 = 1

for i in range(iloscLiczb):
    num1 = num2 - num1
    print("Aktualne num1:", num1)
    num2 = num1 + num2
    print("Aktualne num2:", num2)

    lista.append(num1)
    print(lista)
    
