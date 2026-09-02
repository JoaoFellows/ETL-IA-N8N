from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database
from app.services.agendas import get_all_agendas

router = APIRouter(prefix="/agendas", tags=["agendas"])

@router.get("/")
def get_all(db: Session = Depends(database.get_db)):
    return get_all_agendas(db)