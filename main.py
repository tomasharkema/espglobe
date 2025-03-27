import time
from machine import Pin
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/tomasharkema/espglobe/main"
 
IN1 = Pin(13,Pin.OUT)
IN2 = Pin(12,Pin.OUT)
IN3 = Pin(27,Pin.OUT)
IN4 = Pin(33,Pin.OUT)

# LED = Pin(25,Pin.OUT)

pins = [IN1, IN2, IN3, IN4]
steps = [
    [IN1],
    [IN1, IN2],
    [IN2],
    [IN2, IN3],
    [IN3],
    [IN3, IN4],
    [IN4],
    [IN4, IN1],
]
current_step = 0
 
def set_pins_low(pins):
    [pin.off() for pin in pins]
 
 
def set_pins_high(pins):
    [pin.on() for pin in pins]
    
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()
    
while True:
    # print("step")
    
    # set_pins_high([LED])
    # set_pins_low([LED])
    
    high_pins = steps[current_step]
    set_pins_low(pins)
    set_pins_high(high_pins)
    current_step += 1
    if current_step == len(steps):
        current_step = 0
    time.sleep(0.01)
