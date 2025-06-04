##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks
# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(page_title="Consensus Login", layout="wide")



# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False
# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)
logger.info("Loading the Home page of the app")

# title
st.markdown("<h1 style='font-size: 72px; text-align: center;'>Consensus</h1>", unsafe_allow_html=True)


st.markdown("---")
st.markdown("### Who would you like to log in as?")

# Login Buttons in three columns
b1, b2, b3 = st.columns(3)

with b1:
    if st.button("Log in as Voter,\nPrince Maximilian", use_container_width=True):
        st.session_state["role"] = "Voter"
        st.session_state["first_name"] = "Prince Maximilian"
        st.success("Logged in as Voter")

with b2:
    if st.button("Log in as Politician,\nJT Nance", use_container_width=True):
        st.session_state["role"] = "Politician"
        st.session_state["first_name"] = "JT Nance"
        st.success("Logged in as Politician")

with b3:
    if st.button("Log in as Economist,\nEmeka Okonkwo", use_container_width=True):
        st.session_state["role"] = "Economist"
        st.session_state["first_name"] = "Emeka Okonkwo"
        st.success("Logged in as Economist")