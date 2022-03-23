#For PascoliBZ22
import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import time
import textwrap
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide",initial_sidebar_state="expanded")
cardWidth=130
pluscardwidht=130
missionCardWidth=160
vertiPaddingWidth=35
vertiPaddingWidthhalf=17
codetitle=""
codesubtitle=""
groupnum="0"
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
                width: 300px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 300px;
                margin-left: -300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
)

gamelevel=0
input_name= ["no Input"  ,"no Input"  ,"no Input"]
output_name=["no Output" ,"no Output" ,"no Output"]

input1 = st.sidebar.selectbox(
	'seleziona le tue carte di input e output',      
	( 'no Input'  , 
	 'Il pulsante premuto',
         'Il pulsante non è premuto',
         'L\'accelerazione è basso',
         'L\'accelerazione è alta',
         'La bussola punta ad Est'  ,
         'La bussola punta ad Ovest'  ,
         'La bussola punta a Nord',
         'La bussola punta a Sud'  ,
         'Il gesto è scuotere' ,
         'Il gesto è inclinare' ,
         'C\'è movimento nei dintorni' ,
         'Non c\'è movimento nei dintorni',
         'Il rumore è basso' ,
         'Il rumore è alto',
         'Il cursore è al minimo' ,
         'Il cursore è al massimo',
         'La temperatura è bassa',
         'La temperatura è alta',
         'L\'intensità di luce è bassa',
         'L\'intensità di luce è alta',
         'Il logo è toccato',
         'Il logo non è toccato',
                 ))


##	("buttonNotPress","buttonPress","accelLow" , "accelHigh"  , "compassE"  , 
##         "compassW"  , "compassN"  , "compassS"  , "gestureShake"  , "gestureTilt"  ,
##         "movementPresent"  ,"movementNotPresent"  , "noiseLow"  , "noiseHigh"  ,"sliderLow"  ,
##         "sliderHigh"  , "tempLow"  ,"tempHigh"  ,"lightlevelLow","lightlevelHigh",
##        "touchYes" ,"touchNo"  ,"noInput"))

output1 = st.sidebar.selectbox(
	'   &   ',
	(
	'no Output', 
        'Mostra un\'icona felice' ,
        'Mostra un\'icona triste' ,
        'Smette di mostrare un\'icona' ,
  	'Accende una luce' ,
 	'Spegne una luce' , 
  	'Suona una melodia triste'  , 
  	'Suona una melodia allegra'  , 
	'Smette di suonare'   , 
	'Mostra del testo'  , 
	'Mostra un numero'  , 
	'Smette di mostrare testi o numeri'  , 
	'Attiva un\'animazione luminosa'  , 
	'Spegne un\'animazione luminosa' , 	
	'Accende un ventilatore'  , 
	'Spegne un ventilatore'  ,
	'Fa ruotare il motore' 
         ))	
        

##	("iconHappy","iconSad","iconNone","lightOn","lightOff","lightOff",
##         "musicHappy" ,"musicSad"  ,"musicNone"  ,"displayText"  ,"displayInput"  ,
##         "displayNone"  ,"showStripRainbow"  ,"showStripBlack","fanOn"  ,
##         "fanOff"  , "rotateMax"  , "noOutput",))




#st.sidebar.write('You selected:', input1,output1,input2,output2)




it2en_in= {
    "Il pulsante premuto":"buttonPress",
    'Il pulsante non è premuto':"buttonNotPress",
    'L\'accelerazione è basso':"accelLow" , 
    'L\'accelerazione è alta':"accelHigh"  , 
    'La bussola punta ad Est':"compassE"  , 
    'La bussola punta ad Ovest':"compassW"  , 
    'La bussola punta a Nord':"compassN"  , 
    'La bussola punta a Sud':"compassS"  , 
    'Il gesto è scuotere':"gestureShake"  , 
    'Il gesto è inclinare':"gestureTilt"  , 
    'C\'è movimento nei dintorni':"movementPresent"  , 
    'Non c\'è movimento nei dintorni':"movementNotPresent"  , 
    'Il rumore è basso':"noiseLow"  , 
    'Il rumore è alto':"noiseHigh"  ,
    'Il cursore è al minimo':"sliderLow"  , 
    'Il cursore è al massimo':"sliderHigh"  , 
    'La temperatura è bassa':"tempLow"  , 
    'La temperatura è alta':"tempHigh"  ,
    'L\'intensità di luce è bassa':"lightlevelLow",
    'L\'intensità di luce è alta':"lightlevelHigh",
    'Il logo è toccato':"touchYes" ,#v2  
    'Il logo non è toccato':"touchNo"  , #v2    
    'no Input':"noInput",
    'recezione dati' :"recieveData",
    }
    
