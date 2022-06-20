# Importando módulo de erro do SQLite
from datetime import datetime
from sqlite3 import Error

# Importando o módulo/classe de formatação
from time import sleep
from cores import Cores

# Importando arquivo de criação do banco
import schema

# Importando as classes com os metódos
from tipoU import TipoUsuario
from colaborador import Colaborador 
from projeto import Projeto
from tarefa import Tarefa


# Menu principal
def menu():
    print(30 * '*')
    print(f"{Cores.BOLD}{Cores.OKBLUE}******* Menu de Opções *******{Cores.ENDC}")
    print(30 * '*')
    print(f"{Cores.BOLD}1. Colaboradores{Cores.ENDC}")
    print(f"{Cores.BOLD}2. Projetos{Cores.ENDC}")
    print(f"{Cores.BOLD}3. Tarefas{Cores.ENDC}")
    print(f"{Cores.BOLD}4. Usuários{Cores.ENDC}")
    print(f"{Cores.BOLD}{Cores.FAIL}0. Sair{Cores.ENDC}")
    print(30 * '*')

    selecao = int(input('Selecione uma opcão: '))
    return selecao

# Submenu
def submenu(opcao):
    print(30 * '*')
    print(f"{Cores.BOLD}{Cores.OKBLUE}****** {opcao} ******{Cores.ENDC}")
    print(30 * '*')
    print(f"{Cores.BOLD}1. Visualizar registros")
    print(f"2. Inserir {opcao}")
    print(f"3. Atualizar {opcao}")
    print(f"4. Pesquisar em {opcao}")
    print(f"5. Excluir {opcao}{Cores.ENDC}")
    print(f"{Cores.BOLD}{Cores.FAIL}0. Voltar{Cores.ENDC}")
    print(30 * '*')
    opcaosub = int(input('Selecione uma opcão: '))
    return opcaosub


def criar_conexao():
    #Criando a conexão com o banco de dados Sqlite3.
    try:
        schema.initDB()
        print(f"{Cores.BOLD}{Cores.OKGREEN}Tabelas criadas com sucesso!{Cores.ENDC}")
    except Error as e:
        print(e)
        

# Função para limpar a tela antes de exibir a próxima instrução
def limpar():
    import os
    from time import sleep
    
    # Limpar tela
    def screen_clear():
    # Mac/Linux
        if os.name == 'posix':
            _ = os.system('clear')
        else:
        # Windows
            _ = os.system('cls')
    # Aguardar 2 segundos para executar a próxima instrução
    sleep(2)
    # Chamar função de limpeza
    screen_clear()


if __name__ == '__main__':
    limpar()
    print(33 * '*')
    print(f"{Cores.BOLD}{Cores.OKBLUE}******* PROJETO SEMESTRAL *******{Cores.ENDC}")
    print(33 * '*')
    print(f"{Cores.BOLD}{Cores.WARNING}Criando o banco de dados...{Cores.ENDC}")
    sleep(2) 
    print(f"{Cores.BOLD}{Cores.WARNING}Estabelecendo conexão...{Cores.ENDC}")
    sleep(3)
    print(f"{Cores.BOLD}{Cores.WARNING}Criando tabelas do banco de dados...\n{Cores.ENDC}")
    sleep(2)
    criar_conexao()
    input(f"{Cores.BOLD}\nPressione <ENTER> para continuar.{Cores.ENDC}")
    limpar()
    
