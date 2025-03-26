#importe o customtkinter
import customtkinter as ctk

#criar funcao para validar o login

def validar_login():
    usuario = campo_usuario.get() #pega o valor do campo usuario
    senha = campo_senha.get() #pega o valor do campo senha

    #verificar usuario e senha
    if usuario == 'admin' and senha == '1234':
        resultado_login.configure(text='Login realizado com sucesso', text_color='green')
    else:
        resultado_login.configure(text='Usuário ou senha inválidos', fg='red')

#configuração da janela (aparencia)
ctk.set_appearance_mode('dark')

#criação da janela
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

#criação dos campos (label, entry, button)
#label
label_usuario = ctk.CTkLabel(app, text='Usuário') #cria o label
label_usuario.pack(pady=10) #coloca o código da label na app

