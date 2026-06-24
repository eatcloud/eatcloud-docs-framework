# Development Guide - EatCloud Dashboards

## Entorno Local (Desarrollo)
Para desplegar visualizaciones o dashboards localmente:
1. Navega a la carpeta que contiene el archivo HTML generado.
2. Inicia un servidor local en el puerto 8080:
   `python3 -m http.server 8080`
3. Puedes exponer el servidor local a internet temporalmente usando Cloudflare Tunnels (para revisiones en vivo).

## Despliegue en Hugging Face Spaces (Producción)
Los dashboards consolidados deben desplegarse en Hugging Face Spaces.
**Reglas obligatorias de despliegue:**
1. **Configuración de Docker (Nginx):** El contenedor debe escuchar OBLIGATORIAMENTE en el puerto `7860`.
   - Modifica `default.conf` de Nginx o el `Dockerfile` para redirigir el puerto 80 al 7860. Si no se hace, el Space se quedará en estado "Starting" indefinidamente.
2. **SDK del Space:** Para dashboards que son archivos estáticos (HTML/JS/CSS), se debe configurar el SDK como `docker` en el archivo `README.md` del Space (evitar conflictos con Gradio/Streamlit).
