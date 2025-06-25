import streamlit as st
import base64
import os
from PIL import Image

# --- Configuración de la página ---
st.set_page_config(
    page_title="Portafolio | Fabrizio Ramírez Luy",
    page_icon="📝",
    layout="wide"
)

# --- Función para fondo personalizado ---
def set_background(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data).decode()
        page_bg_img = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        st.warning(f"❗ Imagen de fondo no encontrada: {image_file}")

# --- Llamar a la función con la imagen de fondo ---
# --- Encabezado ---
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Sebastián Fabrizio Ramírez Luy</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Estudiante de Periodismo | Creador de contenido | Editor de videos</h4>", unsafe_allow_html=True)
# --- Fotos de presentación ---
st.markdown("### ")
st.markdown("#### 🖼️ Presentación visual")

fotos_presentacion = ["pictures/foto1.jpeg", "pictures/foto2.jpeg", "pictures/foto3.jpeg", "pictures/foto4.jpeg"]

cols = st.columns(4)
for i in range(4):
    if os.path.exists(fotos_presentacion[i]):
        image = Image.open(fotos_presentacion[i])
        cols[i].image(image, use_column_width=True)
    else:
        cols[i].info(f"Falta {fotos_presentacion[i]}")
fotos_presentacion = [
    "pictures/foto1.jpeg",
    "pictures/foto2.jpeg.",
    "pictures/foto3.jpeg.",
    "pictures/foto4.jpeg."
]
# --- Sección: Acerca de mí ---
st.header("🙋‍♂️ Acerca de mí")
st.write("""
Soy un estudiante de Periodismo en busca de oportunidades para aplicar mi creatividad y responsabilidad en el ámbito laboral. Me apasiona crear contenido audiovisual, comunicar ideas con impacto y aprender constantemente para aportar a cada proyecto con entusiasmo.
""")

# --- Contacto ---
st.markdown("📧 sebasfabri683@icloud.com | 📱 960 678 325 | 📍 Lima, Perú")

# --- Sección: Experiencia Profesional ---
st.header("💼 Experiencia Profesional")
st.subheader("Auxiliar de creación de contenido - Net Axxes SAC (2023 - 2024)")
st.write("""
- Producción de videos orgánicos y con IA para promover productos.
- Edición y postproducción con enfoque en marketing digital.
""")
st.subheader("Voluntariado Educativo - Empodérate PE (Ago 2024 - Oct 2024)")
st.write("""
- Facilitación de talleres educativos sobre ciudadanía, ODS y empoderamiento.
- Producción de contenido digital para redes sociales del proyecto.
""")
st.subheader("Voluntariado - Kuska Risunchis (Ago 2024)")
st.write("""
- Registro y documentación de un encuentro nacional sobre educaciones alternativas.
""")

# --- Educación ---
st.header("🎓 Educación")
st.write("**Pontificia Universidad Católica del Perú** – Periodismo (2022 - actualidad)")
st.write("**ICPNA** – Inglés Intermedio (2022)")
st.write("**Colegio José María Arguedas** – Primer puesto de la promoción (2020)")

# --- Habilidades ---
st.header("🛠️ Habilidades y Conocimientos")
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

# --- Galería de trabajos ---
st.header("📸 Galería de trabajos")
ruta_imagenes = "imagenes"
if os.path.exists(ruta_imagenes):
    imagenes = [img for img in os.listdir(ruta_imagenes) if img.endswith(("jpg", "png"))]
    for i in range(0, len(imagenes), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(imagenes):
                image = Image.open(os.path.join(ruta_imagenes, imagenes[i + j]))
                cols[j].image(image, use_column_width=True)
else:
    st.info("Sube tus fotos en la carpeta 'imagenes/' para que aparezcan aquí.")

# --- Pie de página ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>© 2025 Sebastián Fabrizio Ramírez Luy</p>", unsafe_allow_html=True)
