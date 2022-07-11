from random import randint


SALDO_INICIAL = 300
BONUS_VOLTA_COMPLETA = 100


class Jogador():
    def __init__(self, tipo_do_jogador) -> None:
        self.saldo = SALDO_INICIAL
        self.tipo_do_jogador = tipo_do_jogador
        self.propriedades = []
        self.volta_completa = False
        self.posicao = -1

    def compra_propriedade(self, propriedade):
        if self.saldo >= propriedade.custo_de_venda:
            if self.tipo_do_jogador == 'exigente' and propriedade.valor_do_aluguel <= 50:
                return False
            elif self.tipo_do_jogador == 'cauteloso' and self.saldo - propriedade.custo_de_venda < 80:
                return False
            elif self.tipo_do_jogador == 'aleatorio' and randint(1, 2) == 2:
                return False
            propriedade.proprietario = self
            self.saldo -= propriedade.custo_de_venda
            self.propriedades.append(propriedade)
            return True

    def pagar_aluguel(self, proprietario, aluguel):
        self.saldo -= aluguel
        proprietario.saldo += aluguel

    def mudar_posicao(self, dado, tamanho_tabuleiro):
        self.posicao += dado
        if self.posicao >= tamanho_tabuleiro:
            self.posicao = self.posicao - tamanho_tabuleiro
            self.volta_completa = True

    def bonus_volta_completa(self):
        self.saldo += BONUS_VOLTA_COMPLETA
        self.volta_completa = False

    def eliminado(self):
        for propriedade in self.propriedades:
            propriedade.proprietario = None

    def __str__(self) -> str:
        return f"Jogador: {self.tipo_do_jogador}, Saldo: {self.saldo}, Propriedades: {self.propriedades}"
