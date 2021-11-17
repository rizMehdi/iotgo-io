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
                width: 200px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 200px;
                margin-left: -200px;
        }
        </style>
        """,
        unsafe_allow_html=True,
)


input_name= ["noInput"  ,"noInput"  ,"noInput"]
output_name=["noOutput" ,"noOutput" ,"noOutput"]


input1 = st.sidebar.selectbox(
	'your first input and output are:',
	("buttonNotPress","buttonPress","accelLow" , "accelHigh"  , "compassE"  , 
         "compassW"  , "compassN"  , "compassS"  , "gestureShake"  , "gestureTilt"  ,
         "movementPresent"  ,"movementNotPresent"  , "noiseLow"  , "noiseHigh"  ,"sliderLow"  ,
         "sliderHigh"  , "tempLow"  ,"tempHigh"  ,"lightlevelLow","lightlevelHigh",
        "touchYes" ,"touchNo"  ,"noInput"))

output1 = st.sidebar.selectbox(
	'&',
	("iconHappy","iconSad","iconNone","lightOn","lightOff","lightOff",
         "musicHappy" ,"musicSad"  ,"musicNone"  ,"displayText"  ,"displayInput"  ,
         "displayNone"  ,"showStripRainbow"  ,"showStripBlack","fanOn"  ,
         "fanOff"  , "rotateMax"  , "noOutput",))
st.sidebar.subheader("")
input2 = st.sidebar.selectbox(
	'your second input and output are:', 
	("buttonNotPress","buttonPress","accelLow" , "accelHigh"  , "compassE"  , 
         "compassW"  , "compassN"  , "compassS"  , "gestureShake"  , "gestureTilt"  ,
         "movementPresent"  ,"movementNotPresent"  , "noiseLow"  , "noiseHigh"  ,"sliderLow"  ,
         "sliderHigh"  , "tempLow"  ,"tempHigh"  ,"lightlevelLow","lightlevelHigh",
        "touchYes" ,"touchNo"  ,"noInput","recieveData"))
output2 = st.sidebar.selectbox(
	'& ',
	("iconHappy","iconSad","iconNone","lightOn","lightOff","lightOff",
         "musicHappy" ,"musicSad"  ,"musicNone"  ,"displayText"  ,"displayInput"  ,
         "displayNone"  ,"showStripRainbow"  ,"showStripBlack","fanOn"  ,
         "fanOff"  , "rotateMax"  , "noOutput", "sendData",))	


st.sidebar.write('You selected:', input1,output1,input2,output2)





input_name[0]= input1 
input_name[1]= input2 
output_name[0]=output1
output_name[1]=output2



langPrefix=['EN','IT','DE','UR']
lang=1


baseURL="https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/"


grabURL =    {
    "pictoral":     "-thing-art-1.png",
    "sculpture":    "-thing-art-2.png",
    "decor":        "-thing-art-3.png",    
    "model":        "-thing-art-4.png",
    "ceramic":      "-thing-art-5.png",
    "textile":      "-thing-art-6.png" ,   
    "jewellery":    "-thing-art-7.png",
    "book":         "-thing-art-8.png",
    "informative":  "-thing-art-9.png",    
    "thing_blank":        "-thing-art-0.png",
    
    "engagePeople":     "-mission-1.png",
    "makePeopleUnderstand":"-mission-2.png",
    "inspirePeople":    "-mission-3.png",    
    "addUtility":       "-mission-4.png",
    "addDimension":     "-mission-5.png",
    "connectEmotionally":"-mission-6.png",    
    "connectMemories":  "-mission-7.png",
    "getToKnowPeople":  "-mission-8.png",
    "mission_blank":    "-mission-0.png",  
    "91":               "-mission-91.png",    
    "92":               "-mission-92.png",
    "93":               "-mission-93.png",
    "94":               "-mission-94.png",    

    "myself":           "-persona-1.png",
    "elderly":          "-persona-2.png",
    "teenager":         "-persona-3.png",
    "child":            "-persona-4.png",
    "minority":         "-persona-5.png",
    "physciallyChallenged":"-persona-6.png",
    "immigrant":        "-persona-7.png",
    "pet":              "-persona-8.png",
    "anyone":           "-persona-9.png",
    "persona_blank":            "-persona-0.png",
    "new_user":         "-control-1.png",
    "new_idea":         "-control-2.png",
  	
    "noMission"     :   "-noMission.png",  
    "noThing"       :   "-noThing.png",  
    "noPersona"     :   "-noPersona.png",  
    "noInput"       :   "-noInput.png",  
    "noOutput"      :   "-noOutput.png",
    "none"          :   "",
    "blankCard"     :   "blankcard.png",
    "blank"     :   "blankcard.png",

    "codeCard"      :   "-codecard.png",
    "playerCard"    :   "-playercard.png",#not used in app

    
    "buttonNotPress":   "-inputPhy-buttonNotpressed.png",
    "buttonPress":      "-inputPhy-buttonPress.png",
    "accelLow":         "-inputPhy-AccelerationLow.png",
    "accelHigh" :       "-inputPhy-AccelerationHigh.png",
    "compassN" :        "-inputPhy-CompassNorth.png",
    "compassE" :        "-inputPhy-CompassEast.png",
    "compassS" :        "-inputPhy-CompassSouth.png",
    "compassW" :        "-inputPhy-CompassWest.png",
    "gestureShake":     "-inputPhy-GestureShake.png",
    "gestureTilt" :     "-inputPhy-GestureTilt.png",
    "movementNotPresent":"-inputPhy-MovementNotPresent.png",
    "movementPresent" : "-inputPhy-MovementPresent.png",
    "noiseLow"  :       "-inputPhy-NoiseLow.png",
    "noiseHigh"	:       "-inputPhy-NoiseHigh.png",
    "touchYes" 	:       "-inputPhy-LogoTouched.png",
    "touchNo"	:       "-inputPhy-LogoNotTouched.png",
    "sliderLow":        "-inputPhy-SliderMinimum.png",
    "sliderMid":        "-inputPhy-SliderMaximum.png",#not used. 
    "sliderHigh":       "-inputPhy-SliderMaximum.png",
    "tempLow"  :        "-inputPhy-TemperatureLow.png",
    "tempHigh" :        "-inputPhy-TemperatureHigh.png",
    "lightlevelLow" :   "-inputPhy-LightlevelLow.png",
    "lightlevelHigh":   "-inputPhy-LightlevelHigh.png",
    
        
    "forecastTempHigh" :    "-inputCloud-ForecastTempreatureHigh.png",
    "forecastTempLow" :     "-inputCloud-ForecastTempreatureLow.png",
    "forecastHumidityHigh" :"-inputCloud-ForecastHumidityHigh.png",
    "forecastHumidityLow" : "-inputCloud-ForecastHumidityLow.png",
    "forecastWindHigh" :    "-inputCloud-ForecastWindHigh.png",
    "forecastWindLow" :     "-inputCloud-ForecastWindLow.png",
    "forecastprecipHigh" :  "-inputCloud-ForecastPercipitationHigh.png",
    "forecastprecipLow" :   "-inputCloud-ForecastPercipitationLow.png",
    "todayStartOfMonth" :   "-inputCloud-TodayMonthStart.png",
    "todayWeekday" :        "-inputCloud-TodayWeekday.png",
    "todayWeekend":         "-inputCloud-TodayWeekend.png",
    "todaySummerMonth":     "-inputCloud-TodaySummerMonth.png",
    "todayNewYear":         "-inputCloud-TodayNewYearDay.png",
    "timeForSchool" :       "-inputCloud-TimeForSchool.png",     
    
    
    "iconHappy":    "-outputPhy-ShowHappyIcon.png",
    "iconSad":      "-outputPhy-ShowSadIcon.png",
     "iconNone":    "-outputPhy-StopShowIcon.png",
    "lightOn":      "-outputPhy-TurnOnLight.png",
    "lightOff":     "-outputPhy-TurnOffLight.png",
    "musicHappy":   "-outputPhy-PlayHappyMusic.png",
    "musicSad" :    "-outputPhy-PlaySadMusic.png",
    "musicNone" :   "-outputPhy-TurnOffMusic.png", 
    "displayText" : "-outputPhy-ShowText.png",  
    "displayInput": "-outputPhy-ShowInputValue.png",
    "displayNone" : "-outputPhy-StopShowText.png", 
    "showStripRainbow" :"-outputPhy-TurnRainbowLight.png",
    "showStripBlack" :"-outputPhy-TurnOffRainbowLight.png",
    "fanOn" :       "-outputPhy-TurnOnFan.png",	 
    "fanOff"  :     "-outputPhy-TurnOffFan.png",
    "rotateMin":    "-outputPhy-RotateMin.png", 
    "rotateMid":    "-outputPhy-RotateMax.png",#not used. 
    "rotateMax":    "-outputPhy-RotateMax.png",
    
    "tweetText"  :  "-outputCloud-TweetText.png", 
    "tweetInput" :  "-outputCloud-TweetValue.png",   
    "logInput"   :  "-outputCloud-LogValue.png", #fixed

    "sendData":"-sendData.png",
    "recieveData":"-recieveData.png",
    

    
}




input0path=  baseURL+langPrefix[lang]+grabURL[ input_name[0]]
output0path= baseURL+langPrefix[lang]+grabURL[output_name[0]]
input1path=  baseURL+langPrefix[lang]+grabURL[ input_name[1]]
output1path= baseURL+langPrefix[lang]+grabURL[output_name[1]]
#input2path=  baseURL+langPrefix[lang]+grabURL[ input_name[2]]
#output2path= baseURL+langPrefix[lang]+grabURL[output_name[2]]
    
 


st.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo-hor.png",width=380)
input_col, plus_col, output_col, pad, code_col= st.columns([1,1,1,1,6])
with input_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" se...")
	# ("Input1:")
	st.image(input0path, width=cardWidth)
	# ("Input2:")
	st.image(input1path, width=cardWidth)
with plus_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht) 
with output_col:    
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" allora...")
	# ("Output1:")
	st.image(output0path, width=cardWidth)
	# ("Output2:")
	st.image(output1path, width=cardWidth) 

with code_col:
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
