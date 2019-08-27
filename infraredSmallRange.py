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
# SHARP Infrared Sensor 10cm to 150cm CONFIGURATION
# ---------------------------------------------------------
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
