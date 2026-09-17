import streamlit as st, requests, urllib.parse
from PIL import Image

st.set_page_config(page_title="Bouy AI", page_icon="🔥")

# Try to load logo with whatever name you have
logo_found = False
for name in ["logo.png", "logo.jpg", "IMG-20260917-WA7650.jpg", "IMG-20260917-WA7650.jpeg"]:
    try:
        logo = Image.open(name)
        st.image(logo, width=200)
        logo_found = True
        break
    except:
        pass

st.title("BOUY AI")
st.caption("ItsYourBouy AI - It Helps With Everything | Kimberley, SA 🔥")

if "chat" not in st.session_state:
    st.session_state.chat = []

q = st.text_input("Ask Bouy AI anything:")
if st.button("Ask 🔥") and q:
    st.session_state.chat.append(("You", q))
    prompt = urllib.parse.quote(f"You are Bouy AI, made by Botshelo from Kimberley, cool, helpful, like ItsYourBouy. Answer in friendly style: {q}")
    try:
        r = requests.get(f"https://text.pollinations.ai/{prompt}", timeout=30)
        ans = r.text
    except:
        ans = "Eish network slow Bouy, try again!"
    st.session_state.chat.append(("Bouy AI", ans))

for who, msg in reversed(st.session_state.chat):
    if who == "You":
        st.write(f"**{who}:** {msg}")
    else:
        st.success(f"**{who}:** {msg}")
