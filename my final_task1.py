#******************  task 1  ********************

'''

APM:

BESIAR AWLI AHSANT



'''
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

class Device:
    def __init__(self, topic, mqtt_broker='localhost', port=1883):
        self.topic = topic
        self.topic_list = self.topic.split('/')
        self.location = self.topic_list[0]
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.device_name = self.topic_list[3]
        self.mqtt_broker = mqtt_broker
        self.port = port


    def connect_mqtt(self):
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect(self.mqtt_broker, self.port)
        print(f'{self.device_name} connected to MQTT broker at {self.mqtt_broker}:{self.port}')

    def setup_gpio(self):
        def get_gpio(self):
            if self.device_type == 'lamps':
                return 17
            elif self.device_type == 'doors':
                return 27
            elif self.device_type == 'fans':
                return 22
            elif self.device_type == 'camera':
                return 100
            else:
                return None
        
    def turn_on(self):
        if self.gpio_pin is not None:
            GPIO.output(self.gpio_pin, True)
        self.send_commands('TURN_ON')
        print(f'{self.device_name} turned ON')

    def turn_off(self):
        if self.gpio_pin is not None:
            GPIO.output(self.gpio_pin, False)
        self.send_commands('TURN_OFF')
        print(f'{self.device_name} turned OFF')

    def send_commands(self, command):
        self.mqtt_client.publish(self.topic, command)
        print(f'Command "{command}" sent to topic "{self.topic}"')


cam = Device('home/room1/camera/cam1')  
cam.connect_mqtt()
cam.setup_gpio()   
cam.turn_on()      
cam.turn_off()     