it2en_out= {
    'Mostra un\'icona felice':"iconHappy",
    'Mostra un\'icona triste':"iconSad",
    'Smette di mostrare un\'icona':"iconNone",
  	'Accende una luce':"lightOn",
 	'Spegne una luce':"lightOff", 
  	'Suona una melodia triste':"musicSad" , 
  	'Suona una melodia allegra':"musicHappy"  , 
	'Smette di suonare':"musicNone"  , 
	'Mostra del testo':"displayText"  , 
	'Mostra un numero':"displayInput"  , 
	'Smette di mostrare testi o numeri':"displayNone"  , 
	'Attiva un\'animazione luminosa':"showStripRainbow"  , 
	'Spegne un\'animazione luminosa':"showStripBlack", 
	'Accende un ventilatore':"fanOn"  , 
	'Spegne un ventilatore':"fanOff"  ,
	'Fa ruotare il motore':"rotateMin"  ,   
	'no Output':"noOutput",#<<<<<<<------- new  card.
        'invio dati' :"sendData",

    }


input_name[0]= it2en_in[input1]
output_name[0]=it2en_out[output1]



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
#input2path=  baseURL+langPrefix[lang]+grabURL[ input_name[2]]
#output2path= baseURL+langPrefix[lang]+grabURL[output_name[2]]
    
 


urlis=""
jscode=""


#defining a dictionary for any additional extension/package needed for each output: %60%60%60package%0Aservo%0A%60%60%60  wrong="%60%60%%0Aservo%0A%60%60%60"
package_suffix = {
	"rotateMin"         : "%60%60%60package%0Aservo%0A%60%60%60", 
	"rotateMid"         : "%60%60%60package%0Aservo%0A%60%60%60",
	"rotateMax"         : "%60%60%60package%0Aservo%0A%60%60%60",
	"showStripRainbow"  : "%60%60%60package%0Aneopixel%3Dgithub%3Amicrosoft%2Fpxt-neopixel%0A%0A%60%60%60", 
	"showStripBlack"    : "%60%60%60package%0Aneopixel%3Dgithub%3Amicrosoft%2Fpxt-neopixel%0A%0A%60%60%60", 
} #only where needed

 

on_end = {
  	"recieveData":   '\nradio.onReceivedValue(function (name, value) {\n\tif (name == "replace_me" && value == 1) {\n\t\trecieved = 1\n\t}\n})',
        }


#defining a dictionary for startup-code for each output:
on_start = {
  	"fanOn":   "basic.pause(1000)",
  	"lightOn": "basic.pause(1000)", 
  	"fanOff":   "basic.pause(1000)",
  	"lightOff": "basic.pause(1000)", 
  	"iconHappy":  "basic.pause(1000)", 
  	"iconSad":  "basic.pause(1000)", 
  	"iconNone":  "basic.pause(1000)", 
	"musicHappy": "music.setVolume(255)", 
	"musicSad":  "music.setVolume(255)",  
	"musicNone":  "music.setVolume(255)",   	
# 	"speakText": "",
# 	"speakInput": "",
# 	"speakNone": "",
  	"showStripRainbow": "let strip = neopixel.create(DigitalPin.P1,7,NeoPixelMode.RGB)", 
  	"showStripBlack": "let strip = neopixel.create(DigitalPin.P1,7,NeoPixelMode.RGB)", 
	"rotateMin":"servos.P1.setRange(0,180)", 
	"rotateMid":"servos.P1.setRange(0,180)", 
	"rotateMax":"servos.P1.setRange(0,180)", 
	"tweetText" : "radio.setGroup(313)\nradio.setTransmitSerialNumber(true)\nradio.sendValue(\"b#\", 8903)", 
	"tweetInput": "radio.setGroup(313)\nradio.setTransmitSerialNumber(true)\nradio.sendValue(\"b#\", 8903)", 
	"logInput"  : "radio.setGroup(313)\nradio.setTransmitSerialNumber(true)\nradio.sendValue(\"log4\", 8791)",  
	"forecastTempHigh":     "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"forecastTempLow":      "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"forecastHumidityHigh": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"forecastHumidityLow":  "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"forecastWindHigh":     "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"forecastWindLow":      "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"forecastprecipHigh":   "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"forecastprecipLow":    "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"todayStartOfMonth":    "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"todayWeekday":         "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"todayWeekend":         "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"todaySummerMonth":     "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"todayNewYear":         "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
	"timeForSchool":         "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
#	"timeSunrise":"radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
# 	"timeSunset": "radio.setGroup(313)\nradio.onReceivedValue(function (name, value) {\n forecastName = name\nforecastValue = value\n})\nlet forecastValue = 0\nlet forecastName = \"none\" ",
# 	"compassN" :"input.calibrateCompass()" , 
# 	"compassE" :"input.calibrateCompass()" , 
#   "compassS" :"input.calibrateCompass()" , 
#   "compassW" :"input.calibrateCompass()" ,
        "noInput": "basic.pause(1000)",#<<<<<<-----new added 17oct
        "noOutput": "basic.pause(1000)",#<<<<<<-----new added 17oct
        "sendData":"radio.setGroup(1)",# todo: set group automatically
        "recieveData":"radio.setGroup(1)\nlet recieved = 0",# todo: set group automatically, new added 11Nov
}
 

