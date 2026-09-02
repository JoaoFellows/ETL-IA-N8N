from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database
from app.services import agenda_rh
from app.schemas.agenda_rh import AgendaRHCreate, AgendaRHRead, AgendaRHUpdate

router = APIRouter(prefix="/agendaRH", tags=["agendaRH"])

@router.post("/", response_model=AgendaRHRead)
def criar_agendaRH(agenda: AgendaRHCreate, db: Session = Depends(database.get_db)):
    return agenda_rh.criar_agendaRH(db, agenda)

@router.get("/", response_model=list[AgendaRHRead])
def listar_agendaRH(db: Session = Depends(database.get_db)):
    return agenda_rh.listar_agendaRH(db)

@router.patch("/{agenda_id}", response_model=AgendaRHRead)
def atualizar_agendaRH(agenda_id: int, agenda: AgendaRHUpdate, db: Session = Depends(database.get_db)):
    agenda_atualizada = agenda_rh.atualizar_agendaRH(db, agenda_id, agenda)
    if agenda_atualizada:
        return agenda_atualizada
    return {"error": "AgendaRH não encontrada"}

@router.delete("/{agenda_id}", response_model=AgendaRHRead)
def deletar_agendaRH(agenda_id: int, db: Session = Depends(database.get_db)):
        agenda_deletada = agenda_rh.deletar_agendaRH(db, agenda_id)
        if agenda_deletada:
            return agenda_deletada
        return {"error": "AgendaRH não encontrada"}
