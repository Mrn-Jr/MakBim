


class Jogador:

    def __init__(self, nome: str, saldo_inicial: float = 25000.0):

        if not nome or not nome.strip() :

            raise ValueError("O nome do jogador não pode ser vazio")

        if saldo_inicial <= 0:
            raise ValueError("Valor inicial não pode ser menor ou igual a 0")


        self.nome = nome
        self.saldo = saldo_inicial



    def debitar(self, valor: float) -> None:
        """
        Deduz uma quantia específica de fundos do saldo atual do jogador.
        
        Parâmetros:
            valor (float): O montante a ser retirado da conta do jogador.
            
        Regras de Negócio / Validações:
            - O valor a ser debitado deve ser estritamente maior que zero.
            - O jogador deve possuir saldo igual ou superior ao valor do débito solicitado.
              Caso contrário, o sistema deve impedir a operação por Saldo Insuficiente.
              
        Efeitos:
            - Altera o estado do objeto Jogador, reduzindo o seu saldo atual.
        """
        pass

    def creditar(self, valor: float) -> None:
        """
        Adiciona uma quantia específica de fundos ao saldo atual do jogador.
        
        Parâmetros:
            valor (float): O montante a ser adicionado à conta do jogador.
            
        Regras de Negócio / Validações:
            - O valor a ser creditado deve ser estritamente maior que zero.
            
        Efeitos:
            - Altera o estado do objeto Jogador, incrementando o seu saldo atual.
        """
        pass

    def obter_saldo(self) -> float:
        """
        Consulta e retorna o saldo financeiro atual do jogador.
        
        Retorno:
            float: O saldo atual do jogador.
        """
        pass

