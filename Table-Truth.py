# ***** Feito por Elioenai Siqueira Costa *****
# ***** Email: elscost@gmail.com *****


from string import ascii_uppercase as alf

l = []

def cont(b,a):
	clock = 1 # Contador iniciado em 1
	for element in a:
		c = b.find(element) #Retorna a posicao de elementos que existem nos 2 conjuntos
		if(b[c] == element): #Se esses elementos forem iguais inicia o contador e retorna a quantidade de elementos iguais
			clock += 1
	return clock - 1


def t(*args,c): #Retorna em forma de lista a expressão necessária para gerar a Tabela, por exemplo = (A = int(Binário[posição]))
	clock = -1
	for elem in args:
			if(clock != c - 1):
				clock += 1
				l.append(elem + " = " + "int(Binário["+str(clock)+"])")
			else:
				l.append(elem+" = None") #Se o clock for menor do que a quantidade de elementos retorna a quantidade de elementos restantes iguais a None por exemplo (cont("A",c=2)) : (A = int(Binário[0]),B = None)
	return (l)

print("\n"+"USE X >> Y PARA (X * Ῡ)")
print("USE X ^ Y PARA PORTA XOR")
print("USE X | Y PARA PORTA OR OU X + Y")
print("USE X & Y PARA PORTA AND OU X * Y")
print("USE 1 >> X PARA PORTA NOT"+"\n")

Equacao = input("Digite a equacao booleana: ").upper()
Quantidade = cont(Equacao,alf) #A quantidade é equivalente a quantidade de elementos iguais entre o conjunto do alfabeto e a Equação
def point(*args):
	 Resultado = eval(Equacao)
	 if(Resultado >= 1):
	 	return 1
	 else:
	 	return 0
print("\n")

for w in list(alf):
	print(alf[0:Quantidade]+" S"+"\n")
	break

Função = t('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',c=Quantidade)

for x in range(2**Quantidade):
	y = bin(x)[2:] #Converte os valores de X para Binário
	Binário = y.zfill(Quantidade) #Preenche com zeros a esquerda os espaços sobrando
	for z in range(0,len(l)):
		d = exec(l[z]) #Executa a expressão contida dentro da lista "l"
	print(Binário,point(Função))
print("\n"+'Quantidade = %s'%(2**Quantidade))
