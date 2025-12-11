# app.py

# Ferramentas: Flask (web framework), SQLAlchemy (ORM), os (gerenciar ambiente) [cite: 66]
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

# Inicialização do Flask
app = Flask(__name__) # [cite: 70, 71]

# Configuração do Banco de Dados (PostgreSQL)
# Entrada: URL de conexão (Requisito de Confiabilidade) [cite: 73]
# Tenta usar a variável de ambiente DATABASE_URL, senão usa a URL local padrão.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://dev_user:dev_pass@localhost/todolist_db') # [cite: 74]

# Configuração de Segurança (OWASP A05: Security Misconfiguration) [cite: 75]
# Tenta usar a variável de ambiente SECRET_KEY, senão usa um valor default.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'chave_super_secreta_para_flash_msgs') # [cite: 76]

# Inicializa o ORM SQLAlchemy
db = SQLAlchemy(app) # [cite: 77, 78]

# Modelo de Dados (ORM) [cite: 79]
class Tarefa(db.Model):
    # LGPD: Minimização de Dados (apenas o essencial está sendo coletado) [cite: 81]
    id = db.Column(db.Integer, primary_key=True) # [cite: 82]
    titulo = db.Column(db.String(100), nullable=False) # [cite: 83]
    concluida = db.Column(db.Boolean, default=False) # [cite: 84]

    # Saída: Representação do objeto para debug [cite: 85]
    def __repr__(self): # [cite: 86]
        return f'<Tarefa {self.id}: {self.titulo}>' # [cite: 87]

# Rota Principal (Entrada: GET /; Saída: render_template com dados) [cite: 88]
@app.route('/')
def index():
    # Consulta ao DB: Obtém todas as tarefas (Saída do ORM) [cite: 91]
    todas_tarefas = Tarefa.query.all() # [cite: 92]
    # Saída para a web: Renderiza o HTML, passando a lista de objetos Tarefa [cite: 93]
    return render_template('index.html', tarefas=todas_tarefas) # [cite: 94]

# Este bloco será expandido na Etapa 4, mas é necessário para rodar o app:
if __name__ == '__main__':
    # Bloco para criar as tabelas no PostgreSQL (O db.create_all() será feito na Ação 3.3) [cite: 96, 97]
    app.run(debug=True) # [cite: 98]