


class Jogador:

    def __init__(self, nome: str, saldo_inicial: float = 25000.0):

        if not nome or not nome.strip() :

            raise ValueError("O nome do jogador não pode ser vazio")

        if saldo_inicial <= 0:
            raise ValueError("Valor inicial não pode ser menor ou igual a 0")


        self.nome = nome
        self.saldo = saldo_inicial



    def debitar(self, valor: float) -> None:


        if valor <= 0 :
            raise ValueError("O valor precisa ser positivo") 


        if valor > self.saldo :
            raise ValueError(
                "Saldo insuficiente."
                f"O valor precisa ser menor que {self.saldo}"
            )

        self.saldo -= valor 

    def creditar(self, valor: float) -> None:

        if valor < 0 :
            raise ValueError("O valor precisa ser maior que 0")


        self.saldo += valor


    def obter_saldo(self) -> float:
    
        return self.saldo

