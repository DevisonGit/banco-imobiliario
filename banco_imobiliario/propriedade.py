from random import randrange

PORCENTAGEM_DO_ALUGUEL = 0.30
PRECO_MINIMO = 150
PRECO_MAXIMO = 500
PASSO = 5


class Propriedade():
    def __init__(self) -> None:
        self.custo_de_venda = randrange(PRECO_MINIMO, PRECO_MAXIMO, PASSO)
        self.valor_do_aluguel = self.custo_de_venda * PORCENTAGEM_DO_ALUGUEL
        self.proprietario = None


    def __str__(self) -> str:
        return f"Custo: {self.custo_de_venda}, Aluguel: {self.valor_do_aluguel}, Proprietario: {self.proprietario}"