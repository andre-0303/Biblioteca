class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

    def __str__(self):
        return f'{self.titulo} - {self.autor} ({self.ano_publicacao}), {self.genero}'
    
class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def listar_livros(self):
        if not self.catalogo:
            print("A biblioteca está vazia")
        else:
            print("Lista de livros na biblioteca:")
            for index, livro in enumerate(self.catalogo, start=1):
                print(f'{index}. {livro}')  

if __name__ == "__main__":
    biblioteca = Biblioteca()

    livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605, "Romance")
    livro2 = Livro("Harry Potter e a Pedra Filosofal", "J.K Rowling", 1996, "Ficção")
    livro3 = Livro("1984", "George Orwell", 1949, "Ficção Científica")
    livro4 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Literatura infantil")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)
    biblioteca.adicionar_livro(livro4)

    biblioteca.listar_livros()