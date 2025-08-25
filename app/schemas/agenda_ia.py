from pydantic import BaseModel

class AgendaIACreate(BaseModel):
    data: str
    evento: str
    descricao: str
    engajamento: int
    status: str
    areaEvento: str

class AgendaIARead(AgendaIACreate):
    id: int
    data: str
    evento: str
    descricao: str
    engajamento: int
    status: str
    areaEvento: str

    class Config:
        from_attributes = True

class AgendaIAUpdate(BaseModel):
    data: str | None = None
    evento: str | None = None
    descricao: str | None = None
    engajamento: int | None = None
    status: str | None = None
    areaEvento: str | None = None