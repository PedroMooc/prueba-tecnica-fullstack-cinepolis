from datetime import datetime, timedelta

def validate_showtime(start_time: str, duration_min: int, opening: str, closing: str) -> dict:
    """
    Valida si una función de cine puede programarse dentro del horario de apertura y cierre.
    
    Args:
        start_time: Hora de inicio "HH:MM"
        duration_min: Duración total en minutos (incluye créditos)
        opening: Hora de apertura del cine "HH:MM"
        closing: Hora de cierre del cine "HH:MM"
        
    Returns:
        {"valid": True} o {"valid": False, "reason": "..."}
    """
    time_format = "%H:%M"
    
    # 1. Convertir strings de hora a objetos datetime para operar matemáticamente
    try:
        dt_start = datetime.strptime(start_time, time_format)
        dt_opening = datetime.strptime(opening, time_format)
        dt_closing = datetime.strptime(closing, time_format)
    except ValueError:
        return {"valid": False, "reason": "Formato de hora inválido. Use HH:MM"}
    
    # 2. Calcular la hora de término sumando la duración
    dt_end = dt_start + timedelta(minutes=duration_min)
    
    # 3. Regla 1: No puede empezar antes del horario de apertura
    if dt_start < dt_opening:
        return {
            "valid": False, 
            "reason": f"Starts before opening ({opening})"
        }
    
    # 4. Regla 2: Debe terminar antes (o exacto a) la hora de cierre
    # Caso especial: Si el cierre es a las "00:00" o medianoche, o la función pasa de medianoche
    if dt_closing < dt_opening:
        dt_closing += timedelta(days=1)
        
    if dt_end > dt_closing:
        end_time_str = dt_end.strftime("%H:%M")
        return {
            "valid": False, 
            "reason": f"Ends after closing ({end_time_str} > {closing})"
        }
    
    return {"valid": True}


# --- Pruebas unitarias con los casos del examen ---
if __name__ == "__main__":
    # Caso 1: Válido (termina 16:30)
    res1 = validate_showtime("14:30", 120, "10:00", "23:00")
    print("Test 1:", res1)
    # Output esperado: {'valid': True}

    # Caso 2: Empieza antes de abrir
    res2 = validate_showtime("09:00", 90, "10:00", "23:00")
    print("Test 2:", res2)
    # Output esperado: {'valid': False, 'reason': 'Starts before opening (10:00)'}

    # Caso 3: Termina después de cerrar (21:30 + 150 min = 00:00 > 23:00)
    res3 = validate_showtime("21:30", 150, "10:00", "23:00")
    print("Test 3:", res3)
    # Output esperado: {'valid': False, 'reason': 'Ends after closing (00:00 > 23:00)'}