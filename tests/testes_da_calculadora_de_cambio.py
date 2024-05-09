from unittest import TestCase
import src.calculadora_de_cambio as calc

class TestesDaCalculadoraDeCambio(TestCase):

    def teste_conversao_cambio_valor_0_taxa_5_03_retorna_0(self):
        # Arrange
        valor = 0
        taxa = 3.37
        resultado_esperado = 0

        # Act
        resultado_obtido = calc.converter(valor, taxa)

        # Assert
        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_conversao_cambio_valor_1000_taxa_5_10_retorna_196_07(self):
        # Arrange
        valor = 1000.0
        taxa = 5.10
        resultado_esperado = 196.07

        # Act
        resultado_obtido = calc.converter(valor, taxa)

        # Assert
        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_conversao_cambio_valor_1000_taxa_2_retorna_500_00(self):
        # Arrange
        valor = 1000.0
        taxa = 2
        resultado_esperado = 500.00

        # Act
        resultado_obtido = calc.converter(valor, taxa)

        # Assert
        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_conversao_cambio_valor_50_taxa_5_05_retorna_0(self):
        valor = -50.0
        taxa = 5.05
        resultado_esperado = 0.00

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_conversao_cambio_valor_0_10_taxa_5_05_retorna_0_01(self):
        valor = 000.01
        taxa = 5.05
        resultado_esperado = 0.01

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_conversao_cambio_valor_35_10_taxa_5_05_retorna_6_95(self):
        valor = 35.10
        taxa = 5.05
        resultado_esperado = 6.95

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)
