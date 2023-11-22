import streamlit as st
import mysql.connector
from passlib.hash import bcrypt

# Function to check if the entered login credentials are valid
def check_user(username, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysqlroot",
        database="cms"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.verify(password, user[3]):
        return True
    else:
        return False

# Streamlit UI with basic CSS for login
def login():
    # Initialize session state
    if 'user_authenticated' not in st.session_state:
        st.session_state.user_authenticated = False

    st.set_page_config(page_title="Login Page", page_icon="🔒")
    st.title("Login Page")
    st.markdown('<link rel="stylesheet" href="styles.css">', unsafe_allow_html=True)

    # Check if the user is already authenticated
    if st.session_state.user_authenticated:
        st.success("You are already logged in.")
        return

    # Login
    st.header("Login")
    login_username = st.text_input("Username:")
    login_password = st.text_input("Password:", type="password")
    if st.button("Login"):
        if check_user(login_username, login_password):
            st.session_state.user_authenticated = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    login()
