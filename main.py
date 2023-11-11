from ui import Interface
from bd import BD

ui = Interface()

opcao = ""
while opcao != 0:
    ui.menuInicial()
    ui.mostrarMenuInicial()
    opcao = ui.selecionaOpcao([1,2,3,4, 0])
    ui.limpaTela()

    if opcao == 1:
        ui.mostrarCadastroCarros()
        opcao = ""
        ui.limpaTela()

    elif opcao == 2:
        ui.mostarCarrosCadastrados()
        opcao = ""
        ui.limpaTela    


