from generator import Generator
import random

random.seed(777)

class TransferenciaPIX:

    def __init__(self, valor = None, tipo_pessoa_debitante = None, instituicao_debitante = None, tipo_chave = None, sigla = None, descricao = None,  instituicao_creditante = None, agendado = None):
        hora = Generator.generate_hora()
        self.transferencia = dict({
            'chave': self.gerar_chave_pix_pelo_tipo(tipo_chave_pix = tipo_chave),
            'tipo_chave': tipo_chave,
            'instituicao_debitante': instituicao_debitante,
            'nome_instituicao_debitante': Instituicao.obter_nome_pelo_ispb(instituicao_debitante),
            'tipo_pessoa_debitante': tipo_pessoa_debitante,
            'instituicao_creditante': instituicao_creditante,
            'nome_instituicao_creditante': Instituicao.obter_nome_pelo_ispb(instituicao_creditante),
            'tipo_pessoa_creditante': self.obter_tipo_pessoa_creditante(tipo_chave = tipo_chave),
            'valor': self.obter_valor_baseado_hora(hora[0], valor),
            'tipo_iniciacao': self.obter_tipo_iniciacao(tipo_chave),
            'sigla_estado': sigla,
            'nome_estado': Instituicao.obter_estado_pela_sigla(sigla),
            'comentario': descricao,
            'hora': hora[1],
            'dia': Instituicao.dias_uteis_pix(),
            'mes': Instituicao.mes_uteis(),
            'data_transacao': Generator.generate_date(agendado = agendado),
            'agendado': agendado
        })

    def __str__(self) -> str:
        return str(self.transferencia)


    def obter_tipo_iniciacao(self, tipo_chave):

        if tipo_chave == "EVP":
            return "QR_CODE"
        
        return random.choice(Instituicao.get_tipos_iniciacao())


    def gerar_chave_pix_pelo_tipo(self, tipo_chave_pix):
        switch = {
            "CPF": Generator.generate_cpf(),
            "CNPJ": Generator.generate_cnpj(),
            "EVP": Generator.generate_uuid(),
            "PHONE": Generator.generate_phone_number()
        }

        return switch.get(tipo_chave_pix, "Tipo chave inexistente.")

    def obter_tipo_pessoa_creditante(self, tipo_chave):

        if tipo_chave == "CPF":
            return "PF"

        if tipo_chave == "CNPJ":
            return "PJ"

        return random.choice(["PJ", "PF"])

    def obter_valor_baseado_hora(self, hora, valor):
        if hora <= 6 or hora >= 23:
            valor = round(random.uniform(1,1000),2)

        return valor

    def get_transferencia(self):
        return self.transferencia

    def get_instituicao(self):
        return self.transferencia['instituicao_debitante']



class Instituicao:

    def get_ispbs():
        return ["18236120", "31872495", "58160789", "90400888", "00416968"]

    def get_tipos_pessoa():
        return ["PJ", "PF"]

    def get_tipos_iniciacao():
        return ["CHAVE", "DEVOLUCAO", "MANUAL"]

    def obter_nome_pelo_ispb(ispb):

        switch = {
            "18236120": "NU PAGAMENTOS S.A.",
            "31872495": "Banco C6 S.A.",
            "58160789": "Banco Safra S.A.",
            "90400888": "BANCO SANTANDER (BRASIL) S.A.",
            "00416968": "Banco Inter S.A."
        }

        return switch.get(ispb, "Instituição não encontrada.")

    def status_envio_transacoes_pix():
        return ["ENVIADA", "EFETIVADA", "RECUSADA", "ERRO", "CANCELADA"]

    def get_tipos_chaves_pix():
        return ["CPF","CNPJ", "EVP", "PHONE"]

    def verdadeiro():
        return  [0,1]
        
    
    def get_siglas_estados():
        return ["AC", "AL" ,"AM" ,"AP" ,"BA","CE" ,"DF"  ,"ES"  ,"GO" ,"MA" ,"MG"  ,"MS"  ,"MT"  ,"PA" ,"PB" ,"PE" ,"PI" ,"PR" ,"RJ"  ,"RN"  ,"RO" ,"RR" ,"RS"  ,"SC"  ,"SE" ,"SP" ,"TO"]

    def dias_uteis_pix():
        array_dias =  [
            "DOMINGO",
            "SEGUNDA",
            "TERÇA-FEIRA",
            "QUARTA-FEIRA",
            "QUINTA-FEIRA",
            "SEXTA-FEIRA",
            "SÁBADO"
        ]

        return random.choice(array_dias)

    def mes_uteis():
        array_meses = [
            "JANEIRO",
            "FEVEREIRO",
            "MARÇO",
            "ABRIL",
            "MAIO",
            "JUNHO",
            "JULHO",
            "AGOSTO",
            "SETEMBRO",
            "OUTUBRO",
            "NOVEMBRO",
            "DEZEMBRO"
        ]

        return random.choice(array_meses)

    def obter_estado_pela_sigla(sigla):
        switch = {
            "AC" : "Acre",
            "AL" : "Alagoas",
            "AM" : "Amazonas",
            "AP" : "Amapá",
            "BA" : "Bahia",
            "CE" : "Ceará",
            "DF" : "Distrito Federal",
            "ES" : "Espirito Santo",
            "GO" : "Goiás",
            "MA" : "Maranhão",
            "MG" : "Minas Gerais",
            "MS" : "Mato Grosso do Sul",
            "MT" : "Mato Grosso",
            "PA" : "Pará",
            "PB" : "Paraíba",
            "PE" : "Pernambuco",
            "PI" : "Piauí",
            "PR" : "Paraná",
            "RJ" : "Rio de Janeiro",
            "RN" : "Rio Grande do Norte",
            "RO" : "Rondônia",
            "RR" : "Roraima",
            "RS" : "Rio Grande do Sul",
            "SC" : "Santa Catarina",
            "SE" : "Sergipe",
            "SP" : "São Paulo",
            "TO" : "Tocantins"
        }

        return switch.get(sigla, "Estado não encontrado")