def maior_numero(num1,num2,num3):
    maior=max(num1,num2,num3)
    return maior

num1=float(input('digite o primeiro numero: '))
num2=float(input('digite o segundo numero: '))
num3=float(input('digite o terceiro numero: '))
resultado=maior_numero(num1,num2,num3)
print(f'o maior deles é {resultado}')