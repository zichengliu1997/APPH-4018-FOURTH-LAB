# Import the necessary packages
import numpy as np 
import matplotlib.animation as animation
import matplotlib.pyplot as plt


# On and off values
ON = 1
OFF = 0
vals = [ON, OFF]

def randomGrid(N): 
    np.random.seed(4)
    return np.random.choice(vals, N*N, p=[0.1, 0.9]).reshape(N, N) 

def update(frameNum, img, grid, N): 
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

	# Update the next frame
	img.set_data(newGrid) 
	grid[:] = newGrid[:] 
	return img, 



	
# Let the grid be 100 * 100
N = 100 
# Let the delay between frames be 200 ms
updateInterval = 50
# Let the number of frames be 100 (100 moves)
numFrames = 500
grid = np.array([]) 
grid = randomGrid(N)  
fig, ax = plt.subplots() 
img = ax.imshow(grid, interpolation='nearest') 
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), 
								frames = numFrames, 
								interval=updateInterval, 
								save_count=50,
                                repeat = False) 
ani.save("LIFE.mp4")
plt.show()
