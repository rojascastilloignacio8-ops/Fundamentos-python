from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Regisro(BaseModel):
    Nombre: str

app = FastAPI()


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
async def InicioRegistro(credencial: Regisro):
    return credencial