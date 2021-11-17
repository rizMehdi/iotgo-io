                #this file was updated on Wed Nov 17 09:40:40 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide",initial_sidebar_state="expanded")
urlis=""
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
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-inputPhy-buttonPress.png", width=cardWidth) 
with plus_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht) 
with output_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" allora...")
	# ("Output1:")
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-outputPhy-RotateMax.png", width=cardWidth)

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
st.code('''servos.P1.setRange(0,180)
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)){
        servos.P1.setAngle(180)
	basic.pause(1000)
    } else {
        servos.P1.setAngle(0)
	basic.pause(1000)
    }
})''',language="javascript")


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
