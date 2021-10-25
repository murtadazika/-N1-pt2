# INTEGRANTES DO GRUPO E RA'S:

#GUILHERME DOS SANTOS XAVIER RA: 21593383
#JONATHAN ALMEIDA DE SIQUEIRA FARIAS RA: 21516599
#MATHEUS FERREIRA RA: 21531006
#MURTADA MOBARAK MOHAMED KHAIR RA: 21623280 

# LISTAS E DICIONÁRIOS:
		
usuariosCadastrados = []
usuario = {}

nomes = []
emails = []

# FUNÇÕES UTILIZADAS NO PROGRAMA:

def adicionar_remover_usuario():

	resposta = int(input("\n       [1] Cadastrar um novo usuário\t            [3] Menu de opções\n\n       [2] Remover usuário cadastrado\n\n\n           Opção selecionada: "))
	print("\n     ________________________________________________________________________________")

	if resposta == 1:	
		usuario ["\n         __________________________________________\n\n           Nome completo"] = str(input("\n           Informe o nome completo:\n\n           "))
		print("\n           __________________________________________________________________________")
		usuario ["\n           Endereço de e-mail"] = str(input("\n           Insira o endereço de e-mail\n\n           "))
		usuariosCadastrados.append(usuario.copy())
		nomes.append(usuario ["\n         __________________________________________\n\n           Nome completo"])
		emails.append(usuario ["\n           Endereço de e-mail"])
		print("\n     ________________________________________________________________________________\n\n\t\t\t        USUÁRIO CADASTRADO COM SUCESSO\n     ________________________________________________________________________________\n\n")
		a = input()

	elif resposta == 2:
		print("\n     ________________________________________________________________________________\n\n\t\t     SERVIÇO INDISPONÍVEL, TENTE NOVAMENTE MAIS TARDE\n     ________________________________________________________________________________\n\n")
		a = input()
		resposta == 3

	else:
		resposta == 3

def consultar():
	resposta = int(input("\n       [1] Consultar por ordem de cadastro\t [3] Menu de opções\n\n       [2] Consultar por ordem alfabética\t [4] Verificar cadastro (por e-mail)\n\n\n           Opção selecionada: "))
	print("\n     ________________________________________________________________________________")

	if resposta == 1:
		print("\n     ________________________________________________________________________________\n\n         POR ORDEM DE CADASTRO:")
		for e in usuariosCadastrados:
			for k, v in e.items():
				print(f"{k}: \n\n            {v}")
				a = input()

	elif resposta == 2:
		alternativa = int(input("\n        Deseja consultar por:\n\n        [1] Nome completo\t [2] Endereço de e-mail\n\n\n           Opção selecionada: "))
		print("\n     ________________________________________________________________________________")
		
		if alternativa == 1:
			print("\n         NOMES COMPLETOS (A-Z):\n")
			for v in sorted(nomes):
				print(f"\n          {v}\n         ___________________________________________________________________________")
			a = input()		
		
		elif alternativa == 2:
			print("\n         ENDEREÇOS DE E-MAIL (A-Z):\n")
			for v in sorted(emails):
				print(f"\n          {v}\n         ___________________________________________________________________________")
			a = input()

	elif resposta == 4:
		verificado = str(input("\n\t   Informe o endereço de e-mail do usuário a ser verificado:\n\n\t   "))
		print("\n     ________________________________________________________________________________")
		if verificado in emails:
			print("\n\t\t\t        USUÁRIO CADASTRADO\n     ________________________________________________________________________________\n\n")
			a = input()
		else:
			print("\n\t\t\t       USUÁRIO NÃO CADASTRADO\n     ________________________________________________________________________________\n\n")
			a = input()

# PROGRAMA PRINCIPAL:

if (__name__ == "__main__"):

	resposta = 3

	print("\n"*15)
	while (resposta == 3):

		print("\n"*3)
		respostaUsuario = int(input("\n     ________________________________________________________________________________\n\n                                 GERENCIADOR DE INSCRIÇÕES\n     ________________________________________________________________________________\n\n       [1] Consultar os usuários cadastrados\t    [3] Adicionar/remover usuário\n\n       [2] Alterar os dados do usuário\t            [4] Finalizar o programa\n\n\n           Opção selecionada: "))
		print("\n     ________________________________________________________________________________")
		
		if respostaUsuario == 4:
			resposta = int(input("\n\n           Deseja confirmar a ação?\n\n       [2] Confirmar\t [3] Cancelar \n\n\n           Opção selecionada: "))
			print("\n     ________________________________________________________________________________","\n"*15)
			if resposta == 3:
				print()
			else:
				print("\n     ________________________________________________________________________________\n\n\t\t\t        PROGRAMA FINALIZADO\n     ________________________________________________________________________________\n\n\n\n")
				break
		
		elif respostaUsuario == 3:
			adicionar_remover_usuario()

		elif respostaUsuario == 2:
			print("\n\t\t     SERVIÇO INDISPONÍVEL, TENTE NOVAMENTE MAIS TARDE\n     ________________________________________________________________________________\n\n")
			a = input()

		elif respostaUsuario == 1:
			consultar()

		else:
			resposta == 3
