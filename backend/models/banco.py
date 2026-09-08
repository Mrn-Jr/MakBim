from backend.models.jogador import Jogador



class Banco:
    """
    Representa a entidade reguladora da economia do jogo.
    
    O Banco atua com dinheiro infinito, sendo capaz de injetar fundos na partida 
    (pagando prêmios, salários) ou absorver fundos (recebendo taxas, impostos, leilões e compras de propriedades).
    """
    def pagar_jogador(self, jogador: Jogador, valor: float) -> None:
        """
        Realiza um repasse de capital do Banco para o saldo de um Jogador específico.
        
        Parâmetros:
            jogador (Jogador): A instância do jogador que deve ser creditado.
            valor (float): O montante a ser pago pelo Banco.
            
        Regras de Negócio / Validações:
            - O valor de repasse deve ser estritamente maior que zero.
            - Como o Banco possui caixa infinito, não há verificação ou impedimento por saldo insuficiente do emissor.
            
        Efeitos:
            - Altera o estado do Jogador fornecido através do método de crédito deste.
        """
        pass

    def receber_de_jogador(self, jogador: Jogador, valor: float) -> None:
        """
        Recebe fundos de um jogador que está realizando um pagamento oficial ao Banco.
        
        Parâmetros:
            jogador (Jogador): A instância do jogador que está efetuando o pagamento.
            valor (float): O montante a ser transferido ao Banco.
            
        Regras de Negócio / Validações:
            - O valor de pagamento deve ser estritamente maior que zero.
            - O jogador de origem deve possuir fundos suficientes para quitar a dívida com o Banco.
            
        Efeitos:
            - Altera o estado do Jogador fornecido através do método de débito deste.
        """
        pass
