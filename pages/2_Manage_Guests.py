import dbconnect as db
import streamlit as st


st.set_page_config(
    page_title="Manage Guests",
    page_icon="🏨"
)


st.title("Manage Guests")


tab_add, tab_list, tab_del = st.tabs(["ADD GUEST", "LIST ALL GUESTS", "DELETE GUEST"])

with tab_add:
    with st.form("addGuest"):
        gno = st.number_input("Enter Guest Number (GNo)", step=1)
        gname = st.text_input("Enter Full Name")
        address = st.text_area(label="Enter Permanent Address")
        phone = st.number_input("Enter Phone Number", step=1)
        submit = st.form_submit_button("Add Guest")

    if gno and gname and address and phone and submit:
        sql = "INSERT INTO guest (Gno, Gname, Address, Phone) VALUES (%s, %s, %s, %s)"
        val = (gno, gname, address, phone)
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        st.success("Guest details added successfully!")
    else:
        st.warning("Please fill in all fields.")


def listAllGuests():
    db.mycursor.execute("select * from guest")
    res = db.mycursor.fetchall()
    for i in res:
        st.dataframe([
            {"Gno": i[0], "Full Name" : i[1], "Address" : i[2], "Phone No." : i[3]}
        ],use_container_width=True)


with tab_del:
    with st.form("delGuest"):
        del_gno = st.text_input('Enter the Guest number to delete')
        submit = st.form_submit_button("Delete Guest")
    if del_gno and submit:
        sql = 'DELETE FROM guest WHERE `guest`.`Gno` = %s'
        val = (del_gno,)
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        st.success("Guest deleted successfully!")
    else:
        st.warning("Please fill in all fields.")

with tab_list:
    listAllGuests()

st.write("____")