from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    __tablename__ = 'aluno'
    numero_matricula = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    nome_mae = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    ano_serie = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Professor(db.Model):
    __tablename__ = 'professor'
    id_professor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    formacao = db.Column(db.String(100), nullable=False)
    data_contratacao = db.Column(db.Date, nullable=False)
    departamento = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)

class Materia(db.Model):
    __tablename__ = 'materia'
    id_materia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)

class AlunoMateria(db.Model):
    __tablename__ = 'aluno_materia'
    id_aluno_materia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_matricula = db.Column(db.Integer, db.ForeignKey('aluno.numero_matricula'), nullable=False)
    id_materia = db.Column(db.Integer, db.ForeignKey('materia.id_materia'), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=True)
    nota_final = db.Column(db.Float, nullable=True)

class ProfessorMateria(db.Model):
    __tablename__ = 'professor_materia'
    id_professor_materia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_professor = db.Column(db.Integer, db.ForeignKey('professor.id_professor'), nullable=False)
    id_materia = db.Column(db.Integer, db.ForeignKey('materia.id_materia'), nullable=False)
    semestre = db.Column(db.String(6), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
