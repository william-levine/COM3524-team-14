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

from capyle.ca import Grid2D, Neighbourhood, randomise2d
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

    # 0 = chapparal
    # 1 = forest 
    # 2 = lake
    # 3 = canyon
    # 4 = town
    # 5 = burning state
    # 6 = burnt state

    config.state_colors = [
        (0.70,0.59,0.02),   # chaparral
        (0,1,0),            # forest 
        (0.67,0.85,0.90),   # lake
        (0.0,0.70,0.54),    # canyon
        (0.48,0.24,0),      # town 
        (1,0.3,0),          # burning state
        (0,0,0)             # burnt state

    ]
  
    ####################################################
    # the GUI calls this to pass the user defined config
    # into the main system with an extra argument
    # do not change
    if len(args) == 2:
        config.save()
        sys.exit()
    return config

def transition_function(grid, neighbourstates, neighbourcounts):
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
        CHAPARRAL: 14,     #7 days
        FOREST: 60,        #30 days
        LAKE: 0,
        CANYON: 1          #1/2 day
    }

    #Ignite probability
    IGNITE_PROB = {
        0 : 0.6,
        1 : 0.1,
        2 : 0.0,
        3 : 0.9
    }


    # neighbourcounts stores the number of neighbour for each state
    chaparral, forest, lake, canyon, town, burning, burnt = neighbourcounts
    notburning = (chaparral, forest, lake,canyon)

    # burning logic 
    for terrain in (CHAPARRAL, FOREST, LAKE,  CANYON):
        prob = IGNITE_PROB[terrain]
        if prob == 0:
            continue #skip lake

        # find cells that will burn
        adjacency = (grid == terrain) & (burning>0)
        # burning_duration = BURN_DURATION[terrain]
        # burnt_state = ( grid == burning )  
        adjusted_prob = np.min((burning * 0.05) + prob, 1)

        # method to decide to burn
        rand = np.random.random()
        ignite = adjacency & (rand < adjusted_prob)

        # ignite
        grid[ignite] = 5
    
    return grid


def main():
    """ Main function that sets up, runs and saves CA"""
    # Get the config object from set up
    config = setup(sys.argv[1:])
    
    #initialise the decay grid 
    # decaygrid = np.zeros(config.grid_dims)
    # decaygrid.fill(2)

    # Create grid object using parameters from config + transition function
    grid = Grid2D(config, transition_function)

    # Run the CA, save grid state every generation to timeline
    timeline = grid.run()

    # Save updated config to file
    config.save()
    # Save timeline to file
    utils.save(timeline, config.timeline_path)

if __name__ == "__main__":
    main()
