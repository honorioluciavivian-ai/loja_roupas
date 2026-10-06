
#tupla: a lista de tamanhos não muda
TAMANHOS = ("PP", "P", "M", "G", "GG")

#lista de dicionários: um por produto
vitrine = [
    {"nome": "camiseta basica", "preco": 39.90, "tamanho": "M"},
    {"nome": "calça jeans", "preco": 129.90, "tamanho": "G"},
    {"nome": "moletom", "preco": 159.90, "tamanho": "P"},
]

    #listra de pares (nome, quantidade)
carrinho = [("camiseta basica", 3), ("calça jeans", 1)]

precos = {}

for produto in vitrine:
    precos[produto["nome"]] = produto["preco"]

total = 0

for nome, quantidade in carrinho: 
    total = total + precos[nome] * quantidade 

print("peças na vitrine:", len(vitrine))
print("total do carrinho: R$", round(total, 2))

print(vitrine[1] ["preco"])
print(TAMANHOS[-1])
print(len(carrinho))
print(precos["moletom"] * 2)
