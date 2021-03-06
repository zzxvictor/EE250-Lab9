"""EE 250L Lab 07 Skeleton Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""
import sys
import paho.mqtt.client as mqtt
import time
import grovepi
import grove_rgb_lcd 
import grove_i2c_temp_hum_mini


state = 0
def lcdCallBack(client, userdata, message):
   grove_rgb_lcd.setText(str(message.payload,"utf-8"))

def ledCallBack(client, userdata, message):

    led = 2
    global state
    msg = str(message.payload, "utf-8")
    print (msg)
    if msg == "LED_toggle":
        if state == 0:
            grovepi.digitalWrite(led, 1)
            state = 1
        elif state == 1:
            grovepi.digitalWrite(led, 0)
            state = 0
        else:
            state = state


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("anrg-pi1/led")
    client.message_callback_add("anrg-pi1/led", ledCallBack)
    client.subscribe("anrg-pi1/lcd")
    client.message_callback_add("anrg-pi1/lcd", lcdCallBack)
    client.subscribe("anrg-pi1/tempreture")
    client.subscribe("anrg-pi1/humidity")

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    grove_rgb_lcd.setRGB(0,64,128)
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()
    while True:
        #read tempreture sensor
        #publish it 

        #read humidity sensor
        #publish it 


        time.sleep(1)
