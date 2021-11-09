#this file was updated on Mon Oct 18 15:48:54 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide",initial_sidebar_state="expanded")
urlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Amusic.setVolume%28255%29%0Alet%20strip%20%3D%20neopixel.create%28DigitalPin.P1%2C7%2CNeoPixelMode.RGB%29%0Abasic.pause%281000%29%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28pins.digitalReadPin%28DigitalPin.P0%29%20%3E%3D%201%29%7B%0A%20%20%20%20%20%20%20%20music.startMelody%28music.builtInMelody%28Melodies.Birthday%29%2C%20MelodyOptions.Forever%29%0A%20basic.pause%281000%29%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20music.stopMelody%28MelodyStopOptions.All%29%0Abasic.pause%281000%29%0A%0A%0A%20%20%20%20%7D%0A%20%20%20%20if%20%28input.lightLevel%28%29%20%3C%20127%29%7B%0A%20%20%20%20%20%20%20%20strip.showRainbow%281%2C%20360%29%0Astrip.show%28%29%0A%20basic.pause%281000%29%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20strip.showColor%28neopixel.colors%28NeoPixelColors.Black%29%29%0Abasic.pause%281000%29%0A%0A%0A%20%20%20%20%7D%0A%7D%29%0A%60%60%60%0A%0A%60%60%60package%0Aneopixel%3Dgithub%3Amicrosoft%2Fpxt-neopixel%0A%0A%60%60%60"

cardWidth=130
pluscardwidht=130
missionCardWidth=160
vertiPaddingWidth=35


html = """
  <style>
    .reportview-container {
      flex-direction: row-reverse;
    }

    header > .toolbar {
      flex-direction: row-reverse;
      left: 1rem;
      right: auto;
    }

    .sidebar .sidebar-collapse-control,
    .sidebar.--collapsed .sidebar-collapse-control {
      left: auto;
      right: 0.5rem;
    }

    .sidebar .sidebar-content {
      transition: margin-right .3s, box-shadow .3s;
    }

    .sidebar.--collapsed .sidebar-content {
      margin-left: auto;
      margin-right: -21rem;
    }

    @media (max-width: 991.98px) {
      .sidebar .sidebar-content {
        margin-left: auto;
      }
    }
  </style>
"""
st.markdown(html, unsafe_allow_html=True)

st.title("New Sidebar")
st.sidebar.text("I'm here now.")



# st.markdown("""""")

#hide_full_screen = '''
#<style>
#.element-container:nth-child(3) .overlayBtn {visibility: hidden;}
#.element-container:nth-child(12) .overlayBtn {visibility: hidden;}
#</style>
#'''
#st.markdown(hide_full_screen, unsafe_allow_html=True) 

#ROW-1---------------------------------------------------------------------------
#code,e,edit  = st.columns([9,2,1])

#applogo,edit  = st.beta_columns(3,5)

#with code:
components.iframe(urlis, height=1000, scrolling=True)    
st.markdown("[Modifica questa codice]("+urlis+")", unsafe_allow_html=True)

#with edit:
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=60)
    #st.markdown("[Modifica]("+urlis+")", unsafe_allow_html=True)
    
#ROW-2--------------------------------------------------------------------------- 


 
#ROW-3---------------------------------------------------------------------------
#st.button("Refresh")
