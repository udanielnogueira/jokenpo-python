"""
Jogue "Pedra, Papel ou Tesoura" contra o computador.
"""

import random

from time import sleep

# Título do jogo
print("=" * 30)
msg = "JOKENPÔ GAME"
print(f"{msg:^30}")
print("=" * 30)
print()

# Escolha do usuário
print("[1] Pedra [2] Papel [3] Tesoura")
u = input("Escolha: ")

# Escolha do computador
lista = ["1", "2", "3"]
random.shuffle(lista)
c = random.choice(lista)

# Animação
print()
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!")
sleep(1)

# Análise do vencedor
if u == "1":
    if c == "1":
        print("\nEmpate")
    elif c == "2":
        print("\nComputador ganhou!")
    elif c == "3":
        print("\nVocê ganhou!")
elif u == "2":
    if c == "2":
        print("\nEmpate")
    elif c == "1":
        print("\nVocê ganhou!")
    elif c == "3":
        print("\nComputador ganhou!")
elif u == "3":
    if c == "3":
        print("\nEmpate")
    elif c == "1":
        print("\nComputador ganhou!")
    elif c == "2":
        print("\nVocê ganhou!")
else:
    print("\nOpção inválida")
    exit()

# Escolhas
print()
print(f"Usuário escolheu [{u}] Computador escolheu [{c}]")
