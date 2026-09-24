# importando biblioteca
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Date, func
from sqlalchemy.orm import relationship, sessionmaker,declarative_base, scoped_session

# Base de dados - endereço
engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/taskflow')

#config sessao
#db é database
db_session = scoped_session (sessionmaker(bind=engine))

Base = declarative_base()

class Tarefa(Base):
    __tablename__ = 'tarefa'
    id = Column(Integer, primary_key=True)
    nome_tarefa = Column(String(30), nullable=False)
    data_tarefa = Column(DateTime, nullable=False)
    hora_tarefa = Column(DateTime, nullable=False)
    recurso_tarefa = Column(Integer, nullable=False)
    prioridade_tarefa = Column(String(20), nullable=False)
    categoria_tarefa = Column(String(20), nullable=False)
    responsavel_tarefa = Column(String(20), nullable=False)
    descricao_tarefa = Column(String(100), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Tarefa {self.nome_tarefa}, data {self.data_tarefa}, hora {self.hora_tarefa}, recurso {self.recurso_tarefa}, prioridade {self.prioridade_tarefa}, categoria {self.categoria_tarefa}, responsavel {self.responsavel_tarefa}, descricao {self.descricao_tarefa}, criado_em{self.criado_em}'

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome_pessoa = Column(String(30), nullable=False)
    email_pessoa= Column(String(20), nullable=False, unique=True)
    senha_pessoa = Column(String(20), nullable=False)
    papel = Column(String(20), default='usuario', nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Pessoa {self.nome_pessoa}, email {self.email_pessoa}, senha {self.senha_pessoa}, criado_em{self.criado_em}'

class Tipo(Base):
    __tablename__ = 'tipos'
    id = Column(Integer, primary_key=True)
    nome_tipo = Column(String(30), nullable=False)
    descricao_tipo = Column(String(30), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Tipo {self.nome_tipo}, descricao {self.descricao_tipo}, criado_em{self.criado_em}'

class Recurso(Base):
    __tablename__ = 'recursos'
    id = Column(Integer, primary_key=True)
    nome_recurso = Column(String(30), nullable=False)
    descricao_recurso = Column(String(30), nullable=False)
    tipo_recurso = Column(String(30), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Recurso {self.nome_recurso}, descricao {self.descricao_recurso}, tipo {self.tipo_recurso}, criado_em{self.criado_em}'