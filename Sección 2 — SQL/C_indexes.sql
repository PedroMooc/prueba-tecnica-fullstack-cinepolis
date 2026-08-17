-- =============================================================================
-- Pregunta C: Estrategia de Índices para la tabla 'showtimes'
-- =============================================================================

-- Índice 1: Optimización de la Consulta A (Covering Index)
CREATE INDEX idx_showtimes_date_cine 
ON showtimes (show_date, id_cine) 
INCLUDE (id_movie, tickets_sold, capacity);

-- Índice 2: Optimización de la Consulta B (Búsqueda por FK y Fecha)
CREATE INDEX idx_showtimes_cine_date 
ON showtimes (id_cine, show_date);