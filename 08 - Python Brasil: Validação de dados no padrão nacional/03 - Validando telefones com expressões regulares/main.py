from TelefonesBr import TelefonesBr
import re

telefone = "esse é o meu telefone 556198440a minha esposa 5548991901576 é 25561984631000 e não tenho mais outros"

telefone_objeto = TelefonesBr(telefone)


print(telefone_objeto.numeros_encontrados())