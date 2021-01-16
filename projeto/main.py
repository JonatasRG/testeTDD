class lerConta:
    def __init__(self, conta):
        self.conta = conta

    def coloca_x_entre_numero_e_o_parantes(self):
        #self.conta=self.conta[:]

        abre_paranteses=self.conta.find("(",1)
        #while (abre_paranteses >=0)  and (abre_paranteses < len(self.conta)):
        while abre_paranteses >= 0 :
            e_numero= self.conta[abre_paranteses - 1].isnumeric()
            e_fecha_parentes = True if self.conta[abre_paranteses - 1] == ")" else False
            if e_numero or e_fecha_parentes:
                self.conta=self.conta[:abre_paranteses]+"x"+self.conta[abre_paranteses:]

            abre_paranteses = self.conta.find("(",abre_paranteses+1)

    def transforma_subtracao_em_soma_de_negativo(self):
        subtracao_de_numero = self.conta.find("-", 1)
        while subtracao_de_numero >= 0:
            e_numero = self.conta[subtracao_de_numero - 1].isnumeric()
            e_fecha_parentes = True if self.conta[subtracao_de_numero - 1] == ")" else False
            if e_numero or e_fecha_parentes:
                self.conta=self.conta[:subtracao_de_numero]+"+"+self.conta[subtracao_de_numero:]
            subtracao_de_numero = self.conta.find("-", subtracao_de_numero + 1)




