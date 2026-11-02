# Catálogo de fuentes potenciales | Potential data sources

**These sources are candidates for future evaluation. They have not been downloaded, harmonized or validated by the ANDES-RISK AI prototype.**

| Fuente | Tipo de datos | Sitio oficial | Consideraciones |
|---|---|---|---|
| NASA GPM IMERG | Precipitación estimada por satélite | https://gpm.nasa.gov/data/imerg | Resolución, latencia, acceso, versión del producto y incertidumbre dependen del dataset. Estimaciones satelitales no equivalen a estaciones locales. |
| NASA Global Landslide Catalog | Inventario de eventos reportados | https://data.nasa.gov/dataset/global-landslide-catalog-export | La exportación puntual llega al 7 de marzo de 2016, según su ficha. La ausencia de un reporte no prueba que no ocurrió un evento; no es inventario exhaustivo de Bolivia. |
| NASA LHASA | Investigación de amenazas por deslizamientos | https://github.com/nasa/lhasa | Referencia científica para comparación, no prueba de que el prototipo implementa LHASA. |
| USGS SRTM / EarthExplorer | Modelo digital de elevación | https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm-void | Seleccionar versión y resolución concretas; documentar vacíos, interpolación, datum y método de cálculo de pendiente. Acceso mediante https://earthexplorer.usgs.gov/. |
| SENAMHI Bolivia | Datos y estaciones hidrometeorológicas | https://onsc.senamhi.gob.bo/public/public-stations-info-export | Verificar disponibilidad por estación y periodo, calidad, permisos y condiciones de uso antes de adquirir o redistribuir datos. |

### Notas para la evaluación de cada fuente

Consulta de las fichas oficiales: **2 de noviembre de 2026**. Esta fecha identifica la revisión documental; no es una fecha de descarga de datos.

- **IMERG:** NASA ofrece productos Early, Late y Final, con diferentes procesamientos y latencias. Para investigación NASA recomienda evaluar el uso de [Final Run](https://gpm.nasa.gov/resources/faq/what-are-differences-between-imerg-early-late-and-final-runs-and-which-should-be-used). Registrar versión, producto, unidades, intervalo de agregación y resolución; contrastar cuando sea posible con observaciones locales. La [documentación técnica de V07](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation) describe sus campos de media hora sobre una cuadrícula de 0,1°.
- **Global Landslide Catalog:** la [ficha de NASA](https://data.nasa.gov/dataset/global-landslide-catalog-export) describe eventos informados por medios, bases de desastres e informes científicos y señala que la exportación es una captura puntual, no el catálogo mantenido posteriormente. La ficha no especifica una licencia y remite a términos y citas requeridos: deben revisarse antes de cualquier uso o redistribución. Evaluar sesgos de reporte e incertidumbre de ubicación y fecha.
- **SRTM:** la [descripción de USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm-void) diferencia SRTM Void Filled de cobertura global a 3 segundos de arco de SRTM 1 Arc-Second Global. La pendiente calculada depende de la resolución y del procesamiento; los vacíos pueden haberse rellenado con interpolación u otras fuentes.
- **SENAMHI:** su [portal de información de estaciones](https://onsc.senamhi.gob.bo/public/public-stations-info-export) permite seleccionar variables y periodos. Esto no confirma disponibilidad, calidad ni permiso de redistribución de una serie concreta. Consultar también los procedimientos de [solicitud de datos](https://prueba.senamhi.gob.bo/contacto) y conservar las condiciones aplicables a cada adquisición.

### Manifiesto mínimo propuesto por conjunto

Registrar identificador y versión del producto, entidad y URL oficial, fecha de adquisición, cobertura temporal y espacial, CRS, resolución, unidades, licencia o condiciones y atribución, método de acceso, checksum cuando sea posible, tratamiento de valores faltantes y limitaciones conocidas. Registrar además cada transformación, versión del código y parámetros. Un valor desconocido debe marcarse como pendiente; no inferir permisos de la sola disponibilidad de una página.

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

