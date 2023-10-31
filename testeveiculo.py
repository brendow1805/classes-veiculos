# Testando a classe em veiculo

# Criação e instância do objeto da classe:
from Veiculos import veiculos

minhaCaranga = veiculos('147', 'Fiat', 'Amarelo',  0)

#Acelerar a minha caranga
for cont in range (1,151):
    minhaCaranga.acelerar()
    minhaCaranga. frear()
# Exibir a minha caranga
print (minhaCaranga)