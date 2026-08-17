import json

def summarize_by_movie(showtimes: list[dict]) -> list[dict]:
    grouped = {}

    for show in showtimes:
        movie = show["movie"]
        tickets = show["tickets_sold"]

        if movie not in grouped:
            grouped[movie] = {
                "total_shows": 0,
                "total_tickets": 0
            }

        grouped[movie]["total_shows"] += 1
        grouped[movie]["total_tickets"] += tickets

    summary = []
    for movie, data in grouped.items():
        total_shows = data["total_shows"]
        total_tickets = data["total_tickets"]
        avg_tickets = round(total_tickets / total_shows, 2)

        summary.append({
            "movie": movie,
            "total_shows": total_shows,
            "total_tickets": total_tickets,
            "avg_tickets": avg_tickets
        })

    summary_sorted = sorted(summary, key=lambda x: x["total_tickets"], reverse=True)

    return summary_sorted

if __name__ == "__main__":
    showtimes = [
    {"movie": "Inside Out 3", "cine": "Perisur", "format": "IMAX", "tickets_sold": 120},
    {"movie": "Inside Out 3", "cine": "Perisur", "format": "2D", "tickets_sold": 85},
    {"movie": "Inside Out 3", "cine": "Santa Fe", "format": "2D", "tickets_sold": 90},
    {"movie": "Deadpool 4", "cine": "Perisur", "format": "3D", "tickets_sold": 200},
    {"movie": "Deadpool 4", "cine": "Santa Fe", "format": "IMAX", "tickets_sold": 180},
    {"movie": "Moana 3", "cine": "Perisur", "format": "2D", "tickets_sold": 60},
    ]


    #RESULTADO ESPERADO: # Ordenado por total_tickets descendente

    # [
    #  {"movie": "Deadpool 4", "total_shows": 2, "total_tickets": 380, "avg_tickets": 190.0},
    #  {"movie": "Inside Out 3", "total_shows": 3, "total_tickets": 295, "avg_tickets": 98.33},
    #  {"movie": "Moana 3", "total_shows": 1, "total_tickets": 60, "avg_tickets": 60.0},
    # ]
    resultado = summarize_by_movie(showtimes)

    print(resultado)

