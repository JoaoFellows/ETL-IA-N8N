from sqlalchemy import Column, Integer, String
from .database import Base


class AgendaIA(Base):
    __tablename__ = "agendaIA"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, nullable=False)
    evento = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    engajamento = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    areaEvento = Column(String, nullable=False)

class AgendaMKT(Base):
    __tablename__ = "agendaMKT"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, nullable=False)
    evento = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    status = Column(String, nullable=False)
    areaEvento = Column(String, nullable=False)

class AgendaRH(Base):
    __tablename__ = "agendaRH"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, nullable=False)
    evento = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    alcance = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    areaEvento = Column(String, nullable=False)
