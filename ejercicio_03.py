from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

class Regisro(BaseModel):
    Nombre: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/productos")
async def obtenerProducto():
    return [ 
        {"id": 1, "Descripcion": "Electronicos", "Producto": "Televisor"},
        {"id": 2, "Descripcion": "Casa y jardin", "Producto": "Herbicida"},
        {"id": 3, "Descripcion": "Comida", "Producto": "Pan integral Bimbo"} 
        ]

@app.post("/registro")
async def inicioRegistro(credencial: Regisro):
    return credencial