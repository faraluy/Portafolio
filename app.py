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
