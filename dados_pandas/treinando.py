import pandas as pd


vendas = {'Data': ['15/07/2022', '16/07/2022', '18/07/2022', '19/07/2022', '20/07/2022', '21/07/2022', '22/07/2022'],
'Produtos': ['frango', 'feijão', 'ovo', 'arroz', 'macarrão', 'café', 'cuscuz'],
'Valor': [18, 8, 15, 4, 2, 7, 1.70],
'Quantidade': [70, 50, 25, 40, 60, 75, 80]}

vendas_df = pd.DataFrame(vendas)

#Visualização do DataFrame:
print(vendas_df)
print(vendas_df.head())
print(vendas_df.shape)
print(vendas_df.describe())

#Edição do DataFrame:
produtos = vendas_df['Produtos']  
print(produtos)                   #Visualiza só a coluna/serie do pandas 'Produtos'.

produtos_valor = vendas_df[['Produtos', 'Valor']] 
print(produtos_valor)             #Visualiza as colunas 'produtos' e 'valor'.

#MÉTODO LOC.
print(vendas_df.loc[1])           #Pega uma linha/serie do DataFrame de acordo com o índice.
print(vendas_df.loc[1:4])         #Pega duas linhas do DataFrame de acordo com o índice(do índice 1 ao 4).

#Pegar linhas que corresponde a uma condição.
print(vendas_df.loc[vendas_df['Produtos'] == 'arroz'])  #Pega todas as linhas onde o valor  
                                                        #esteja em 'Produtos' e se chame 'arroz'

print(vendas_df.loc[vendas_df['Valor'] == 200])  #Pega todas as linhas onde o valor  
                                                 #esteja em 'Valor' e seja 200.
                                                
#Pegar várias linhas e colunas usando o loc.
#Sequência do loc sempre é:LINHAS, COLUNAS, então...:
print(vendas_df.loc[vendas_df['Produtos'] == 'arroz', ['Data', 'Produtos', 'Valor']]) #Pega todas as linhas onde o valor  
                                                                            #esteja em 'Produtos' e se chame 'arroz'
                                                                            #mostrando apenas as colunas 'Data',
                                                                            #'Produtos' e 'Valor'.

print(vendas_df.loc[1, 'Produtos'])     #Pega um valor específico


#ADICIONAR UMA NOVA COLUNA NO DATAFRAME:
#A partir de uma coluna que já existe:
vendas_df['Valor final'] = vendas_df['Valor'] * vendas_df['Quantidade']
print(vendas_df)

#Criar uma coluna com valor padrão:
vendas_df.loc[:, 'Imposto'] = 0  #Cria uma coluna 'Imposto' pq ela não existe no Dataframe,
                                 #adicionando o valor 0 em todas as linhas(através do ':' na parte de linhas)
print(vendas_df)

#ADICIONANDO NOVAS LINHAS NO DATAFRAME:

#criando novo DataFrame:
vendas_jul = {'Data': ['15/07/2022', '16/07/2022', '18/07/2022', '19/07/2022', '20/07/2022', '21/07/2022', '22/07/2022'],
'Produtos': ['frango', 'feijão', 'ovo', 'arroz', 'macarrão', 'café', 'cuscuz'],
'Valor': [18, 8, 15, 4, 2, 7, 1.70],
'Quantidade': [50, 40, 30, 55, 60, 55, 90]}
vendas_jul_df = pd.DataFrame(vendas_jul)
vendas_jul_df['Valor final'] = vendas_df['Valor'] * vendas_df['Quantidade']
vendas_jul_df.loc[:, 'Imposto'] = 0
print(vendas_jul_df)

#Adicionando DataFrame 'vendas_jul_df' no DataFrame 'vendas_df':
vendas_df = vendas_df.append(vendas_jul_df)
print(vendas_df)

#EXCLUIR LINHAS E COLUNAS                            #eixo(axis) = 0 é para linha
                                                     #eixo(axis) = 1 é para coluna

vendas_df = vendas_df.drop("Imposto", axis=1)       #Excluindo a coluna 'Imposto'
                                                     

vendas_df = vendas_df.drop(0, axis=0)               #Excluindo a linha com índice 0

print(vendas_df)

#TRATANDO VALORES VAZIOS

