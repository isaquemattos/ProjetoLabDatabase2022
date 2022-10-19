from connection.oracle_queries import OracleQueries

class SplashScreen:

    def __init__(self):
        self.qry_total_ = "select count(1) as total_produtos from " # informar tabela 
        self.qry_total_ = "select count(1) as total_clientes from " # informar tabela 
        self.qry_total_ = "select count(1) as total_fornecedores from " # informar tabela 
        self.qry_total_ = "select count(1) as total_pedidos from " # informar tabela 
        self.qry_total_ = "select count(1) as total_itens_pedido from " # informar tabela 
        self.created_by = "Daniel Marinho"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_total_produtos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_produtos)["total_produtos"].values[0]

    def get_total_clientes(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_clientes)["total_clientes"].values[0]

    def get_total_fornecedores(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_fornecedores)["total_fornecedores"].values[0]

    def get_total_pedidos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_pedidos)["total_pedidos"].values[0]

    def get_total_itens_pedidos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_itens_pedido)["total_itens_pedido"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - :         {str(self.get_total_produtos()).rjust(5)} #informar nome da tabela
        #      2 - :         {str(self.get_total_clientes()).rjust(5)} #informar nome da tabela 
        #      3 - :         {str(self.get_total_fornecedores()).rjust(5)} #informar nome da tabela 
        #      4 - :         {str(self.get_total_pedidos()).rjust(5)} #informar nome da tabela 
        #      5 - :         {str(self.get_total_itens_pedidos()).rjust(5)} #informar nome da tabela 
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """