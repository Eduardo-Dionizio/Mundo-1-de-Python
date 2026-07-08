print("------------\nAnalisando triangluos\n------------")

r1 = float(input("Digite o comprimento da reta 1: "))
r2 = float(input("Digite o comprimento da reta 2: "))
r3 = float(input("Digite o comprimento da reta 3: "))

if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print("As retas acima podem formar um triângulo")

else:
    print("As retas acima não podem formar um triângulo")