from fastapi import FastAPI

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