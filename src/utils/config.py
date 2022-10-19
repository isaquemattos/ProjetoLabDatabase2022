MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de 
2 - Relatório de 
3 - Relatório de 
4 - Relatório de 
5 - Relatório de 
6 - Relatório de  
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - 
2 - 
3 - 
4 - 
5 -
"""

def clear_console(wait_time:int=3):
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")