# Name: Modelling Forest Fire
# Dimensions: 2

# --- Set up executable path, do not edit ---
import sys
import inspect
this_file_loc = (inspect.stack()[0][1])
main_dir_loc = this_file_loc[:this_file_loc.index('ca_descriptions')]
sys.path.append(main_dir_loc)
sys.path.append(main_dir_loc + 'capyle')
sys.path.append(main_dir_loc + 'capyle/ca')
sys.path.append(main_dir_loc + 'capyle/guicomponents')
# ---

from capyle.ca import Grid2D, Neighbourhood, randomise2d, CAConfig
import capyle.utils as utils
import numpy as np

def setup(args):
    """Set up the config object used to interact with the GUI"""
    config_path = args[0]
    config = utils.load(config_path)

    # -- THE CA MUST BE RELOADED IN THE GUI IF ANY OF THE BELOW ARE CHANGED --
    config.title = "Modelling Forest Fire"
    config.dimensions = 2
    config.states = (0,1,2,3,4,5,6)
    config.num_generations = 150
    

    # 0 = chapparal
    # 1 = forest 
    # 2 = lake
    # 3 = canyon
    # 4 = town
    # 5 = burning state
    # 6 = burnt state
    # 7 = town

    config.state_colors = [
        (0.70, 0.59, 0.02),   # chaparral
        (0, 0.5, 0.05),       # forest 
        (0.67, 0.85, 0.90),   # lake
        (0.9, 0.85, 0.00),    # canyon
        (0.0, 0.0, 0.0),      # town 
        (1, 0.3, 0),          # burning state
        (0.3, 0.2, 0)         # burnt state
    ]
  
    ####################################################
    # the GUI calls this to pass the user defined config
    # into the main system with an extra argument
    # do not change
    if len(args) == 2:
        config.save()
        sys.exit()
    
    initial_grid = config.initial_grid

    return config

def transition_function(grid, neighbourstates, neighbourcounts, decay_grid, config):
    """Function to apply the transition rules
    and return the new grid"""
    # YOUR CODE HERE

    # STATES
    CHAPARRAL= 0 
    FOREST = 1
    LAKE = 2
    CANYON = 3
    TOWN = 4
    BURNING = 5
    BURNT = 6

    #Burn Duration
    # 1 iteration = 1/2 day
    BURN_DURATION = {    
        CHAPARRAL: 30,    # 30 points deducted for each iteration (will last 14 iterations/ 7 days)
        FOREST: 7,        # 7 points deducted for each iteration (will last 60 iterations/ 30 days)
        LAKE: 0,
        CANYON: 420       # 420 points deducted for each iteration (will last 1 iteration/ 1/2 day) 
    }

    #Ignite probability
    IGNITE_PROB = {
        CHAPARRAL : 0.6,
        FOREST : 0.1,
        LAKE : 0.0,
        CANYON : 0.9
    }

    MAX_PROB = 0.9 # not 1 as it will then become deterministic and won't be as realistic

    """ adjacent neighbours have a more intersecting surface points 
    than corner neighbours, so the probability is higher for 
    the adjacent neighbours """

    # NW, N, NE, W, E, SW, S, SE = neighbourstates
    # EXTRA_IGNITION = {
    #     N,W,E,S : 1,
    #     NW,NE,SW,SE : 0.5
    # }


    # 0:NW, 1:N, 2:NE, 3:W, 4:E, 5:SW, 6:S, 7:SE = neighbourstates
    wind_direction = 6

    # neighbourcounts stores the number of neighbour for each state
    chaparral, forest, lake, canyon, town, burning, burnt = neighbourcounts
    notburning = (chaparral, forest, lake,canyon)

    initial_grid = config.initial_grid

    # burning logic 
    for terrain in (CHAPARRAL, FOREST, LAKE,  CANYON):
        prob = IGNITE_PROB[terrain]
        if prob == 0:
            continue #skip lake

        # find cells that will burn
        adjacency = (grid == terrain) & (burning > 0)

        # find cells affected by the wind
        upwind_neighbour_states = neighbourstates[np.abs(7 - wind_direction)]
        downwind_neighbour_states = neighbourstates[wind_direction] 

        # cells that have a higher chance of catching fire due to wind direction
        wind_increased = (grid == terrain) & (upwind_neighbour_states == BURNING)
        # cells that have a lower chance of catching fire due to wind direction
        wind_decreased = (grid == terrain) & (downwind_neighbour_states == BURNING)

        # additive terms depending on what factors affect the cell
        burning_increment = burning * 0.05
        wind_increment = 0.2

        # probability must account for:
        #   material 'flammability'
        #   number of burning neighbours
        #   wind
        adjusted_prob = np.where(
            wind_increased,
            np.minimum((burning_increment + prob) + wind_increment, MAX_PROB),
            np.minimum(burning_increment + prob, MAX_PROB))

        # method to decide to burn
        rand = np.random.random()
        ignite = adjacency & (rand < adjusted_prob)


        """as of now, fire dont spread if it is surrounded by burnt area"""
        # duration of burning 
        burning_duration = BURN_DURATION[terrain]
        ## to get the initial element of the cell after it burned (by looking at its neighbour state)
        #  a better way need to be found to get the initial state of the cell
        post_burning = ( grid == BURNING ) & (initial_grid == terrain)
        decay_grid[post_burning] -= burning_duration
        decayed_to_zero = (decay_grid == 0)


        
        grid[decayed_to_zero] = 6
        grid[ignite] = 5
        
    
    return grid


def main():
    """ Main function that sets up, runs and saves CA"""
    # Get the config object from set up
    config = setup(sys.argv[1:])
    
    #initialise the decay grid 
    decay_grid = np.zeros(config.grid_dims)

    """420 because it is the least common multiple for 60 and 14.
    the burning duration kinda work like merit point,
    for each iteration, 7 points will be deducted from
    forest element, once it reaches 0 (basically after 60 iteration),
    it will go to burnt state, same for other element"""
    decay_grid.fill(420)

    # Create grid object using parameters from config + transition function
    grid = Grid2D(config, (transition_function, decay_grid, config))

    # Run the CA, save grid state every generation to timeline
    timeline = grid.run()

    # Save updated config to file
    config.save()
    # Save timeline to file
    utils.save(timeline, config.timeline_path)
    # print("transition function",transition_function)

if __name__ == "__main__":
    main()
