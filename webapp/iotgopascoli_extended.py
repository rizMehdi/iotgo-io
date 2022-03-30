#For PascoliBZ- 29March22
import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import time
import textwrap
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide",initial_sidebar_state="expanded")

codetitle=""
codesubtitle=""
groupnum="0"



hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

fix_sidebar= """
<style>
[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
	width: 350px;}
[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
	width: 350px;margin-left: -350px;}
</style>
"""

st.markdown(hide_img_fs, unsafe_allow_html=True)
st.markdown(fix_sidebar,unsafe_allow_html=True)



	 
inputs_microbitv1= ("l\'accelerazione è alta" ,
		    "l\'accelerazione è basso" ,
		    "il pulsante non è premuto",
		    "il pulsante è premuto",
		    "la bussola punta ad Est",
		    "la bussola punta a Nord" ,
		    "la bussola punta a Sud" ,
		    "la bussola punta ad Ovest" ,
		    "il gesto è scuotere" ,
		    "il gesto è inclinare" ,
		    "l\'intensità di luce è alta",
		    'l\'intensità di luce è bassa',
		    'la temperatura è alta' ,
		    'la temperatura è bassa' ,
	
		   )
inputs_microbitv2= ( "il rumore è alto" ,
		    'il rumore è basso' ,
		    'il logo non è toccato', #v2 
		    'il logo è toccato' ,#v2 
		   )
inputs_exBosonKit= ('non c\'è movimento nei dintorni (BosonKit)' ,
'c\'è movimento nei dintorn (BosonKit)' ,
'il cursore è al massimo (BosonKit)' ,
'il cursore è al minimo (BosonKit)' ,
"il cursore è al medio (BosonKit)" ,
		   )
inputs_exEnviroBit= ("c\'è tanta umidità (Envirobit)",
"c\'è poca umidità (Envirobit)",
"la pressione atmosferica è alta (Envirobit)",
"la pressione atmosferica è bassa (Envirobit)",
'il rumore è alto (Envirobit)' ,
'Il rumore è basso (Envirobit)' ,
"la temperatura è alta (Envirobit)" ,
"la temperatura è bassa (Envirobit)" ,
"l\'intensità di luce è alta (Envirobit)",
"l\'intensità di luce è bassa (Envirobit)",
"il colore  è rosso (Envirobit)"
"il colore  è verde (Envirobit)"
"il colore  è blu (Envirobit)"
"il colore  è nero (Envirobit)"
"c\'è un applauso (Envirobit)"
"non c’è un applauso (Envirobit)"
)




outputs_microbitv1= (     'Mostra un\'icona felice' ,
        'Mostra un\'icona triste' ,
        'Smette di mostrare un\'icona' ,	
	'Mostra del testo'  , 
	'Mostra un numero'  , 
	'Smette di mostrare testi o numeri'  ,
		    )
outputs_microbitv2= ('Suona una melodia triste'  , 
  	'Suona una melodia allegra'  , 
	'Smette di suonare'   , 
		    )
outputs_exBosonKit=('Accende una luce' ,
 	'Spegne una luce' , 	
	'Attiva un\'animazione luminosa'  , 
	'Spegne un\'animazione luminosa' , 	
	'Accende un ventilatore'  , 
	'Spegne un ventilatore'  ,
	'Fa ruotare il motore',
		   )
outputs_exEnviroBit= ()

	 
	

input_options=  ('no Input',) 
output_options=  ('no Output',)


st.sidebar.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo3.png",width=200)
	
hardware = st.sidebar.radio("Seleziona l\'elettronica che hai",("Solo Micro:bit", "Micro:bit con BosonKit", "Micro:bit con EnviroBit"))
if hardware == "Solo Micro:bit":
	input_options=  ('no Input',) + inputs_microbitv1 + inputs_microbitv2 
	output_options=  ('no Output',) + outputs_microbitv1 + outputs_microbitv2 
elif hardware == "Micro:bit con BosonKit":
	input_options=  ('no Input',) + inputs_microbitv1 + inputs_microbitv2 + inputs_exBosonKit 
	output_options=  ('no Output',) + outputs_microbitv1 + outputs_microbitv2 + outputs_exBosonKit
elif hardware == "Micro:bit con EnviroBit":
	input_options=  ('no Input',) + inputs_microbitv1 + inputs_microbitv2 +  inputs_exEnviroBit
	output_options=  ('no Output',) + outputs_microbitv1 + outputs_microbitv2 + outputs_exEnviroBit


input1 =  st.sidebar.selectbox('Seleziona la tua carta di input', input_options)
output1 = st.sidebar.selectbox('Seleziona la tua carta di output', output_options)



