from sqlalchemy.orm import Session
from app import models
from app.schemas.agenda_mkt import AgendaMKTCreate, AgendaMKTUpdate

def criar_agendaMKT(db: Session, agenda: AgendaMKTCreate):
    db_agenda = models.AgendaMKT(
        data=agenda.data,
        evento=agenda.evento,
        descricao=agenda.descricao,
        status=agenda.status,
        areaEvento=agenda.areaEvento
    )
    db.add(db_agenda)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda

def listar_agendaMKT(db: Session):
    return db.query(models.AgendaMKT).all()

def atualizar_agendaMKT(db: Session, agenda_id: int, agenda: AgendaMKTUpdate):
    db_agenda = db.query(models.AgendaMKT).filter(models.AgendaMKT.id == agenda_id).first()
    if db_agenda:
        if agenda.data is not None:
            db_agenda.data = agenda.data
        if agenda.evento is not None:
            db_agenda.evento = agenda.evento
        if agenda.descricao is not None:
            db_agenda.descricao = agenda.descricao
        if agenda.status is not None:
            db_agenda.status = agenda.status
        if agenda.areaEvento is not None:
            db_agenda.areaEvento = agenda.areaEvento
        db.commit()
        db.refresh(db_agenda)
    return db_agenda

def deletar_agendaMKT(db: Session, agenda_id: int):
    db_agenda = db.query(models.AgendaMKT).filter(models.AgendaMKT.id == agenda_id).first()
    if db_agenda:
        db.delete(db_agenda)
        db.commit()
    return db_agenda