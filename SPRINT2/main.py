from numpy import array
from contexto_bancario import TransferenciaPIX, Instituicao
import random
# from generator import Generator
# from transferencia_pix_service import MakeCSV
from conexao_mysql import ConexaoMySQL


conexao = ConexaoMySQL("localhost", "root", "urubu100", "database_data_script")

random.seed(777)

transacoes = []

lista_tipos_pessoa = Instituicao.get_tipos_pessoa()
lista_ispbs = Instituicao.get_ispbs()
lista_tipos_chave_pix = Instituicao.get_tipos_chaves_pix()
lista_siglas=Instituicao.get_siglas_estados()
descricao=Instituicao.verdadeiro()

for i in range(200_000):
    valor = round(random.uniform(100_000,9_999_999),2)
    tipo_pessoa_debitante = random.choice(lista_tipos_pessoa)
    instituicao_debitante = random.choice(lista_ispbs)
    tipo_chave_pix = random.choice(lista_tipos_chave_pix)
    siglas= random.choice(lista_siglas)
    informacao_entre_usuarios = random.choice(descricao)
    instituicao_creditante = random.choice(lista_ispbs)
    agendado = random.choice([True, False, False, False, False, False])

    transacoes.append(TransferenciaPIX(valor, tipo_pessoa_debitante, instituicao_debitante, tipo_chave_pix, siglas,informacao_entre_usuarios, instituicao_creditante, agendado).get_transferencia())
    conexao.insercao(transacoes[i],'transacoes_pix')




for i in range(800_000):
    valor = round(random.uniform(10,50_000),2)
    tipo_pessoa_debitante = random.choice(lista_tipos_pessoa)
    instituicao_debitante = random.choice(lista_ispbs)
    tipo_chave_pix = random.choice(lista_tipos_chave_pix)
    siglas = random.choice(lista_siglas)
    informacao_entre_usuarios = random.choice(descricao)
    instituicao_creditante = random.choice(lista_ispbs)
    agendado = random.choice([True, False, False, False, False, False])
    transacoes.append(TransferenciaPIX(valor, tipo_pessoa_debitante, instituicao_debitante, tipo_chave_pix, siglas, informacao_entre_usuarios, instituicao_creditante, agendado).get_transferencia())
    conexao.insercao(transacoes[i],'transacoes_pix')

#print(transacoes)
# make_csv = MakeCSV(transacoes)
# make_csv.write()