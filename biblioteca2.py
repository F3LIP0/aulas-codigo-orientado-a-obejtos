class Livro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponivel = True

    def adicionar(self, biblioteca):
        biblioteca.livros.append(self)

    @staticmethod
    def buscar(biblioteca, termo):
        resultados = []
        for livro in biblioteca.livros:
            if termo.lower() in livro._titulo.lower() or termo.lower() in livro._autor.nome.lower():
                resultados.append(livro)
        return resultados

    def emprestar(self, usuario):
        if self._disponivel:
            self._disponivel = False
            usuario.livros_emprestados.append(self)
            print(f"{self._titulo} foi emprestado a {usuario.nome}.")
        else:
            print(f"{self._titulo} não está disponível para empréstimo.")

    def devolver(self, usuario):
        if self in usuario.livros_emprestados:
            self._disponivel = True
            usuario.livros_emprestados.remove(self)
            print(f"{self._titulo} foi devolvido por {usuario.nome}.")
        else:
            print(f"{usuario.nome} não possui o livro {self._titulo}.")

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def isbn(self):
        return self._isbn

    @property
    def disponivel(self):
        return self._disponivel


class Autor:
    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    @property
    def nome(self):
        return self._nome


class Usuario:
    def __init__(self, nome, usuario_id):
        self._nome = nome
        self._usuario_id = usuario_id
        self.livros_emprestados = []

    @property
    def nome(self):
        return self._nome


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.log_alugueis = []  

    def listar_livros(self):
        if self.livros:
            print("\nLivros disponíveis na biblioteca:")
            for livro in self.livros:
                status = "Disponível" if livro.disponivel else "Emprestado"
                print(f"Título: {livro.titulo}, Autor: {livro.autor.nome}, ISBN: {livro.isbn}, Status: {status}")
        else:
            print("Nenhum livro na biblioteca.")

    def registrar_aluguel(self, usuario, livro):
        self.log_alugueis.append(f"{usuario.nome} alugou {livro.titulo}")

    def registrar_devolucao(self, usuario, livro):
        self.log_alugueis.append(f"{usuario.nome} devolveu {livro.titulo}")

    def listar_logs(self):
        if self.log_alugueis:
            print("\nLogs de Aluguel e Devolução:")
            for log in self.log_alugueis:
                print(log)
        else:
            print("Nenhum registro de aluguel ou devolução.")



def main():
    
    autor1 = Autor("J.K. Rowling", "Britânica")
    autor2 = Autor("George Orwell", "Britânico")

    
    livro1 = Livro("Harry Potter e a Pedra Filosofal", autor1, "9780747532743")
    livro2 = Livro("1984", autor2, "9780451524935")

    
    biblioteca = Biblioteca()
    livro1.adicionar(biblioteca)
    livro2.adicionar(biblioteca)

    
    usuario1 = Usuario("Alice", 1)

    while True:
        print("\nMenu:")
        print("1. Buscar um livro na biblioteca")
        print("2. Aluguel de livros")
        print("3. Adicionar um novo livro")
        print("4. Sair")

        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == '1':
            biblioteca.listar_livros()
            termo = input("Digite o título ou autor para buscar: ")
            resultados = Livro.buscar(biblioteca, termo)
            print(f"\nResultados da busca por '{termo}':")
            if resultados:
                for livro in resultados:
                    print(f"Título: {livro.titulo}, Autor: {livro.autor.nome}, ISBN: {livro.isbn}")
            else:
                print("Nenhum livro encontrado com esse termo.")

        elif escolha == '2':
            biblioteca.listar_livros()
            livro_titulo = input("Digite o título do livro que deseja alugar: ")
            livro_encontrado = next((livro for livro in biblioteca.livros if livro.titulo.lower() == livro_titulo.lower()), None)

            if livro_encontrado:
                livro_encontrado.emprestar(usuario1)
                if not livro_encontrado.disponivel:
                    biblioteca.registrar_aluguel(usuario1, livro_encontrado)

            else:
                print("Livro não encontrado.")

            
            devolver = input("Deseja devolver um livro? (s/n): ")
            if devolver.lower() == 's':
                livro_titulo_devolver = input("Digite o título do livro que deseja devolver: ")
                livro_encontrado = next((livro for livro in usuario1.livros_emprestados if livro.titulo.lower() == livro_titulo_devolver.lower()), None)

                if livro_encontrado:
                    livro_encontrado.devolver(usuario1)
                    if livro_encontrado.disponivel:
                        biblioteca.registrar_devolucao(usuario1, livro_encontrado)
                else:
                    print("Você não possui esse livro.")

        elif escolha == '3':
            titulo = input("Digite o título do livro: ")
            nome_autor = input("Digite o nome do autor: ")
            nacionalidade_autor = input("Digite a nacionalidade do autor: ")
            isbn = input("Digite o ISBN do livro: ")

            autor = Autor(nome_autor, nacionalidade_autor)
            novo_livro = Livro(titulo, autor, isbn)
            novo_livro.adicionar(biblioteca)
            print(f"O livro '{titulo}' foi adicionado com sucesso à biblioteca!")

        elif escolha == '4':
            print("Saindo...")
            break

        else:
            print("Escolha inválida.")

        
        biblioteca.listar_logs()


if __name__ == "__main__":
    main()