import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks



st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("Welcome to the Legendary Board of Pages")
st.write('')
st.write('')
st.write("#### Hint: the file is app/src/pages/98_Legendary_UX_Design_HQ.py")
st.write("### Throw a new button down here to access a new page you've built")


if st.button("Paulo's home page design", 
             type='primary',
             use_container_width=True):
  st.switch_page("pages/97_Paulo_Homepage.py")

if st.button('Replace these with links to pages like above', 
             type='secondary',
             use_container_width=True):
  st.balloons()

if st.button('Replaceee these with links to pages like above', 
             type='primary',
             use_container_width=True):
  st.balloons()

if st.button('Replacee these with links to pages like above', 
             type='secondary',
             use_container_width=True):
  st.balloons()