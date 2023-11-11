import os
from bd import BD

class Interface:
    def __init__(self):
        self.banco = BD("catalogoCarros.db")
    
    def menuInicial(self):
        print("======================")
        print("--Cadastro de carros--")
        print("======================")
        print()

    def limpaTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def selecionaOpcao(self, opcoesPermitidas = []):
        opcaoSelecionada = input("Digite a opçao desejada: ") 

        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcaoSelecionada)
        
        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcaoSelecionada)

        #verificar se a opção selecianada é uma das opções validas
        if opcaoSelecionada not in opcoesPermitidas:
            print("Opção inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        return opcaoSelecionada


    def mostrarMenuInicial(self):
        print("1 - Adicionar carros")
        print("2 - Carros Cadastrado")
        print("3 - Excluir carro")
        print("4 - Alterar dados")    
        print("0 - SAIR")
        print()

    def mostrarCadastroCarros(self):
        self.menuInicial()

        print("Insira os dados do carro:")
        print("(Campos com * são obrigatórios)")
        print()

        marca = self.inserirValor('Digite a marca*: ', 'texto', False)
        modelo = self.inserirValor('Digite o modelo*: ', 'texto', False)
        anoFabricacao = self.inserirValor('Digite o ano de fabricação*: ', 'texto', False)
        anoModelo = self.inserirValor('Digite o ano do modelo*: ', 'texto', False)
        tipoCarro = self.inserirValor('Digite o tipo do seu carro*:      (hatch, sedan, SUV, pickup)', 'texo', False)
        versaoModelo = self.inserirValor('Digite o versão do seru carro: ', 'texto', True)
        cor = self.inserirValor('Digite a cor: ', 'texto', True)
        
        # Armazenar os valores no banco de dados!

        valores = {
            "marca": marca,
            "modelo": modelo,
            "ano_fabricacao": anoFabricacao,
            "ano_modelo": anoModelo,
            "tipo_carro": tipoCarro,
            "versao_modelo": versaoModelo,
            "cor": cor
        }
        
        self.banco.inserir('carros', valores)

    def mostarCarrosCadastrados(self):
        self.menuInicial()
        print("Veja a lista de carros cadadstrados.")
        print()

        carros = self.banco.buscarDados('carros')

        for carro in carros:
            id, marca, modelo, ano_fabricacao, ano_modelo, tipo_carro, versao_modelo, cor = carro
            print (f"Carros {id} - {modelo, marca, versao_modelo} | {ano_fabricacao, ano_modelo} | {cor} ")
            
        print()


        input("Aperte Enter para continuar...")



    def inserirValor(self, dados, tipo = 'texto', permiteNulo = False):
        valor = input(dados)

        #verificar se está vazio
        if valor == "" and not permiteNulo:
            print("Valor inválido!")
            return self.inserirValor(dados, tipo, permiteNulo)
        elif valor == "" and permiteNulo:
            return valor


        if tipo == 'numero':
            try:
                valor = float(valor)
            except ValueError:
                print("Valor inválido!") 
                return self.solicitarValor(dados, tipo, permiteNulo)     
            
        return valor
        
        
    