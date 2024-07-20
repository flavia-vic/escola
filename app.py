from flask import Flask
from config import Config
from models import db, Aluno, Professor, Materia, AlunoMateria, ProfessorMateria

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Criação das tabelas na inicialização da aplicação
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
