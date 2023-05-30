import math
import time


class PID:

    def __init__(self, kp: float, tn: float, tv: float):
        self.kp = kp
        if tn == 0:
            self.ki = 0
        else:
            self.ki = kp / tn
        if tv == 0:
            self.kd = 0
        else:
            self.kd = kp / tv
        self.tau = 0
        self.target = 0
        self.last_time = time.time()
        self.e_last = 0
        self.e_sum = 0

    def cap(self, value, max, min):
        max = 2
        min = -2
        if value > max:
            value = max
        elif value < min:
            value = min
        return value



    def update(self, current: float, delta_time):
        ctime = time.time()
        e = self.target - current
        self.e_sum += e
        self.e_sum = self.cap(self.e_sum, 50,-50)

        p = self.kp * e
        i = self.ki * self.e_sum
        d = self.kd * (e - self.e_last)

        u = p + i + d
        # u = self.cap(u, 2, -1)

        self.e_last = e
        return u, p, i, d
