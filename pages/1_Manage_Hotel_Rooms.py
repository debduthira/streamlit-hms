import dbconnect as db
import streamlit as st


st.set_page_config(
    page_title="Manage Hotel",
    page_icon="🏨"
)


st.title("Manage Hotels")


tab_add, tab_list, tab_del = st.tabs(["ADD HOTEL ROOM", "LIST ALL HOTEL ROOMS", "DELETE HOTEL ROOM"])

with tab_add:
    with st.form("addHotel"):
        hno = st.number_input("Enter Hotel Number (HNo)", step=1)
        hname = st.text_input("Enter Hotel Name")
        city = st.selectbox(label="Select City of Hotel", options=[
            "Kolkata",
            "Delhi",
            "Mumbai",
            "Bangalore",
            "Chennai"
        ])
        phone = st.number_input("Enter Phone Number of Hotel", step=1)
        rno = st.number_input("Enter Room Number(Rno)", step=1)
        roomType = st.selectbox(label="Select Room Type", options=[
            "Single Bed Non A/C (max. 3PAX)",
            "Double Bed Non A/C (max. 6PAX)",
            "Single Bed A/C (max. 3PAX)",
            "Double Bed A/C (max. 6PAX)"
        ])
        price = st.number_input("Enter Price of Hotel")
        submit = st.form_submit_button("Add Hotel")

    if hno and hname and city and phone and rno and roomType and price and submit:
        sql = "INSERT INTO hotel (Hno, Hname, city, phone, Rno, Room_type, Price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (hno, hname, city, phone, rno, roomType, price)
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        st.success("Hotel details added successfully!")
    else:
        st.warning("Please fill in all fields.")


def listAllHotels():
    db.mycursor.execute("select * from hotel")
    res = db.mycursor.fetchall()
    for i in res:
        st.dataframe([
            {"Hno": i[0], "Hotel Name" : i[1], "City" : i[2], "Phone No." : i[3],"Rno" : i[4] , "Room Type" : i[5], "Price" : "₹" "{:.2f}".format(i[7])}
        ],use_container_width=True)
# def delHotel():
#     db.mycursor.execute("select * from hotel where Rno = 1")
#     res = db.mycursor.fetchall()
#     for i in res:
#         st.dataframe([
#             {"Hno": i[0], "Hotel Name" : i[1], "City" : i[2], "Phone No." : i[3],"Rno" : i[4] , "Room Type" : i[5], "Price" : "₹" "{:.2f}".format(i[7])}
#         ],use_container_width=True)



with tab_del:
    # delHotel()

    with st.form("delHotel"):
        del_hno = st.text_input('Enter the Hotel number to delete')
        del_rno = st.text_input('Enter the Room number to delete')
        submit = st.form_submit_button("Delete Hotel")
    if del_hno and del_rno and submit:
        sql = 'DELETE FROM hotel WHERE Hno=%s AND Rno=%s'
        val = (del_hno, del_rno)
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        st.success("Hotel deleted successfully!")
    else:
        st.warning("Please fill in all fields.")

with tab_list:
    listAllHotels()

st.write("____")