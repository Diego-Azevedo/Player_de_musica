from view.tela_abstrata import TelaAbstrata

class TelaPlayer(TelaAbstrata):
    def tela_opcoes(self):
        print("____PLAYER____")
        print("1 - Escolher Música")
        print("2 - Tocar Música Aleatória")
        print("0 - Voltar")
        opcao = int(input("Escolha a Opção: "))
        return opcao