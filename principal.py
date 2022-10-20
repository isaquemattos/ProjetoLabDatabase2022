from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
#from controller.controller_produto import Controller_Produto
#from controller.controller_cliente import Controller_Cliente
#from controller.controller_fornecedor import Controller_Fornecedor
#from controller.controller_pedido import Controller_Pedido
#from controller.controller_item_pedido import Controller_Item_Pedido

tela_inicial = SplashScreen()
relatorio = Relatorio()



#ctrl_produto = Controller_Produto()
#ctrl_cliente = Controller_Cliente()
#ctrl_fornecedor = Controller_Fornecedor()
#ctrl_pedido = Controller_Pedido()
#ctrl_item_pedido = Controller_Item_Pedido()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-6]: "))
            config.clear_console(1)

            #reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            #inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            #atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            #excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()