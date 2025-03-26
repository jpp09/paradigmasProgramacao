#1 - Sucessor e antecessor
#numero = int(input("Digite um n° inteiro: "))
#print(f"n° = {numero}\nAntecessor = {numero -1}\nSucessor = {numero +1}")

#2 - N° interio com duas casas decimais
#n = int(input("Digite um número inteiro: "))
#print(f"Esse é o n°: {n:.2f}")

#3 - Média de 4 notas
#notas = []
#for i in range(1,5):
#    nota = float(input(f"Digite o valor da {i}° nota:"))
#    notas.append(nota)

#print(f"A média é: {sum(notas)/4}")


#4 - Par e impar
#n = int(input("Digite um numero: "))
#if n % 2 == 0:
#    print("Par")
#else:
#    print("Impar")

#5 - Urna eletronica
    #3 Candidatos fixos - (Menu) - N° + Nome
    #Escolher o candidato
    #Encerrar votação - Computar os votso para cada candidato | Vencedor

candidatos = {
    "Maria": 0,
    "Pedro": 0,
    "José": 0,
}

while True:
    print('-'*20)
    print("Eleição 2030")
    print("-"*20)
    print("Aperte:\n1 - Votar em Maria\n2 - Votar em Pedro\n3 - Votar em José\n4 - Sair")
    choice = int(input("Digite o n° do seu candidato: "))
    if choice == 1:
        candidatos["Maria"] += 1
    elif choice == 2:
        candidatos["Pedro"] += 1
    elif choice == 3:
        candidatos["José"] += 1
    else:
        print("*"*20)
        print("Obrigado pela sua votação")
        print("*"*20)

