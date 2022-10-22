from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_fundos import Controller_fundos


tela_inicial = SplashScreen()
relatorio = Relatorio()



ctrl_fundos = Controller_fundos()


def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

   
if __name__ == "__main__":
    run()