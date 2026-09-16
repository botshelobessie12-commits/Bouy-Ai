import streamlit as st, requests, urllib.parse
from PIL import Image

logo = Image.open("logo.png")
st.set_page_config(page_title="Bouy AI", page_icon=logo)
st.image("logo_full.png", width=280)
st.write("It Helps With Everything - Kimberley, built by Botshelo 🔥")

if "chat" not in st.session_state:
    st.session_state.chat = []

q = st.text_input("Ask me anything:")

if st.button("Ask 🔥") and q:
    st.session_state.chat.append(("You", q))
    prompt = urllib.parse.quote(f"You are ItsYourBouy AI from Kimberley, friendly, helpful, cool. Answer: {q}")
    try:
        r = requests.get(f"https://text.pollinations.ai/{prompt}", timeout=30)
        ans = r.text
    except:
        ans = "Yo Bouy! My signal slow, ask me again dawg!"
    st.session_state.chat.append(("Bouy AI", ans))

for who, msg in reversed(st.session_state.chat):
    if who == "You":
        st.write(f"**{who}:** {msg}")
    else:
        st.success(f"**{who}:** {msg}")
