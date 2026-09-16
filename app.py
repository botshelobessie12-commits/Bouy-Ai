import streamlit as st
st.title("ItsYourBouy Botshelo AI")
st.write("It Helps With Everything - Kimberley")
q=st.text_input("Ask me anything:")
if st.button("Ask"):
 st.write(f"Yo! You asked {q}. I got you!")
