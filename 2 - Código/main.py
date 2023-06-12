from classe import *


def exibir_menu():
    print("Menu:")
    print("1. Cadastrar animal")
    print("2. Cadastrar pessoa interessada")
    print("3. Pesquisar animais disponíveis")
    print("4. Pesquisar pessoas")
    print("5. Gerar relatório")
    print("6. Sair")

# Instanciar a classe Prefeitura
prefeitura = Prefeitura()

while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")


    if escolha == "1":
        tipo = input("Tipo do animal: ")
        idade = input("Idade do animal: ")
        cor = input("Cor do animal: ")
        porte = input("Porte do animal: ")
        particularidade = input("Particularidade do animal: ")
        prefeitura.cadastrar_animal(tipo, idade, cor, porte, particularidade)
        print("Animal cadastrado com sucesso!")

    elif escolha == "2":
        nome = input("Nome da pessoa interessada: ")
        contato = input("Contato da pessoa interessada: ")
        especie_interesse = input("Espécie de interesse da pessoa: ")
        preferencia = input("Preferência da pessoa (opcional): ")
        prefeitura.cadastrar_pessoa_interessada(nome, contato, especie_interesse, preferencia)
        print("Pessoa interessada cadastrada com sucesso!")

    elif escolha == "3":
        especie = input("Espécie a pesquisar: ")
        preferencia = input("Preferência (opcional): ")
        animais_encontrados = prefeitura.pesquisar_animal(especie, preferencia)
        if animais_encontrados:
            print("Animais disponíveis:")
            for animal in animais_encontrados:
                print(f"Tipo: {animal.tipo}")
                print(f"Idade: {animal.idade}")
                print(f"Cor: {animal.cor}")
                print(f"Porte: {animal.porte}")
                print(f"Particularidade: {animal.particularidade}")
                print("----------")
        else:
            print("Nenhum animal encontrado.")
    
    elif escolha == "4":
        pessoa = input("Digite o nome da pessoa: ")
        pessoa_encontrada = prefeitura.pesquisar_pessoas(pessoa)
        if pessoa_encontrada:
            print("Pessoas: ")
            for pessoa in pessoa_encontrada:
                print(f"Tipo: {pessoa.nome}")
                print(f"Idade: {pessoa.contato}")
                print(f"Cor: {pessoa.especie_interesse}")
                print(f"Porte: {pessoa.preferencia}")
                print("----------")
        else:
            print("Nenhum dado encontrado.")

    elif escolha == "5":
        prefeitura.gerar_relatorio()

    elif escolha == "6":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Escolha novamente.")
