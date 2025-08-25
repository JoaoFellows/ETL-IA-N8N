from sqlalchemy.orm import Session
from app import models
from app.schemas.agenda_ia import AgendaIACreate, AgendaIAUpdate

def criar_agendaIA(db: Session, agenda: AgendaIACreate):
    db_agenda = models.AgendaIA(
        data=agenda.data,
        evento=agenda.evento,
        descricao=agenda.descricao,
        engajamento=agenda.engajamento,
        status=agenda.status,
        areaEvento=agenda.areaEvento
    )
    db.add(db_agenda)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda

def listar_agendaIA(db: Session):
    return db.query(models.AgendaIA).all()

def atualizar_agendaIA(db: Session, agenda_id: int, agenda: AgendaIAUpdate):
    db_agenda = db.query(models.AgendaIA).filter(models.AgendaIA.id == agenda_id).first()
    if db_agenda:
        if agenda.data is not None:
            db_agenda.data = agenda.data
        if agenda.evento is not None:
            db_agenda.evento = agenda.evento
        if agenda.descricao is not None:
            db_agenda.descricao = agenda.descricao
        if agenda.engajamento is not None:
            db_agenda.engajamento = agenda.engajamento
        if agenda.status is not None:
            db_agenda.status = agenda.status
        if agenda.areaEvento is not None:
            db_agenda.areaEvento = agenda.areaEvento
        db.commit()
        db.refresh(db_agenda)
    return db_agenda

def deletar_agendaIA(db: Session, agenda_id: int):
    db_agenda = db.query(models.AgendaIA).filter(models.AgendaIA.id == agenda_id).first()
    if db_agenda:
        db.delete(db_agenda)
        db.commit()
    return db_agenda