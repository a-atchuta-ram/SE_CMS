# import streamlit as st
# from bs4 import BeautifulSoup
# import urllib.request
# import re

# @st.cache_data
# def get_live_scores():
#     score_page = 'http://static.cricinfo.com/rss/livescores.xml'
#     page = urllib.request.urlopen(score_page)
#     soup = BeautifulSoup(page, 'html.parser')
#     result = soup.find_all('description')
#     return [match.get_text() for match in result]

# def main():
#     st.title("Live Cricket Scores")

#     # Display live scores
#     matches = get_live_scores()
#     st.text("Current Live Scores:")
#     for match in matches:
#         # Extract teams and scores using regular expressions
#         teams_and_scores = re.findall(r'([a-zA-Z\s]+)\s?(\d+/\d+\s\*?)?', match)

#         # Filter out empty tuples and those with no scores
#         teams_and_scores = [(team.strip(), score.strip()) for team, score in teams_and_scores if team and score]

#         # Display the result if there is a score
#         if teams_and_scores:
#             st.text(match)

#     # Button to refresh scores
#     if st.button("Refresh Scores"):
#         st.text("Scores refreshed!")

# if __name__ == "__main__":
#     main()
import streamlit as st
from bs4 import BeautifulSoup
import urllib.request
import re

@st.cache_data
def get_live_scores():
    score_page = 'http://static.cricinfo.com/rss/livescores.xml'
    page = urllib.request.urlopen(score_page)
    soup = BeautifulSoup(page, 'html.parser')
    result = soup.find_all('title')  # Use 'title' instead of 'description'
    return [match.get_text() for match in result]

def main():
    st.title("Live Cricket Scores")

    # Display live scores
    matches = get_live_scores()
    st.text("Current Live Scores:")
    for match in matches:
        # Extract teams and scores using regular expressions
        teams_and_scores = re.findall(r'([a-zA-Z\s]+)\s?(\d+/\d+\s\*?)?', match)

        # Filter out empty tuples and those with no scores
        teams_and_scores = [(team.strip(), score.strip()) for team, score in teams_and_scores if team and score]

        # Display the result if there is a score
        if teams_and_scores:
            st.text(match)

    # Button to refresh scores
    if st.button("Refresh Scores"):
        st.text("Scores refreshed!")

if __name__ == "__main__":
    main()
