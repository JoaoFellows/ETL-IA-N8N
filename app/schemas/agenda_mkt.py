from pydantic import BaseModel

class AgendaMKTCreate(BaseModel):
    data: str
    evento: str
    descricao: str
    status: str
    areaEvento: str

class AgendaMKTRead(AgendaMKTCreate):
    id: int
    data: str
    evento: str
    descricao: str
    status: str
    areaEvento: str

    class Config:
        from_attributes = True

class AgendaMKTUpdate(BaseModel):
    data: str | None = None
    evento: str | None = None
    descricao: str | None = None
    status: str | None = None
    areaEvento: str | None = None