from cpf_cnpj import Documento
from validate_docbr import CNPJ

# cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))

exemplo_cnpj = '34419285000111'
exemplo_cpf = '09131316956'

documento = Documento.cria_documento(exemplo_cnpj)



print(documento)
