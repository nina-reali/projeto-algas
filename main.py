from mysqlConnector import Connector
from script import Data

connection = Connector("127.0.0.1", "root", "urubu100", "database_data_script")
data = Data

array_block = list(([], [], [], [], []))
array_sum_time_memory = list(([], [], [], [], []))
array_tables = ['bloco_1', 'bloco_2', 'bloco_3', 'bloco_4', 'bloco_5']
array_input = [[], [], [], [], []]

def user_input():
    loop = True
    for item in range(5):
        chosen_block = int(input("Choose your block of transaction: \n"))

        start = int(input(f"Block {chosen_block}: \n Enter the start number:"))
        array_input[chosen_block-1].append(start)

        end = int(input(f"Block {chosen_block}: \n Enter the end number:"))
        array_input[chosen_block-1].append(end)

        gap = int(input(f"Block {chosen_block}: \n Enter the gap number:"))
        array_input[chosen_block-1].append(gap)

    print(array_input)
user_input()

#dados de entrada - transações
for item in range(len(array_input)):
    for value in range(array_input[item][0], array_input[item][1], array_input[item][2]):
        array_block[item].append(value)


#calculo de tempo e memoria
count = 0
for input_values in array_input:
    outcome_sum_time_memory = data.sum_time_memory(input_values)
    array_sum_time_memory[count].append(outcome_sum_time_memory)
    count += 1

#insere os dados em blocos
count = 0
for item in array_sum_time_memory:
    for index in item:
        for unit in index:
            connection.insert(unit[0], array_tables[count])
    count += 1

