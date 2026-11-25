## Convierte Markdown proporcionado sin cuenta

Envía el Markdown completo, hasta **128 KiB** (131.072 bytes UTF-8). El resultado es un archivo base64 integrado de hasta **2 MiB** (2.097.152 bytes); el cliente debe guardar o adjuntar esos bytes. Su URI no es una descarga alojada ni un enlace permanente. La conversión pública no lee archivos ni proyectos privados y nunca obtiene URLs o imágenes remotas.

Los presupuestos actuales son **3 conversiones por minuto y dirección de red**, **20 por día UTC y dirección**, y **80 por día UTC compartidas entre usuarios públicos**. Un límite separado de 20 solicitudes MCP POST por 60 segundos también incluye el descubrimiento. Son tamaños máximos y presupuestos de capacidad: la conversión puede fallar por debajo de ellos. Ante una denegación de capacidad, espera; no repitas automáticamente una denegación o un resultado incierto, no acortes el texto ni afirmes que se creó un archivo.
