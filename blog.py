def Blog():
  class blog():
    #def __init__(self, postagens="4", programados="2", lixeira="3"):
        #self.postagens = postagens
        #self.programados = programados
        #self.lixeira = lixeira

    def __init__(self,identf, tema, titulo, texto, data_public = 0):
        self.identf = identf
        self.tema = tema
        self.titulo = titulo
        self.texto = texto
        self.data_public = data_public

    def alterarIdentf(self, novoIdentf):
            novoIdentf = input("Digite o nome do novo identificador:")
            self.Identf = novoIdentf
      
    def alterarTema(self, novoTema):
            novoTema = input("Digite o nome do novo tema:")
            self.tema = novoTema
      
    def alterarTitulo(self, novoTitulo):
            novoTitulo = input("Digite o nome do novo titulo:")
            self.titulo = novoTitulo
    def alterarTexto(self, novoTexto):
            novoTexto = input("Digite o nome do novo texto:")
            self.texto = novoTexto

    
    @property
    def postagens(self):
        return self.__postagens

    @postagens.setter
    def postagens(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num > 1 and num <= 4:
                self.__postagens = num
            else:
                print("Postagem inexistente")

        else:
            print("Escolha apenas números!")

    @property
    def programados(self):
        return self.__programados

    @programados.setter
    def programados(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num >= 1 and num <= 2:
                self.__programados = num
            else:
                print("Essa postagem não está programada")

        else:
            print("Escolha apenas números!")

    @property
    def lixeira(self):
        return self.__lixeira

    @lixeira.setter
    def lixeira(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num >= 1 and num <= 3:
                self.__lixeira = num
            else:
                print("Essa postagem não está na lixeira")

        else:
            print("Escolha apenas números!")



    #def criarPostagem(self):
     #   ufhjhfjfh
    def editarPostagens(self):
        num = input("Olhar/editar POSTAGEM: ")
        self.postagens = num
    def editarProgramados(self):
        num = input("Olhar/editar PROGRAMADO: ")
        self.programados = num

    def editarLixeira(self):
        num = input("Olhar/editar LIXEIRA: ")
        self.lixeira = num

    def __str__(self):
        return "POSTAGENS: {} \nPROGRAMADOS: {}\nLIXEIRA: {} \n".format(
            self.postagens, self.programados, self.lixeira)
    Blog()