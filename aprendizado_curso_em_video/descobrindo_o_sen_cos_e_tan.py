import math
ang = float(input("Digite o valor do ângulo:"))
sen = math.sin(math.radians(ang))
print ("O seno de {} é: {:.2f}".format(ang, sen))
cos = math.cos(math.radians(ang))
print ("O cosseno de {} é: {:.2f}".format(ang, cos))
tan = math.tan(math.radians(ang))
print ("A tangente de {} é: {:.2f}".format(ang, tan))
