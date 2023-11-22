import streamlit as st

# Function to clear user session or authentication tokens
def logout():
    # Clear the user authentication status
    st.session_state.user_authenticated = False

# Streamlit UI for logout
def main():
    # Initialize session state
    if 'user_authenticated' not in st.session_state:
        st.session_state.user_authenticated = False

    st.set_page_config(page_title="Logout Page", page_icon="🔓")
    st.title("Logout Page")

    # Check if the user is already logged out
    if not st.session_state.user_authenticated:
        st.warning("You are already logged out.")
        return

    st.info("Are you sure you want to log out?")
    
    if st.button("Logout"):
        logout()
        st.success("Logout successful!")
        # You can redirect the user to the login page or another page if needed

if __name__ == "__main__":
    main()
