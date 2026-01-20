import pandas as pd

# Carregar o arquivo de logs
log_file ='access.log'

# Definir os nomes das colunas conforme o formato do log
log_columns = ['ip','identd','user','date','method','status_code','response_size']

# Ler o arquivo de log
logs = pd.read_csv(log_file, sep=' ', names=log_columns, header=None, engine='python')

