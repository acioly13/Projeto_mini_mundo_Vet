import PySimpleGUI as sg


class Dono:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('CPF',size=(5,0)), sg.Input(size=(15,0),key='cpf')],
            [sg.Text('Nome',size=(5,0)), sg.Input(size=(30,0),key='nome')],
            [sg.Text('Email',size=(5,0)), sg.Input(size=(30,0),key='email')],
            [sg.Button('Cadastrar'),sg.Button('Sair')],
            [sg.Text('',key='out')]
                ]
        # janela
        self.janela = sg.Window('Cadastro Dono(a)').layout(layout)

    def cad_pessoa(self):
        self.nomes = []
        self.cpfs = []
        self.emails = []
        while True:
            # extrair dados da tela
            self.button, self.values = self.janela.Read()
            if self.button is None or self.button == 'Sair':
                break
            # Herança, encapsulamento e polimorfismo usado em tudo a partir daqui
            self.cpf = self.values['cpf']
            cpf = self.cpf
            self.cpfs.append(cpf)
            self.nome = self.values['nome']
            nome = self.nome
            self.nomes.append(nome)
            self.email = self.values['email']
            email = self.email
            self.emails.append(email)
            # exceção usada com while( Só aceita cpfs validos)
            while cpf == '':
                print('CPF Inválido, Digite Novamente')
                self.button, self.values = self.janela.Read()
                if self.button is None or self.button == 'Sair':
                    break
                # Herança, encapsulamento e polimorfismo usado em tudo a partir daqui
                self.cpf = self.values['cpf']
                cpf = self.cpf
                self.cpfs.append(cpf)
                self.nome = self.values['nome']
                nome = self.nome
                self.nomes.append(nome)
                self.email = self.values['email']
                email = self.email
                self.emails.append(email)

            print('')
            print('--Cadastro de Dono(a) Concluido--')
            print(f'CPF: {self.cpf}')
            print(f'Nome: {self.nome}')
            print(f'Email: {self.email}')
            print('')
            self.janela.close()

            class Animal:
                def __init__(self):
                    self.tipoC = []
                    self.tipoG = []
                    self.raca = []
                    self.nomea = []
                    # layout
                    layout = [
                        [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='nomea')],
                        [sg.Text('Raça', size=(5, 0)), sg.Input(size=(30, 0), key='raca')],
                        [sg.Text('Qual seu Animal?')],
                        [sg.Radio('Cachorro', 'tipo', key='Tcachorro'), sg.Radio('Gato', 'tipo', key='Tgato')],
                        [sg.Button('Cadastrar'), sg.Button('Sair')],

                    ]
                    # janela
                    self.janela = sg.Window('Cadastro Animal').layout(layout)

                def cad_animal(self):
                    while True:
                        # extrair dados da tela
                        self.button, self.values = self.janela.Read()
                        if self.button is None or self.button == 'Sair':
                            break
                        # Herança, encapsulamento e polimorfismo usado em tudo a partir daqui
                        self.nomea = self.values['nomea']
                        self.raca = self.values['raca']
                        self.tipoC = self.values['Tcachorro']
                        self.tipoG = self.values['Tgato']
                        print(f'--Cadastro do Animal de {nome} Concluido--')
                        print(f'Nome: {self.nomea}')
                        print(f'Raça: {self.raca}')
                        if self.tipoC:
                            print(f'Animal: Cachorro')
                        else:
                            print(f'Animal: Gato')
                        print('')
                        print(f'Dono(a) {nome} de CPF {cpf} é responsavel pelo {self.nomea}')
                        self.janela.close()
            tela2 = Animal()
            tela2.cad_animal()


tela = Dono()
tela.cad_pessoa()
