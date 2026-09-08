import datetime 


class Transacao:

    def __init__(self, origem: str, destino: str, valor: int, descricao: str):

        self.origem = origem
        self.destino = destino
        self.valor = valor
        self.descricao = descricao

        self.timestamp = datetime.datetime.now()
