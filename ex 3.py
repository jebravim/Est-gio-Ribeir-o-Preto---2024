
# Sequência a
# Adiciona 2 ao número anterior
a = [1, 3, 5, 7]
proximo_a = a[-1] + 2
a.append(proximo_a)
print("a) Sequência a:", a)

# Sequência b
# Multiplica por 2 o número anterior
b = [2, 4, 8, 16, 32, 64]
proximo_b = b[-1] * 2
b.append(proximo_b)
print("b) Sequência b:", b)

# Sequência c
# Adiciona o próximo quadrado perfeito
c = [0, 1, 4, 9, 16, 25, 36]
proximo_c = c[-1] + (len(c))**2
c.append(proximo_c)
print("c) Sequência c:", c)

# Sequência d
# Adiciona o próximo quadrado perfeito
d = [4, 16, 36, 64]
proximo_d = d[-1] + (len(d)*2)**2
d.append(proximo_d)
print("d) Sequência d:", d)

# Sequência e
# Soma os dois números anteriores (sequência de Fibonacci)
e = [1, 1, 2, 3, 5, 8]
proximo_e = e[-1] + e[-2]
e.append(proximo_e)
print("e) Sequência e:", e)

# Sequência f
# Aumenta o próximo número de 1 em 1, exceto em alguns casos
f = [2, 10, 12, 16, 17, 18, 19]
proximo_f = f[-1] + 1
f.append(proximo_f)
print("f) Sequência f:", f)
