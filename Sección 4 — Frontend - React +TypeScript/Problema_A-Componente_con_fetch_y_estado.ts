import { useState, useEffect } from "react";

// Interfaces para el tipado estricto de TypeScript
interface Week {
  id_week: number;
  week_number: number;
  init_date: string;
  end_date: string;
  movies_count: number;
}

interface WeeksApiResponse {
  data: Week[];
}

interface WeekSelectorProps {
  year: number;
  onWeekSelect: (idWeek: number) => void;
}

export function WeekSelector({ year, onWeekSelect }: WeekSelectorProps) {
  const [weeks, setWeeks] = useState<Week[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<boolean>(false);

  // Helper para formatear fechas de "YYYY-MM-DD" a formato legible (ej: "04 Ago")
  const formatDate = (dateStr: string): string => {
    const [y, m, d] = dateStr.split("-").map(Number);
    const date = new Date(y, m - 1, d);
    return date.toLocaleDateString("es-ES", { day: "2-digit", month: "short" });
  };

  useEffect(() => {
    // AbortController para cancelar la petición si el componente se desmonta (Bonus Cleanup)
    const controller = new AbortController();

    const fetchWeeks = async () => {
      setLoading(true);
      setError(false);

      try {
        const response = await fetch(
          `/api/v1/weeks?year=${year}&status=assigned`,
          { signal: controller.signal }
        );

        if (!response.ok) {
          throw new Error("Error en la petición de semanas");
        }

        const result: WeeksApiResponse = await response.json();
        setWeeks(result.data);
      } catch (err: any) {
        // Se ignora el error si fue provocado por el abort del cleanup
        if (err.name !== "AbortError") {
          setError(true);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchWeeks();

    // Limpieza (Cleanup)
    return () => {
      controller.abort();
    };
  }, [year]);

  // Manejo de estados de la UI
  if (loading) return <p>Cargando...</p>;
  if (error) return <p>Error al cargar semanas</p>;

  return (
    <select
      defaultValue=""
      onChange={(e) => onWeekSelect(Number(e.target.value))}
    >
      <option value="" disabled>
        Selecciona una semana
      </option>
      {weeks.map((week) => (
        <option key={week.id_week} value={week.id_week}>
          Semana {week.week_number} ({formatDate(week.init_date)} - {formatDate(week.end_date)})
        </option>
      ))}
    </select>
  );
}