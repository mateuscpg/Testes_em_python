from time import sleep
import pandas as pd

i = 0
while i != 2:
    while True:
        try:
            print('''=== Selecione uma opção ===
            [1] Adicionar data, descrição e valor.
            [2] Sair do programa e ver a tabela.
            ''')
            opc = int(input("Escolha sua opção: "))
            sleep(0.7)
            break
        except:
            print("Opção inválida")
    
    
    if opc == 1:
            print("=== Insira os dados ====\n")
            while True:
                try:
                    data = str(input("Digite a data da compra: "))
                    break
                except:
                    print("Opção inválida")
            while True:
                try:
                    desc = str(input("Descrição da compra: "))
                    break
                except:
                    print("Opção inválida")
            while True:
                try:
                    valor = str(input("Valor da compra: "))
                    break
                except:
                    print("Opção inválida")
            
            fatura = {'Data': [data],
            'Descrição': [desc],
            'Valor': [valor]}   
        

    elif opc == 2:
        print("Fim do programa!")
        print("=== FATURA DO MÊS ===")
        i = 2
        
fatura_df = pd.DataFrame(fatura)
print(fatura_df)
sleep(0.7)

while True:
    try:
        desc = str(input("Deseja ver a descrição da tabela?[s/n]").upper().strip())
        break
    except:
        print("Opção inválida!")

if desc == 'S':
    print(fatura_df.describe())

    