from conexao import Conexao
from cores import Cores
from sqlite3 import Error

# TIPOUSUARIO
# IDTIPOUSUARIO, DESCRICAOTU, SIGLATU
# {idtu}, {descricaotu}, {siglatu}

# definir classe tipo usuário 
class TipoUsuario:
    # função: ver registros tipo usuário 
    def exibirTU():
        try:
            conecta = Conexao()
            conecta.connect()   
            conecta.execute("SELECT * FROM TIPOUSUARIO;")   
            rows = conecta.fetchall()
            #atributos: IDTIPOUSUARIO, DESCRICAOTU, SIGLAU
            print("{:<10} {:<20} {:<10}".format("ID", "DESCRIÇÃO", "SIGLA"))
            for item in range(len(rows)):
                print("{:<10} {:<20} {:<10}".format(rows[item][0], rows[item][1], rows[item][2]))
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nExibindo informações cadastradas em Usuários.{Cores.ENDC}")
            input(f"{Cores.BOLD}Aperte <ENTER> para continuar.{Cores.ENDC}")
        conecta.disconnect()
        
        # --------------------------------------------------------------------------- #
    
    # função: pesquisar em tipo usuário
    def pesquisarTU(idtu="", descricaotu="", siglatu=""):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("SELECT * FROM TIPOUSUARIO WHERE IDTU=? or DESCRICAOTU=? or SIGLATU=?;", (idtu, descricaotu, siglatu))
            rows = conecta.fetchall()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nPesquisa realizada com sucesso em Usuários.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
        
        # --------------------------------------------------------------------------- #
     
    # função: inserir em tipo usuário    
    def inserirTU(descricaotu, siglatu):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("INSERT INTO TIPOUSUARIO (DESCRICAOTU, SIGLATU) VALUES (?,?)", (descricaotu, siglatu))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nInserção realizada com sucesso em Usuários.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
            
        # --------------------------------------------------------------------------- #

    # função: deletar em tipo de usuário
    def deletarTU(idtu):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("DELETE FROM TIPOUSUARIO WHERE IDTU = ?;", (idtu))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nRegistro deletado com sucesso.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
            
        # --------------------------------------------------------------------------- #
    
    # função: atualizar em tipo usuário
    def atualizarTU(descricaotu, siglatu, idtu):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("UPDATE TIPOUSUARIO SET DESCRICAOTU=?, SIGLATU=? WHERE IDTU=?;", (descricaotu, siglatu, idtu))
            rows = conecta.fetchall()       
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nDados atualizados com sucesso.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
        
        # --------------------------------------------------------------------------- #