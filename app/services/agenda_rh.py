from sqlalchemy.orm import Session
from app import models
from app.schemas.agenda_rh import AgendaRHCreate, AgendaRHUpdate

def criar_agendaRH(db: Session, agenda: AgendaRHCreate):
    db_agenda = models.AgendaRH(
        data=agenda.data,
        evento=agenda.evento,
        descricao=agenda.descricao,
        alcance=agenda.alcance,
        status=agenda.status,
        areaEvento=agenda.areaEvento
    )
    db.add(db_agenda)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda

def listar_agendaRH(db: Session):
    return db.query(models.AgendaRH).all()

def atualizar_agendaRH(db: Session, agenda_id: int, agenda: AgendaRHUpdate):
    db_agenda = db.query(models.AgendaRH).filter(models.AgendaRH.id == agenda_id).first()
    if agenda.data is not None:
        db_agenda.data = agenda.data
    if agenda.evento is not None:
        db_agenda.evento = agenda.evento
    if agenda.descricao is not None:
        db_agenda.descricao = agenda.descricao
    if agenda.alcance is not None:
        db_agenda.alcance = agenda.alcance
    if agenda.status is not None:
        db_agenda.status = agenda.status
    if agenda.areaEvento is not None:
        db_agenda.areaEvento = agenda.areaEvento
    db.commit()
    db.refresh(db_agenda)
    return db_agenda

def deletar_agendaRH(db: Session, agenda_id: int):
    db_agenda = db.query(models.AgendaRH).filter(models.AgendaRH.id == agenda_id).first()
    if db_agenda:
        db.delete(db_agenda)
        db.commit()
    return db_agenda