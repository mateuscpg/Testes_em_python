import pandas as pd 
import texttable 
vendas = {'data': ['15/06/2022', '16/06/2022'],
'valor': [500, 600],
'produtos': ['carne', 'feijão'],
'quantidade': [70, 50]}

vendas_df = pd.DataFrame(vendas)


print(texttable(vendas_df))