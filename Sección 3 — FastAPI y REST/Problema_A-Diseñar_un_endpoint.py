# from datetime import date
# from typing import Optional, List
# from fastapi import FastAPI, HTTPException, Path, Query
# from pydantic import BaseModel

# app = FastAPI()

# # Schemas de salida (Pydantic)
# class MovieSchema(BaseModel):
#     movie_id: int
#     title: str
#     duration_minutes: int
#     rating: str

# class ShowtimeSchema(BaseModel):
#     showtime_id: int
#     movie: MovieSchema
#     format: str
#     start_time: str
#     end_time: str
#     price: float
#     available_tickets: int

# class ScreenSchema(BaseModel):
#     screen_id: int
#     screen_name: str
#     capacity: int
#     showtimes: List[ShowtimeSchema]

# class CinemaDetailResponse(BaseModel):
#     cinema_id: int
#     name: str
#     brand: str
#     address: str
#     query_date: date
#     screens: List[ScreenSchema]


# @app.get(
#     "/api/v1/cinemas/{cinema_id}/showtimes", 
#     response_model=CinemaDetailResponse,
#     status_code=200
# )
# def get_cinema_showtimes(
#     cinema_id: int = Path(..., description="ID único del cine"),
#     show_date: Optional[date] = Query(default=date.today(), alias="date")
# ):
#     cinema = find_cinema_by_id(cinema_id)
#     if not cinema:
#         raise HTTPException(status_code=404, detail=f"Cinema with ID {cinema_id} not found.")
    
#     return build_cinema_schedule(cinema_id, show_date)