lampadas = [0, 0, 0]

# Função para ligar/desligar os interruptores
def botao_inter(interruptor):
    lampadas[interruptor] = 1 - lampadas[interruptor]

# Primeira ida à sala
botao_inter(0)

# Segunda ida à sala
botao_inter(0)
botao_inter(1)

# Verificar resultados
for i, lampada in enumerate(lampadas):
    print(f"Lâmpada {i + 1}: {'Acesa' if lampada == 1 else 'Apagada'}")