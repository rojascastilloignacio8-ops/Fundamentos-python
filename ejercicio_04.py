from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
categorias = [
    {"id": 1,"Nombre": "Electrodomesticos", "Descripcion": "Productos para el hogar"},
    {"id": 2,"Nombre": "Computacion" ,"Descripcion": "Equipos y accesorios informaticos"},
    {"id": 3,"Nombre": "Telefonia", "Descripcion": "Smartphones y accesorios moviles"} 
]
class Categoria(BaseModel):
    ID: int
    Nombre: str
    Descripcion: str | None = None
app = FastAPI()
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)
@app.get("/categoria")
async def obtenerCategorias():
    return categorias

@app.get("/categorias/{categoria_id}")
async def obtenerCategoriaId(categoria_id: int):
    for categoria in categorias:
        if categoria["id"] == categoria_id:
            return categoria
    return None
