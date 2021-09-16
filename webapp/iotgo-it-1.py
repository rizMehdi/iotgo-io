#this file was updated on Thu Sep 16 14:11:40 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide")
urlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Abasic.pause%281000%29%0Aradio.setGroup%28313%29%0Aradio.onReceivedValue%28function%20%28name%2C%20value%29%20%7B%0A%20forecastName%20%3D%20name%0AforecastValue%20%3D%20value%0A%7D%29%0Alet%20forecastValue%20%3D%200%0Alet%20forecastName%20%3D%20%22none%22%20%0Amusic.setVolume%28127%29%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28input.isGesture%28Gesture.Shake%29%29%7B%0A%20%20%20%20%20%20%20%20basic.showIcon%28IconNames.Happy%29%0A%20%20%20%20%20%20%20%20basic.pause%28100%29%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20basic.clearScreen%28%29%0Abasic.pause%28100%29%0A%0A%0A%20%20%20%20%7D%0A%20%20%20%20if%20%28input.temperature%28%29%20%3E%3D%2028%29%7B%0A%20%20%20%20%20%20%20%20pins.digitalWritePin%28DigitalPin.P1%2C1%29%0A%20%20%20%20%20%20%20%20basic.pause%28100%29%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20pins.digitalWritePin%28DigitalPin.P1%2C0%29%0Abasic.pause%28100%29%0A%0A%0A%20%20%20%20%7D%0A%20%20%20%20if%20%28forecastName%20%3D%3D%20%22day%22%20%26%26%20forecastValue%20%3E%3D%206%29%7B%0A%20%20%20%20%20%20%20%20music.startMelody%28music.builtInMelody%28Melodies.Birthday%29%2C%20MelodyOptions.Forever%29%0A%20%20%20%20%20%20%20%20basic.pause%28100%29%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20radio.sendString%28%22get_day%22%29%0Abasic.pause%282000%29%0A%0A%20%20%20%20%7D%0A%7D%29%0A%60%60%60%0A%0A"

cardWidth=100
pluscardwidht=100
missionCardWidth=160
vertiPaddingWidth=35

# st.markdown("""""")
applogo, empty1, empty2, mission,empty3, persona, thing, empty4,edit  = st.columns(9)

with applogo:
    st.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo3.png",width=300)
with mission:
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-noMission.png", width=missionCardWidth)
with persona:
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-noPersona.png", width=cardWidth)
with thing:
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-noThing.png", width=cardWidth)
with edit:
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=60)
    st.markdown("[Edit]("+urlis+")", unsafe_allow_html=True)

input_col, plus_col, output_col,  code_col, emptycol , emptycol , emptycol, emptycol,emptycol,emptycol,emptycol = st.beta_columns(11)

with input_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
    st.write("if...")
    # ("Input1:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-inputPhy-GestureShake.png", width=cardWidth)
    # ("Input2:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-inputPhy-TemperatureHigh.png", width=cardWidth)
    # ("Input3:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-inputCloud-TodayWeekend.png", width=cardWidth)

with plus_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)    

with output_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
    st.write("then...")
    # ("Output1:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-outputPhy-ShowHappyIcon.png", width=cardWidth)
    # ("Output2:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-outputPhy-TurnOnFan.png", width=cardWidth)
    # ("Output3:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/EN-outputPhy-PlayHappyMusic.png", width=cardWidth)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)

with code_col:
    # st.header("My code is:")
    components.iframe(urlis,width=900, height=1500, scrolling=True)

st.button("Refresh")
