def Login():
    arq = open('registrados.txt', 'a')
    print('Olá, gostaria de criar uma conta?')
    conf_user = input('Responda S se você quer criar uma conta e N se já possui uma: ')
    if (conf_user == 'S') or (conf_user == 's') or (conf_user == 'sim') or (conf_user == 'Sim'):
      nome_usuario = input('Digite o nome de usuário: ')
      arq.write('{}\n'.format(nome_usuario))
      senha_usuario = input('Digite uma senha: ')
      arq.write('{}\n'.format(senha_usuario))
      print('Cadastro realizado com sucesso!\n')
      print('Agora, efetue o seu login')
    elif (conf_user == 'N') or (conf_user == 'n'):
      print('Efetue o seu login')
    else: 
      print('Você deve ter digitado seu nome de usuario errado, por favor verifique.')
    arq.close()
    arq = open('registrados.txt')
    nome_login = input('Digite o seu nome de usuario: ')
    senha_usuario = input('Digite sua senha: ')
    registrados = arq.readlines()
      if nome_login + '\n' in registrados:
        print('Bem vindo ao seu blog, {}!'.format(nome_login))
      else:
        print('Você deve ter digitado seu nome de usuario errado, por favor verifique.'
      )
  arq.close()
Login()