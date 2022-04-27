import datetime
from itertools import tee
from lib2to3.pgen2.pgen import generate_grammar
import random
#from readline import get_endidx
import uuid
import phonenumbers
from phone_gen import PhoneNumber
from datetime import date, timedelta

random.seed(777)

class Generator:

    def generate_cpf():
        cpf = [random.randint(0, 9) for x in range(9)]                              
                                                                                
        for _ in range(2):                                                          
            val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
                                                                                    
            cpf.append(11 - val if val > 1 else 0)                                  
                                                                                
        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

    def generate_cnpj():
        def calculate_special_digit(l):                                             
            digit = 0                                                               
                                                                                    
            for i, v in enumerate(l):                                               
                digit += v * (i % 8 + 2)                                            
                                                                                    
            digit = 11 - digit % 11                                                 
                                                                                    
            return digit if digit < 10 else 0                                       
                                                                                    
        cnpj =  [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]             
                                                                                    
        for _ in range(2):                                                          
            cnpj = [calculate_special_digit(cnpj)] + cnpj                           
                                                                                    
        return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])

    def generate_uuid():
        return str(uuid.uuid4())

    def generate_phone_number():

        phone_number = PhoneNumber("Brazil")
        
        telefone_formulario = phone_number.get_national()

        while len(telefone_formulario) <= 13:
            telefone_formulario = phone_number.get_mobile()

        telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")

        return phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.NATIONAL)

    def generate_hora():
        hora = random.randint(00,23)
        minuto = str(random.randint(00,59))
        return [hora, str(str(hora) + ":" + minuto)]

    def generate_date(agendado = None):

        array_datas = [2019, 2019, 2020, 2020, 2020, 2021, 2021,2021,2021,2021,2021,2021, 2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022]

        date_now = date.today()
        month_date = date_now.strftime("%m")
        day_date = date_now.strftime("%d")

        data_gerada = date(random.choice(array_datas), int(month_date), int(day_date))

        if agendado == True:
            data_gerada = data_gerada + timedelta(days=2)
        
        return str(data_gerada)
        
        

# Generator.generate_date()
