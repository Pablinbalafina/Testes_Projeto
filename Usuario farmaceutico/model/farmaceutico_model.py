from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definindo a base para as classes mapeadas
Base = declarative_base()

class Farmaceutico(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False)
    nascimento = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    endereco = Column(String(100), nullable=False)
    crm = Column(String(100), nullable=False)
    
    # Adicionando __repr__ para facilitar a visualização dos objetos
    def __repr__(self):
        return f"<Farmaceutico(id={self.id}, nome={self.nome}, cpf={self.cpf})>"

class Medicamentos(Base):
    __tablename__ = 'medicamentos'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    principio_ativo = Column(String(50), nullable=False)
    forma_farmaceutica = Column(String(50), nullable=False)
    validade = Column(Date, nullable=False)  # Usando o tipo Date aqui
    
    # Adicionando __repr__ para facilitar a visualização dos objetos
    def __repr__(self):
        return f"<Medicamento(id={self.id}, nome={self.nome}, principio_ativo={self.principio_ativo})>"
    

# Configuração do banco de dados
DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/postgres'

# Criando a engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def get_session():
    return Session()  
# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

