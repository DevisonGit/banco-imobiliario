import unittest

from banco_imobiliario.jogador import Jogador
from banco_imobiliario.propriedade import Propriedade

TIPOS_DE_JOGADORES = ['impulsivo', 'exigente', 'cauteloso', 'aleatorio']
QTD_PROPRIEDADES = 20


class TestJogador(unittest.TestCase):
    def setUp(self):
        self.lista_jogadores = [Jogador(tipo) for tipo in TIPOS_DE_JOGADORES]
        self.propriedade = Propriedade()
        self.jogador = self.lista_jogadores[0]
        self.proprietario = self.lista_jogadores[1]

    def compra_propriedade(self, **kwargs):
        self.propriedade.custo_de_venda = kwargs.get('custo')
        self.propriedade.valor_do_aluguel = kwargs.get('aluguel')
        self.jogador.compra_propriedade(self.propriedade)
        self.assertEqual(self.propriedade.proprietario,
                         kwargs.get('proprietario_esperado'))
        self.assertEqual(self.jogador.saldo, kwargs.get('saldo_esperado'))
        self.assertEqual(self.jogador.propriedades,
                         kwargs.get('propriedades_esperada'))

    def dict_compra_sucesso(self, custo, aluguel):
        return {"custo": custo, "aluguel": aluguel, "proprietario_esperado": self.jogador, "propriedades_esperada": [
            self.propriedade], "saldo_esperado": self.jogador.saldo - custo}

    def dict_compra_insucesso(self, custo, aluguel):
        return {"custo": custo, "aluguel": aluguel, "proprietario_esperado": None, "propriedades_esperada": [], "saldo_esperado": self.jogador.saldo}

    def test_muda_posicao_inicial(self):
        self.jogador.mudar_posicao(5, QTD_PROPRIEDADES)
        self.assertEqual(self.jogador.posicao, 4)

    def test_muda_posicao_final(self):
        self.jogador.posicao = 19
        self.jogador.mudar_posicao(5, QTD_PROPRIEDADES)
        self.assertEqual(self.jogador.posicao, 4)

    def test_saldo_inicial(self):
        valida_saldo = []
        for jogador in self.lista_jogadores:
            if jogador.saldo == 300:
                valida_saldo.append(True)
        self.assertNotIn(False, valida_saldo)

    def test_bonus_volta_completa(self):
        self.test_muda_posicao_final
        self.jogador.bonus_volta_completa()
        self.assertEqual(self.jogador.saldo, 400)

    def test_pagar_aluguel(self):
        self.jogador.pagar_aluguel(self.proprietario, 50)
        self.assertEqual(self.jogador.saldo, 250)
        self.assertEqual(self.proprietario.saldo, 350)

    def test_elimado(self):
        self.compra_propriedade(**self.dict_compra_sucesso(200, 100))
        self.jogador.eliminado()
        self.assertEqual(self.propriedade.proprietario, None)

    def test_compra_propriedade_impulsivo_com_saldo(self):
        self.compra_propriedade(**self.dict_compra_sucesso(200, 100))

    def test_compra_propriedade_impulsivo_sem_saldo(self):
        self.compra_propriedade(**self.dict_compra_insucesso(350, 100))

    def test_compra_propriedade_exigente_com_saldo(self):
        self.jogador = self.lista_jogadores[1]
        self.compra_propriedade(**self.dict_compra_sucesso(200, 100))

    def test_compra_propriedade_exigente_sem_saldo(self):
        self.jogador = self.lista_jogadores[1]
        self.compra_propriedade(**self.dict_compra_insucesso(350, 100))

    def test_compra_propriedade_exigente_valor_aluguel_sucesso(self):
        self.jogador = self.lista_jogadores[1]
        self.compra_propriedade(**self.dict_compra_sucesso(200, 100))

    def test_compra_propriedade_exigente_valor_aluguel_insucesso(self):
        self.jogador = self.lista_jogadores[1]
        self.compra_propriedade(**self.dict_compra_insucesso(200, 45))

    def test_compra_propriedade_cauteloso_com_saldo(self):
        self.jogador = self.lista_jogadores[2]
        self.compra_propriedade(**self.dict_compra_sucesso(200, 100))

    def test_compra_propriedade_cauteloso_custo(self):
        self.jogador = self.lista_jogadores[2]
        self.compra_propriedade(**self.dict_compra_insucesso(250, 45))

    def test_compra_propriedade_cauteloso_sem_saldo(self):
        self.jogador = self.lista_jogadores[2]
        self.compra_propriedade(**self.dict_compra_insucesso(350, 45))
