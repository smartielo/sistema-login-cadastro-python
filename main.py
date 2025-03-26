#instale o customtkinter com o comando pip install customtkinter
#instal o mysql-connector-python com o comando pip install mysql-connector-python

#importe o customtkinter
import customtkinter as ctk

#importe o mysql.connector
import mysql.connector

#importe o messagebox(ele cria mensagens de alerta para o usuário)
from tkinter import messagebox

#importe o hashlib (ele é usado para criptografar a senha)
import hashlib

#função para conectar com o banco de dados (mysql)
def conectar_bd():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='sistema_login'

#função para criptografar a senha




#criar funcao para validar o login
def validar_login():
    usuario = campo_usuario.get() #pega o valor do campo usuario
    senha = campo_senha.get() #pega o valor do campo senha

    #verificar usuario e senha
    if usuario == 'admin' and senha == '1234':
        resultado_login.configure(text='Login realizado com sucesso', text_color='green')
    else:
        resultado_login.configure(text='Usuário ou senha inválidos', text_color='red')

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

#entry
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário') #cria o campo de entrada
campo_usuario.pack(pady=5) #coloca o código na app

#label
label_senha = ctk.CTkLabel(app, text='Senha') #cria o label
label_senha.pack(pady=10) #coloca o código da label na app

#entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha') #cria o campo de entrada
campo_senha.pack(pady=5) #coloca o código na app

#button
ctk.CTkButton(app, text='Login', command=validar_login).pack(pady=10) #cria o botão e coloca o código na app

#campo de texto feedback do login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)


#inicia a janela
app.mainloop()


