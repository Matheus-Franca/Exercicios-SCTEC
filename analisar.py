import csv

with open("dados.csv", encoding="utf-8") as arquivo:
    dados = csv.DictReader(arquivo)
    for aluno in dados:
        print(aluno["nome"], aluno["nota"])