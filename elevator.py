class Elevator:
    def __init__(self):
        self.velocity = 1
        self.position = 0
        self.gravity = 9.82
        self.friction = 0.9

    def update(self, dtime: float):
        self.position += self.friction * self.velocity * dtime
        # print("Velocity " + str(self.velocity))

    def changeVelocity(self, velocity):
        self.velocity = velocity
