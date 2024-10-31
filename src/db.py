from sqlalchemy import create_engine
from model import Base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./itu_bank.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(engine)

# Configurar uma sessão
Session = sessionmaker(autoflush=False,autocommit=False,bind=engine)
session = Session()