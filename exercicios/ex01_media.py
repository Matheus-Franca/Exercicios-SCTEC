nota1 = 3
nota2 = 4
nota3 = 2

media = (nota1 + nota2 + nota3) / 3

if media < 5 : print(f"Média: {media:.2f} - Reprovado")
elif media == 5 and media < 7 : print(f"Média: {media:.2f} - Recuperação")
else : print(f"Média: {media:.2f} - Aprovado")