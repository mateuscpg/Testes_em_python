nome='JOGO DAS PERGUNTAS'
print()
print(nome.center(50,'='))
perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a':'1', 'b':'4', 'c':'3', 'd':'5'},
            'resposta_certa': 'B',
    }, 
    'Pergunta 2':{
        'pergunta': 'Quanto é 5*5? ',
        'respostas': {'a':'15', 'b':'10', 'c':'25', 'd':'5'},
            'resposta_certa': 'C',
    },
     'Pergunta 3':{
        'pergunta': 'Quanto é 8*5? ',
        'respostas': {'a':'35', 'b':'50', 'c':'45', 'd':'40'},
            'resposta_certa': 'D'
    }
}
 
print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    usu = str(input("Sua resposta: ")).upper().strip()
    
    if usu == pv['resposta_certa']:
        print("\nPARABÉNS, VOCÊ ACERTOU!!!")
        respostas_certas += 1
    else:
        print("\nPUTS, VOCÊ ERROU!!!")
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas/ qtd_perguntas * 100

print('='*50)
print()
print(f'Você acertou o total de {respostas_certas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto:.2f}%')
if porcentagem_acerto < 70:
    print('Logo, ESTUDE MAIS!!!')
else:
    print('\nPARABÉNS, VOCÊ PASSOU!!')            