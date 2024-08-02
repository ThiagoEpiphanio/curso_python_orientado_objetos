# 1) Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular='', saldo=0, ativo=False)
        self.titular = titular
        self.saldo = saldo
        self._ativo = ativo

# 2) Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
class ContaBancaria:
    def __init__(self, titular='', saldo=0, ativo=False)
        self.titular = titular
        self.saldo = saldo
        self._ativo = ativo
    
    def __str__(self):
        return f'Olá {self.titular}, você tem disponível R${self.saldo} de saldo'
    
titular1 = ContaBancaria('Thiago', 4500.00)
titular2 = ContaBancaria('Isabel', 3000.00)

print(titular1)
print(titular2)


# 3) Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
@classmethod
def ativar_conta(cls, conta):
    conta._ativo = True

titular3 = ContaBancaria('Antonio Carlos', 7000.00)
print(f'Antes de ativar: Conta ativa? {titular3._ativo}')
ContaBancaria.ativar_conta(titular3)
print(f'Depois de ativar: Conta ativa? {titular3._ativo}')   

# 4)Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

# 5) Crie uma instância da classe e imprima o valor da propriedade titular.
titular4 = ContaBancariaPythonica('Thomas', 2000.00)
print(f'Titular dessa conta: {titular4.titular}')

# 6) Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome='', idade=0, ativo=False, profissao='', renda=0.00):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.renda = renda

cliente1 = ClienteBanco('Thiago', 39, True, 'Orçamentista', 2200.00)
cliente2 = ClienteBanco('Thais', 37, True, 'Compradora', 5000.00)
cliente3 = ClienteBanco('Isabel', 58, True, 'Operadora de Atendimento', 3000.00)

# 7) Crie um método de classe para a conta ClienteBanco.
class ClienteBanco:
    
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta