import streamlit as st
import requests
import urllib.parse
from PIL import Image

# --- LOGO ---
try:
    logo = Image.open("logo.png")
    st.set_page_config(page_title="Bouy AI", page_icon=logo)
except:
    st.set_page_config(page_title="Bouy AI", page_icon="🔥")

# Show logos if they exist
try:
    st.image("logo_full.png", width=300)
except:
    try:
        st.image("logo.png", width=150)
    except:
        pass

st.title("ItsYourBouy Botshelo AI")
st.write("It Helps With Everything - Kimberley 🔥")

# --- AI CHAT ---
if "chat" not in st.session_state:
    st.session_state.chat = []

q = st.text_input("Ask me anything, Bouy:")

if st.button("Ask 🔥") and q:
    st.session_state.chat.append(("You", q))
    
    prompt = urllib.parse.quote(f"You are ItsYourBouy AI, a cool helpful AI from Kimberley, South Africa, made by Botshelo. Answer friendly: {q}")
    try:
        r = requests.get(f"https://text.pollinations.ai/{prompt}", timeout=30)
        ans = r.text
    except:
        ans = "Eish, signal is slow Bouy, ask me again!"

    st.session_state.chat.append(("Bouy AI", ans))

for who, msg in reversed(st.session_state.chat):
    if who == "You":
        st.write(f"**{who}:** {msg}")
    else:
        st.success(f"**{who}:** {msg}")
