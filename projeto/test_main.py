from unittest import TestCase

from projeto.main import lerConta


class TestlerConta(TestCase):
    def test_coloca_x_entre_numero_e_o_parantes(self):
        conta_testada=lerConta("4(4-1)")
        conta_testada.coloca_x_entre_numero_e_o_parantes()
        self.assertEqual(conta_testada.conta,"4x(4-1)")

    def test_coloca_x_entre_numeros_e_os_parantes(self):
        conta_testada=lerConta("4(4-1)-5(4-2)")
        conta_testada.coloca_x_entre_numero_e_o_parantes()
        self.assertEqual(conta_testada.conta,"4x(4-1)-5x(4-2)")

    def test_coloca_x_entre_fecha_e_abre_parantes(self):
        conta_testada=lerConta("(4-1)(4-2)")
        conta_testada.coloca_x_entre_numero_e_o_parantes()
        self.assertEqual(conta_testada.conta,"(4-1)x(4-2)")