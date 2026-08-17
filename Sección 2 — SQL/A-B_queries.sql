-- =============================================================================
-- Pregunta A: Top 5 películas con mayor ocupación promedio en cines VIP (última semana)
-- =============================================================================
SELECT 
    m.title,
    ROUND(AVG(s.tickets_sold::NUMERIC / s.capacity) * 100, 2) AS avg_occupancy_percentage
FROM showtimes s
JOIN cinemas c ON s.id_cine = c.id_cine
JOIN movies m ON s.id_movie = m.id_movie
WHERE c.brand = 'VIP'
  AND s.show_date >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY m.id_movie, m.title
ORDER BY avg_occupancy_percentage DESC
LIMIT 5;

-- =============================================================================
-- Pregunta B: Cines que NO tuvieron ninguna función programada ayer
-- =============================================================================
SELECT 
    c.id_cine,
    c.name,
    c.brand
FROM cinemas c
LEFT JOIN showtimes s 
    ON c.id_cine = s.id_cine 
   AND s.show_date = CURRENT_DATE - INTERVAL '1 day'
WHERE s.id IS NULL;