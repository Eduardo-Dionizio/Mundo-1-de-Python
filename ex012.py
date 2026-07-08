preco = float(input("Qual é o preço do produto? R$"))
desconto = preco * 0.05

valor_total = preco - desconto

print(f"O produto custava R${preco}, na promoção com 5% de desconto vai custar R${valor_total:.2f}")
