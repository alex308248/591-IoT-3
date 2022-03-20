# 591-IoT-3

## Introduction
This is the part of the third assignment of 591-IoT. For this assignment, we are going to use three Raspberry Pis (I will call them Raspberry Pi A, Raspberry Pi B, and Raspberry Pi C) and two computers/laptops (or one computer/laptop and one smart phone) with WiFi interfaces, three LEDs, a light dependent resistor (LDR), a potentiometer, and some general resisters to demo the MQTT communication. We used `Python` and the python library `mosquitto` in the repo, it is necessary to install both of them before you implement it. 

## Some impoprtant reminds
This repo will only include the code running on Raspberry Pi C and requirement files for testing it's correctness. Other files in this repo will not be able to run on other Raspberry Pis or laptops during the experiment.

## Discription
* PiC.py: It will subscrib to topics `lightSensor`, `threshold` and `Status/RaspberryPiC` and publish `LightStatus`, `Status/RaspberryPiC`. By caculating the difference between lightSensor and threshold, PiC will determine LightStatus is `TurnOn` or `TurnOff`. It will also use retain flag and last will message to show it's status is `online` or `offline` by `Status/RaspberryPiC`.
* PiA-Sample.py: The file will publish lightSensor and threshold randomly, which will be the subscribe topics of PiC.py.
* laptop2.py: It will subscribe to all of the topics and record the recieved messages in record.txt. It will also display messages sent by the broker on these topics along with the timestamps.
* record.txt: The log file which reocrd all of the messages that recieved by laptop.py.

## How to run it locally?
1. Install Python3, mosquitto and Paho
2. Start a broker in a local terminal by running `sudo service mosquitto start`
3. Modify the value of variable `broker` in files to `"localhost"`
4. Run files PiC.py laptop2.py PiA-Sample.py in three terminals
5. Check the record.txt for the log

## How to run it with other Pis and laptops?
1. Make sure you installed Python3, mosquitto and Paho
2. Set up a public broker on another PC
3. Set up other Raspberry Pis and laptops
4. Modify the value of variable `broker` in files to `"*IP ADDRESS OF BROKER*"` in PiC.py
5. Run files PiC.py

