import sys
import numpy as np
from capyle.utils import save, get_metadata, scale_array, gens_to_dims
from capyle.ca import Neighbourhood


class CAConfig(object):
    ROOT_PATH = sys.path[0]

    def __init__(self, filepath):
        self.filepath = filepath
        # parse the file for the best guess of the dimensions and name
        self.title, self.dimensions = get_metadata(filepath)
        self.states = None
        self.grid_dims = None
        self.rule_num = None
        self.state_colors = None
        self.num_generations = None
        self.nhood_arr = None
        self.initial_grid = None
        # default wrapping behaviour is True
        self.wrap = False
        self.default_paths()
        self.start_fire = "RIGHT"  #by default
        self.gen_town = None
        self.enable_water = None
        self.start_drop = None
        self.water_drop = None
        self.water_drop_left = 200

    def fill_in_defaults(self):
        """ if any of the fields are not filled in in description
        they are filled in with defaults here """
        # rule number

        # number of generations
        if self.num_generations is None:
            self.num_generations = 100

        # grid dimensions
        if self.grid_dims is None:
            if self.dimensions == 2:
                self.grid_dims = (200, 200)
            else:
                self.grid_dims = gens_to_dims(self.num_generations)
            

        # initial grid with each element 
        if self.initial_grid is None:
            
            # provided in the template
            fillstate = self.states[0] if self.states is not None else 0
            self.rule_num = 0 if self.rule_num is None else self.rule_num  


            # use this to toggle the value between left and right position 
            POWER_STATION = self.start_fire

            # matrices for each element
            self.size = 10  # to resize every element at once
            self.forest = np.ones((8*self.size,3*self.size), dtype=type(fillstate))
            self.forest1 = np.ones((1*self.size,3*self.size), dtype=type(fillstate))
            self.forest2 = np.ones((4*self.size,8*self.size), dtype=type(fillstate))

            self.lake = np.full((4*self.size,1*self.size),2, dtype=type(fillstate))
            self.lake1 = np.full((1*self.size,6*self.size),2, dtype=type(fillstate))

            self.canyon = np.full((9*self.size,1*self.size),3, dtype=type(fillstate))

            self.town = np.full((1*self.size,1*self.size),4, dtype=type(fillstate))


            # provided in the template
            self.initial_grid = np.zeros(self.grid_dims, dtype=type(fillstate))  
            self.initial_grid.fill(fillstate)

            # positioning the element in a blank grid
            self.initial_grid[20:20+self.forest.shape[0], 20:20+self.forest.shape[1]]+= self.forest
            self.initial_grid[20:20+self.forest1.shape[0], 50:50+self.forest1.shape[1]]+= self.forest1
            self.initial_grid[100:100+self.forest2.shape[0], 20:20+self.forest2.shape[1]]+= self.forest2

            self.initial_grid[40:40+self.lake.shape[0], 70:70+self.lake.shape[1]]+= self.lake
            self.initial_grid[160:160+self.lake1.shape[0], 100:100+self.lake1.shape[1]]+= self.lake1

            self.initial_grid[40:40+self.canyon.shape[0], 140:140+self.canyon.shape[1]]+= self.canyon

            # positioning the town 
            self.initial_grid[175:175+self.town.shape[0], 55:55+self.town.shape[1]]+= self.town

            # for different position of power station
            if POWER_STATION == "LEFT":
                self.initial_grid[0,20] = 5
            elif POWER_STATION == "RIGHT":
                self.initial_grid[0,-10] = 5

        # neighbourhood array
        if self.nhood_arr is None:
            if self.dimensions == 2:
                self.nhood_arr = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
            else:
                self.nhood_arr = np.array([1, 1, 1])

    def default_paths(self):
        self.path = self.ROOT_PATH + '/temp/config.pkl'
        self.timeline_path = self.ROOT_PATH + '/temp/timeline.pkl'

    def neighbourhood(self):
        if self.nhood_arr is None:
            self.nhood_arr = [0, 1, 0]
        return Neighbourhood(self.nhood_arr, dims=self.dimensions)

    def save(self):
        save(self, self.path)

    def set_grid_dims(self, dims=None, num_generations=None):
        if dims is not None:
            i = dims[0] if dims[0] > 2 else 3
            j = dims[1] if dims[1] > 2 else 3
            self.grid_dims = i, j
        else:
            if num_generations < 1:
                num_generations = 1
            self.num_generations = num_generations
            self.grid_dims = gens_to_dims(self.num_generations)
        if self.initial_grid is not None:
            self.initial_grid = scale_array(self.initial_grid, *self.grid_dims)
        else:
            self.intitial_grid = np.zeros(self.grid_dims)

    def set_initial_grid(self, grid):
        if grid.shape[0] == 1:
            self.initial_grid[0] = np.copy(grid[0])
        else:
            self.initial_grid = np.copy(grid)
