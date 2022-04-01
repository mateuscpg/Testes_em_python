expressao = input("Digite a expressão: ")
pilha1 = []
pilha2 = []
pilha3 = []

for caractere in expressao:
  if(caractere == '('):
    pilha1.append('(')
  elif(caractere == ')'):
    if (len(pilha1) > 0):
      pilha1.pop()
    else:
      pilha1.append(')')
      break
  
  if(caractere == '['):
    pilha2.append('[')
  elif(caractere == ']'):
    if (len(pilha2) > 0):
      pilha2.pop()
    else:
      pilha2.append(']')
      break
  
  if(caractere == '{'):
    pilha3.append('{')
  elif(caractere == '}'):
    if (len(pilha3) > 0):
      pilha3.pop()
    else:
      pilha3.append('}')
      break

if(len(pilha1) == 0 and len(pilha2) == 0 and len(pilha3) == 0):
  print("Sua expressão está válida!")
else:
  print("Sua expressão está errada!")