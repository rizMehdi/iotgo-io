                #this file was updated on Sun Nov 14 22:15:20 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide",initial_sidebar_state="expanded")
urlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Aradio.setGroup%281%29%0Alet%20recieved%20%3D%200%0Amusic.setVolume%28255%29%0Aradio.setGroup%281%29%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28recieved%20%3D%3D%201%29%7B%0A%20%20%20%20%20%20%20%20music.stopMelody%28MelodyStopOptions.All%29%0A%09basic.pause%281000%29%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20music.startMelody%28music.builtInMelody%28Melodies.Birthday%29%2C%20MelodyOptions.Forever%29%0A%09basic.pause%281000%29%0A%20%20%20%20%7D%0A%20%20%20%20if%20%28pins.digitalReadPin%28DigitalPin.P2%29%20%3E%3D%201%29%7B%0A%20%20%20%20%20%20%20%20radio.sendValue%28%22movementPresent%22%2C1%29%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20basic.pause%281000%29%0A%20%20%20%20%7D%0A%7D%29%0Aradio.onReceivedValue%28function%20%28name%2C%20value%29%20%7B%0A%09if%20%28name%20%3D%3D%20%22replace_me%22%20%26%26%20value%20%3D%3D%201%29%20%7B%0A%09%09recieved%20%3D%201%0A%09%7D%0A%7D%29%0A%0A%60%60%60%0A%0A"
cardWidth=130
pluscardwidht=130
missionCardWidth=160
vertiPaddingWidth=35


st.markdown(
        """
        <style type="text/css">
        iframe{
        top: 0;
        left: 0;
        width: 100%;
        max-width: 1200px;
        min-width: 900px;
        }
        </style>
        """,
          unsafe_allow_html=True,
)

st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                width: 400px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 400px;
                margin-left: -400px;
        }
        </style>
        """,
        unsafe_allow_html=True,
)


st.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo-hor.png",width=380)
input_col, plus_col, output_col, empty= st.sidebar.columns([1,1,1,1])
with input_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" se...")
	# ("Input1:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-recieveData.png", width=cardWidth)
	# ("Input2:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-inputPhy-MovementPresent.png", width=cardWidth)
with plus_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht) 
with output_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" allora...")
	# ("Output1:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-outputPhy-TurnOffMusic.png", width=cardWidth)
	# ("Output2:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-sendData.png", width=cardWidth) 

st.subheader("")
st.subheader("")
st.subheader("")
st.markdown(
        """
        <style> .font{
        font-size:50px;}
        </style>
        """,
        unsafe_allow_html=True,
        )
st.code('''radio.setGroup(1)
let recieved = 0
music.setVolume(255)
radio.setGroup(1)
basic.forever(function () {
    if (recieved == 1){
        music.stopMelody(MelodyStopOptions.All)
	basic.pause(1000)
    } else {
        music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Forever)
	basic.pause(1000)
    }
    if (pins.digitalReadPin(DigitalPin.P2) >= 1){
        radio.sendValue("movementPresent",1)
    } else {
        basic.pause(1000)
    }
})
radio.onReceivedValue(function (name, value) {
	if (name == "replace_me" && value == 1) {
		recieved = 1
	}
})
''',language="javascript")


e,edit  = st.columns([1,1])
with edit:
        #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=60)
        st.markdown("[Modifica...]("+urlis+")", unsafe_allow_html=True)

#e,edit  = st.columns([1,1])
#with edit:
#        #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=60)
#        st.markdown("[Modifica...]("+urlis+")", unsafe_allow_html=True)


st.subheader("")
components.iframe(urlis, height=1000, scrolling=True)    



#st.button("Refresh")