#st.sidebar.write('You selected:', input1,output1,input2,output2)
it2en_intout={
"il rumore è alto":"noiseHigh" ,
'il rumore è basso':"noiseLow" ,
'il logo non è toccato':"touchNo" , #v2 
'il logo è toccato':"touchYes" ,#v2 
"l\'accelerazione è alta":"accelHigh" ,
"l\'accelerazione è basso":"accelLow" ,
"il pulsante non è premuto":"buttonNotPress",
"il pulsante è premuto":"buttonPress",
"la bussola punta ad Est":"compassE" ,
"la bussola punta a Nord":"compassN" ,
"la bussola punta a Sud":"compassS" ,
"la bussola punta ad Ovest":"compassW" ,
"il gesto è scuotere":"gestureShake" ,
"il gesto è inclinare":"gestureTilt" ,
"l\'intensità di luce è alta":"lightlevelHigh",
'l\'intensità di luce è bassa':"lightlevelLow",
'la temperatura è alta':"tempHigh" ,
'la temperatura è bassa':"tempLow" ,
'recezione dati' :"recieveData",
"c\'è tanta umidità (Envirobit)": "EB_humidityHigh",
"c\'è poca umidità (Envirobit)" : "EB_humidityLow",
"la pressione atmosferica è alta (Envirobit)" : "EB_pressureHigh"
"la pressione atmosferica è bassa (Envirobit)" : "EB_pressureLow"
'il rumore è alto (Envirobit)':"EB_noiseHigh" ,
'Il rumore è basso (Envirobit)':"EB_noiseLow" ,
"la temperatura è alta (Envirobit)":"EB_tempHigh" ,
"la temperatura è bassa (Envirobit)":"EB_tempLow" ,
"l\'intensità di luce è alta (Envirobit)":"EB_lightlevelHigh",
"l\'intensità di luce è bassa (Envirobit)":"EB_lightlevelLow",
"il colore  è rosso (Envirobit)": "EB_colorIsRed"
"il colore  è verde (Envirobit)": "EB_colorIsGreen"
"il colore  è blu (Envirobit)": "EB_colorIsBlue"
"il colore  è nero (Envirobit)": "EB_colorIsBlack"
"c\'è un applauso (Envirobit)": "EB_colorIsBlack"
"non c’è un applauso (Envirobit)": "EB_colorIsBlack"
'non c\'è movimento nei dintorni (BosonKit)':"movementNotPresent" ,
'c\'è movimento nei dintorn (BosonKit)i':"movementPresent" ,
'il cursore è al massimo (BosonKit)':"sliderHigh" ,
'il cursore è al minimo (BosonKit)':"sliderLow" ,
"il cursore è al medio (BosonKit)":"sliderMid" ,
'no Input':"noInput",
'suona una melodia allegra':"musicHappy" ,
'smette di suonare':"musicNone" ,
'suona una melodia triste':"musicSad" ,
"suona un allarme":"musicAlarm" ,
'mostra un numero':"displayInput" ,
'smette di mostrare testi o numeri':"displayNone" ,
'mostra del testo':"displayText" ,
'mostra un\'icona felice':"iconHappy",
'smette di mostrare un\'icona':"iconNone",
'mostra un\'icona triste':"iconSad",
'invio dati' :"sendData",
"accende i LED bianchi (Envirobit)": "EB_whiteLEDon"
"spegne i LED bianchi (Envirobit)": "EB_whiteLEDoff"
'spegne un ventilatore (BosonKit)':"fanOff" ,
'accende un ventilatore (BosonKit)':"fanOn" ,
'spegne una luce (BosonKit)':"lightOff",
'accende una luce (BosonKit)':"lightOn",
'fa ruotare il motore (BosonKit)':"rotateMax" ,
'smette di ruotare il motore (BosonKit)':"rotateMin" ,
'spegne un\'animazione luminosa (BosonKit)':"showStripBlack",
'attiva un\'animazione luminosa (BosonKit)':"showStripRainbow" ,
'spegne un\'animazione luminosa verde (BosonKit)':"showStripGreen",
'spegne un\'animazione luminosa rossa (BosonKit)':"showStripRed",
}

it2en_inoutold= {
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
	'no Output':"noOutput", 
        'invio dati' :"sendData",
    }



gamelevel=0
input_name= ["no Input"  ,"no Input"  ,"no Input"]
output_name=["no Output" ,"no Output" ,"no Output"]
input_name[0]= it2en_inout[input1]
output_name[0]=it2en_inout[output1]



langPrefix=['EN','IT','DE','UR']
lang=1