input_code = {
  	"buttonNotPress":"!input.buttonIsPressed(Button.A)",
 	"buttonPress":"input.buttonIsPressed(Button.A)",
  	"accelLow":"input.acceleration(Dimension.X) < 511" , 
  	"accelHigh":"input.acceleration(Dimension.X) >= 511"  , 
	"compassN" :"input.compassHeading() < 45" , 
	"compassE" :"input.compassHeading() >= 45 && input.compassHeading() < 135" , 
  	"compassS" :"input.compassHeading() >= 135 && input.compassHeading() < 225" , 
  	"compassW" :"input.compassHeading() >= 225 && input.compassHeading() < 315" , 
	"gestureShake":"input.isGesture(Gesture.Shake)"  , 
	"gestureTilt"  :"input.isGesture(Gesture.TiltLeft) || input.isGesture(Gesture.TiltRight)", 
	"movementNotPresent":"pins.digitalReadPin(DigitalPin.P2) == 0"  ,
	"movementPresent" :"pins.digitalReadPin(DigitalPin.P2) >= 1" , # >= 1000" ,
	"noiseLow"  :"input.soundLevel() < 128" , #v2
	"noiseHigh"	:"input.soundLevel() >= 128"  , #v2
 	"touchYes" 	:"input.logoIsPressed()" ,  #v2
 	"touchNo"	:"!input.logoIsPressed()"  , #v2
	"sliderLow":"pins.analogReadPin(AnalogPin.P2) <= 100"  , 
 	"sliderMid":"pins.analogReadPin(AnalogPin.P2) > 500 && pins.analogReadPin(AnalogPin.P2) <= 700",
	"sliderHigh":"pins.analogReadPin(AnalogPin.P2) >= 1000"  , 
	"tempLow"  :"input.temperature() < 28", 
	"tempHigh" :"input.temperature() >= 28" ,
	"lightlevelLow" :"input.lightLevel() < 127", 
	"lightlevelHigh":"input.lightLevel() >= 127",
	"forecastTempHigh" 		:"forecastName == \"temp\" && forecastValue >= 28",
	"forecastTempLow" 		:"forecastName == \"temp\" && forecastValue < 28",
# 	"forecastCloudsHigh" 		:"forecastName == \"clouds\" && forecastValue >= 28 ",
# 	"forecastCloudsLow" 		:"forecastName == \"clouds\" && forecastValue < 28",
	"forecastHumidityHigh"	:"forecastName == \"humid\" && forecastValue >= 0.5",
	"forecastHumidityLow" 	:"forecastName == \"humid\" && forecastValue < 0.5",
	"forecastWindHigh" 		:"forecastName == \"wind\" && forecastValue >= 0.5",
	"forecastWindLow" 		:"forecastName == \"wind\" && forecastValue < 0.5",
	"forecastprecipHigh" 	:"forecastName == \"precip\" && forecastValue >= 0.5",
	"forecastprecipLow" 	:"forecastName == \"precip\" && forecastValue < 0.5",	
 	"todayStartOfMonth" 	:"forecastName == \"date\" && forecastValue == 1",
	"todayWeekday" 			:"forecastName == \"day\" && forecastValue <= 5",#1,2,3,4,5
	"todayWeekend" 			:"forecastName == \"day\" && forecastValue >= 6",#6,7
	"todaySummerMonth" 		:"forecastName == \"month\" && (forecastValue >= 6 && forecastValue <= 8)",#6,7,8
	"todayNewYear" 			:"forecastName == \"year\" && forecastValue == 2022",
	"timeForSchool" 		:"forecastName == \"time\" && forecastValue >= 0745",
# 	"timeSunrise" 			:"forecastName == \"sunrise\" && forecastValue == 28",
# 	"timeSunset" 			:"forecastName == \"sunset\" && forecastValue == 28",
        "noInput":"true",#<<<<<<-----new added 17oct
        "recieveData":"recieved == 1", 
} 




