class Calculadora:
	def __init__(self, batMax):
		self.bateria = 0
		self.bateriamax = batMax

	def __str__(self):
		return "Bateria Restante: " + str(self.bateria) + "/" + str(self.bateriaMax)

	def carregarBateria(self, carga):
		self.bateria += carga
		if (self.bateria > self.bateriaMax):
			self.bateria = self.bateriaMax
  
	def somar(self, n1, n2):
		print (n1 + n2)
		self.bateria -= 1

	def dividir(self, n1, n2):
		if (n2 == 0):
			print ("Erro: Numero nao pode ser dividido por 0")
		else:	
			print (n1 / n2)
		self.bateria -= 1

calculadora = Calculadora()
operacao = " "
print ("Digite: iniciar _cargaMax, bateria, carregar _valor, somar _a _b, dividir _a _b ou finalizar")
while (operacao != "finalizar"):
	operacao = input()

	if (operacao == "finalizar"):
		break
	elif (operação == "iniciar"):
		calculadora = Calculadora int(input("Digite 
	elif (operacao == "bateria"):
		print (calculadora)
	elif (operacao == "carregar"):
		carga = int(input("Digite o quanto deseja carregar: "))
		calculadora.carregarBateria(carga)
	elif (operacao == "somar"):
		n1 = int(input("Digite o primeiro numero: "))
		n2 = int(input("Digite o segundo numero: "))
		if (calculadora.bateria == 0):
			print ("Sem bateria")
		else:
			calculadora.somar(n1, n2)
	elif (operacao == "dividir"):
		n1 = int(input("Digite o dividendo: "))
		n2 = int(input("Digite o divisor: "))
		if (calculadora.bateria == 0):
			print ("Sem bateria")
		else:
			calculadora.dividir(n1, n2)
	else:
		print ("Comando invalido")
