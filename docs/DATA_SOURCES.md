# Catálogo de fuentes potenciales | Potential data sources

**These sources are candidates for future evaluation. They have not been downloaded, harmonized or validated by the ANDES-RISK AI prototype.**

| Fuente | Tipo de datos | Sitio oficial | Consideraciones |
|---|---|---|---|
| NASA GPM IMERG | Precipitación estimada por satélite | https://gpm.nasa.gov/data/imerg | Resolución, latencia, acceso, versión del producto y incertidumbre dependen del dataset. Estimaciones satelitales no equivalen a estaciones locales. |
| NASA Global Landslide Catalog | Inventario de eventos reportados | https://data.nasa.gov/dataset/global-landslide-catalog-export | Cobertura histórica y sesgo de reportes; no es inventario exhaustivo de eventos en Bolivia. |
| NASA LHASA | Investigación de amenazas por deslizamientos | https://github.com/nasa/lhasa | Referencia científica para comparación, no prueba de que el prototipo implementa LHASA. |
| USGS EarthExplorer | Fuentes de elevación y observación terrestre | https://earthexplorer.usgs.gov/ | Elegir producto, resolución, coordenadas, restricciones y licencia. |

## Dataset acceptance checklist

- [ ] URL oficial y nombre del producto, versión y fecha de consulta registrados.
- [ ] Licencia, atribución y restricciones de redistribución comprobadas.
- [ ] Rango temporal, sistema de coordenadas, resolución y área de cobertura documentados.
- [ ] Unidades, valores faltantes, duplicados y anomalías inspeccionados.
- [ ] Definición de evento documentada; etiquetas verificadas y limitaciones explicitadas.
- [ ] Uniones espaciales/temporales revisadas por fugas de datos.
- [ ] Datos de entrenamiento y de evaluación separados antes de ajustar transformaciones.
- [ ] Script reproducible y checksum documentados cuando los términos lo permitan.
- [ ] Revisión independiente de seguridad y pertinencia antes de divulgar mapas de riesgo.

## Formato de entrada de la versión experimental

El prototipo actual acepta un CSV que contiene:

`date,site_id,rainfall_24h_mm,rainfall_7d_mm,slope_deg,landslide_observed`

Sus ejemplos son **sintéticos**. Antes de usar datos observacionales debe existir un procedimiento de etiquetado real, enlaces de procedencia, unidades y permisos verificables.

No cargues aquí datos personales ni documentos de acceso restringido.
