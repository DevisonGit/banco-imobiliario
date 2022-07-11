import unittest
from banco_imobiliario.propriedade import PRECO_MAXIMO, PRECO_MINIMO, Propriedade
from banco_imobiliario.jogador import Jogador


class TestPropriedade(unittest.TestCase):
    def setUp(self) -> None:
        self.propriedade = Propriedade()
        
    
    def test_custo_de_venda_dentro_range(self):
        self.assertTrue(PRECO_MINIMO <= self.propriedade.custo_de_venda <= PRECO_MAXIMO)
        
    def test_custo_de_venda_fora_range(self):
        self.propriedade.custo_de_venda = 502
        self.assertFalse(PRECO_MINIMO <= self.propriedade.custo_de_venda <= PRECO_MAXIMO)

    def test_none_proprietario_inicio(self):
        self.assertEqual(self.propriedade.proprietario, None)
    
    def test_proprietario(self):
        self.propriedade.proprietario = Jogador('teste')
        self.assertIsInstance(self.propriedade.proprietario, Jogador)
        
    def test_custo_venda(self):
        self.assertIsInstance(self.propriedade.custo_de_venda, int)
        
    def test_valor_aluguel(self):
        self.assertIsInstance(self.propriedade.valor_do_aluguel, float)