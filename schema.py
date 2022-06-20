#importar classe de conexão
from conexao import Conexao

#criar tabelas do banco
def initDB():
    conecta = Conexao()
    conecta.connect()
    conecta.execute("create table if not exists COLABORADOR (IDC integer primary key autoincrement," 
                    "NOMEC text not null,"
                    "IDADEC integer," 
                    "COLAB_IDTU integer,"
                    "FOREIGN KEY(COLAB_IDTU) references TIPOUSUARIO(IDTU));")
    
    conecta.execute("create table if not exists TIPOUSUARIO (IDTU integer primary key autoincrement,"
                    "DESCRICAOTU text," 
                    "SIGLATU text not null);")
    
    conecta.execute("create table if not exists PROJETO (IDP integer primary key autoincrement," 
                    "SIGLAP text not null,"
                    "DESCRICAOP text,"
                    "NOMEGERENTEP text," 
                    "PROJETO_IDC integer," 
                    "FOREIGN KEY(PROJETO_IDC) references COLABORADOR(IDC));")
    
    conecta.execute("create table if not exists TAREFA (IDT integer primary key autoincrement,"
                    "SIGLAT text,"
                    "DESCRICAOT text," 
                    "DATAINICIOT timestamp," 
                    "DATAPREVISAOFIMT datetime," 
                    "DATACONCLUSAOT datetime," 
                    "ACOESREALIZADAST text," 
                    "NOMECOLABORADORT text," 
                    "TAREFA_IDP integer," 
                    "TAREFA_IDC integer,"
                    "FOREIGN KEY(TAREFA_IDP) references PROJETO(IDP),"
                    "FOREIGN KEY(TAREFA_IDC) references COLABORADOR(IDC));")
    
    conecta.persist()
    conecta.disconnect()