# Import the necessary packages
import numpy as np
import matplotlib.pyplot as plt
import os

# On and off values
ON = 1
OFF = 0
vals = [ON, OFF]
cwd = os.getcwd()

def randomGrid(N, seed):
    np.random.seed(seed)
    return np.random.choice(vals, N*N, p=[0.1, 0.9]).reshape(N,N)

def update(grid, N): 
    newGrid = grid.copy() 
    for i in range(N):
        for j in range(N):
            # Summing the neighboring 1's
            # Assuming the boundary conditions are in a torus
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
						grid[(i-1)%N, j] + grid[(i+1)%N, j] +
						grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
						grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])) 
            # Rules of the game
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON 
    grid[:] = newGrid[:]
    return grid

# Let the number of frames be 100 (100 moves)
numFrames = 500
FILES = os.listdir()
if ("averages.npy" not in FILES) and ("standard deviations.npy" not in FILES):
    # Let the grid be 100 * 100
    N = 100 
    
    # Number of ensembles
    numEns = 100
    
    
    seed_list=[]
    for i in range(numEns):
        seed_list.append((i+1)*4)
    
    grid = np.array([])
    stats = np.zeros((numEns,numFrames))
    counter = 0
    for i in range(numEns):
        grid = randomGrid(N, seed_list[i])
        stats[i][0] = stats[i][0] + np.sum(grid)
        for j in range(numFrames - 1):
            grid = update(grid,N)
            stats[i][j+1] = stats[i][j+1] + np.sum(grid)
        counter += 1
        print(str(counter) + " done")
    
    #%%
    ave = np.array([])
    std = np.array([])
    for i in range(numFrames):
        summ = 0
        arr = np.array([])
        for j in range(numEns):
            summ += stats[j][i]
            arr = np.append(arr, stats[j][i])
        ave = np.append(ave, summ/numEns)
        std = np.append(std, np.std(arr))
    #%%
    np.save("averages", ave)
    np.save("standard deviations", std)
else: 
    ave = np.load("averages.npy")
    std = np.load("standard deviations.npy")
#%%
x = np.array([])
for i in range(numFrames):
    x = np.append(x, i + 1)
plt.figure()
plt.errorbar(x,ave,yerr = std, ecolor = 'y', label = "Average population with standard deviation")
plt.grid()
plt.title("Average population of 100 different ensembles vs. evolution steps")
plt.xlabel("Evolution steps")
plt.ylabel("Average population")
plt.legend()
plt.show()