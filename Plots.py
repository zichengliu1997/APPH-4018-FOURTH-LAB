import numpy as np
import matplotlib.pyplot as plt

averages = np.empty((0, 500))
x = np.array([])
for i in range(500):
        x = np.append(x, i + 1)


for i in range(4):
    percentage = round(0.1 + i*0.1, 1)
    ave = np.load("averages " + str(percentage) + " initial population.npy")
    std = np.load("standard deviations " + str(percentage) + " initial population.npy")
    averages = np.concatenate((averages, np.array([ave])), axis = 0)
    plt.figure()
    plt.errorbar(x,ave,yerr = std, ecolor = 'y', label = "Average population with standard deviation")
    plt.grid()
    plt.title("Average populations of 100 different ensembles vs. evolution steps (" + str(percentage*100) + "% initial)")
    plt.xlabel("Evolution steps")
    plt.ylim(0,4500)
    plt.ylabel("Average population")
    plt.legend()
    plt.show()

plt.figure()
plt.plot(x, averages[0], label = "10%")
plt.plot(x, averages[1], label = "20%")
plt.plot(x, averages[2], label = "30%", c = 'k')
plt.plot(x, averages[3], label = "40%")
plt.title("Average populations of 100 different ensembles of different initial conditions vs. evolution steps")
plt.xlabel("Evolution steps")
plt.ylabel("Average population")
plt.ylim(0,4500)
plt.legend()
plt.legend()
plt.grid()
plt.show()