from sqlalchemy.orm import Session
from app import models

def get_all_agendas(db: Session):
    ia = db.query(models.AgendaIA).all()
    rh = db.query(models.AgendaRH).all()
    mkt = db.query(models.AgendaMKT).all()
    return {
        "agenda_ia": ia,
        "agenda_rh": rh,
        "agenda_mkt": mkt
    }