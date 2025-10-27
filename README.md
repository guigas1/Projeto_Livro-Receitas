# Livro de Receitas com Flask e Login

Este é um aplicativo web completo construído com Python e Flask, onde usuários podem se cadastrar, fazer login, e gerenciar sua própria coleção de receitas.

##  Objetivo do Projeto

O principal objetivo deste projeto foi evoluir de um simples aplicativo CRUD (como o projeto Mini-Blog) para uma aplicação web **multi-usuário** completa.

O foco foi aprender e implementar os conceitos fundamentais de **autenticação**, **segurança** e **relacionamentos de banco de dados**, que são a base de quase todas as aplicações web modernas.

Os principais conceitos aprendidos foram:
1.  **Autenticação:** Criar um sistema de registro (`/register`), login (`/login`) e logout (`/logout`) funcional.
2.  **Segurança de Senha:** Usar o **Flask-Bcrypt** para nunca salvar senhas em texto puro, armazenando apenas *hashes* seguros.
3.  **Gerenciamento de Sessão:** Usar o **Flask-Login** para "lembrar" quem é o usuário (`current_user`) e proteger rotas com `@login_required`.
4.  **Relacionamentos de Banco de Dados:** Conectar dois "moldes" (Models) usando um relacionamento "Um-para-Muitos" (Um `User` tem muitas `Recipes`).
5.  **Autorização:** Implementar lógica de segurança para garantir que um usuário só possa editar ou deletar as receitas que ele mesmo criou (`abort(403)`).

##  Funcionalidades

* **Sistema de Contas:** Registro de novos usuários com senha criptografada e login/logout.
* **Proteção de Rotas:** Apenas usuários logados podem ver, criar ou gerenciar receitas.
* **CRUD de Receitas:**
    * **Create:** Usuários podem criar e salvar novas receitas.
    * **Read:** Usuários veem *apenas* sua lista de receitas na página inicial e podem clicar para ver uma página de detalhes.
    * **Update:** Usuários podem editar suas receitas existentes.
    * **Delete:** Usuários podem deletar suas receitas.
* **Autorização Segura:** Um usuário logado **não pode** ver, editar ou deletar receitas de outro usuário, mesmo se tentar acessar a URL diretamente (recebe um erro 403 Forbidden).
* **Estilização Customizada:** Interface com um tema "aconchegante", usando CSS para formatar formulários, botões, mensagens de feedback e o conteúdo das receitas (preservando quebras de linha).

##  Tecnologias Utilizadas

* **Backend:**
    * **Python 3**
    * **Flask:** Framework web principal.
    * **Flask-SQLAlchemy:** ORM para o banco de dados.
    * **Flask-Login:** Gerenciamento de sessão de usuários (login/logout, `current_user`).
    * **Flask-Bcrypt:** Hashing (criptografia) de senhas.
    * **SQLite:** Banco de dados.
* **Frontend:**
    * **HTML5 / Jinja2:** Templates dinâmicos.
    * **CSS3:** Estilização personalizada.

##  Como Executar o Projeto Localmente

### Pré-requisitos

* [Python 3.7+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/guigas1/NOME_DO_SEU_REPO.git](https://github.com/guigas1/NOME_DO_SEU_REPO.git)
    cd NOME_DO_SEU_REPO
    ```
    *(**Nota:** Substitua `NOME_DO_SEU_REPO` pelo nome real do seu repositório no GitHub)*

2.  **Crie e ative um ambiente virtual (venv):**
    * *No Linux/macOS:*
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * *No Windows:*
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    O Flask iniciará o servidor. O banco de dados `recipes.db` será criado automaticamente na primeira vez.
    ```bash
    python app.py
    ```

5.  **Acesse no navegador:**
    Abra seu navegador e acesse [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    *(Você será redirecionado para a página de login, como esperado)*

