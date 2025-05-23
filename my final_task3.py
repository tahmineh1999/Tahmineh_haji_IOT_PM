#******************  task 3  ********************

'''
APM:

Besiar awli ahsant , 
daryaft shod


'''

class Device:
    def __init__(self, topic):
        self.topic = topic
        self.device_name = topic.split('/')[-1]
        self.status = "OFF"
    
    def turn_on(self):
        self.status = "ON"
        print(f'{self.device_name} is now ON.')
        
    def turn_off(self):
        self.status = "OFF"
        print(f'{self.device_name} is now OFF.')

import random

class Sensor:
    def __init__(self, topic):
        self.topic = topic
        self.sensor_name = topic.split('/')[-1]
        self.value = 0

    def read_value(self):
        self.value = random.randint(20, 30)
        return self.value


class Admin_panel:
    def __init__(self):
        self.groups = {}
    
    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'Group "{group_name}" created.')
        else:
            print('Your group name already exists.')
    
    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'{device.device_name} is added to {group_name}.')
        else:
            print(f'Group {group_name} does not exist.')
    
    def create_device(self, group_name, device_type, name):
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'{new_device.device_name} is added to {group_name}.')
        else:
            print(f'Group {group_name} does not exist.')
    
    def create_multiple_devices(self, group_name, device_type, number_of_devices):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f'{device_type}{i}'
                topic = f'home/{group_name}/{device_type}/{device_name}'
                new_device = Device(topic)
                self.add_device_to_group(group_name, new_device)
            print(f'All {number_of_devices} devices created in group "{group_name}".')
        else:
            print(f'Group {group_name} does not exist.')
    
    def turn_on_all_in_group(self, group_name):
        if group_name in self.groups:
            all_devices = self.groups[group_name]
            for device in all_devices:
                device.turn_on()
            print(f'All devices in {group_name} turned ON.')
        else:
            print(f'Group {group_name} does not exist.')
    
    def turn_off_all_in_group(self, group_name):
        if group_name in self.groups:
            all_devices = self.groups[group_name]
            for device in all_devices:
                device.turn_off()
            print(f'All devices in {group_name} turned OFF.')
        else:
            print(f'Group {group_name} does not exist.')

    def turn_on_all(self):
        for group in self.groups.values():
            for device in group:
                device.turn_on()
        print('All devices in all groups turned ON.')
    
    def turn_off_all(self):
        for group in self.groups.values():
            for device in group:
                device.turn_off()
        print('All devices in all groups turned OFF.')

    def get_status_in_group(self, group_name):
        if group_name in self.groups:
            for device in self.groups[group_name]:
                print(f'{device.device_name}: {device.status}')
        else:
            print(f'Group {group_name} not found.')
    
    def get_status_in_device_type(self, device_type):
        found = False
        for group in self.groups:
            for device in self.groups[group]:
                if device_type in device.topic:
                    print(f'{device.device_name} in group {group}: {device.status}')
                    found = True
        if not found:
            print(f'No devices of type {device_type} found.')

    def create_sensor(self, group_name, sensor_type, sensor_name):
        if group_name in self.groups:
            topic = f'home/{group_name}/{sensor_type}/{sensor_name}'
            new_sensor = Sensor(topic)
            self.groups[group_name].append(new_sensor)
            print(f'Sensor {sensor_name} added to {group_name}.')
        else:
            print(f'Group {group_name} does not exist.')

    def get_status_sensor_in_group(self, group_name):
        if group_name in self.groups:
            print(f'\nStatus of sensors in group "{group_name}":')
            for device in self.groups[group_name]:
                if isinstance(device, Sensor):
                    value = device.read_value()
                    print(f'{device.sensor_name}: {value}')
        else:
            print(f'Group {group_name} does not exist.')

panel = Admin_panel()

panel.create_group("kitchen")
panel.create_sensor("kitchen", "temperature", "temp1")
panel.create_sensor("kitchen", "humidity", "hum1")

panel.get_status_sensor_in_group("kitchen")
