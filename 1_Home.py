import streamlit as st



st.set_page_config(
    page_title="HomePage",
    page_icon="🏨"
)

st.write("# 🏨 Hotel Management System")
st.write("""### Welcome to HMS Portal. You can manage your hotels and your guests from right here. <br> 
1. Head over to **Add Hotel** page to register new hotels to your database.
2. Head over to **Add Guest** page to add guests to your database.
3. Head over to **Book Hotel** page to book hotels for the added guests in the database.
""", unsafe_allow_html=True)
