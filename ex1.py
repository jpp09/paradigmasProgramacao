lista_alunos = []
notas_aluno = []



for i in range(1,4):
    nomeAluno = input("Digite nome do aluno: ")
    nota1 = float(input(f"Digite a 1° nota do {nomeAluno}: "))
    nota2 = float(input(f"Digite a 2° nota do {nomeAluno}: "))
    lista_alunos.append(nomeAluno)
    notas_aluno.append([nota1,nota2])

print(f"{"Nome".ljust(10)} | {"P1".ljust(10)} | {"P2".ljust(10)} | {"Média".ljust(10)} | {"Situação".ljust(10)}")

for i in range(len(lista_alunos)):
    media = sum(notas_aluno[i])/2
    if media >= 6:
        print(f"{f"{lista_alunos[i]}".ljust(10)} | {f"{notas_aluno[i][0]}".ljust(10)} | {f"{notas_aluno[i][1]}".ljust(10)} | {media} | {f"Aprovado".ljust(10)}")
    else:
        print(f"{f"{lista_alunos[i]}".ljust(10)} | {f"{notas_aluno[i][0]}".ljust(10)} | {f"{notas_aluno[i][1]}".ljust(10)} | {media} | {f"Reprovado".ljust(10)}")

    