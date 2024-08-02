# 1)Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro(modelo='Corolla', cor='Preto', ano=1984)

# 2)Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome, categoria, funcionarios, delivery, ativo):
        self.nome = nome
        self.categoria = categoria
        self.funcionarios = funcionarios
        self.delivery = delivery
        self.ativo = ativo

restaurante1 = Restaurante(nome='Subway', categoria='Fast Food', funcionarios='3', delivery='Sim', ativo=True)

# 3)Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
class Restaurante:
    def __init__(self, nome, categoria, funcionarios, delivery, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.funcionarios = funcionarios
        self.delivery = delivery
        self.ativo = ativo

restaurante1 = Restaurante(nome='Subway', categoria='Fast Food', funcionarios='3', delivery='Sim', ativo=True)

# 4)Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
class Restaurante:
    def __init__(self, nome, categoria, funcionarios, delivery, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.funcionarios = funcionarios
        self.delivery = delivery
        self.ativo = ativo
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante1 = Restaurante(nome='Subway', categoria='Fast Food', funcionarios='3', delivery='Sim', ativo=True)
print(restaurante1)

# 5)Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    def __init__(self, nome, idade, classificacao, ativo):
        self.nome = nome
        self.idade = idade
        self.classificacao = classificacao
        self.ativo = ativo

cliente1 = Cliente(nome='Thiago', idade='39', classificacao=4.9, ativo=True)
cliente2 = Cliente(nome='Thais', idade='37', classificacao=4.6, ativo=False)
cliente3 = Cliente(nome='Matheus', idade='1', classificacao=5, ativo=True)