#only for tweeting, logging paired physical sensorValues:
input_sensorValue = {
  	"buttonNotPress":"input.buttonIsPressed(Button.A)",
 	"buttonPress":"input.buttonIsPressed(Button.A)",
  	"accelLow":"input.acceleration(Dimension.X)" , 
  	"accelHigh":"input.acceleration(Dimension.X)"  , 
	"compassN" :"input.compassHeading()" , 
	"compassE" :"input.compassHeading()" , 
  	"compassS" :"input.compassHeading()" , 
  	"compassW" :"input.compassHeading()" , 
	"gestureShake":"input.isGesture(Gesture.Shake)"  , 
	"gestureTilt"  :"input.isGesture(Gesture.TiltLeft) || input.isGesture(Gesture.TiltRight)", 
	"movementNotPresent":"pins.digitalReadPin(DigitalPin.P0)"  ,
	"movementPresent" :"pins.digitalReadPin(DigitalPin.P0)" , 
	"noiseLow"  :"input.soundLevel()" , #v2
	"noiseHigh"	:"input.soundLevel()"  , #v2
 	"touchYes" 	:"input.logoIsPressed()" ,  #v2
 	"touchNo"	:"input.logoIsPressed()"  , #v2
	"sliderLow":"pins.analogReadPin(AnalogPin.P0)"  , 
 	"sliderMid":"pins.analogReadPin(AnalogPin.P0)",
	"sliderHigh":"pins.analogReadPin(AnalogPin.P0)"  , 
	"tempLow"  :"input.temperature()", 
	"tempHigh" :"input.temperature()" ,
	"lightlevelLow" :"input.lightLevel()", 
	"lightlevelHigh":"input.lightLevel()",
	"forecastTempHigh" :"forecastValue",
	"forecastTempLow" :"forecastValue",
	"forecastHumidityHigh" :"forecastValue",
	"forecastHumidityLow" :"forecastValue",
	"forecastWindHigh" :"forecastValue",
	"forecastWindLow" :"forecastValue",
	"forecastprecipHigh" :"forecastValue",
	"forecastprecipLow" :"forecastValue",
	"todayStartOfMonth" :"forecastValue",
	"todayWeekday" :"forecastValue",
	"todayWeekend" :"forecastValue",
	"todaySummerMonth" :"forecastValue",
	"todayNewYear" :"forecastValue",
	"timeForSchool" :"forecastValue",#should this be a value converted to str
	"none" :"none",
	"noInput" :"noInput",
	"noOutput" :"noOutput",
	"sendData" :"sendData",
	"recieveData" :"recieveData",
        
# 	"timeSunrise"  :"forecastValue",
# 	"timeSunset" :"forecastValue",
}


