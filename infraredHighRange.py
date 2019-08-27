# ******************************************
# © 2019 Amar Lokman Some Rights Reserved
# ******************************************

# ---------------------------------------------------------
# ADD MODULES
# ---------------------------------------------------------
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import datetime
import RPi.GPIO as GPIO

# ---------------------------------------------------------
# GPIO CONFIGURATION
# ---------------------------------------------------------
GPIO.setmode(GPIO.BCM)

CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

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
            dist = distance()
            print("Distance {:.2f}".format(dist))
            time.sleep(2)
           
    except KeyboardInterrupt:
        print("Ending Script Coding")
