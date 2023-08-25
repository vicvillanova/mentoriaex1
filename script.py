# Importa a biblioteca Datetime pra poder transformar a data/string em objeto.
from datetime import datetime
# Importa a biblioteca JSON pra poder lidar com o arquivo de signos
import json

# Abre o arquivo e salva o conteudo na variavel signos.
with open("signos.json") as file: 
    signos = json.load(file)

# Pede a data de nascimento pro usuário
data_nascimento = input('Data de Nascimento: ')

# Converte a data de nascimento (string) pra objeto datetime a partir do formato ISO
data_nascimento = datetime.fromisoformat(data_nascimento)

# Percorre cada objeto da lista de signos pra comparar a data de nascimento com as datas dos signos
for signo in signos['signos']:
    # Converte o valor da data de inicio pra objeto datetime, considerando o formato DD/MM
    data_inicio = datetime.strptime(signo['data_inicio'], '%d/%m')
    
    # Quando não é informado o ano, o objeto datetime é criado com o ano 1900, o que faria com que tanto a data inicio,
    # quanto a data fim serem menores que a data de nascimento, entao nunca seria possivel encontrar a data de nascimento
    # dentro do intervalo inicio-fim. Pra contornar isso, eu alterei o ano da data inicio e fim pro mesmo ano da
    # data de nascimento.
    data_inicio = data_inicio.replace(year=data_nascimento.year)

    # Converte o valor da data fim pra objeto datetime, considerando o formato DD/MM
    data_fim = datetime.strptime(signo['data_fim'], '%d/%m')
    # Altero o ano da data_fim pro mesmo ano de nascimento.
    data_fim = data_fim.replace(year=data_nascimento.year)

    if ((data_inicio.month == 12) and (data_nascimento.month == 1) and (data_nascimento.day <= 20)):
        data_inicio = data_inicio.replace(year=(data_nascimento.year - 1))

    if ((data_inicio.month == 12) and (data_nascimento.month == 12) and (data_nascimento.day >= 22)):
        data_fim = data_fim.replace(year=(data_nascimento.year + 1))
     
    # Verifica se a data de nascimento esta entre a data de inicio e a data fim desse signo.
    if data_inicio <= data_nascimento <= data_fim:
        # se for, mostra na tela o nome do signo
        print('Signo:', signo['nome'])
        break 