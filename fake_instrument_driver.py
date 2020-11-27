import numpy as np
class Instrument:
    def __init__(self):
        self.ID = f'GPS{np.random.randint(1e6)}'
        self.heartbeat = True

    def get_measurement(self):
        latitude = 40*np.random.random() - 60
        longitude = 60*np.random.random() - 80
        return (latitude, longitude)