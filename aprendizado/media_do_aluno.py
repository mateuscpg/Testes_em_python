not1 = float(input("Digite a primeira nota:"))
not2 = float(input("Digite a segunda nota:"))
not3 = float(input("Digite a terceira nota:"))
media = (not1 + not2 + not3) / 3

if media >= 7:
    print("MÉDIA {:.2f}, APROVADO!".format(media))
elif media >= 5 and media <= 6.9:
    print("MÉDIA {:.2f}, RECUPERAÇÃO!".format(media))
else:
    print("MÉDIA {:.2f}, REPROVADO!".format(media))
