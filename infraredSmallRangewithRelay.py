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
# SHARP Infrared Sensor 10cm to 150cm CONFIGURATION
# ---------------------------------------------------------
def distance():
    runningTotal = 0
    avgFactor = 30
    for x in range(avgFactor):
        v = (mcp.read_adc(2) / 1023.0) * 3.3
        distance1 = (16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439)
        runningTotal = runningTotal + distance1
        #print distance1
        #print "No.", x, "distance = ", distance1
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
                    #Switch ON bulb and LED
                    GPIO.output (GPIO_RELAY,GPIO.LOW)
                    GPIO.output(GPIO_LED, GPIO.HIGH)
                    count1 += 1
                    count2 = 0
                    print ("---------- State 1 ------------")
                    
                    time.sleep(2)

            else:
                if ( dist > 40 and dist < 220):
                    # Stay Condition
                    #Switch ON bulb and LED
                    GPIO.output (GPIO_RELAY,GPIO.LOW)
                    GPIO.output(GPIO_LED, GPIO.HIGH)
                    count1 += 1
                    print ("---------- State 2 ------------")
                    time.sleep(2)

                else:
                    if (count2 == 0) :
                        # Exit Condition
                        #Switch OFF bulb and LED
                        GPIO.output (GPIO_RELAY,GPIO.HIGH)
                        GPIO.output(GPIO_LED, GPIO.LOW)
                        count2 += 1
                        print ("---------- State 3 ------------")
                        time.sleep(1)
                    
                    else:
                        # Nobody Condition
                        #Switch OFF bulb and LED
                        GPIO.output (GPIO_RELAY,GPIO.HIGH)
                        GPIO.output(GPIO_LED, GPIO.LOW)
                        count1 = 0
                        print ("---------- State 4 ------------")
                        time.sleep(1)
           
    except KeyboardInterrupt:
        print("Ending Script Coding")
