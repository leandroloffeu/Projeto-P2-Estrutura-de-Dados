[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2022/03/campus_marica.png)](https://universidadedevassouras.edu.br/campus-marica/)

# Engenharia de Software
### Cristiano Cesar Xavier Marinho
### Leandro Loffeu Pereira Costa
## Estrutura de Dados - 3º Período
### Professor: Marcio Garrido

P2 - Enunciado e regras

P2 - Enunciado e regras
A Universidade de Vassouras do Campus 1 foi convidada pela prefeitura de Maricá para promover uma solução tecnológica em um dos problemas sociais da cidade, o abandono de animais. Mesmo considerado crime (O abandono de animais é crime, previsto na Lei de Crimes Ambientais - Lei Federal n° 9.605 de 1998), e notório que o índice de abandono vem crescendo a cada ano.
Os alunos do curso de Engenharia de Software foram convocados para a reunião com a secretaria da cidade para entender a demanda solicitada e alguns pontos foram levantados.
A prefeitura precisa de um sistema que possa cadastrar todos os animais por tipo (canino, felino, etc.) e para tanto, é uma premissa que seja possível inserir novos tipos dinamicamente. Precisa ainda, que sejam classificados por idade aproximada, cor, porte e se possui alguma particularidade. No mesmo sistema, deverá ter também um cadastro de pessoas interessadas na adoção, contendo os dados principais de contato e qual espécie teria o interesse de adotar. Ao escolher a espécie, deve também informar se possui alguma preferência do animal. Por fim, no final do mês a prefeitura emitirá um relatório de cruzamento de espécies disponíveis x possíveis candidatos, ou quando um candidato a adoção ligar, que o atendente possa pesquisar se há algum animal com as características informadas.
Os alunos anotaram atentamente a todas as observações, criaram o fluxograma do estudo de caso, e posteriormente o primeiro protótipo em Python, ainda que em modo texto, e sem requisitos gráficos. A ideia foi apenas validar a proposta do programa junto ao solicitante.



Regras de avaliação
Fluxograma em PDF no repositório (1 ponto )
Organização clara (0,5 pontos)
Funcional de acordo com o enunciado (0,5 pontos)
Estrutura de dados do algoritmo (4 pontos)
Uso de ao menos 4 métodos de fila ou pilha (0,5 ponto)
Uso de ao menos 4 métodos recursivos (0,5 pontos)
Uso de pesquisa binária, lista encadeada (0,5 pontos)
O programa rodar com tratamento de erros - "entradas inválidas do usuário" (0,5 pontos)
O programa atender ao enunciado proposto (2 pontos)
Organização do projeto (3 pontos)
Hierarquia dos arquivos e organização das pastas - diretórios, nome de arquivos, classes etc... (1 ponto)
Relação commit/dia com no mínimo 50 commits no final do projeto e no máximo 5 commits dia ( 1ponto)
Organização do Readme do projeto contendo Título do projeto, enunciado, participantes, nome do professor (linkando para meu github), disciplina e ao menos 3 imagens do fluxograma, código e o programa rodando. (1 ponto)





A estrutura do código é composta por três classes: Animal, Pessoa e Prefeitura.

A classe Animal define as características de um animal, como tipo, idade, cor, porte e particularidade. O método __init__ é o construtor da classe e é responsável por inicializar os atributos do objeto.

A classe Pessoa representa uma pessoa interessada em adotar um animal. Ela possui atributos como nome, contato, espécie de interesse e preferência. Assim como na classe Animal, o método __init__ é responsável pela inicialização dos atributos.
