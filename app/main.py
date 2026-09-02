from fastapi import FastAPI
from . import models, database
from app.routes import agenda_ia, agenda_mkt, agenda_rh, agendas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(agenda_ia.router)
app.include_router(agenda_mkt.router)
app.include_router(agenda_rh.router)
app.include_router(agendas.router)
