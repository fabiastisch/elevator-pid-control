class Elevator:
    def __init__(self):
        self.velocity = 1
        self.position = 0
        self.gravity = 9.82
        self.friction = 0.9
        self.acceleration = 0

    def update(self, dtime: float):
        self.position += self.friction * self.velocity * dtime
        # print("Velocity " + str(self.velocity))

    def changeSpeed(self, velocity):
        max = 1.6
        if velocity > max:
            self.velocity = max
        elif velocity < -max:
            self.velocity = -max
        else:
            self.velocity = velocity


class AccelerationElevator:
    def __init__(self):
        self.velocity = 0
        self.acceleration = 0
        self.position = 0
        self.gravity = 9.82
        self.friction = 0.9

    def update(self, dtime: float):
        self.velocity += self.friction * (self.acceleration - self.gravity) * dtime
        self.position += self.velocity * dtime

    def changeSpeed(self, acceleration):
        acceleration += self.gravity
        max = 20
        # if acceleration > max:
        #    self.acceleration = max
        # elif acceleration < -max:
        #    self.acceleration = -max
        # else:
        self.acceleration = acceleration
