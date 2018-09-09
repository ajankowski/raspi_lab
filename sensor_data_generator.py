import random
import time
from datetime import datetime
import json

class Sensor:
    def __init__(self, name, s_range, change_size = 1,  first_read = False, bias = 0):
        # s_range is sensing range (tuple, the sensor will select reading from this range)
        # change_size (data will change in range(-change_size, +change_size))
        # first_read: first sensor reading (has to be within s_range, defaults to random)
        # trend (up for sensor data trending upwards, down, defaults to random) prefferably trend should be lower than change_size
        self.name = name
        self.s_range = s_range
        self.change_size = change_size
        self.first_read = first_read
        self.data = None
        self.trend = [0, 0, 0]
        self.bias = bias
         
    def timestamp(self):
        stamp  = str(datetime.now())
        return stamp[0:19]
    
    def first_r(self):
        if self.first_read:
            self.first_read = self.first_read
        else:
            self.first_read = random.randrange(self.s_range[0], self.s_range[1])
        return self.first_read
    
    def read(self):
        if self.data == None:
            self.data = self.first_r()
        random_change = random.randrange(0-self.change_size, self.change_size + 1)
        self.trend.append(random_change)
        self.trend.pop(0)
        change = sum(self.trend)/float(len(self.trend)) + self.bias
        self.data = self.data + change
        
        if self.data < self.s_range[0]:
            self.data = self.s_range[0] + self.change_size/2
        elif self.data > self.s_range[1]:
            self.data = self.s_range[1] - self.change_size/2
        return change, int(self.data), self.timestamp()  

            
if __name__ == '__main__':
    from sensor_data_generator import Sensor

    #s = Sensor((-10, 30)) 
    #s.first_r()
    #print(s.first_read)

    t = Sensor('temp', s_range = (-10.0, 30.0), change_size = 3.0, first_read = 15, bias = 0) 
    h = Sensor('humidity', s_range = (5, 95), change_size = 5.0, bias = 0.2) 

    while True: 
        msg = {'Timestamp': t.read()[2], 'Temperature' : t.read()[1] , 'Humidity': h.read()[1] }
        mqtt_msg = json.dumps(msg)
        print(msg)
        time.sleep(1)
    




