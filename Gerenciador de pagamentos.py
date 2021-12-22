print ('{:=^40}'.format("LOJA CORREIA"))
preço = float(input("Preço das compras: R$"))
print ('''FORMAS DE PAGAMENTO:
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input("Qual a opção?"))

if opção == 1:
    desconto = preço - (preço * 10 / 100)
    print ("O valor da compra de R${} ficou R${} com o desconto".format(preço, desconto))

elif opção == 2:
    desconto = preço - (preço * 5 / 100)
    print ("O valor da compra de R${} ficou R${} com o desconto".format(preço, desconto))

elif opção == 3:
    print ("O valor da sua compra é de R${}".format(preço))

elif opção == 4:
    juros = preço + (preço * 20 / 100)
    totalpar = int(input("Quantas parcelas serão?"))
    parcela = juros / totalpar 
    print ("Sua compra será parcelada em {}x e a parcela ficou R${:.2f} com os juros".format(totalpar, parcela))

else: 
    total = 0
    print("ERRO, TENTE DE NOVO!")