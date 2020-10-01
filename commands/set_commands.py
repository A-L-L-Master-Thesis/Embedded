class SetCommands():
    def __init__(self, command):
        self.command = command
        
    def speed(self, x: int):
        """
        description: set speed to x cm/s x: 10-100
        response: ok, error
        """
        return self.command(f'speed {x}')
        
    def rc_control(self, a, b, c, d):
        """
        description: Send RC control via four channels.
                    a: left/right (-100~100)
                    b: forward/backward (-100~100)
                    c: up/down (-100~100)
                    d: yaw (-100~100)
        response: ok, error
        """
        return self.command(f'rc {a} {b} {c} {d}')
        
    def wifi(self, ssid: str, psw: str):
        """
        description: Set Wi-Fi with SSID password
        response: ok, error
        """
        return self.command(f'wifi {ssid} {psw}')