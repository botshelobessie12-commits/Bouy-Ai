
import streamlit as st

st.set_page_config(page_title="ItsYourBouy AI", page_icon="🔥")
st.title("ItsYourBouy Botshelo AI")
st.write("It Helps With Everything - Kimberley")

q = st.text_input("Ask me anything:")

if st.button("Ask"):
    if not q:
        st.write("Type something Bouy!")
    else:
        q_low = q.lower()
        try:
            # If it's math like 1+1, calculate it
            if any(c in q for c in "+-*/()"):
                ans = eval(q)
                st.success(f"Yo Bouy! {q} = {ans} 🔥")
            elif "hello" in q_low or "hi" in q_low:
                st.success("Hey Bouy! What's good? I'm your AI from Kimberley, ready to help!")
            elif "who are you" in q_low:
                st.success("I am ItsYourBouy — Botshelo's AI. Built in Kimberley to help with everything!")
            else:
                st.success(f"You asked: '{q}'\n\nI'm Bouy AI! I got you. For now I do math perfect, and chat. Tell me more about '{q}' and I'll help you out, my dawg!")
        except:
            st.success(f"You asked: {q}. Answer is 2 if you asked 1+1! I'm learning Bouy, ask me again!")
