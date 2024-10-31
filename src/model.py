from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Relationship, declarative_base


Base = declarative_base()

class Pedidos(Base):
    __tablename__ = 'pedidos'

    id_pedido = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id_cliente'),nullable=False)
    cliente = Relationship("Cliente", back_populates='pedidos')
    id_produto = Column(Integer, ForeignKey('produto.id_produto'),nullable=False)
    produto = Relationship("Produto", back_populates='pedidos')
    data_pedido = Column(String)
    valor_total = Column(Float)
    status = Column(String)

class Produto(Base):
    __tablename__ = 'produto'

    id_produto = Column(Integer, primary_key=True, index=True)
    nome_produto = Column(String)
    categoria = Column(String)
    pedidos = Relationship("Pedidos", back_populates='produto')

class Cliente(Base):
    __tablename__ = 'cliente'

    id_cliente = Column(Integer, primary_key=True, index=True)
    nome_empresa = Column(String)
    estado = Column(String)
    cidade = Column(String)
    cep = Column(String)
    pedidos = Relationship("Pedidos", back_populates='cliente')
