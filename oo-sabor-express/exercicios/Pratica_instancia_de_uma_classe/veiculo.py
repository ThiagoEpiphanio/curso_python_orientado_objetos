class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self._marca} {self.modelo} - Status: {status}"