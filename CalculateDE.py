import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
g = 9.8
L = 2
airResistance = 0.1
theta_0 = np.pi/4  # starts at 60 degrees
theta_dot_0 = 20  # starts with angular velocity 0
t = 10000
xar = []
yar = []


def acceleration(theta, theta_dot):
    return -airResistance*theta_dot - (g/L) * np.sin(theta)


def step():
    #Initializing basics stuff

    theta = theta_0
    theta_dot = theta_dot_0
    delta_step = 0.1


    #Loop to update and save interval states of theta

    for time in range(0, t):
        theta += theta_dot * delta_step
        theta_dot += acceleration(theta, theta_dot)
        print(theta)
        print(theta_dot)
        xar.append(theta)
        yar.append(theta_dot)

    drawGraph()
    return theta, theta_dot


def drawGraph():
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)



    ax1.clear()
    ax1.plot(xar, yar)
    plt.show()


print(step())
