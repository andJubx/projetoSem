from conexao import Conexao
from cores import Cores
from sqlite3 import Error

# TAREFA 
# IDT, SIGLAT, DESCRICAOT, DATAINICIOT, DATAPREVISAOFIMT, DATACONCLUSAOT, ACOESREALIZADAST, NOMECOLABORADORT
# {idt}, {siglat}, {descricaot}, {datainiciot}, {dataprevisaofimt}, {dataconclusaot}, {acoesrealizadast}, {nomecolaboradort}, {tarefa_idp}, {tarefa_idc}

# definir classe tarefa 
class Tarefa:
    # função: exibir tarefa 
    def exibirT():
        try:
            conecta = Conexao()
            conecta.connect()   
            conecta.execute("SELECT * FROM TAREFA;")   
            rows = conecta.fetchall()
            #atributos: IDT, SIGLAT, DESCRICAOT, DATAINICIOT, DATAPREVISAOFIMT, DATACONCLUSAOT, ACOESREALIZADAST, NOMECOLABORADORT, TAREFA_IDP, TAREFA_IDC
            print("{:<5} {:<5} {:<20} {:<10} {:<10} {:<10} {:<20} {:<20} {:<5} {:<5}".format("ID", "SIGLA", "DESCRIÇÃO", "INÍCIO", "PREVISÃO", "CONCLUSÃO", "FEITO", "COLABORADOR", "ID PROJETO", "ID COLABORADOR"))
            for item in range(len(rows)):
                print("{:<5} {:<5} {:<20} {:<10} {:<10} {:<10} {:<20} {:<20} {:<5} {:<5}".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3], rows[item][4], rows[item][5], rows[item][6], rows[item][7], rows[item][8], rows[item][9]))
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}Pesquisa realizada com sucesso em Tarefas.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")
        #return rows
        conecta.disconnect()
        
    # --------------------------------------------------------------------------- #
        
    # função: pesquisar em tarefa
    def pesquisarT(filtro, id):
        try:
            conecta = Conexao()
            conecta.connect()
            if filtro == 1: 
                pass
            elif filtro == 2:
                conecta.execute(f"SELECT * FROM TAREFA WHERE TAREFA_IDC={id};")
            elif filtro == 3:
                conecta.execute(f"SELECT * FROM TAREFA WHERE TAREFA_IDP={id};")
            else:
                print("Operação inválida. Tente novamente.")
                       
            rows = conecta.fetchall()
            print("{:<5} {:<5} {:<20} {:<10} {:<10} {:<10} {:<20} {:<20} {:<5} {:<5}".format("ID", "SIGLA", "DESCRIÇÃO", "INÍCIO", "PREVISÃO", "CONCLUSÃO", "FEITO", "COLABORADOR", "ID PROJETO", "ID COLABORADOR"))
            for item in range(len(rows)):
                print("{:<5} {:<5} {:<20} {:<10} {:<10} {:<10} {:<20} {:<20} {:<5} {:<5}".format(rows[item][0], rows[item][1], rows[item][2], rows[item][3], rows[item][4], rows[item][5], rows[item][6], rows[item][7], rows[item][8], rows[item][9]))
        
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nPesquisa realizada com sucesso em Tarefas.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
        
    # --------------------------------------------------------------------------- #
        
    # função: inserir em tarefa    
    def inserirT(siglat, descricaot, datainiciot, dataprevisaofimt, dataconclusaot, acoesrealizadast, nomecolaboradort, tarefa_idp, tarefa_idc):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("INSERT INTO TAREFA (SIGLAT, DESCRICAOT, DATAINICIOT, DATAPREVISAOFIMT, DATACONCLUSAOT, ACOESREALIZADAST, NOMECOLABORADORT, TAREFA_IDP, TAREFA_IDC) VALUES (?,?,?,?,?,?,?,?,?)", (siglat, descricaot, datainiciot, dataprevisaofimt, dataconclusaot, acoesrealizadast, nomecolaboradort, tarefa_idp, tarefa_idc))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nInserção realizada com sucesso em Tarefas.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
            
    # --------------------------------------------------------------------------- #
        
    # função: deletar em tarefa
    def deletarT(idt):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("DELETE FROM TAREFA WHERE IDT = ?;", (idt))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nRegistro deletado com sucesso.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
            
        # --------------------------------------------------------------------------- #
    
    # função: atualizar em tarefa
    def atualizarT(siglat, descricaot, datainiciot, dataprevisaofimt, dataconclusaot, acoesrealizadast, nomecolaboradort, tarefa_idp, tarefa_idc, idt):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("UPDATE TAREFA SET SIGLAT=?, DESCRICAOT=?, DATAINICIOT=?, DATAPREVISAOFIMT=?, DATACONCLUSAOT=?, ACOESREALIZADAST=?, NOMECOLABORADORT=?, TAREFA_IDP=?, TAREFA_IDC=? WHERE IDT=?;", (siglat, descricaot, datainiciot, dataprevisaofimt, dataconclusaot, acoesrealizadast, nomecolaboradort, tarefa_idp, tarefa_idc, idt))
            conecta.fetchall()       
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.OKGREEN}\nDados atualizados com sucesso.{Cores.ENDC}")
            input(f"{Cores.BOLD}Pressione <ENTER> para continuar.{Cores.ENDC}")
        finally:
            conecta.disconnect()
        
        # --------------------------------------------------------------------------- #