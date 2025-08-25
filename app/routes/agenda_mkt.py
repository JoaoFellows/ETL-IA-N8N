from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database
from app.services import agenda_mkt
from app.schemas.agenda_mkt import AgendaMKTCreate, AgendaMKTRead, AgendaMKTUpdate

router = APIRouter(prefix="/agendaMKT", tags=["agendaMKT"])

@router.post("/", response_model=AgendaMKTRead)
def criar_agendaMKT(agenda: AgendaMKTCreate, db: Session = Depends(database.get_db)):
    return agenda_mkt.criar_agendaMKT(db, agenda)

@router.get("/", response_model=list[AgendaMKTRead])
def listar_agendaMKT(db: Session = Depends(database.get_db)):
    return agenda_mkt.listar_agendaMKT(db)

@router.patch("/{agenda_id}", response_model=AgendaMKTRead)
def atualizar_agendaMKT(agenda_id: int, agenda: AgendaMKTUpdate, db: Session = Depends(database.get_db)):
    agenda_atualizada = agenda_mkt.atualizar_agendaMKT(db, agenda_id, agenda)
    if agenda_atualizada:
        return agenda_atualizada
    return {"error": "AgendaMKT não encontrada"}

@router.delete("/{agenda_id}", response_model=AgendaMKTRead)
def deletar_agendaMKT(agenda_id: int, db: Session = Depends(database.get_db)):
    agenda_deletada = agenda_mkt.deletar_agendaMKT(db, agenda_id)
    if agenda_deletada:
        return agenda_deletada
    return {"error": "AgendaMKT não encontrada"}