output_code = {
 	"iconHappy":"basic.showIcon(IconNames.Happy)\n\tbasic.pause(1000)",
    "iconSad":  "basic.showIcon(IconNames.Sad)\n\tbasic.pause(1000)",
    "iconNone":  "basic.clearScreen()\n\tbasic.pause(1000)",
  	"lightOn": "pins.digitalWritePin(DigitalPin.P1,1)\n\tbasic.pause(1000)",
 	"lightOff": "pins.digitalWritePin(DigitalPin.P1,0)\n\tbasic.pause(1000)",
  	"musicHappy" : "music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Forever)\n\tbasic.pause(1000)", 
  	"musicSad" : "music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Forever)\n\tbasic.pause(1000)", 
  	"musicNone" : "music.stopMelody(MelodyStopOptions.All)\n\tbasic.pause(1000)" , 
#   "speakText"  : "", 
#   "speakInput" : "" , 
#   "speakNone" : "" , 
	"displayText" : "basic.showString(\"Ciao \")\n\tbasic.pause(1000)" , 
	"displayInput": "basic.showNumber(9)\n\tbasic.pause(1000)"  , 
	#"displayInput": "basic.showString(\""+input_name[gamelevel]+"\")\n\tbasic.pause(1000)"  , 
 	"displayNone" :"basic.clearScreen()\n\tbasic.pause(1000)" , 
	"showStripRainbow" : "strip.showRainbow(1, 360)\n\tbasic.pause(1000)", 
	"showStripBlack" : "strip.showColor(neopixel.colors(NeoPixelColors.Black))\n\tbasic.pause(1000)", 
	"fanOn" :  	"pins.digitalWritePin(DigitalPin.P1,1)\n\tbasic.pause(1000)", 
	"fanOff"  : "pins.digitalWritePin(DigitalPin.P1,0)\n\tbasic.pause(1000)", 
 	"rotateMin" :"servos.P1.setAngle(0)\n\tbasic.pause(1000)" ,    
 	"rotateMid" :"servos.P1.setAngle(90)\n\tbasic.pause(1000)" ,  #card not used 
 	"rotateMax" :"servos.P1.setAngle(180)\n\tbasic.pause(1000)" ,    
	"tweetText"  : "radio.sendString(\"#Ciao\")\n\tbasic.pause(1000)" , 
	"tweetInput" : "radio.sendString(\"#nameValue\")\n\tbasic.pause(1000)" , #add input name and value directly???use variable
#	"tweetInput" : "radio.sendString(\"#"+input_name[gamelevel]+"\")\n\tbasic.pause(1000)" , #add input name and value directly???use variable
 	"logInput"   : "radio.sendValue(\"&value\", 0)",  #add input name and value directly??? use variable
#	"logInput"   : "radio.sendValue(\"&value\","+input_sensorValue[input_name[gamelevel]]+")\n\tbasic.pause(1000)",  #add input name and value directly???use variable
        "noOutput":"",#<<<<<<-----new added 17oct
        "sendData": "radio.sendValue(\"inputName\",inputValue)",# #<<<<<<-----new added 11nov
#       "sendData": "radio.sendValue(\""+input_name[gamelevel]+"\","+input_sensorValue[input_name[gamelevel]]+")",# #<<<<<<-----new added 11nov
}# 
#confirm displayInput, tweetInput, logInput


