import streamlit as st

st.header("Contact Me!..")
# st.write("[Please contact me](anulsasidharan@gmail.com)")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print("I was pressed")