from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_fundos import Controller_fundos
#from controller.controller_cliente import Controller_Cliente
#from controller.controller_fornecedor import Controller_Fornecedor
#from controller.controller_pedido import Controller_Pedido
#from controller.controller_item_pedido import Controller_Item_Pedido

tela_inicial = SplashScreen()
relatorio = Relatorio()



ctrl_produto = Controller_fundos()
#ctrl_cliente = Controller_Cliente()
#ctrl_fornecedor = Controller_Fornecedor()
#ctrl_pedido = Controller_Pedido()
#ctrl_item_pedido = Controller_Item_Pedido()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

   
if __name__ == "__main__":
    run()