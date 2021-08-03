#this file was updated on Mon Aug  2 18:29:11 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide")
urlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Aradio.setGroup%28313%29%0Aradio.onReceivedValue%28function%20%28name%2C%20value%29%20%7B%0A%20forecastName%20%3D%20name%0AforecastValue%20%3D%20value%0A%7D%29%0Alet%20forecastValue%20%3D%200%0Alet%20forecastName%20%3D%20%22none%22%20%0Abasic.pause%281000%29%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28forecastName%20%3D%3D%20%22wind%22%20%26%26%20forecastValue%20%3C%200.5%29%7B%0A%20%20%20%20%20%20%20%20basic.showString%28%22Ciao%20from%20Bari%22%29%0A%20%20%20%20%20%20%20%20basic.pause%28100%29%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20radio.sendString%28%22get_wind%22%29%0Abasic.pause%282000%29%0A%0A%20%20%20%20%7D%0A%20%20%20%20if%20%28forecastName%20%3D%3D%20%22wind%22%20%26%26%20forecastValue%20%3C%200.5%29%7B%0A%20%20%20%20%20%20%20%20pins.digitalWritePin%28DigitalPin.P1%2C0%29%0A%20%20%20%20%20%20%20%20basic.pause%28100%29%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20radio.sendString%28%22get_wind%22%29%0Abasic.pause%282000%29%0A%0A%20%20%20%20%7D%0A%7D%29%0A%60%60%60%0A%0A"

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

input_col, plus_col, output_col,  code_col, editbutton, emptycol , emptycol  , emptycol,emptycol,emptycol, emptycol = st.beta_columns(11)


with input_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
    st.write("when...")
    # ("Input1:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-inputCloud-ForecastWindLow.png", width=cardWidth)
    # ("Input2:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-inputCloud-ForecastWindLow.png", width=cardWidth)
    # ("Input3:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-inputCloud-ForecastWindLow.png", width=cardWidth)

with plus_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)    
with output_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
    st.write("then...")
    # ("Output1:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-outputPhy-ShowText.png", width=cardWidth)
    # ("Output2:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-outputPhy-TurnOffLight.png", width=cardWidth)
    # ("Output3:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-outputPhy-ShowText.png", width=cardWidth)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)


with code_col:
    # st.header("My code is:")
    components.iframe(urlis,width=900, height=1500, scrolling=True)

with emptycol5:
    st.button("Refresh")
with editbutton:
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=32)
    st.markdown("[Edit]("+urlis+")", unsafe_allow_html=True)
