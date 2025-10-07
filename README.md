# API RESTful de Cadastro de Usuários

## Descrição

Este projeto é uma API RESTful desenvolvida em Python, utilizando **Flask**, para gerenciamento de usuários. A API permite o cadastro, login e listagem de usuários, com autenticação baseada em JWT e integração com banco de dados **PostgreSQL**. A documentação interativa é gerada automaticamente via **Swagger**.

---

## Funcionalidades

- **Cadastro de Usuários:** Permite criar novos usuários com dados básicos (nome, email, senha).
- **Login:** Autenticação de usuários via email e senha, com geração de token JWT.
- **Listagem de Usuários:** Retorna a lista de usuários cadastrados (acesso protegido).
- **Autenticação JWT:** Protege rotas sensíveis, garantindo acesso apenas a usuários autenticados.
- **Integração com PostgreSQL:** Persistência dos dados dos usuários.
- **Testes:** Endpoints testados via Postman e com testes unitários automatizados.
- **Documentação Swagger:** Interface interativa para explorar e testar a API.

---

## Checklist de Implementação

- [x] **Definir Endpoints**
  - `/register` : Cadastro de usuário
  - `/login` : Autenticação e geração de token JWT
  - `/users` : Listagem de usuários (protegido)
- [x] **Implementar Autenticação JWT**
  - Geração e validação de tokens para rotas protegidas
- [x] **Conectar com Banco de Dados PostgreSQL**
  - Modelagem de usuários e integração via ORM (SQLAlchemy)
- [x] **Testar Endpoints**
  - Testes manuais com Postman
  - Testes unitários automatizados (pytest)
- [x] **Documentar API**
  - Documentação automática via Swagger

---

## Como Executar

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/Flavio-LP/flask_user_api.git
    cd nome-do-projeto
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\/venv/Scripts/activate     # Windows
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente:**
    - Crie um arquivo `.env` com as configurações do banco de dados e chave secreta JWT.

    ```bash
    PG_HOST = ' sua credencial'
    PG_PORT = ' sua credencial'
    PG_USER = ' sua credencial'
    PG_PASSWORD = ' sua credencial'
    PG_DATABASE = ' sua credencial'
    DATABASE_URL = ' sua credencial'
    SECRET_KEY = ' sua credencial'
    ```

5. **Execute as migrações do banco de dados:**
    - Com SQLAlchemy/Alembic ou conforme instruções do projeto.

6. **Inicie a aplicação:**

    ```bash
    flask run                  # Para Flask
    ```

7. **Acesse a documentação Swagger:**
    - Flask (com flask-swagger): [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

---

## Testes

- **Testes Manuais:** Utilize o arquivo de coleção do Postman disponível no repositório.
- **Testes Automatizados:** Execute `pytest` para rodar os testes unitários.

---

## Tecnologias Utilizadas

- Python 3.12.10
- Flask
- PostgreSQL
- SQLAlchemy
- JWT (PyJWT)
- Swagger
- Pytest

---

## Contribuição

Contribuições são bem-vindas! Siga o fluxo de fork, branch, pull request e descreva suas alterações.

---

## Licença

Este projeto está sob a licença MIT.

---

**Dúvidas?**  
Abra uma issue ou entre em contato pelo email do mantenedor no repositório.
