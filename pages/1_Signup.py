import streamlit as st
import mysql.connector
from passlib.hash import bcrypt

# Function to add a new user to the database
def add_user(username, email, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysqlroot",
        database="cms"
    )
    cursor = conn.cursor()
    hashed_password = bcrypt.hash(password)

    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
    conn.commit()
    conn.close()

# Streamlit UI with basic CSS for signup
def signup():
    st.set_page_config(page_title="Signup Page", page_icon="📝")
    st.title("Signup Page")
    st.markdown('<link rel="stylesheet" href="styles.css">', unsafe_allow_html=True)

    # Signup
    st.header("Signup")
    signup_username = st.text_input("Create Username:")
    signup_email = st.text_input("Enter Email:")
    signup_password = st.text_input("Create Password:", type="password")
    if st.button("Signup"):
        add_user(signup_username, signup_email, signup_password)
        st.success("Signup successful! You can now go to the login page.")

if __name__ == "__main__":
    signup()
