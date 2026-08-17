#  @router.post("/movies")
#  async def create_movie(data: dict):
#  movie = Movie(
#  title=data["title"],
#  release_date=data["release_date"],
#  distributor=data["distributor"],
#  )
#  db.add(movie)
#  db.commit()
#  return movie

#errores
#1.-Falta de validación en la entrada de datos (data: dict)
#2.-La sesión de la base de datos (db) no está inyectada
#3.-Uso incorrecto de async def con operaciones sincrónicas
#4.-Ausencia de manejo de excepciones y rollback


#Código corregido

from datetime import date
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Movie

router = APIRouter()

# 1. Esquema con Pydantic para validar la entrada
class MovieCreate(BaseModel):
    title: str
    release_date: date
    distributor: str

class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True


# Endpoint con los 4 arreglos aplicados
@router.post("/movies", response_model=MovieResponse, status_code=status.HTTP_201_CREATED)
def create_movie(
    movie_in: MovieCreate, 
    db: Session = Depends(get_db)  # 2. Inyección de dependencia
):
    movie = Movie(
        title=movie_in.title,
        release_date=movie_in.release_date,
        distributor=movie_in.distributor,
    )
    
    # 4. Manejo explícito de errores y rollback
    try:
        db.add(movie)
        db.commit()
        db.refresh(movie)
        return movie
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se pudo registrar la película."
        )