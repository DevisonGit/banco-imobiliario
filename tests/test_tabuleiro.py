from unittest import mock
from banco_imobiliario.tabuleiro import QTD_JOGADORES, QTD_MAXIMA_RODADAS, QTD_PROPRIEDADES, Tabuleiro
from banco_imobiliario.propriedade import Propriedade
from banco_imobiliario.jogador import Jogador
import unittest
from unittest.mock import Mock, patch


class TestTabuleiro(unittest.TestCase):
    def setUp(self) -> None:
        self.tabuleiro = Tabuleiro()
        

    def test_popular_propriedades(self):
        self.tabuleiro.popular_propriedades()
        self.assertEqual(QTD_PROPRIEDADES, len(
            self.tabuleiro.lista_propriedades))

    def test_objeto_propriedade(self):
        self.tabuleiro.popular_propriedades()
        self.assertIsInstance(
            self.tabuleiro.lista_propriedades[0], Propriedade)

    def test_popular_jogadores(self):
        self.tabuleiro.popular_jogadores()
        self.assertEqual(QTD_JOGADORES, len(self.tabuleiro.lista_jogadores))

    def test_objeto_jogador(self):
        self.tabuleiro.popular_jogadores()
        self.assertIsInstance(
            self.tabuleiro.lista_jogadores[0], Jogador)
    
    def test_ordem_aleatoria_inicio(self):
        self.tabuleiro.popular_jogadores()
        lista_inicial = self.tabuleiro.lista_jogadores
        self.tabuleiro.ordem_aleatoria()
        self.assertEqual(lista_inicial, self.tabuleiro.lista_jogadores)
    
    def test_partida(self):
        self.tabuleiro.popular_propriedades()
        self.tabuleiro.popular_jogadores()
        self.tabuleiro.ordem_aleatoria()
        resultado = self.tabuleiro.partida()
        self.assertIsNotNone(resultado)
        self.assertIsInstance(resultado, tuple)
        
   
    @patch('banco_imobiliario.tabuleiro')
    def test_partida_resultado_mocado(self, MockTabuleiro):
        tabuleiro = MockTabuleiro()
        tabuleiro.partida.return_value = ('exigente', 200)
        self.assertEqual(tabuleiro.partida(), ('exigente', 200))
        self.assertIsInstance(tabuleiro.partida(), tuple)
    
    def test_vencedor_unico_na_lista(self):
        self.tabuleiro.lista_jogadores = [Jogador('aleatorio')]
        self.tabuleiro.qtd_rodadas = 300
        resultado = self.tabuleiro.vencedor()
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(resultado, ('aleatorio', 300))    
        
    def test_vencedor_time_out_saldo_empatado(self):
        self.tabuleiro.lista_jogadores = [Jogador('exigente'), Jogador('caulteloso') ]
        self.tabuleiro.qtd_rodadas = 1001
        resultado = self.tabuleiro.vencedor()
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(resultado, ('exigente', 1001))
        
    def test_vencedor_time_out_saldo_maior(self):
        self.tabuleiro.lista_jogadores = [Jogador('exigente'), Jogador('caulteloso')]
        self.tabuleiro.lista_jogadores[1].saldo = 500
        self.tabuleiro.qtd_rodadas = 1001
        resultado = self.tabuleiro.vencedor()
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(resultado, ('caulteloso', 1001))
        
    def test_vencedor_time_out_saldo_igual_ordem_jogada(self):
        self.tabuleiro.lista_jogadores = [Jogador('exigente'), Jogador('caulteloso'), Jogador('impulsivo')]
        self.tabuleiro.lista_jogadores[1].saldo = 500
        self.tabuleiro.lista_jogadores[1].saldo = 500
        self.tabuleiro.qtd_rodadas = 1001
        resultado = self.tabuleiro.vencedor()
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(resultado, ('caulteloso', 1001))