import time

import PID
import elevator

import matplotlib.pyplot as plt


if __name__ == '__main__':
    target = 10
    pid = PID.PID(4, 10, 1, 0)
    pid.target = target
    elev = elevator.Elevator()
    results = []
    velocities = []
    line = []
    time = []
    ctime = 0
    pVals = []
    iVals = []
    dVals = []

    dtime = 0.1
    for j in range(500):
        v, p,i,d = pid.update(elev.position, dtime)
        elev.changeVelocity(v)
        elev.update(dtime)

        velocities.append(v)
        line.append(target)
        results.append(elev.position)
        ctime += dtime
        time.append(ctime)
        pVals.append(p)
        iVals.append(i)
        dVals.append(d)
        # print(elev.position)
        # time.sleep(dtime)

    #plt.subplot(2,1,1)
    plt.plot(time, results, label= "Position")
    plt.plot(time, velocities, label="Velocity")
    plt.plot(time, line, label="Ideal", linewidth=0.8)
    plt.plot(time, pVals, label="P")
    plt.plot(time, iVals, label="I")
    plt.plot(time, dVals, label="D")
    plt.legend()
    #plt.subplot(2,1,2)
#
    #plt.plot(time, results)

    plt.show()