#defining a dictionary for inverse code for each output: 
output_else_code={
 	"iconHappy":"basic.clearScreen()\n\tbasic.pause(1000)",
    "iconSad":  "basic.clearScreen()\n\tbasic.pause(1000)",
    "iconNone":  "basic.showIcon(IconNames.Happy)\n\tbasic.pause(1000)",
  	"lightOn": "pins.digitalWritePin(DigitalPin.P1,0)\n\tbasic.pause(1000)",
 	"lightOff": "pins.digitalWritePin(DigitalPin.P1,1)\n\tbasic.pause(1000)",
  	"musicHappy": "music.stopMelody(MelodyStopOptions.All)\n\tbasic.pause(1000)",  
  	"musicSad" 	: "music.stopMelody(MelodyStopOptions.All)\n\tbasic.pause(1000)", 
  	"musicNone" :  "music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Forever)\n\tbasic.pause(1000)", 
#   "speakText"  : "", 
#   "speakInput" : "" , 
#   "speakNone" : "" , 
	"displayText" : "basic.clearScreen()\n\tbasic.pause(1000)" , 
	"displayInput": "basic.clearScreen()\n\tbasic.pause(1000)"  , 
 	"displayNone" : "basic.showString(\"hello\")\n\tbasic.pause(1000)" , 
#  	"displayNone" : "basic.showString(\""+input_name+"\")\n\tbasic.pause(100)" , 
	"showStripRainbow":  "strip.showColor(neopixel.colors(NeoPixelColors.Black))\n\tbasic.pause(1000)", 
	"showStripBlack" :"strip.showRainbow(1, 360)\n\tbasic.pause(1000)",  
	"fanOn" :  	"pins.digitalWritePin(DigitalPin.P1,0)\n\tbasic.pause(1000)", 
	"fanOff"  : "pins.digitalWritePin(DigitalPin.P1,1)\n\tbasic.pause(1000)", 
 	"rotateMin" :"servos.P1.setAngle(180)\n\tbasic.pause(1000)",#card not used 
 	"rotateMid" :"servos.P1.setAngle(0)\n\tbasic.pause(1000)" , #card not used 
 	"rotateMax" :"servos.P1.setAngle(0)\n\tbasic.pause(1000)" , #card not used    
	"tweetText"  : "basic.pause(1000)" , #not needed for cloud cards, can else statement remains empty??
	"tweetInput" : "basic.pause(1000)" , #not needed for cloud cards, can else statement remains empty??
	"logInput"   : "basic.pause(1000)",  #not needed for cloud cards, can else statement remains empty??
	"forecastTempHigh" 		:"radio.sendString(\"get_temp\")\n\tbasic.pause(2000)",
	"forecastTempLow" 		:"radio.sendString(\"get_temp\")\n\tbasic.pause(2000)",
	"forecastHumidityHigh"	:"radio.sendString(\"get_humid\")\n\tbasic.pause(2000)",
	"forecastHumidityLow" 	:"radio.sendString(\"get_humid\")\n\tbasic.pause(2000)",
	"forecastWindHigh" 		:"radio.sendString(\"get_wind\")\n\tbasic.pause(2000)",
	"forecastWindLow" 		:"radio.sendString(\"get_wind\")\n\tbasic.pause(2000)",
	"forecastprecipHigh" 	:"radio.sendString(\"get_precip\")\n\tbasic.pause(2000)",
	"forecastprecipLow" 	:"radio.sendString(\"get_precip\")\n\tbasic.pause(2000)",
	"todayStartOfMonth" 	:"radio.sendString(\"get_date\")\n\tbasic.pause(2000)",
	"todayWeekday" 			:"radio.sendString(\"get_day\")\n\tbasic.pause(2000)",
	"todayWeekend" 			:"radio.sendString(\"get_day\")\n\tbasic.pause(2000)",
	"todaySummerMonth" 		:"radio.sendString(\"get_month\")\n\tbasic.pause(2000)",
	"todayNewYear" 			:"radio.sendString(\"get_year\")\n\tbasic.pause(2000)",
	"timeForSchool" 		:"radio.sendString(\"get_time\")\n\tbasic.pause(2000)",
        "noOutput":"",#<<<<<<-----new added 17oct
        "sendData":"basic.pause(1000)",# #<<<<<<-----new added 11nov
}





