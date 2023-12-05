from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.config import engine

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime, default=None)
    deletedAt = Column(DateTime, default=None)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    senha = Column(String(255), nullable=False)
    empresa_id = Column(Integer, ForeignKey('companies.id'))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime, default=None)
    deletedAt = Column(DateTime, default=None)
    empresa = relationship('Company', back_populates='users') 

class Dashboard(Base):
    __tablename__ = 'dashboards'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text)
    empresa_id = Column(Integer, ForeignKey('companies.id'))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime, default=None)
    deletedAt = Column(DateTime, default=None)
    empresa = relationship('Company', back_populates='dashboards')  

class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text)
    empresa_id = Column(Integer, ForeignKey('companies.id'))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime, default=None)
    deletedAt = Column(DateTime, default=None)
    empresa = relationship('Company', back_populates='models')  

Company.users = relationship('User', back_populates='empresa')
Company.dashboards = relationship('Dashboard', back_populates='empresa')
Company.models = relationship('Model', back_populates='empresa')

Base.metadata.create_all(engine)
