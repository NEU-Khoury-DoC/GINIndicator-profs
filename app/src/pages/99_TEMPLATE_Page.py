"""




ATTENTION 
# NOTE - If you are directly editing this template page (rather than 
# working out of a new copy of the page) then you are messing up our repo. 
# Please create a duplicate page (you can simply copy and paste files in 
# VSCode sidebar) and then rename the file that should be called 99_TEMPLATE_Page copy.py
# Thank you thank you thank youuuuu sincerely Sean



"""

import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks



st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"WELCOME TO THIS TEMPLATE PAGE.")
st.write('')
st.write('')
st.write('### Edit this perhaps')

if st.button('Secret Button', 
             type='primary',
             use_container_width=True):
  st.balloons

if st.button('Another Secret Button', 
             type='secondary',
             use_container_width=True):
  st.balloons