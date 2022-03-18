import re


class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Telefone não encontrado!")

    def __str__(self):
        return self.numeros_encontrados()

    def numeros_encontrados(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"  # "?" indica que aquele grupo não é obrigatorio
        numeros_encontrados = re.findall(padrao, self.numero)
        for numero in numeros_encontrados:  # passando por cada numero que ele encontrar
            print("+{}({}){}-{}".format(numero[0], numero[1], numero[2], numero[3]))

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"     # "?" indica que aquele grupo não é obrigatorio
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"  # "?" indica que aquele grupo não é obrigatorio
        resposta = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(resposta.group(1), resposta.group(2), resposta.group(3), resposta.group(4))
        return numero_formatado