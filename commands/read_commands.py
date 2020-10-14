class ReadCommands():
    def __init__(self, command):
        self.command = command
        
    def speed(self):
        """
        description: get current speed (cm/s)
        response: int 1 - 100
        """
        return int(self.command(f'speed?'))
        
    def battery(self):
        """
        description: get current battery percentage
        response: int 1 - 100
        """
        return int(self.command(f'battery?'))
        
    def time(self):
        """
        description: get current fly time (s) 
        response: string time
        """
        return self.command(f'time?')
        
    def height(self):
        """
        description: get height (cm)
        response: int 0 - 3000
        """
        return int(self.command(f'height?'))
        
    def temp(self):
        """
        description: get temperature (℃)
        response: int 0 - 90
        """
        return int(self.command(f'temp?'))
        
    def attitude(self):
        """
        description: attitude
        response: pitch roll yaw
        """
        return self.command(f'attitude?')
        
    def baro(self):
        """
        description: get barometer value (m) 
        response: int
        """
        return int(self.command(f'baro?'))
        
    def acceleration(self):
        """
        description: get IMU angular acceleration data (0.001g)
        response: x y z
        """
        return self.command(f'acceleration?')

    def tof(self):
        """
        description: get distance value from TOF（cm）
        response: x: 30-1000
        """
        return int(self.command(f'tof?'))
        
    def wifi(self):
        """
        description: get Wi-Fi SNR
        response: SNR
        """
        return self.command(f'wifi?')