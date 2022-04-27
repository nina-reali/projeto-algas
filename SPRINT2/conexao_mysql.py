import mysql.connector

class ConexaoMySQL:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conexao(self):
        print("\nEstabelecendo conexão com o Banco de Dados...")
        try:
            mydb = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print("Conexão feita com sucesso!\n")
            return mydb
        except Exception as e:
            print(e)
            self.fechar_codigo("Erro na conexão com o Banco de Dados...")

    def insercao(self, valores, tabela):
        mydb = ConexaoMySQL.conexao(self)
        insert = mydb.cursor()
        query = "INSERT INTO {} (chave,tipoChave,instituicaoDebitante,nomeInstituicaoDebitante,tipoPessoaDebitante,instituicaoCreditante,nomeInstituicaoCreditante,tipoPessoaCreditante,valor,tipoIniciacao,siglaEstado,nomeEstado,comentario,hora,dia,mes,dataTransacao,agendado) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(tabela)

        if not valores:
            self.fechar_codigo("Dados vazios...")

        try:
            valor_inserir = (valores['chave'], valores['tipo_chave'], valores['instituicao_debitante'],valores['nome_instituicao_debitante'], valores['tipo_pessoa_debitante'], valores['instituicao_creditante'], valores['nome_instituicao_creditante'], valores['tipo_pessoa_creditante'], valores['valor'], valores['tipo_iniciacao'], valores['sigla_estado'], valores['nome_estado'], valores['comentario'], valores['hora'], valores['dia'],valores['mes'],valores['data_transacao'],valores['agendado'])
            insert.execute(query, valor_inserir)
            mydb.commit()
            print("\nDados inseridos com sucesso!\n")
        except Exception as e:
            print(e)
            self.fechar_codigo("Erro na inserção com o Banco de Dados...")

    def fechar_codigo(self, mensagem):
        print(mensagem)
        from sys import exit
        exit(0)