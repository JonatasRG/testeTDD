from unittest import TestCase

from projeto.main import lerConta


class TestlerConta(TestCase):
    def test_coloca_1x(self):
        conta_testada=lerConta("4(4-1)")
        conta_testada.coloca_1x()
        self.assertEqual(conta_testada.conta,"4x(4-1)")
        #self.fail()
