from pydantic import BaseModel

class AgendaRHCreate(BaseModel):
    data: str
    evento: str
    descricao: str
    alcance: int
    status: str
    areaEvento: str

class AgendaRHRead(AgendaRHCreate):
    id: int
    data: str
    evento: str
    descricao: str
    alcance: int
    status: str
    areaEvento: str

    class Config:
        from_attributes = True

class AgendaRHUpdate(BaseModel):
    data: str | None = None
    evento: str | None = None
    descricao: str | None = None
    alcance: int | None = None
    status: str | None = None
    areaEvento: str | None = None