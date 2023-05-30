import time

from matplotlib import figure

import PID
import elevator

import matplotlib.pyplot as plt

if __name__ == '__main__':
    target = 10
    pid = PID.PID(1, 8.005, 0)
    elev = elevator.Elevator()

    # pid = PID.PID(1, 0, 0)
    # elev = elevator.AccelerationElevator()

    pid.target = target
    results = []
    velocities = []
    accelerations = []
    line = []
    zero = []
    time = []
    ctime = 0
    pVals = []
    iVals = []
    dVals = []

    dtime = 0.01
    for j in range(5000):
        v, p, i, d = pid.update(elev.position, dtime)
        elev.changeSpeed(v)
        elev.update(dtime)

        velocities.append(elev.velocity)
        line.append(target)
        zero.append(0)
        results.append(elev.position)
        accelerations.append(elev.acceleration)
        ctime += dtime
        time.append(ctime)
        pVals.append(p)
        iVals.append(i)
        dVals.append(d)

    print("Max height: " + str(max(results)))
    firstReached = next(i for i,v in enumerate(results) if v >= 10)
    print("Seconds to reach first time: " + str(time[firstReached]))

    firstInTolerance = next(i for i,v in enumerate(reversed(results)) if v >= 10.001)
    print("Seconds to reach second time with .001 tolerance: " + str(time[len(time)-firstInTolerance]))

    plt.figure(1)

    plt.plot(time, results, label="Position")
    plt.plot(time, line, label="Ideal", linewidth=0.8)
    plt.legend()

    plt.figure(2)

    plt.subplot(2, 1, 1)
    plt.plot(time, velocities, label="Velocity")
    plt.plot(time, accelerations, label="Acceleration")
    plt.plot(time, zero, linewidth=0.8)

    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(time, zero, linewidth=0.8)

    plt.plot(time, pVals, label="P")
    plt.plot(time, iVals, label="I")
    plt.plot(time, dVals, label="D")
    plt.legend()

    plt.show()
