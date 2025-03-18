dados =  {'alunos': [{'nome': 'João','P1': 10, 'P2': 5.5},{'nome': 'Pedro','P1': 2, 'P2': 8}]}
lista_aprovados = []
for aluno in dados['alunos']:

    print(f"{aluno['nome']} | Média: {(aluno["P1"]+aluno["P2"])/2} | Situação: {"APROVADO" if (aluno['P1']+aluno['P2'])/2 > 6 else "REPROVADO"}| Nota1: {aluno['P1'] } | Nota2: {aluno['P2']}")

