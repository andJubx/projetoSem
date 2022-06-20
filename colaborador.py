from conexao import Conexao
from cores import Cores
from sqlite3 import Error

# COLABORADOR
# IDC, NOMEC, IDADEC, COLAB_IDTU
# {icd}, {nomec}, {idadec}, {colab_idtu}

# definir classe colaborador 
class Colaborador:
    # função: exibir registros em colaborador 
    def exibirC():
        try:
            conecta = Conexao()
            conecta.connect()   
            conecta.execute("SELECT * FROM COLABORADOR;")   
            rows = conecta.fetchall()
            print("{:<5} {:<20} {:<2} {:<5}".format("ID", "NOME", "IDADE", "CARGO"))
            for item in range(len(rows)):
                print("{:<5} {:<20} {:<2} {:<5}".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3]))
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nExibindo informações cadastradas em Colaborador.{Cores.ENDC}")
            input(f"{Cores.BOLD}Aperte <ENTER> para continuar.{Cores.ENDC}")
        #return rows
        conecta.disconnect()
        
        # --------------------------------------------------------------------------- #
        
        # função: pesquisar em colaborador
    def pesquisarC(idc="", nomec="", idadec="", colab_idtu=""):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("SELECT * FROM COLABORADOR WHERE IDC=? or NOMEC=? or IDADEC=? or COLAB_IDTU=?;", (idc, nomec, idadec, colab_idtu))
            rows = conecta.fetchall()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nPesquisa realizada com sucesso em Colaborador.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
        
        # --------------------------------------------------------------------------- #

    # função: inserir em colaborador
    def inserirC(nomec, idadec, colab_idtu):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("INSERT INTO COLABORADOR (NOMEC, IDADEC, COLAB_IDTU) VALUES (?,?,?)", (nomec, idadec, colab_idtu))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nInserção realizada com sucesso em Colaborador.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
            
        # --------------------------------------------------------------------------- #
        
    # função: deletar em colaborador
    def deletarC(idc):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("DELETE FROM COLABORADOR WHERE IDC = ?;", (idc))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nRegistro deletado com sucesso.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
            
        # --------------------------------------------------------------------------- #
        
    # função: atualizar em colaborador
    def atualizarC(nomec, idadec, colab_idtu, idc):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("UPDATE COLABORADOR SET NOMEC=?, IDADEC=?, COLAB_IDTU=? WHERE IDC=?;", (nomec, idadec, colab_idtu, idc))
            rows = conecta.fetchall()       
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nDados atualizados com sucesso.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
        
        # --------------------------------------------------------------------------- #