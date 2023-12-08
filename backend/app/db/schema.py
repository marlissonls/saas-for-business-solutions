from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.config import engine

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime, default=None)
    deleted_at = Column(DateTime, default=None)

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    profile_image = Column(String, nullable=False)
    company_id = Column(String, ForeignKey('companies.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime, default=None)
    deleted_at = Column(DateTime, default=None)
    company = relationship('Company', back_populates='users') 

class Dashboard(Base):
    __tablename__ = 'dashboards'
    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    company_id = Column(String, ForeignKey('companies.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime, default=None)
    deleted_at = Column(DateTime, default=None)
    company = relationship('Company', back_populates='dashboards')  

class Model(Base):
    __tablename__ = 'models'
    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    company_id = Column(String, ForeignKey('companies.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime, default=None)
    deleted_at = Column(DateTime, default=None)
    company = relationship('Company', back_populates='models')  

Company.users = relationship('User', back_populates='company')
Company.dashboards = relationship('Dashboard', back_populates='company')
Company.models = relationship('Model', back_populates='company')

Base.metadata.create_all(engine)
