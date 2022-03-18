class Cliente:

    def __init__(self, nome):
        self.__nome = nome  # Aqui é adicionado os 2 __ após o ponto. Isso indica que o atributo é privado.
        
    # get em Python (presisa ter o mesmo nome do atributo)
    @property # Diz ao Python que aqui é uma propriedade que acessa o atributo da classe (igual ao get em java) e nao é preciso usar o (). mas para ele funcionar o atributo nome tem que ter dois __.
    def nome(self):
        print('Chamando @property nome()') 
        return self.__nome.title()

    # set em Python (presisa ter o mesmo nome do atributo)
    @nome.setter
    def nome(self, nome):
        print('Chamando setter nome()') 
        self.__nome = nome