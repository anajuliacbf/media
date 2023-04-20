print("Digite o primeiro número:")
num1 = int(input())
print("Digite o segundo número:")
num2 = int(input())

if num1 == num2:
    media = (num1+num2) / 2
    print ("Os números são iguais e a média deles é:", media)
elif num1>num2:
    print("O maior número é:", num1)
else:
    print("O maior número é:", num2)  
