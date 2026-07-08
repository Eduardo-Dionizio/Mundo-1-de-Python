a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

if a >= b and a >= c:
    maior = a
if b >= a and b >= c:
    maior = b
if c >= b and c >= a:
    maior = c


if a <= b and a <= c:
    menor = a
if b <= c and b <= a:
    menor = b
if c <= b and c <= a: 
    menor = c

print(f"O maior número é {maior}, e menor número é {menor}")