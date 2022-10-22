from model.fundos import Fundo
from connection.oracle_queries import OracleQueries

class Controller_fundos:
    def __init__(self):
        pass
        
    def inserir_fundos(self) -> Fundo:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo CPF
        ticker = input("Fundos (Novo): ")

        if self.verifica_existencia_fundos(oracle, ticker):
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            # Insere e persiste o novo cliente
            oracle.write(f"insert into clientes values ('{ticker}', '{nome}')")
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_fundo = oracle.sqlToDataFrame(f"select ticker, nome from fundos where ticker = '{ticker}'")
            # Cria um novo objeto Cliente
            novo_fundo = Fundo(df_fundo.ticker.values[0], df_fundo.nome.values[0])
            # Exibe os atributos do novo cliente
            print(novo_fundo.toString)
            # Retorna o objeto novo_cliente para utilização posterior, caso necessário
            return novo_fundo
        else:
            print(f"O ticker do fundos {ticker} já está cadastrado.")
            return None

    def atualizar_fundos(self) -> Fundo:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        ticker = int(input("informe o ticker do fundo: "))

        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia_fundos(oracle, ticker):
            # Solicita a nova descrição do cliente
            novo_nome = input("Nome (Novo): ")
            # Atualiza o nome do cliente existente
            oracle.write(f"update fundo set nome = '{novo_nome}' where ticker = {ticker}")
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_fundos = oracle.sqlToDataFrame(f"select ticker, nome from fundos where ticker = {ticker}")
            # Cria um novo objeto cliente
            nome_fundos_atualizado = Fundo(df_fundos.ticker.values[0], df_fundos.nome.values[0])
            # Exibe os atributos do novo cliente
            print(nome_fundos_atualizado.toString())
            # Retorna o objeto cliente_atualizado para utilização posterior, caso necessário
            return nome_fundos_atualizado
        else:
            print(f"O ticker do fundos {ticker} não existe.")
            return None

    def excluir_fundos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o CPF do Cliente a ser alterado
        ticker = int(input("ticker do fundo que irá excluir: "))        

        # Verifica se o cliente existe na base de dados
        if not self.verifica_existencia_cliente(oracle, ticker):            
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_cliente = oracle.sqlToDataFrame(f"select ticker, nome from fundos where ticker = {ticker}")
            # Revome o cliente da tabela
            oracle.write(f"delete from fundos where ticker = {ticker}")            
            # Cria um novo objeto Cliente para informar que foi removido
            fundo_excluido = Fundo(df_cliente.ticker.values[0], df_cliente.nome.values[0])
            # Exibe os atributos do cliente excluído
            print("Cliente Removido com Sucesso!")
            print(fundo_excluido.toString())
        else:
            print(f"O ticker do fundo {ticker} não existe.")

    def verifica_existencia_fundos(self, oracle:OracleQueries, fundos:str=None) -> bool:
        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_cliente = oracle.sqlToDataFrame(f"select fundo, from clientes where ticker = {fundos}")
        return df_cliente.empty