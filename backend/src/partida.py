from backend.models.transacao import Transacao
from typing import List, Dict



class Partida:
    """
    Orquestrador e gerente de estado central da partida do jogo de tabuleiro.
    
    Esta classe encapsula a lógica das entidades Jogador e Banco, valida as regras de limite
    de participantes, gerencia transferências multilaterais e centraliza o histórico de auditoria.
    """
    def __init__(self, saldo_inicial: float = 25000.0):
        """
        Inicializa uma nova partida do jogo, criando a instância do Banco e definindo
        a estrutura de dados para o gerenciamento de jogadores e logs de auditoria.
        
        Parâmetros:
            saldo_inicial (float): O saldo padrão que será distribuído para cada novo jogador cadastrado.
        """
        pass

    def cadastrar_jogador(self, nome: str) -> None:
        """
        Registra um novo participante na partida antes de o jogo de fato iniciar.
        
        Parâmetros:
            nome (str): O nome único identificador do jogador.
            
        Regras de Negócio / Validações:
            - O nome do jogador não pode ser nulo, vazio ou conter apenas espaços em branco.
            - Não é permitido o cadastro de dois jogadores com o mesmo nome na mesma partida.
            - O número de jogadores cadastrados deve estar estritamente na faixa de 2 a 6 pessoas.
              Se houver tentativa de cadastrar um 7º jogador, uma exceção de capacidade máxima deve ser lançada.
              
        Efeitos:
            - Instancia um novo objeto Jogador e o armazena na lista/dicionário de controle de jogadores ativos.
        """
        pass

    def transferir_entre_jogadores(self, nome_pagador: str, nome_recebedor: str, valor: float) -> None:
        """
        Executa uma transferência de fundos direta de um jogador para outro jogador.
        
        Parâmetros:
            nome_pagador (str): O nome do jogador que pagará o valor.
            nome_recebedor (str): O nome do jogador que receberá o valor.
            valor (float): O montante financeiro a ser transferido.
            
        Regras de Negócio / Validações:
            - Ambos os jogadores (pagador e recebedor) precisam estar ativos e cadastrados na partida.
            - O valor da transferência deve ser estritamente maior que zero.
            - O pagador não pode realizar uma transferência para si mesmo.
            - O pagador deve possuir fundos suficientes em seu saldo atual para realizar a transação.
            
        Efeitos:
            - Deduz o saldo do jogador pagador.
            - Incrementa o saldo do jogador recebedor.
            - Cria e armazena uma nova instância de Transacao no histórico de auditoria da partida.
        """
        pass

    def transacionar_com_banco(self, nome_jogador: str, valor: float, do_banco_para_jogador: bool, descricao: str) -> None:
        """
        Executa e registra transações financeiras unilaterais entre um jogador e o Banco.
        
        Esta função serve para automatizar ações em que o Banco é parte ativa da transação, 
        como o pagamento de aluguéis ao banco, prêmios ou passagem pela casa inicial.
        
        Parâmetros:
            nome_jogador (str): O nome do jogador que está transacionando.
            valor (float): O montante envolvido na transação.
            do_banco_para_jogador (bool): Sinalizador da direção financeira.
                                           - Se True: Banco realiza pagamento para o Jogador.
                                           - Se False: Jogador realiza pagamento para o Banco.
            descricao (str): Descrição contextual do motivo da transação (ex: "Comprou Avenida Paulista", "Imposto de Renda").
            
        Regras de Negócio / Validações:
            - O jogador envolvido precisa estar cadastrado na partida.
            - O valor deve ser estritamente maior que zero.
            - Caso a direção seja do Jogador para o Banco (False), o jogador precisa ter saldo suficiente para o pagamento.
            
        Efeitos:
            - Modifica o saldo do jogador envolvido (incrementando se receber, decrementando se pagar).
            - Registra um novo objeto Transacao no histórico contendo a direção correta de fluxo.
        """
        pass

    def obter_historico_transacoes(self) -> List[Transacao]:
        """
        Recupera todo o histórico de logs de auditoria das transações ocorridas na partida.
        
        Retorno:
            List[Transacao]: Uma lista contendo todas as instâncias de Transacao ordenadas cronologicamente.
        """
        pass

    def obter_relatorio_saldos(self) -> Dict[str, float]:
        """
        Fornece um instantâneo rápido e consolidado do estado financeiro atual de todos os jogadores ativos.
        
        Retorno:
            Dict[str, float]: Um mapeamento chave-valor onde a chave é o nome do jogador e o valor é o seu saldo atual.
        """
        pass
