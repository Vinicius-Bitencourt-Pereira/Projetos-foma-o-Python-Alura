from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            return "Quantidades de digitos está incorreta !"


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.documento = documento
        else:
            raise ValueError("CPF inválido")

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def mask_cpf(self):
        mask = CPF()
        return mask.mask(self.documento)

    def __str__(self):
        return "O CPF {} é válido...".format(self.mask_cpf())


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.documento = documento
        else:
            raise ValueError("CNPJ inválido")

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def mask_cnpj(self):
        mask = CNPJ()
        return mask.mask(self.documento)

    def __str__(self):
        return "O CNPJ {} é válido...".format(self.mask_cnpj())