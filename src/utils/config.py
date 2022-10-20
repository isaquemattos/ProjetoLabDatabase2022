MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Fundos
2 - Relatório de Empreendimentos
3 - Relatório de Cotações Gerais
4 - Relatório de Cotações Por Fundos 
5 - Relatório de Endereços 
6 - Relatório de Endereços por Segmentos
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - FUNDOS 
2 - EMPREENDIMENTOS
3 - COTAÇÕES
4 - ENDEREÇOS
"""

def clear_console(wait_time:int=3):
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")