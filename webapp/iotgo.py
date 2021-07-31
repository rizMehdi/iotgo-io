#new updateSun Aug  1 00:12:21 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide")
#streamlit.components.v1.html(html, width=None, height=None, scrolling=False)
urlis=""
# embed streamlit docs in a streamlit app
st.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo.png",width=250)
st.header("My cards are:")

col1,  col3, col4, col5, col6 ,emptycol3,emptycol2,emptycol1 = st.beta_columns(8)

with col1:
    st.write("Mission:")
    st.image("", width=200)
with col3:
    st.write("Persona:")
    st.image("", width=175)
with col4:
    st.write("Thing:")
    st.image("", width=175)
with col5:
    st.write("Input:")
    st.image("", width=175)
with col6:
    st.write("Output:")
    st.image("", width=175)
with emptycol1:
    st.button("refresh (r)")
st.header("My code is:")
components.iframe(urlis,width=900, height=700)#, scrolling=False)
link ="[Click here to edit/download this code.]()"
st.markdown(link, unsafe_allow_html=True)
