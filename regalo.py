import streamlit as st
from streamlit_extras.let_it_rain import rain

# Configuración inicial
st.set_page_config(page_title="Solo para ti pequitas", page_icon="❤️")

st.title("¡Hola, mi amor! ❤️")
st.write("Cada línea de este código está pensada en ti.")

# Definimos la función de los corazones
def lanzar_corazones():
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=5,
        animation_length="5s",
    )

# Botón interactivo
if st.button("Haz clic para ver cuánto te amo"):
    lanzar_corazones()
    st.success("¡Eres lo más lindo que me ha pasado y amo todo de ti!")

# Un detalle extra: Una dedicatoria
with st.chat_message("user"):
    st.write("Pd: Estoy aprendiendo Python y lo primero que quize hacer es demostrarte cuanto te amo. ✨")
