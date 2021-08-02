#this file was updated on Mon Aug  2 18:27:42 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide")
urlis="https://makecode.microbit.org/--docs?md=Not%20Enough%20cards%20to%20generate%20code"

cardWidth=90
pluscardwidht=90
missionCardWidth=120
vertiPaddingWidth=25

# st.markdown("""""")
applogo, empty1, empty2, mission, persona, empty3, thing, empty4,empty5  = st.beta_columns(9)

with applogo:
    st.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo3.png",width=250)
with mission:
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-mission-8.png", width=missionCardWidth)
with persona:
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-persona-7.png", width=cardWidth)
with thing:
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-thing-art-7.png", width=cardWidth)

input_col, plus_col, output_col,  code_col, emptycol , emptycol2 , emptycol3, emptycol4,emptycol5,emptycol6 = st.beta_columns(10)


with input_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
    st.write("when...")
    # ("Input1:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-inputCloud-ForecastWindLow.png", width=cardWidth)
    # ("Input2:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/noInput.png", width=cardWidth)
    # ("Input3:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/noInput.png", width=cardWidth)

with plus_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)    
with output_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
    st.write("then...")
    # ("Output1:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-outputPhy-TurnOffLight.png", width=cardWidth)
    # ("Output2:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/noOutput.png", width=cardWidth)
    # ("Output3:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/noOutput.png", width=cardWidth)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)


with code_col:
    # st.header("My code is:")
    components.iframe(urlis,width=900, height=1500, scrolling=True)

with emptycol5:
    st.button("Refresh")
with emptycol6:
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=32)
    st.markdown("[Edit]("+urlis+")", unsafe_allow_html=True)
