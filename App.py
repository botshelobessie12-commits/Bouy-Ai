import streamlit as st

st.set_page_config(page_title="ItsYourBouy Botshelo AI")
st.title("ItsYourBouy Botshelo AI 🤖")
st.write("It Helps With Everything 🔥 - Kimberley")

q = st.text_input("Ask me anything:")
if st.button("Ask"):
    if q:
        st.success("ItsYourBouy AI says:")
        st.write(f"Yo Bouy! You asked '{q}'. Here's the plan: 1) Break it into 3 steps 2) Do first step today with your phone 3) Post on WhatsApp to make money. Tell me more about '{q}' and I write it for you.")
    else:
        st.warning("Type something first!")

st.caption("Built by ItsYourBouy Botshelo")
