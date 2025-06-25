import streamlit as st
import base64
import os
from PIL import Image

# --- Configuración de la página ---
st.set_page_config(
    page_title="Portafolio | Fabrizio Ramirez Luy",
    page_icon="📝",
    layout="wide"
)

# --- Fondo azul claro ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f8ff;
    }
    </style>
""", unsafe_allow_html=True)

# --- Encabezado ---
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Sebastian Fabrizio Ramirez Luy</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Estudiante de Periodismo | Creador de contenido | Editor de videos</h4>", unsafe_allow_html=True)
# --- Fotos de presentación (fila de 4) ---
fotos_presentacion = [
    "pictures/foto1.jpeg",
    "pictures/foto2.jpeg",
    "pictures/foto3.jpeg",
    "pictures/foto4.jpeg"
]

st.markdown("### ")
cols = st.columns(4)
for i in range(4):
    if os.path.exists(fotos_presentacion[i]):
        image = Image.open(fotos_presentacion[i])
        cols[i].image(image, use_container_width=True)
    else:
        cols[i].info(f"Falta {fotos_presentacion[i]}")

# --- PESTAÑAS PRINCIPALES ---
tab1, tab2, tab3 = st.tabs(["📄 Información", "📸 Fotos", "🎬 Videos"])

# --- TAB 1: INFORMACIÓN PERSONAL ---
with tab1:
    st.header("Acerca de mí")
    st.write("""
    Soy un estudiante de Periodismo en busca de oportunidades para aplicar mi creatividad y responsabilidad en el ámbito laboral. Me apasiona crear contenido audiovisual, comunicar ideas con impacto y aprender constantemente para aportar a cada proyecto con entusiasmo.
    """)

    st.subheader("📧 Contacto")
    st.markdown("Correo: sebasfabri683@icloud.com  \nTeléfono: 960 678 325  \nUbicación: Lima, Perú")

    st.subheader("💼 Experiencia Profesional")
    st.write("""
    - Auxiliar de creación de contenido - Net Axxes SAC (2023 - 2024)
        - Producción de videos orgánicos y con IA para promover productos.
        - Edición y postproducción con enfoque en marketing digital.
    
    - Voluntariado Educativo - Empodérate PE (Ago 2024 - Oct 2024)
        - Facilitación de talleres educativos sobre ciudadanía, ODS y empoderamiento.
        - Producción de contenido digital para redes sociales del proyecto.
    
    - Voluntariado - Kuska Risunchis (Ago 2024)
        - Registro y documentación de un encuentro nacional sobre educaciones alternativas.
    """)

    st.subheader("🎓 Educación")
    st.write("""
    - Pontificia Universidad Católica del Perú – Periodismo (2022 - actualidad)
    - ICPNA – Inglés Intermedio (2022)
    - Colegio José María Arguedas – Primer puesto de la promoción (2020)
    """)

    st.subheader("🛠️ Habilidades y Conocimientos")
    col1, col2 = st.columns(2)
    with col1:
        st.write("- Resolución de problemas")
        st.write("- Comunicación asertiva")
        st.write("- Pensamiento creativo")
        st.write("- Adaptabilidad")
        st.write("- Trabajo en equipo")
    with col2:
        st.write("- Edición de video (CapCut avanzado)")
        st.write("- Diseño gráfico (Canva, Photoshop básico, Lightroom)")
        st.write("- Word, PowerPoint (avanzado), Excel (básico)")
        st.write("- Creación de contenido para redes sociales")

# --- TAB 2: GALERÍA DE FOTOS ---
with tab2:
    st.header("📸 Galería de trabajos")
    ruta_imagenes = "imagenes"
    if os.path.exists(ruta_imagenes):
        imagenes = [img for img in os.listdir(ruta_imagenes) if img.lower().endswith(("jpg", "jpeg", "png"))]
        if imagenes:
            for i in range(0, len(imagenes), 3):
                cols = st.columns(3)
                for j in range(3):
                    if i + j < len(imagenes):
                        image_path = os.path.join(ruta_imagenes, imagenes[i + j])
                        image = Image.open(image_path)
                        nombre = os.path.splitext(imagenes[i + j])[0]
                        titulo = nombre.replace("_", " ").title()
                        cols[j].image(image, use_container_width=True, caption=titulo)
        else:
            st.info("No hay imágenes en la carpeta 'imagenes/'.")
    else:
        st.warning("La carpeta 'imagenes/' no existe en tu repositorio.")
# --- TAB 3: VIDEOS ---
with tab3:
    st.header("🎬 Mis videos")
    st.subheader("Videos")
    video_path = "videos/2024.mov"
    if os.path.exists(video_path):
        with open(video_path, "rb") as f:
            st.video(f.read())
    else:
        st.info("Sube un archivo .mp4 a la carpeta 'videos/' para que aparezca aquí.")

# --- Pie de página ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>© 2025 Sebastián Fabrizio Ramírez Luy</p>", unsafe_allow_html=True)
