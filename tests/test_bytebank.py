import pytest
from codigo.bytebank import Funcionario
from pytest import mark
class TestClass:
    @mark.idade
    def test_quando_idade_recebe_23_03_1995_deve_retornar_28(self):
        # Given-Contexto
        entrada = '23/03/1995'
        esperado = 28

        # When - Ação
        funcionario_teste = Funcionario('Leonardo', entrada, 1000)
        resultado = funcionario_teste.idade()
        # Then - Então
        assert resultado == esperado
    @mark.sobrenome
    def test_quando_sobrenome_recebe_Leonardo_Grava_deve_retornar_Grava(self):
        # Given-Contexto
        entrada = 'Leonardo Grava'
        esperado = 'Grava'

        # When - Ação
        leonardo = Funcionario(entrada, '23/03/1995', 1000)
        resultado = leonardo.sobrenome()

        # Then - Então
        assert resultado == esperado


    @mark.decrescimo_salario
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        #given-contexto
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome,'10/01/2000',entrada_salario)
        resultado = funcionario_teste.decrescimo_salario()
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # given-contexto
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '10/01/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            # given-contexto
            entrada = 1000000

            funcionario_teste = Funcionario('Teste', '10/01/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
