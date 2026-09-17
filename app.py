import streamlit as st
from PIL import Image
import os

logo_path = "logo.png" if os.path.exists("logo.png") else None

try:
    icon = Image.open(logo_path) if logo_path else "🔥"
except:
    icon = "🔥"

st.set_page_config(page_title="BOUY AI", page_icon=icon, layout="centered")

if logo_path:
    st.image(logo_path, width=130)

st.markdown("# BOUY AI")
st.markdown("ItsYourBouy AI - It Helps With Everything | Kimberley, SA 🔥")

q = st.text_input("Ask Bouy AI anything:")
if st.button("Ask 🔥"):
    if q:
        st.success(f"Bouy AI: You asked '{q}' - I got you!")
    else:
        st.warning("Type something!")

st.markdown("---")
st.caption("Built by ItsYourBouy | Kimberley")
