# importando biblioteca
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker,declarative_base

# Base de dados - endereço
engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/taskflow')

#config sessao
#db é database
db_session = sessionmaker(bind=engine)

Base = declarative_base()

class Tarefa(Base):
    __tablename__ = 'tarefa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    data = Column(DateTime, nullable=False)
    hora = Column(DateTime, nullable=False)
    recurso = Column(Interer, nullable=False)
    prioridade = Column(String(20), nullable=False)
    categoria = Column(String(20), nullable=False)
    responsavel = Column(String(20), nullable=False)
    descricao = Column(String(100), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Tarefa {self.nome}, data {self.data}, hora {self.hora}, recurso {self.recurso}, prioridade {self.prioridade}, categoria {self.categoria}, responsavel {self.responsavel}, descricao {self.descricao}'

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    email= Column(String(20), nullable=False, unique=True)
    senha_hash = Column(String(20), nullable=False)
    papel = Column(String(20), default='usuario', nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Pessoa {self.nome}, email {self.email}, senha {self.senha_hash}'

class Tipo(Base):
    __tablename__ = 'tipos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    descricao = Column(String(30), nullable=False)

    def __repr__(self):
        return f'Tipo {self.nome}, descricao {self.descricao}'

class Recurso(Base):
    __tablename__ = 'recursos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    descricao = Column(String(30), nullable=False)
    tipo = Column(String(30), nullable=False)

    def __repr__(self):
        return f'Recurso {self.nome}, descricao {self.descricao}, tipo {self.tipo}'