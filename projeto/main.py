class lerConta:
    def __init__(self, conta):
        self.conta = conta

    def coloca_1x(self):
        self.conta=self.conta[:]
        self.conta.find("(")



