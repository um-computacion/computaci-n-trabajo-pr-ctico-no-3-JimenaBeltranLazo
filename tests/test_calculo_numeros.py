#FASE 1: Implementación de Pruebas "Manejo de Excepciones"

import unittest
from src.calculo_numeros import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100') # este patch controla lo que hace el input
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='-100') # este patch controla lo que hace el input
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='AAA') # este patch controla lo que hace el input
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()