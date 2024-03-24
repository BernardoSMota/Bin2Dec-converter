binNumber = input('Digite um número binário: ')

while True:  # Checking if the input is a binary number
    ok = 0
    for digit in binNumber:
        if digit != '0' and digit != '1':
            binNumber = input('Erro, digite um número binário: ')
            break
        else:
            ok += 1

    if ok == len(binNumber):
        break

power = len(binNumber) - 1
subtotal = 0
for digit in binNumber:
    partial = int(digit) * 2 ** power
    power -= 1
    subtotal += partial
print(subtotal)
