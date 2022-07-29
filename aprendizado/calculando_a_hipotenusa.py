import math
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjascente:'))
hi = math.hypot(co,ca)
print ("O valor da hipotenusa será {:.2f}".format(hi))

if co == ca == hi:
    print ("O triângulo será equilátero!")
elif co > ca or co > hi or ca < co or ca < hi or hi < co or hi < ca:
    print ("O triângulo séra isósceles!")
elif co != ca or co != hi or ca != co or ca != hi or hi < co or hi <ca:
    print ("O triângulo será escaleno!")
