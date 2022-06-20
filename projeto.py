from conexao import Conexao
from cores import Cores
from sqlite3 import Error

# PROJETO 
# IDP, SIGLAP, DESCRICAOP, NOMEGERENTEP, PROJETO_IDC
# {idp}, {siglap}, {descricaop}, {nomegerentep}, {projeto_idc}

# definir classe projeto 
class Projeto:
    # função: ver registros projeto
    def exibirP():
        try:
            conecta = Conexao()
            conecta.connect()   
            conecta.execute("SELECT * FROM PROJETO;")   
            rows = conecta.fetchall()
            # atributos: IDP, SIGLAP, DESCRICAOP, NOMEGERENTEP, PROJETO_IDC
            print("{:<10} {:<10} {:<50} {:<20} {:<10}".format("ID", "SIGLA", "DESCRIÇÃO", "GERENTE", "ID GERENTE"))
            for item in range(len(rows)):
                print("{:<10} {:<10} {:<50} {:<20} {:<10}".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3], rows[item][4]))
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nExibindo informações cadastradas em Projetos.{Cores.ENDC}")
            input(f"{Cores.BOLD}Aperte <ENTER> para continuar.{Cores.ENDC}")
        conecta.disconnect()
        
        # --------------------------------------------------------------------------- #
    
    # função: pesquisar em projeto
    def pesquisarP(idp="", siglap="", descricaop="", nomegerentep="", projeto_idc=""):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("SELECT * FROM PROJETO WHERE IDP=? or SIGLAP=? or DESCRICAOP=? or NOMEGERENTEP=? or PROJETO_IDC=?;", (idp, siglap, descricaop, nomegerentep, projeto_idc))
            rows = conecta.fetchall()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nPesquisa realizada com sucesso em Projetos.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
        
                # --------------------------------------------------------------------------- #
        
    # função: inserir em projeto    
    def inserirP(siglap, descricaop, nomegerentep, projeto_idc):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("INSERT INTO PROJETO (SIGLAP, DESCRICAOP, NOMEGERENTEP, PROJETO_IDC) VALUES (?,?,?,?)", (siglap, descricaop, nomegerentep, projeto_idc))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nInserção realizada com sucesso em Projetos.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
            
                # --------------------------------------------------------------------------- #
        
    # função: deletar em projeto
    def deletarP(idp):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("DELETE FROM PROJETO WHERE IDP = ?;", (idp))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nRegistro deletado com sucesso.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
            
                # --------------------------------------------------------------------------- #
                
    # função: atualizar em projeto
    def atualizarP(siglap, descricaop, nomegerentep, projeto_idc, idp):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("UPDATE PROJETO SET SIGLAP=?, DESCRICAOP=?, NOMEGERENTEP=?, PROJETO_IDC=? WHERE IDP=?;", (siglap, descricaop, nomegerentep, projeto_idc, idp))
            rows = conecta.fetchall()       
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nDados atualizados com sucesso.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()