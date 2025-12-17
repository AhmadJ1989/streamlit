import streamlit as st
from pathlib import Path
from components.cards import info_card
import base64

# ------------------------
# Pfad zum Projekt & Bild
# ------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = BASE_DIR / "assets" / "Gemini_Generated_Image_cwuxo6cwuxo6cwux.png"

# ------------------------
# Titel
# ------------------------
st.title("👤 Profile")

# ------------------------
# Spalten
# ------------------------
col1, col2 = st.columns([1, 2])

# ------------------------
# Funktion für Base64
# ------------------------
def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ------------------------
# Linke Spalte: Bild
# ------------------------
with col1:
    if IMAGE_PATH.exists():
        img_base64 = image_to_base64(IMAGE_PATH)
        st.markdown(
            f"""
            <div class="profile-image-frame">
                <img src="data:image/png;base64,{img_base64}">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Profile image not found")

# ------------------------
# Rechte Spalte: Infos
# ------------------------
with col2:
    info_card("Name", "AI Consultant")
    info_card("Role", "Data Scientist")
    info_card("Skills", "Python, ML, MLOps")