# Navegação menu
try:
    selecao = menu()
    limpar()
    while selecao != 0:
        
        # OPÇÃO 1: COLABORADORES
        # tabela: COLABORADOR
        # IDC, NOMEC, IDADEC
        if selecao == 1:
            opcao = 'Colaboradores'
            opcaosub = submenu(opcao)
            limpar()
            while opcaosub != 0:
                if opcaosub == 1:
                    print(f"Visualizar registros")
                    Colaborador.exibirC()
                    
                elif opcaosub == 2:
                    print(f"Inserir {opcao}")
                    nomec = input("Nome: ")
                    idadec = input("Idade: ")
                    colab_idtu = input("Cargo: ")
                    Colaborador.inserirC(nomec, idadec, colab_idtu)
                    
                elif opcaosub == 3:
                    print(f"Atualizar {opcao}")
                    
                elif opcaosub == 4:
                    print(f"Pesquisar {opcao}")
                    
                elif opcaosub == 5:
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Excluir {opcao}{Cores.ENDC}")
                    Colaborador.exibirC()
                    idc = input((f"{Cores.BOLD}\nInforme ID do registro a ser deletado: {Cores.ENDC}"))
                    confirma = int(input(f"{Cores.BOLD}{Cores.FAIL}\nTEM CERTEZA QUE DESEJA DELETAR O REGISTRO?\n1 - SIM\n2 - NÃO\n{Cores.ENDC}"))
                    
                    if confirma == 1:
                        Colaborador.deletarC(idc)        
                    elif confirma ==2:
                        print("Operação cancelada.")
                        limpar()
                    else:
                        print("Operação inválida.")
                        limpar()
                    
                elif opcaosub == 0:
                    print(f"Voltar {opcao}")
                    
                else:
                    print('Opção inválida!')
                    limpar()
                limpar()
                opcaosub = submenu(opcao)
                limpar()
            selecao = menu()
            limpar()
            
            
        # OPÇÃO 2: PROJETOS    
        # tabela: PROJETO  
        # IDP, SIGLAP, DESCRICAOP, NOMEGERENTEP
        elif selecao == 2:
            opcao = 'Projetos'
            opcaosub = submenu(opcao)
            limpar()
            while opcaosub != 0:
                if opcaosub == 1:
                    print(f"{Cores.BOLD}{Cores.WARNING}Visualizar registros{Cores.ENDC}")
                    Projeto.exibirP()
                    
                elif opcaosub == 2:
                    print(f"Inserir {opcao}")
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Inserir {opcao}{Cores.ENDC}")
                    # {siglap}, {descricaop}, {nomegerentep}, {projeto_idc}
                    siglap = input("Sigla: ")
                    descricaop = input("Descrição: ")
                    nomegerentep = input("Gerente do projeto: ")
                    projeto_idc = input("Informe o ID do gerente: ")
                    Projeto.inserirP(siglap, descricaop, nomegerentep, projeto_idc)
                                    
                elif opcaosub == 3:
                    print(f"Atualizar {opcao}")
                    
                elif opcaosub == 4:
                    print(f"Pesquisar {opcao}")
                    
                elif opcaosub == 5:
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Excluir {opcao}{Cores.ENDC}")
                    Projeto.exibirP()
                    idp = input((f"{Cores.BOLD}\nInforme ID do registro a ser deletado: {Cores.ENDC}"))
                    confirma = int(input(f"{Cores.BOLD}{Cores.FAIL}\nTEM CERTEZA QUE DESEJA DELETAR O REGISTRO?\n1 - SIM\n2 - NÃO\n{Cores.ENDC}"))
                    
                    if confirma == 1:
                        Projeto.deletarP(idp)        
                    elif confirma ==2:
                        print("Operação cancelada.")
                        limpar()
                    else:
                        print("Operação inválida.")
                        limpar()
                    
                elif opcaosub == 0:
                    print(f"Voltar {opcao}")
                    
                else:
                    print('Opção inválida!')
                    limpar()
                limpar()
                opcaosub = submenu(opcao)
                limpar()
            selecao = menu()
            limpar()
            
            
        # OPÇÃO 3: TAREFAS
        # tabela: TAREFA
        # IDT, SIGLAT, DESCRICAOT, DATAINICIOT, DATAPREVISAOFIMT, DATACONCLUSAOT, ACOESREALIZADAST, NOMECOLABORADORT, TAREFA_IDC, TAREFA_IDP
        elif selecao == 3:
            opcao = 'Tarefas'
            opcaosub = submenu(opcao)
            limpar()
            while opcaosub != 0:
                if opcaosub == 1:
                    print(f"{Cores.BOLD}{Cores.WARNING}Visualizar registros{Cores.ENDC}")
                    Tarefa.exibirT()
                    
                elif opcaosub == 2:
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Inserir {opcao}{Cores.ENDC}")
                    # {idt}, {siglat}, {descricaot}, {datainiciot}, {dataprevisaofimt}, {dataconclusaot}, {acoesrealizadast}, {nomecolaboradort}, {tarefa_idp}, {tarefa_idc}
                    siglat = input("Sigla: ")
                    descricaot = input("Descrição: ")
                    datainiciot = input("Informe a data de inínio: ")
                    dataprevisaofimt = (input("Informe a previsão de conclusão: "))
                    dataconclusaot = input("Informe a data real de conclusão: ")
                    acoesrealizadast = input("Ações realizadas: ")
                    nomecolaboradort = input("Nome do colaborador responsável: ")
                    tarefa_idp = input("A qual projeto esta tarefa pertence? Informe o ID: ")
                    tarefa_idc = input("Informe o ID do colaborador responsável: ")
                    Tarefa.inserirT(siglat, descricaot, datainiciot, dataprevisaofimt, dataconclusaot, acoesrealizadast, nomecolaboradort, tarefa_idp, tarefa_idc)
                    
                elif opcaosub == 3:
                    pass            
                    
                elif opcaosub == 4:
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Pesquisar {opcao}{Cores.ENDC}")
                    
                    print("1. Pesquisar por período\n2. Pesquisar por colaborador\n3. Pesquisar por projeto\n")
                    filtro = int(input(f"{Cores.BOLD}Selecione um filtro: {Cores.ENDC}"))
                    limpar()
                    
                    if filtro == 1:
                        pass 
                    
                    elif filtro == 2:
                        Colaborador.exibirC    
                        tarefa_idc = int(input(f"Informe o {Cores.FAIL}ID{Cores.ENDC} do colaborador: "))
                        Tarefa.pesquisarT(filtro, tarefa_idc)
                        
                    elif filtro == 3:
                        Projeto.exibirP
                        tarefa_idp = int(input(f"Informe o {Cores.FAIL}ID{Cores.ENDC} do projeto: "))
                        Tarefa.pesquisarT(filtro, tarefa_idp)
                    
                elif opcaosub == 5:
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Excluir {opcao}{Cores.ENDC}")
                    Tarefa.exibirT()
                    idt = input((f"{Cores.BOLD}\nInforme ID do registro a ser deletado: {Cores.ENDC}"))
                    confirma = int(input(f"{Cores.BOLD}{Cores.FAIL}\nTEM CERTEZA QUE DESEJA DELETAR O REGISTRO?\n1 - SIM\n2 - NÃO\n{Cores.ENDC}"))
                    
                    if confirma == 1:
                        Tarefa.deletarT(idt)        
                    elif confirma ==2:
                        print("Operação cancelada.")
                        limpar()
                    else:
                        print("Operação inválida.")
                        limpar()
                        
                        
                elif opcaosub == 0:
                    print(f"Voltar {opcao}")
                    
                else:
                    print('Opção inválida!')
                    limpar()
                limpar()
                opcaosub = submenu(opcao)
                limpar()
            selecao = menu()
            limpar()
        
        
        # OPÇÃO 4: USUÁRIOS
        # tabela: TIPOUSUARIO 
        # IDTU, DESCRICAOTU, SIGLATU    
        elif selecao == 4:
            opcao = 'Tipo de usuário'
            opcaosub = submenu(opcao)
            limpar()
            while opcaosub != 0:
                
                if opcaosub == 1:
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Visualizar registros{Cores.ENDC}")
                    TipoUsuario.exibirTU()
                
                elif opcaosub == 2:
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Inserir {opcao}{Cores.ENDC}")
                    # {idtu}, {descricaotu}, {siglatu}
                    descricaotu = input("Descrição: ")
                    siglatu = input("Sigla: ")
                    TipoUsuario.inserirTU(descricaotu, siglatu)
                    
                elif opcaosub == 3:
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Atualizar {opcao}{Cores.OKBLUE}{Cores.ENDC}")
                    TipoUsuario.exibirTU()
                    idtu = int(input(f"{Cores.BOLD}Informe o ID do registro a ser atualizado: {Cores.ENDC}"))
                    descricaotu = (input("\nNova descrição: "))
                    siglatu = (input("Nova sigla: "))
                    TipoUsuario.atualizarTU(idtu, descricaotu, siglatu)
                    
                elif opcaosub == 4:
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Pesquisar {opcao}{Cores.ENDC}")
                    TipoUsuario.pesquisarTU()
                    item = input("Pesquise por ID, descrição ou sigla: ")
                
                elif opcaosub == 5:
                    print(f"{Cores.BOLD}{Cores.OKBLUE}Excluir {opcao}{Cores.ENDC}")
                    TipoUsuario.exibirTU()
                    idtu = input((f"{Cores.BOLD}\nInforme ID do registro a ser deletado: {Cores.ENDC}"))
                    confirma = int(input(f"{Cores.BOLD}{Cores.FAIL}\nTEM CERTEZA QUE DESEJA DELETAR O REGISTRO?\n1 - SIM\n2 - NÃO\n{Cores.ENDC}"))
                                        
                    if confirma == 1:
                        TipoUsuario.deletarTU(idtu)        
                    elif confirma ==2:
                        print("Operação cancelada.")
                        limpar()
                    else:
                        print("Operação inválida.")
                        limpar()                              
                        
                elif opcaosub == 0:
                    print(f"{Cores.BOLD}{Cores.FAIL}Voltar {opcao}{Cores.ENDC}")
                    
                else:
                    print(f'{Cores.BOLD}{Cores.FAIL}Opção inválida!{Cores.ENDC}')
                    limpar()
                limpar()
                opcaosub = submenu(opcao)
                limpar()
            selecao = menu()
            limpar()
            
        else:
            print("Fim.")
            
except ValueError:
    print("Opção inválida. Tente novamente.")

finally:
    print("Pressione <RUN> para executar novamente.")