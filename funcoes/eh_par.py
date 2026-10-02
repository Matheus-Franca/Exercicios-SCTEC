
valor = int(input("Digite um valor para verificar se é par: "))


def eh_par(valor):
    """True se n for par, False se for ímpar."""
    return valor % 2 == 0

print(eh_par(valor))
