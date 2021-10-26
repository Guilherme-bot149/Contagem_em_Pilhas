def main():
    seq = [4, 3, 2, 1]
    pilha = []
    soma_sequencial = 0
    soma_todos = 0
    for elemento in seq:
        pilha.append(elemento)
        print ("Elemento: ", elemento)
        print("Pilha: ", pilha)
        soma_sequencial += elemento
        print("Resultado Sequencial: ", soma_sequencial)
        print("------------------------------------------")

    while len(pilha) > 0:
        print(pilha)
        topo = pilha.pop()
        soma_todos += topo
        print("Elemento do topo: ", topo)
        print("Resultado de todos: ", soma_todos)
        print("------------------------------------------")
main()
