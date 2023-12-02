import streamlit as st
import dbconnect as db

st.set_page_config(
    page_title="Contact Us",
    page_icon="🏨"
)

st.title("Contact Us")
name = st.text_input("Your Name")
email = st.text_input("Your Email")
subject = st.text_input("Subject")
message = st.text_area("Message")
if st.button("Submit"):
    if name and email and subject and message:
        sql = "INSERT INTO contact (name, email, subject, message) VALUES (%s, %s, %s, %s)"
        val = (name, email, subject, message)
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        st.success("Message sent successfully!")
    else:
        st.error("Please fill in all fields.")