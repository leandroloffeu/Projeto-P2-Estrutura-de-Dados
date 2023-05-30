class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade

class Pessoa:
    def __init__(self, nome, contato, especie_interesse, preferencia):
        self.nome = nome
        self.contato = contato
        self.especie_interesse = especie_interesse
        self.preferencia = preferencia

class Prefeitura:
    def __init__(self):
        self.animais = []
        self.pessoas_interessadas = []
        
    #MÉTODO PARA CADASTRAR ANIMAL PARA ADOÇÃO
    def cadastrar_animal(self, tipo, idade, cor, porte, particularidade):
        animal = Animal(tipo, idade, cor, porte, particularidade)
        self.animais.append(animal)
        
    #MÉTODO PARA CADASTRAR PESSOA INTERESSADA NA ADOÇÃO
    def cadastrar_pessoa_interessada(self, nome, contato, especie_interesse, preferencia):
        pessoa = Pessoa(nome, contato, especie_interesse, preferencia)
        self.pessoas_interessadas.append(pessoa)

    #MÉTODO PARA PESQUISAR ANIMAIS POR TIPO/IDADE/COR/PORTE/PARTICULARIDADE    
    def pesquisar_animal(self, especie, preferencia=None):
        animais_encontrados = []
        for animal in self.animais:
            if animal.tipo == especie:
                if preferencia is None or animal.particularidade == preferencia:
                    animais_encontrados.append(animal)
        return animais_encontrados
    
    
    
    
    #MÉTODO PARA PESQUISAR PESSOAS
    def pesquisar_pessoas(self, nome):
        pessoas_encontradas = []
        for pessoa in self.pessoas_interessadas:
            if pessoa.nome == nome:
                pessoas_encontradas.append(pessoa)
        return pessoas_encontradas

    #MÉTODO PARA GERAR RELATÓRIO
    def gerar_relatorio(self):
        for pessoa in self.pessoas_interessadas:
            animais_disponiveis = self.pesquisar_animal(pessoa.especie_interesse, pessoa.preferencia)
            print(f"Nome: {pessoa.nome}")
            print(f"Contato: {pessoa.contato}")
            print("Animais disponíveis:")
            for animal in animais_disponiveis:
                print(f"Tipo: {animal.tipo}")
                print(f"Idade: {animal.idade}")
                print(f"Cor: {animal.cor}")
                print(f"Porte: {animal.porte}")
                print(f"Particularidade: {animal.particularidade}")
                print("----------")

