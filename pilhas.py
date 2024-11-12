class Pilha:
    def __init__(self, max_size):
        self.itens = []
        self.max_size = max_size

    def push(self, item):
        if len(self.itens) < self.max_size:
            self.itens.append(item)
            print(f"{item} foi adicionado na pilha")
        else:
            print("ERRO! pilha no tamanha maximo")
        

    def pop(self):
        if self.is_empty():
            print("ERRO, pilha vazia para realiazar a ação")
            return None
        else:
            item = self.itens.pop()
            print(f"{item} removido da pilha")
            return item

    def peek(self):
        if self.is_empty():
            print("Erro: Pilha vazia. Não é possível realizar 'peek'.")
            return None
        else:
            topo = self.itens[-1]
            print(f"Topo da pilha: '{topo}'")
            return topo

    def is_empty(self):
        return len(self.itens) == 0
   
    def estado_pilha(self):
      
        if self.is_empty():
            print("A pilha está vazia.")
        else:
            print(f"Estado atual da pilha: {self.itens}")

def menu():
    """Função que exibe o menu para o usuário e permite interagir com a pilha."""
    print("Escolha uma operação:")
    print("1. Adicionar elemento (push)")
    print("2. Remover elemento (pop)")
    print("3. Ver topo da pilha (peek)")
    print("4. Ver estado da pilha")
    print("5. Sair")
    return input("Opção: ")

def main():
    """Função principal que executa as operações sobre a pilha."""
    try:
        max_size = int(input("Digite o tamanho máximo da pilha: "))
        itens = Pilha(max_size)

        while True:
            opcao = menu()

            if opcao == '1':  # Operação push
                item = input("Digite o item a ser adicionado: ")
                itens.push(item) # type: ignore
            elif opcao == '2':  # Operação pop
                itens.pop()
            elif opcao == '3':  # Operação peek
                itens.peek()
            elif opcao == '4':  # Ver estado da pilha
                itens.estado_pilha()
            elif opcao == '5':  # Sair
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido para o tamanho da pilha.")

if __name__ == "__main__":
    main()



