from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio

app = FastAPI()

class Livro (BaseModel):
    id: int
    titulo: str
    autor: str
    ano_livro: int

livros = [
    Livro (
        id=1,
        titulo="Dom Casmurro",
        autor="Machado de Assis",
        ano_livro=1889
    ),
    Livro(
        id=2,
        titulo="1984",
        autor="George Orwell",
        ano_livro=1949
    )
]

@app.get("/livros")
async def listar_livros():
    await asyncio.sleep(0)

    if not livros:
        raise HTTPException(
            status_code=404,
            detail="Nenhum livro cadastrado."
        )

    return livros

@app.post("/livros")
async def adicionar_livro(livro: Livro):
    await asyncio.sleep(0)

    for item in livros:
        if item.id == livro.id:
            raise HTTPException(
                status_code=409,
                detail="Erro: Já existe um livro cadastrado com este ID."
            )
        
    livros.append(livro)
    return {
        "mensagem": "Livro cadastrado com sucesso!",
        "livro": livro
    }

@app.put("/livros/{id}")
async def atualizar_livro(id: int, livro_atualizado: Livro):
    await asyncio.sleep(0)

    for indice, livro in enumerate(livros):
        if livro.id == id:
            livros[indice] = livro_atualizado

            return {
                "mensagem": "Livro atualizado com sucesso!",
                "livro": livro_atualizado
            }
    raise HTTPException(
        status_code=404,
        detail="Erro: Livro não cadastrado."
    )

@app.delete("/livros/{id}")
async def remover_livro(id: int):
    await asyncio.sleep(0)

    for indice, livro in enumerate(livros):
        if livro.id == id:
            livro_removido = livros.pop(indice)

            return {
                "mensagem": "Livro removido com sucesso!",
                "livro": livro_removido
            }

    raise HTTPException(
        status_code=404,
        detail="Erro: Livro não cadastrado."
    )

