from enums import DirectionEnum

class ControlCommands():
    def __init__(self, command):
        self.command = command
        
    def takeoff(self):
        """
        description: Tello auto takeoff
        response: ok, error
        """
        return self.command('takeoff')
        
    def land(self):
        """
        description: Tello auto land
        response: ok, error
        """
        return self.command('land')
        
    def streamon(self):
        """
        description: Set video stream on
        response: ok, error
        """
        return self.command('streamon')
        
    def streamoff(self):
        """
        description: Set video stream off
        response: ok, error
        """
        return self.command('streamoff')
        
    def emergency(self):
        """
        description: Stop all motors immediately
        response: ok, error
        """
        return self.command('emergency')
        
    def up(self, x: int):
        """
        description: Tello fly up with distance x cm x: 20-500
        response: ok, error
        """
        return self.command(f'up {x}')
        
    def down(self, x: int):
        """
        description: Tello fly down with distance x cm x: 20-500
        response: ok, error
        """
        return self.command(f'down {x}')
        
    def left(self, x: int):
        """
        description: Tello fly left with distance x cm x: 20-500
        response: ok, error
        """
        return self.command(f'left {x}')

    def right(self, x: int):
        """
        description: Tello fly right with distance x cm x: 20-500
        response: ok, error
        """
        return self.command(f'right {x}')
        
    def forward(self, x: int):
        """
        description: Tello fly forward with distance x cm x: 20-500
        response: ok, error
        """
        return self.command(f'forward {x}')
        
    def back(self, x: int):
        """
        description: Tello fly back with distance x cm x: 20-500
        response: ok, error
        """
        return self.command(f'back {x}')

    def clockwise(self, x: int):
        """
        description: Tello rotate x degree clockwise x: 1-3600
        response: ok, error
        """
        return self.command(f'cw {x}')
        
    def counter_clockwise(self, x: int):
        """
        description: Tello rotate x degree counter-clockwise x: 1-3600
        response: ok, error
        """
        return self.command(f'ccw {x}')
        
    def flip(self, direction: DirectionEnum):
        """
        description: Flip the Tello direction
        response: ok, error
        """
        return self.command(f'flip {direction}')
        
    def go(self, x: int, y: int, z: int, speed: int):
        """
        description: Tello fly to x y z in speed
        response: ok, error
        """
        return self.command(f'go {x} {y} {z} {speed}')
        
    def curve(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, speed: int):
        """
        description: Tello fly a curve defined by the current and two given coordinates with speed
        response: ok, error
        """
        return self.command(f'curve {x1} {y1} {z1} {x2} {y2} {z2} {speed}')



