## 📚 Gerenciador de Tarefas Acessível (Lab Engenharia de Software II)

Projeto desenvolvido como parte do laboratório prático da disciplina de Engenharia de Software II, focado na aplicação de padrões de qualidade, segurança e acessibilidade no desenvolvimento web.

| Detalhe        | Informação                     |
| :------------- | :----------------------------- |
| **Disciplina** | Engenharia de Software II      |
| **Professor**  | Clovis Maxwell Andrade Martins |
| **Aluno**      | Marcelo Hitoshi Kondo Oya      |

---

## 💡 Sobre o Projeto

O Gerenciador de Tarefas é uma aplicação web simples (To-Do List) construída com a _stack_ **Python/Flask** e **PostgreSQL**. O objetivo principal do laboratório não foi apenas construir a funcionalidade CRUD (Criar, Ler, Atualizar, Deletar), mas sim garantir que o software atendesse a rigorosos requisitos **não funcionais** de **qualidade**, **segurança** e **acessibilidade**, conforme as normas internacionais.

### Tecnologias Utilizadas

| Categoria          | Tecnologia                      | Uso no Projeto                                             |
| :----------------- | :------------------------------ | :--------------------------------------------------------- |
| **Backend**        | Python, Flask, Flask-SQLAlchemy | Servidor web, rotas, e Mapeamento Objeto-Relacional (ORM). |
| **Banco de Dados** | PostgreSQL, `psycopg2`          | Persistência e armazenamento seguro das tarefas.           |
| **Frontend**       | HTML5, CSS3, Jinja2             | Estrutura semântica e _templates_ de acessibilidade.       |
| **Qualidade**      | Pytest                          | Testes automatizados unitários e de integração.            |

---

## 🔒 Conformidade Normativa e Qualidade

O projeto foi construído seguindo rigorosamente as diretrizes das normas solicitadas, que são pilares da qualidade do software.

### 1. Acessibilidade (WCAG 2.2)

Foi implementado o princípio **Operável** (do acrônimo POUR) da WCAG para garantir que usuários que dependem da navegação por teclado possam interagir com a aplicação.

- **Foco Visível:** Todos os elementos interativos (`<input>`, `<button>`) possuem um `outline` de alto contraste no `:focus` para guiar a navegação.
- **Fluxo de Foco:** O fluxo de tabulação (tecla `TAB`) foi corrigido utilizando o `display: flex` e regras CSS específicas, garantindo que todos os botões de ação na lista sejam alcançados sequencialmente.
- **HTML Semântico:** Uso de `aria-label` em botões e de um _skip link_ para pular conteúdo repetitivo.

### 2. Segurança (OWASP Top 10)

O foco primário foi prevenir vulnerabilidades de **Injeção**.

- **Prevenção de SQL Injection (A03):** O uso do **SQLAlchemy ORM** garante que todas as interações com o banco de dados sejam feitas através de _Prepared Statements_, desabilitando a possibilidade de injeção de código malicioso via _input_ do usuário.

### 3. Privacidade (LGPD)

Em conformidade com a Lei Geral de Proteção de Dados.

- **Direito de Exclusão:** A rota `/deletar` permite que o usuário elimine permanentemente seus dados do sistema, atendendo ao Artigo 18, Inciso IV da LGPD.
- **Minimização de Dados:** A aplicação coleta apenas o dado estritamente essencial para a funcionalidade (o título da tarefa).

### 4. Confiabilidade e Manutenibilidade (ISO/IEC 25010)

A qualidade do sistema foi assegurada via testes e boas práticas de código.

- **Testes Automatizados (Confiabilidade):** O **Pytest** foi utilizado para criar testes funcionais que validam:
  - O carregamento correto da página inicial (`HTTP 200 OK`).
  - A persistência de dados no banco após a adição de uma tarefa.
  - A prevenção de adição de tarefas com título vazio (Validação de Entrada).
- **Documentação (Manutenibilidade):** O código foi documentado com comentários justificando as decisões normativas (WCAG, OWASP, LGPD) e aderindo a padrões de estilo Python (PEP 8).

---

## 🛠️ Como Rodar o Projeto

### Pré-requisitos

- Python 3.x
- PostgreSQL Server (Rodando na porta 5432)
- Git

### 1. Configuração do Banco de Dados

Crie um usuário e um banco de dados no seu servidor PostgreSQL (se já não o fez):

````sql
CREATE USER dev_user WITH PASSWORD 'dev_pass';
CREATE DATABASE todolist_db WITH OWNER dev_user;

### 2. Setup e Execução

1.  Clone o repositório:
    ```bash
    git clone [https://docs.github.com/pt/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github](https://docs.github.com/pt/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
    cd lab_todolist
    ```
2.  Crie e ative o ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    # .\venv\Scripts\activate  # Windows
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4.  Crie as tabelas no banco de dados (crucial para mapear o modelo `Tarefa` do Python para o PostgreSQL):
    ```bash
    python
    >>> from app import app, db
    >>> with app.app_context():
    ...     db.create_all()
    ...
    >>> exit()
    ```
5.  Inicie a aplicação:
    ```bash
    python app.py
    ```
6.  Acesse: `http://127.0.0.1:5000/`

### 3. Execução dos Testes (Verificação de Qualidade)

Para rodar os testes automatizados (necessário parar o servidor Flask antes):

```bash
pytest
````