baseURLold="https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/"
baseURL=   "https://raw.githubusercontent.com/IoTgo-app/iotgo-io/main/webapp_v2/images/cards_v2/"


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

    
    "buttonNotPress":   "-inputPhysical-buttonNotPress.png",
    "buttonPress":      "-inputPhysical-buttonPress.png",
    "accelLow":         "-inputPhysical-accelLow.png",
    "accelHigh" :       "-inputPhysical-accelHigh.png",
    "compassN" :        "-inputPhysical-compassN.png",
    "compassE" :        "-inputPhysical-compassE.png",
    "compassS" :        "-inputPhysical-compassS.png",
    "compassW" :        "-inputPhysical-compassW.png",
    "gestureShake":     "-inputPhysical-gestureShake.png",
    "gestureTilt" :     "-inputPhysical-gestureTilt.png",
    "movementNotPresent":"-inputPhysical-movementNotPresent.png",
    "movementPresent" : "-inputPhysical-movementPresent.png",
    "noiseLow"  :       "-inputPhysical-noiseLow.png",
    "noiseHigh"	:       "-inputPhysical-noiseHigh.png",
    "touchYes" 	:       "-inputPhysical-touchYes.png",
    "touchNo"	:       "-inputPhysical-touchNo.png",
    "sliderLow":        "-inputPhysical-sliderLow.png",
    "sliderMid":        "-inputPhysical-sliderMid.png",#not used. 
    "sliderHigh":       "-inputPhysical-sliderMax.png",
    "tempLow"  :        "-inputPhysical-tempLow.png",
    "tempHigh" :        "-inputPhysical-tempHigh.png",
    "lightlevelLow" :   "-inputPhysical-lightlevelLow.png",
    "lightlevelHigh":   "-inputPhysical-lightlevelHigh.png",
    
        
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
    
    
    "iconHappy":    "-outputPhysical-iconHappy.png",
    "iconSad":      "-outputPhysical-iconSad.png",
    "iconNone":    "-outputPhysical-iconNone.png",
    "lightOn":      "-outputPhysical-lightOn.png",
    "lightOff":     "-outputPhysical-lightOff.png",
    "musicHappy":   "-outputPhysical-musicHappy.png",
    "musicSad" :    "-outputPhysical-musicSad.png",
    "musicNone" :   "-outputPhysical-musicNone.png", 
    "displayText" : "-outputPhysical-displayText.png",  
    "displayInput": "-outputPhysical-displayInput.png",
    "displayNone" : "-outputPhysical-displayNone.png", 
    "showStripRainbow" :"-outputPhysical-showStripRainbow.png",
    "showStripBlack" :"-outputPhysical-showStripBlack.png",
    "fanOn" :       "-outputPhysical-fanOn.png",	 
    "fanOff"  :     "-outputPhysical-fanOff.png",
    "rotateMin":    "-outputPhysical-rotateMin.png", 
    "rotateMid":    "-outputPhysical-rotateMax.png",#not used. 
    "rotateMax":    "-outputPhysical-rotateMax.png",
    
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
prevUrlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Abasic.pause%281000%29%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28true%29%7B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%7D%0A%7D%29%0A%60%60%60%0A%0A"
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


cardWidth=150
pluscardwidht=150
missionCardWidth=160
vertiPaddingWidth=35
vertiPaddingWidthhalf=17



#st.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo-hor.png",width=380)
#st.header("IoTgo")

#input_col, plus_col, output_col, pad, code_col= st.columns([1,1,1,1,6])
input_col, plus_col, output_col, pad, code_col,pad2,= st.columns([1,1,1,1,1,2])
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

if prevUrlis != urlis:
	with st.spinner('Plz wait. Generating code for you....'):
    		time.sleep(0.1)
	#st.success('Done!')
prevUrlis=urlis


e,edit  = st.columns([1,1])
with edit:
        #st.markdown("[Modifica...]("+urlis+")", unsafe_allow_html=True)
	st.write("[Modifica...]("+urlis+")")


	
	
	
htmliframeold='''
<a id="status" href = test.html></a>blah
<iframe src="
'''+urlis+'''
" id="iframe_a" title="Iframe Example" height="1000"  width="700" style="border:none;" scrolling="yes" loading="eager"></iframe>

<script type="text/javascript">
   var iframe = document.getElementById('iframe_a');
    var iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
    var statusText = "not loaded";
    if (  iframeDoc.readyState  == 'complete' ) {
        iframe.contentWindow.onload = function(){ 
	    statusText = "loaded";
	    document.getElementById("status").innerHTML ="loaded";
        }
	else {
	document.getElementById("status").innerHTML ="not loaded";
	};
     
</script>
'''

htmliframe='''
<a id="status" href = test.html></a>blah
<iframe src="
'''+urlis+'''
" id="iframe_a" title="Iframe Example" height="1000"  width="700" style="border:none;" scrolling="yes" loading="eager"></iframe>

<script type="text/javascript">
    document.getElementById('iframe_a').onload= function() {
    document.getElementById("status").innerHTML="done";
    };
</script>

'''





#st.write("updateS")
components.iframe(urlis, height=1000, scrolling=True)   
#components.html(htmliframe, height=1000, scrolling=False)






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


 

#st.button("Refresh")
