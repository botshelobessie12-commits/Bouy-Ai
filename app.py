import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="ItsYourBouy AI", page_icon="🔥")
st.title("ItsYourBouy Botshelo AI")
st.write("It Helps With Everything - Kimberley")

if "chat" not in st.session_state:
    st.session_state.chat = []

q = st.text_input("Ask me anything:")

if st.button("Ask") and q:
    st.session_state.chat.append(("You", q))
    
    # Ask free AI
    prompt = urllib.parse.quote(f"You are ItsYourBouy Botshelo AI from Kimberley, friendly and helpful, like a cool homie. Answer this: {q}")
    try:
        r = requests.get(f"https://text.pollinations.ai/{prompt}", timeout=30)
        ans = r.text
    except:
        # fallback if internet slow
        if "+" in q or "-" in q or "*" in q or "/" in q:
            try:
                ans = f"Yo Bouy! {q} = {eval(q)} 🔥"
            except:
                ans = "My brain is loading Bouy, ask me again!"
        else:
            ans = f"Yo Bouy! You said '{q}' - I'm your AI from Kimberley and I got you! Ask me anything - maths, school, business, life."

    st.session_state.chat.append(("Bouy AI", ans))

# Show chat
for who, msg in reversed(st.session_state.chat):
    if who == "You":
        st.write(f"**{who}:** {msg}")
    else:
        st.success(f"**{who}:** {msg}")
