# Sistema de Login com Tkinter e MySQL
Desenvolvido por um estudante de Ciências da Computação, praticando Python e Tkinter. 🚀

---

Este projeto é um sistema simples de login e cadastro utilizando Python com a biblioteca `customtkinter` para a interface gráfica e MySQL como banco de dados para armazenar os usuários.

## Tecnologias Utilizadas
- Python 3
- Tkinter (CustomTkinter)
- MySQL
- Biblioteca `mysql-connector-python`

## Funcionalidades
- Cadastro de usuários com armazenamento seguro de senhas.
- Login autenticado verificando credenciais no banco de dados.
- Interface gráfica amigável e responsiva.

## Instalação e Configuração
### 1. Clonar o Repositório
```sh
git clone https://github.com/smartielo/sistema-login-cadastro-python.git
cd sistema-login-tkinter
```

### 2. Instalar Dependências
```sh
pip install customtkinter mysql-connector-python
```

### 3. Criar o Banco de Dados
Execute os seguintes comandos no MySQL:
```sql
CREATE DATABASE sistema_login;
USE sistema_login;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);
```

### 4. Configurar Credenciais do Banco de Dados
No arquivo `main.py`, substitua as credenciais na função `conectar_bd()`:
```python
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",  # Substitua pelo seu usuário do MySQL
        password="sua_senha",  # Substitua pela sua senha do MySQL
        database="sistema_login"
    )
```

### 5. Executar o Programa
```sh
python main.py
```

## Como Usar
1. Insira um nome de usuário e senha.
2. Clique em "Cadastrar" para criar um novo usuário.
3. Para fazer login, insira as credenciais e clique em "Login".

## Melhorias Futuras
- Recuperação de senha.
- Integração com uma API para autenticação.
- Melhorias na interface gráfica.

---

