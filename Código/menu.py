from classe import*


def exibir_menu():
    print("Menu:")
    print("1. Cadastrar animal")
    print("2. Cadastrar pessoa interessada")
    print("3. Pesquisar animais disponíveis")
    print("4. Gerar relatório")
    print("5. Sair")

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
        prefeitura.gerar_relatorio()

    elif escolha == "5":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Escolha novamente.")
