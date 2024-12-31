# Asistente Virtual

Asistente virtual desarrollado en Python que utiliza reconocimiento de voz y síntesis de voz para interactuar con el usuario. Puede realizar diversas tareas como buscar en Wikipedia, reproducir música en YouTube, informar el día y la hora, contar chistes, abrir sitios web, y mucho más.

## Características
- **Reconocimiento de voz:** Escucha comandos hablados del usuario.
- **Síntesis de voz:** Responde en voz alta utilizando un motor de texto a voz.
- **Integración con servicios populares:** 
  - Reproducción de videos en YouTube.
  - Búsquedas en Google y Wikipedia.
  - Obtención de precios de acciones mediante Yahoo Finance.
- **Soporte multilingüe:** Configuración para español e inglés.
- **Funciones de utilidad:** Contar chistes, informar la fecha y hora, abrir aplicaciones web, entre otras.

## Requisitos
- Python
- Paquetes requeridos (instalables con `pip`):
  - `pyttsx3`
  - `speechrecognition`
  - `pywhatkit`
  - `yfinance`
  - `pyjokes`
  - `wikipedia`

## Uso
Ejecuta el script y habla cuando se te indique. Algunos comandos soportados son:
- "Abrir YouTube"
- "Qué día es hoy"
- "Busca en Wikipedia [tema]"
- "Reproduce [nombre de canción]"

## Personalización
Puedes ajustar la voz del asistente modificando las opciones de configuración en el código (id1 para español y id2 para inglés). También puedes añadir comandos personalizados editando la función `pedir_cosas()`.

### Para cambiar el idioma o la voz:
1. Abre el archivo `asistente.py`.
2. Localiza la sección de configuración de voz, donde se definen los IDs para español e inglés (id1 y id2).
3. Modifica el ID según el idioma o la voz que prefieras.
