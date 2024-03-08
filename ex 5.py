# String a ser invertida
string = "Hello, world!"

# Inicializa uma string vazia para armazenar o resultado
inverted_string = ""

# Loop de trás para frente pela string original
for i in range(len(string) - 1, -1, -1):
    inverted_string += string[i]

# Exibe a string invertida
print(inverted_string)