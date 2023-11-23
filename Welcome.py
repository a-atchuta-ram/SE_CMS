import streamlit as st

st.set_page_config(
    page_title="Welcome page",
    page_icon="👋",
)

# Cricket-themed colors
cricket_background_color = "#C5E1A5"  # Light green
cricket_text_color = "#263238"  # Dark blue

# Welcome message with HTML formatting
st.markdown(
    f"""
    <div style="background-color: {cricket_background_color}; padding: 20px; border-radius: 10px;">
        <h1 style="color: {cricket_text_color}; text-align: center;">Welcome to Cricket Management System! 👋</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.success("Select an option above.")

# Introduction text with HTML formatting
st.markdown(
    f"""
    <div style="background-color: {cricket_background_color}; padding: 20px; border-radius: 10px; margin-top: 20px;">
        <p style="color: {cricket_text_color}; font-size: 16px; line-height: 1.5;">
            The Cricket Management System (CMS) is a web-based software designed to consolidate cricket statistics.
            Targeted at broadcasters, journalists, and enthusiasts, the CMS ensures quick access to accurate data,
            enhancing live coverage and personal inquiries. Its primary aim is to simplify the retrieval and presentation
            of both national and international cricket data, offering a one-stop solution for all cricket-related
            statistical needs. Our corporate goal with the CMS is to provide a reliable and user-friendly platform
            that stands as a benchmark in the world of cricket data management.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
