#this file was updated on Mon Oct 18 15:48:54 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide")
urlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Amusic.setVolume%28255%29%0Alet%20strip%20%3D%20neopixel.create%28DigitalPin.P1%2C7%2CNeoPixelMode.RGB%29%0Abasic.pause%281000%29%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28pins.digitalReadPin%28DigitalPin.P0%29%20%3E%3D%201%29%7B%0A%20%20%20%20%20%20%20%20music.startMelody%28music.builtInMelody%28Melodies.Birthday%29%2C%20MelodyOptions.Forever%29%0A%20basic.pause%281000%29%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20music.stopMelody%28MelodyStopOptions.All%29%0Abasic.pause%281000%29%0A%0A%0A%20%20%20%20%7D%0A%20%20%20%20if%20%28input.lightLevel%28%29%20%3C%20127%29%7B%0A%20%20%20%20%20%20%20%20strip.showRainbow%281%2C%20360%29%0Astrip.show%28%29%0A%20basic.pause%281000%29%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20strip.showColor%28neopixel.colors%28NeoPixelColors.Black%29%29%0Abasic.pause%281000%29%0A%0A%0A%20%20%20%20%7D%0A%7D%29%0A%60%60%60%0A%0A%60%60%60package%0Aneopixel%3Dgithub%3Amicrosoft%2Fpxt-neopixel%0A%0A%60%60%60"

cardWidth=130
pluscardwidht=130
missionCardWidth=160
vertiPaddingWidth=35

#st.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo3.png",width=200)


# st.markdown("""""")

#hide_full_screen = '''
#<style>
#.element-container:nth-child(3) .overlayBtn {visibility: hidden;}
#.element-container:nth-child(12) .overlayBtn {visibility: hidden;}
#</style>
#'''
#st.markdown(hide_full_screen, unsafe_allow_html=True) 

#ROW-1---------------------------------------------------------------------------
applogo, null1,edit  = st.columns([4,6,1])

#applogo,edit  = st.beta_columns(3,5)

with applogo:
    st.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo-hor.png",width=350)
with edit:
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=60)
    st.markdown("[Modifica]("+urlis+")", unsafe_allow_html=True)
    
#ROW-2---------------------------------------------------------------------------
input_col, plus_col, output_col,emp0, code_col, emp1,emp2, emp3,emp4 ,emp5 ,emp6  = st.columns(11)

with input_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
    st.write("se...")
    # ("Input1:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-inputPhy-MovementPresent.png", width=cardWidth)
    # ("Input2:")
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-inputPhy-LightlevelLow.png", width=cardWidth)
    # ("Input3:")
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-noInput.png", width=cardWidth)

with plus_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)    

with output_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
    st.write("allora...")
    # ("Output1:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-outputPhy-PlayHappyMusic.png", width=cardWidth)
    # ("Output2:")
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-outputPhy-TurnRainbowLight.png", width=cardWidth)
    # ("Output3:")
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-noOutput.png", width=cardWidth)
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)

with code_col:
    # st.header("Il mio codice è:")
    #components.iframe(urlis, scrolling=True)
    components.iframe(urlis,width=3000, height=1000, scrolling=True)


 
#ROW-3---------------------------------------------------------------------------
st.button("Refresh")
