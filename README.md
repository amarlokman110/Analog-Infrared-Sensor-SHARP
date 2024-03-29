# Analog-Infrared-Sensor-SHARP
There are some infrared distance sensors from the manufacturer Sharp, which can be operated very simply with the Raspberry Pi. There are different distance meters, which cover different distance ranges. These modules work similarly to laser distance meters, but with infrared light. There, bundled light is emitted by a transmitter and an analogue voltage is transmitted through a receiver on the basis of the angle of incidence, whereby the distance can be calculated.

Measuring the distance by using analog infrared sensor with SHARP brand. Two types of infrared sensor is being used which are Sharp GP2Y0A710K0F which can measure from 100cm to 550cm and  Sharp GP2Y0A02YK0F which can measure from 20cm to 150cm. This sensor will be used with the Raspberry Pi 3 Model B+. Language involves is Python language.


<table border="0">
 <tr>
    <td><b style="font-size:30px">SHARP GP2Y0A02YK0F</b></td>
    <td><b style="font-size:30px">SHARP GP2Y0A710K0F</b></td>
    <td><b style="font-size:30px">RASPBERRY PI 3 MODEL B+</b></td>
 </tr>
 <tr>
    <td><img src="https://user-images.githubusercontent.com/54172575/63335910-c9266180-c370-11e9-8ed4-ffd122402ad4.jpg" width="300" /></td>
    <td><img src="https://user-images.githubusercontent.com/54172575/63336549-e6a7fb00-c371-11e9-92f0-e494929007bf.jpg" width="300" /></td>
    <td><img src="https://user-images.githubusercontent.com/54172575/63336903-95e4d200-c372-11e9-80f1-a3af60130970.jpg" width="300" /></td>
 </tr>
</table>

The MCP3008 is a low cost 8-channel 10-bit analog to digital converter. Since Infrared needs Analog input, I use this chip to convert digital input from Raspberry pi to analog input for the infrared sensor. 
   1. MCP3008 VDD to Raspberry Pi 3.3V
   2. MCP3008 VREF to Raspberry Pi 3.3V
   3. MCP3008 AGND to Raspberry Pi GND
   4. MCP3008 DGND to Raspberry Pi GND
   5. MCP3008 CLK to Raspberry Pi pin 18
   6. MCP3008 DOUT to Raspberry Pi pin 23
   7. MCP3008 DIN to Raspberry Pi pin 24
   8. MCP3008 CS/SHDN to Raspberry Pi pin 25

<img src="https://user-images.githubusercontent.com/54172575/63561801-c9e80f00-c58d-11e9-930b-efd69f71d85f.gif" width="300" />

## Library Install 
Install the library from the Python package index with a few commands, or you can install the library from its source on GitHub.
git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
  * cd Adafruit_Python_MCP3008
  * sudo python setup.py install
  * sudo pip install adafruit-mcp3008
   
## Analog Input from MCP3008
Notice this line that reads an ADC channel value and saves it in a list:

values[i] = mcp.read_adc(i)

This line is calling the read_adc() function from the MCP3008 Python library.  The function takes one parameter, the channel number to read (a value of 0 to 7).  As a result the function will return the current ADC value of that channel.

## Relay DC5V Tongling 

<img src="https://user-images.githubusercontent.com/54172575/64125958-77ed8780-cdde-11e9-8542-fdd294aae4b3.JPG" width="300" />

This is a 5V 1 Channcel optical isolated relay interface board, it can be controlled directly by raspberry pi. 
* 5V 1-Channel Relay interface board, and each one needs 15-20mA Driver Current & 5mA trigger current
* Equiped with high-current relay, AC250V 10A ; DC30V 10A
* DC+ Power supply Positive 5V DC
* DC- Power supply Negative 0V DC
* IN: Signal Input Can be TTL High / Low depends on jumper setting
* NO: Dry contact normally Open
* COM: Dry contact Common
* NC: Dry contact normally Close

## Source Code 

### SHARP Infrared Sensor 10cm to 150cm CONFIGURATION
```
def distance():
    runningTotal = 0
    avgFactor = 30
    for x in range(avgFactor):
        v = (mcp.read_adc(2) / 1023.0) * 3.3
        distance1 = (16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439)
        runningTotal = runningTotal + distance1
    else:
        distance = (runningTotal / avgFactor)

    return distance
```

### SHARP Infrared Sensor 100cm to 550cm CONFIGURATION
```
def distance():
    runningTotal = 0
    avgFactor = 75
    for x in range(avgFactor):
        v = mcp.read_adc(0)
        distance = 28250 / (v-229.5)
        runningTotal = runningTotal + distance
    else:
        distance = (runningTotal / avgFactor)

    return distance
```
