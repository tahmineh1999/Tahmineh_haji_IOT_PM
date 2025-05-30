#******************  task 2  ********************

'''



APM: 
besiar awli 
daryaft shod
'''

class Device:
    def __init__(self, topic):
        self.topic = topic
        self.device_name = topic.split('/')[-1]

class Admin_panel:
    def __init__(self):
        self.groups = {}
        
    def create_group(self, group_name):  
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'Group {group_name} created')
        else:
            print('Your group name already exists')
            
    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'{device.device_name} is added to {group_name}')
        else:
            print(f'Group {group_name} does not exist')

    def create_device(self, group_name, device_type, name):
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'{new_device.device_name} is added to {group_name}')
        else:
            print(f'Group {group_name} does not exist')
        
    def create_multiple_devices(self, group_name, device_type, number_of_devices):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f'{device_type}{i}'
                topic = f'home/{group_name}/{device_type}/{device_name}'
                new_device = Device(topic)
                self.add_device_to_group(group_name, new_device)
            print(f'all {number_of_devices} devices created in group"{group_name}".')    
        else:
            print(f'Group {group_name} does not exist')


a = Admin_panel()

a.create_group('parking') 
a.create_group('wc')
a.create_group('room1')

a.create_multiple_devices('parking', 'lamps', 40)

mygp = a.groups 

for group in mygp:
    for device in mygp[group]:
        print(device.device_name)
