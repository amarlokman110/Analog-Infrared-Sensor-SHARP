# ******************************************
# © 2019 Amar Lokman Some Rights Reserved
# ******************************************

# ---------------------------------------------------------
# ADD MODULES
# ---------------------------------------------------------
import time
import Adafruit_MCP3008
import datetime
import RPi.GPIO as GPIO

# ---------------------------------------------------------
# GPIO CONFIGURATION
# ---------------------------------------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_RELAY = 20
GPIO_LED = 16
GPIO.setup(GPIO_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GPIO_RELAY,GPIO.OUT, initial=GPIO.HIGH)

CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
count1 = 0
count2 = 0

# ---------------------------------------------------------
# SHARP Infrared Sensor 100cm to 550cm CONFIGURATION
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------------

if __name__ ==     '__main__':
    try:
        while True:
            print("Distance {:.2f}".format(dist))
            time.sleep(2)
            print ("****************************************************")

            if (count1 == 0) :
                if ( dist > 40 and dist < 220):
                    # Enter Condition
                    # Switch ON bulb and LED
                    GPIO.output (GPIO_RELAY,GPIO.LOW)
                    GPIO.output(GPIO_LED, GPIO.HIGH)
                    count1 += 1
                    count2 = 0
                    print ("---------- State 1 ------------")
                    
                    time.sleep(2)

            else:
                if ( dist > 40 and dist < 220):
                    GPIO.output (GPIO_RELAY,GPIO.LOW)
                    GPIO.output(GPIO_LED, GPIO.HIGH)
                    count1 += 1
                    print ("---------- State 2 ------------")
                    time.sleep(2)

                else:
                    if (count2 == 0) :
                        # Enter Condition
                        # Switch OFF bulb and LED
                        GPIO.output (GPIO_RELAY,GPIO.HIGH)
                        GPIO.output(GPIO_LED, GPIO.LOW)
                        count2 += 1
                        print ("---------- State 3 ------------")
                        time.sleep(1)
                    
                    else:
                        GPIO.output (GPIO_RELAY,GPIO.HIGH)
                        GPIO.output(GPIO_LED, GPIO.LOW)
                        count1 = 0
                        print ("---------- State 4 ------------")
                        time.sleep(1)
           
    except KeyboardInterrupt:
        print("Ending Script Coding")
