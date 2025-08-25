from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database
from app.schemas.agenda_ia import AgendaIACreate, AgendaIARead, AgendaIAUpdate
from app.services import agenda_ia

router = APIRouter(prefix="/agendaIA", tags=["agendaIA"])

@router.post("/", response_model=AgendaIARead)
def criar_agendaIA(agenda: AgendaIACreate, db: Session = Depends(database.get_db)):
    return agenda_ia.criar_agendaIA(db, agenda)

@router.get("/", response_model=list[AgendaIARead])
def listar_agendaIA(db: Session = Depends(database.get_db)):
    return agenda_ia.listar_agendaIA(db)

@router.patch("/{agenda_id}", response_model=AgendaIARead)
def atualizar_agendaIA(agenda_id: int, agenda: AgendaIAUpdate, db: Session = Depends(database.get_db)):
    agenda_atualizada = agenda_ia.atualizar_agendaIA(db, agenda_id, agenda)
    if agenda_atualizada:
        return agenda_atualizada
    return {"error": "AgendaIA não encontrada"}

@router.delete("/{agenda_id}", response_model=AgendaIARead)
def deletar_agendaIA(agenda_id: int, db: Session = Depends(database.get_db)):
    agenda_deletada = agenda_ia.deletar_agendaIA(db, agenda_id)
    if agenda_deletada:
        return agenda_deletada
    return {"error": "AgendaIA não encontrada"}