freeplaymode=True
alwaysfreeplaymode=True
def genURL (*args):#input_name, output_name):#here i am collecting chunks of code, encoding them, and concatenating them into a URL:
     #----------on-start-code---------
    on_start_code=[]
    on_end_code=[]
    jscode=""
    for eachIOpair in args:
        #print(eachIOpair)
        for eachItem in eachIOpair:
            #print(eachItem)
            if True:#eachItem != "noInput" and eachItem != "noOutput": 
                if eachItem in on_start:
                    if eachItem=="sendData":
                        on_start_code.append(on_start[eachItem].replace("1",groupnum)+ '\n')
                    else:
                        on_start_code.append(on_start[eachItem]+ '\n')
                if eachItem in on_end:
                    on_end_code.append(on_end[eachItem]+ '\n')
    #print("onstart:",on_start_code)
    on_start_code_noDup= list( dict.fromkeys(on_start_code) )
    on_end_code_noDup= list( dict.fromkeys(on_end_code) )
    #print("onstart_noDup:",on_start_code_noDup)    
    for eachline in on_start_code_noDup:
        jscode= jscode + eachline
    jscode= jscode + 'basic.forever(function () {' + '\n'
    #-----------if-else-code---------
    if_body_code=""
    if freeplaymode==True or alwaysfreeplaymode==True:
        for eachIOpair in args: #in,out
            if True:#eachIOpair[0] != "noInput" and eachIOpair[1] != "noOuput":
                if eachIOpair[1] in output_code:
                    if eachIOpair[1]=="sendData":
                        if_body_code=output_code[eachIOpair[1]].replace("inputName",input_name[gamelevel]).replace("inputValue","1")
                       #if_body_code=output_code[eachIOpair[1]].replace("inputName",input_name[gamelevel]).replace("inputValue",input_sensorValue[input_name[gamelevel]])
                    else:
                        if_body_code=output_code[eachIOpair[1]]
                if eachIOpair[1] in output_else_code:
                    else_code = output_else_code[eachIOpair[1]]+ '\n'
                else:
                    else_code="basic.pause(100)"
                if eachIOpair[0] in output_else_code:#special cases for forecast: get_temp
                        else_code = output_else_code[eachIOpair[0]]+ '\n'


                jscode= jscode  \
                    + '    ' + 'if (' + input_code[eachIOpair[0]]+'){\n'  \
                    + '    ' + '    ' + if_body_code +'\n'  \
                    + '    ' + '} else {\n' \
                    + '    ' + '    ' + else_code \
                    + '    ' + '}\n'

    else:

        for eachIOpair in args: #in,out
            if eachIOpair[0] != "noInput" and eachIOpair[1] != "noOutput":
                if eachIOpair[1] in output_else_code:
                    else_code = output_else_code[eachIOpair[1]]+ '\n'
                else:
                    else_code="basic.pause(1000)"
                if eachIOpair[0] in output_else_code:#special cases for forecast: get_temp
                        else_code = output_else_code[eachIOpair[0]]+ '\n'

                jscode= jscode  \
                    + '    ' + 'if (' + input_code[eachIOpair[0]]+'){\n'  \
                    + '    ' + '    ' + output_code[eachIOpair[1]]+'\n'  \
                    + '    ' + ' } else {\n' \
                    + '    ' + '    ' + else_code +'\n' \
                    + '    ' + '}\n'
##+ '    ' + '    ' + 'basic.pause(1000)' +'\n' \



                
    #-----------closing forever loop---------
    jscode=jscode+'})'
    #-----------on_end_code---------
    for eachline in on_end_code_noDup:
        jscode= jscode + eachline 
    #print(jscode)
    
    #------enclose jscode in URL:---    
    url='https://makecode.microbit.org/--docs?md='+codetitle+codesubtitle+'%0A%0A%60%60%60%20blocks%0A'
    for eachline in jscode:
        url=url+urllib.parse.quote(eachline) 
    url=url+'%0A%60%60%60%0A%0A'
    #-----------add-extensions-code---------
    on_end_code=[]
    for eachIOpair in args:
        for eachItem in eachIOpair: 
            if True:#eachItem != "noInput" and eachItem != "noOutput":
                if eachItem in package_suffix:
                    on_end_code.append(package_suffix[eachItem])
                #url=url+package_suffix[eachItem]
    #print(on_end_code)
    on_end_code_noDup= list( dict.fromkeys(on_end_code) )
    #print(on_end_code_noDup)
    for eachline in on_end_code_noDup:
        url=url+eachline
    return url, jscode




urlis,jscode=genURL([input_name[0],output_name[0]])




st.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo-hor.png",width=380)
#input_col, plus_col, output_col, pad, code_col= st.columns([1,1,1,1,6])
pad2, input_col, plus_col, output_col, pad, code_col= st.columns([1,1,1,1,1,2])
with input_col:    
	#st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" se...")
	# ("Input1:")
	st.image(input0path, width=cardWidth) 
with plus_col:    
	#st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidthhalf)
	st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht) 
with output_col:    
	#st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
	st.write(" allora...")
	# ("Output1:")
	st.image(output0path, width=cardWidth) 

#with code_col:
#	st.subheader("")
#	st.subheader("")
#	st.markdown(
#        """
#        <style> .font{
#        font-size:50px;}
#        </style>
#        """,
#        unsafe_allow_html=True,
#        )
#	st.code(jscode,language="javascript")



#e,edit  = st.columns([1,1])
#with edit:
#        #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=60)
#        st.markdown("[Modifica...]("+urlis+")", unsafe_allow_html=True)



e,edit  = st.columns([1,1])
with edit:
        #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=60)
        st.markdown("[Modifica...]("+urlis+")", unsafe_allow_html=True)

	
st.subheader("")
components.iframe(urlis, height=1000, scrolling=True)    

#st.button("Refresh")
