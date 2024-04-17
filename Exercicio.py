def mostrar_menu():
    print("Escolha uma das opções:")
    print("1 - Preencher os conjuntos de números")
    print("2 - Realizar as operações")
    print("3 - Sair do programa")

def preencher_numeros():
    global conjunto_A, conjunto_B
    conjunto_A = []
    conjunto_B = []
    print("Insira 5 números para o conjunto A:")
    for i in range(5):
        num = input("Número {}: ".format(i + 1))
        while not num.isdigit():  # Verifica se a entrada é um número
            print("Por favor, insira apenas números.")
            num = input("Número {}: ".format(i + 1))
        conjunto_A.append(int(num))
        
    print("Insira 5 números para o conjunto B:")
    for i in range(5):
        num = input("Número {}: ".format(i + 1))
        while not num.isdigit():  # Verifica se a entrada é um número
            print("Por favor, insira apenas números.")
            num = input("Número {}: ".format(i + 1))
        conjunto_B.append(int(num))

def realizar_operacoes():
    global conjunto_C
    conjunto_C = []
    for i in range(5):
        if conjunto_A[i] % 2 == 0:
            conjunto_C.append(conjunto_A[i] * conjunto_B[i])
        else:
            conjunto_C.append(conjunto_A[i] ** conjunto_B[i])

conjunto_A = []
conjunto_B = []
conjunto_C = []

while True:
    mostrar_menu()
    escolha = input("Digite sua escolha: ")
    if escolha == '1':
        preencher_numeros()
    elif escolha == '2':
        realizar_operacoes()
        print("Conjunto resultante C:", conjunto_C)
    elif escolha == '3':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
2