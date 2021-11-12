                #this file was updated on Fri Nov 12 04:32:01 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide",initial_sidebar_state="expanded")
urlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Abasic.pause%281000%29%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28input.temperature%28%29%20%3C%2028%29%7B%0A%20%20%20%20%20%20%20%20basic.showIcon%28IconNames.Sad%29%20%0A%20basic.pause%281000%29%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20basic.clearScreen%28%29%0Abasic.pause%281000%29%0A%0A%0A%20%20%20%20%7D%0A%20%20%20%20if%20%28pins.digitalReadPin%28DigitalPin.P0%29%20%3D%3D%200%29%7B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%7D%0A%7D%29%0A%60%60%60%0A%0A"

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


st.sidebar.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo-hor.png",width=380)
input_col, plus_col, output_col, empty= st.sidebar.columns([1,1,1,1])
with input_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" se...")
	# ("Input1:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-inputPhy-TemperatureLow.png", width=cardWidth)
	# ("Input2:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-inputPhy-MovementNotPresent.png", width=cardWidth)
with plus_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht) 
with output_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" allora...")
	# ("Output1:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-outputPhy-ShowSadIcon.png", width=cardWidth)
	# ("Output2:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-noOutput.png", width=cardWidth) 


st.subheader("")
components.iframe(urlis, height=1000, scrolling=True)    

e,edit  = st.columns([3,1])
with edit:
        #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=60)
        st.markdown("[Modifica questa codice]("+urlis+")", unsafe_allow_html=True)

#st.button("Refresh")
