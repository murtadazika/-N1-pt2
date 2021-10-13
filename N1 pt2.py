
usuarios_cadastrados = list()
usuario = dict()


def adicionar_usuario():
	print("\n__________________________________________")
	usuario["_________________________________\n\nNome completo"] =   str(input("\n Informe o nome completo do usuário:\n\n "))
	print("\n       --------------------------")
	usuario["Endereço de e-mail"] = str(input("\n Insira o endereço de e-mail do usuário:\n\n "))
	usuarios_cadastrados.append(usuario.copy())
	a = input("\n__________________________________________\n\n     Usuário Cadastrado com sucesso! \n__________________________________________\n\n\n\n")


def consultar_cadastros():
	for e in usuarios_cadastrados:
			for k, v in e.items():
				print(f"\n{k}: \n {v}")

def consulta_alfabetica():
	consulta_alfabetica.sort(usuarios_cadastrados)


	
							
def tente_novamente():
	a = input("\n__________________________________________\n\n [ ! ]         Tente novamente  ")
	print("\n__________________________________________","\n"*20)

#============================================	
												
resposta = "2"

while resposta == "2":
	resposta_usuario = str(input("\n__________________________________________\n\n        GERENCIADOR DE INSCRIÇÕES\n__________________________________________\n\n [1] Consultar usuários cadastrados\n\n [2] Adicionar/remover o usuário\n\n [3] Alterar dados cadastrais do usuário\n\n [4] Encerrar o sistema\n\n\n     Opção: "))
	print("\n__________________________________________")
	if (resposta_usuario == "1"):
		alternativa = str(input("\n [1] Consultar por ordem de cadastro\n\n [2] Consultar por ordem alfabética\n\n [3] Menu de opções\n\n     Opção: "))
		if (alternativa == "1"):
			print("\n_________________________________________\n\n Usuários cadastrados no sistema:")
			consultar_cadastros()
			a = input(("\n__________________________________________\n\n\n"))
		elif (alternativa == "2"):
			print("lista em ordem alfabetica",consulta_alfabetica)#Função para consultar cadastros por ordem alfabética (consulta_alfabetica)
		elif(alternativa == "3"):
			print()
		else:
			print()
	
	elif (resposta_usuario == "2"):
		alternativa = str(input("\n [1] Cadastrar novo usuário\n\n [2] Remover usuário (por e-mail)\n\n [3] Menu de Opções\n\n     Opção: "))
		if (alternativa == "1"):
			adicionar_usuario()
		elif (alternativa == "2"):
			print() #Função para remover usuário (remover_usuario())
		elif(alternativa == "3"):
			print()
		else:
			tente_novamente()
			
	elif (resposta_usuario == "3"):
		print() #Função para alterar dados cadastrais (alterar_dados())
		
	elif (resposta_usuario == "4"):
		resposta = str(input("\n     Deseja confirmar a ação?\n\n     [1] Confirmar\t [2] Cancelar\n\n\n     Opção: "))
		if resposta != "2":
			print("\n__________________________________________\n\n [ ! ]        Sistema finalizado\n__________________________________________")
			break

	else:
		tente_novamente()