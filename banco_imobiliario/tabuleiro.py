from random import randint, shuffle
# comentar caso for rodar os testes
from jogador import Jogador
from propriedade import Propriedade
# Descomentar caso for rodas os testes
# from banco_imobiliario.jogador import Jogador
# from banco_imobiliario.propriedade import Propriedade

QTD_MAXIMA_RODADAS = 1000
QTD_PROPRIEDADES = 20
QTD_JOGADORES = 4
TIPOS_DE_JOGADORES = ['impulsivo', 'exigente', 'cauteloso', 'aleatorio']


class Tabuleiro():
    def __init__(self) -> None:
        self.lista_propriedades = []
        self.lista_jogadores = []
        self.qtd_rodadas = 1

    def popular_propriedades(self):
        for _ in range(QTD_PROPRIEDADES):
            self.lista_propriedades.append(Propriedade())

    def popular_jogadores(self):
        for i in range(QTD_JOGADORES):
            self.lista_jogadores.append(Jogador(TIPOS_DE_JOGADORES[i]))

    def ordem_aleatoria(self):
        # define ordem aleatoria para começo da partida
        shuffle(self.lista_jogadores)

    def partida(self):
        while self.qtd_rodadas <= QTD_MAXIMA_RODADAS:
            self.rodada()
            if len(self.lista_jogadores) == 1:
                break
            self.qtd_rodadas += 1
        return self.vencedor()

    def rodada(self):
        for jogador in self.lista_jogadores:
            dado = randint(1, 6)
            jogador.mudar_posicao(dado, QTD_PROPRIEDADES)
            propriedade = self.lista_propriedades[jogador.posicao]
            if propriedade.proprietario:
                proprietario = propriedade.proprietario
                jogador.pagar_aluguel(
                    proprietario, propriedade.valor_do_aluguel)
            else:
                jogador.compra_propriedade(propriedade)
            if jogador.saldo < 0:
                jogador.eliminado()
                self.lista_jogadores.remove(jogador)
            if jogador.volta_completa:
                jogador.bonus_volta_completa()

    def vencedor(self):
        vencedor = self.lista_jogadores[0]
        if self.qtd_rodadas > QTD_MAXIMA_RODADAS:
            for jogador in self.lista_jogadores:
                if jogador.saldo > vencedor.saldo:
                    vencedor = jogador
        return vencedor.tipo_do_jogador, self.qtd_rodadas

