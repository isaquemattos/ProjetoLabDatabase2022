from connection.oracle_queries import OracleQueries
#
# Implementar 
# Base montada 
# #
class Relatorio:
    def __init__(self):
        with open("sql/relatorio/fundos.sql") as f:
            self.query_relatorio_fundos = f.read()

        with open(".sql") as f:
            self.query_relatorio_= f.read()

        with open(".sql") as f:
            self.query_relatorio_ = f.read()

        with open("sql") as f:
            self.query_relatorio_ = f.read()

        with open(".sql") as f:
            self.query_relatorio_ = f.read()

        with open("sql") as f:
            self.query_relatorio_itens_ = f.read()

    def get_relatorio_(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_pedidos))
        input("Pressione Enter para Sair do Relatório de ")

    def get_relatorio_(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_pedidos_por_fornecedor))
        input("Pressione Enter para Sair do Relatório de ")

    def get_relatorio(iself):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos))
        input("Pressione Enter para Sair do Relatório de ")

    def get_relatorio(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
        input("Pressione Enter para Sair do Relatório de ")

    def get_relatorio(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_fornecedores))
        input("Pressione Enter para Sair do Relatório de ")

    def get_relatorio(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_itens_pedidos))
        input("Pressione Enter para Sair do Relatório de")