larg = float(input("Qual a largura da sua parede?"))
altu = float(input("Qual a altura da sua parede?"))
area = larg * altu 
print ("Sua parede tem dimensão de {}x{} e sua área é de {:.2f}m²".format(larg, altu, area))
tinta = area / 2 
print ("Para pintar essa parede, você precisará de {:.2f} litros de tinta".format(tinta))
