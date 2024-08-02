class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

def _str_(self):
    return f'O(A) {self.nome} tem {self.idade} anos e trabalha como {self.profissao}'

@property
def idade_pessoa(self):
    return f'{self.nome} tem {self.idade} anos'

def aniversario(self):
    self.idade += 1

def saudacao(self):
    if self.profissao:
        return f'Olá {self.nome}! Muito legal você trabalhar como {self.profissao}'
    else:
        return f'Olá {self.nome}!'
    
pessoa1 = Pessoa(nome='Thiago', idade=39, profissao='Orçamentista')
pessoa2 = Pessoa(nome='Thais', idade=37, profissao='Compradora')
pessoa3 = Pessoa(nome='Isabel', idade=58)

print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa3.aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)