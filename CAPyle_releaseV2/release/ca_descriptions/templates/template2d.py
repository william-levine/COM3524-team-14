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

    # 0 = no element 
    # 1 = forest 
    # 2 = lake
    # 3 = chapparal
    # 4 = canyon 
    # 5 = burning state
    # 6 = burnt state
    # -------------------------------------------------------------------------

    # ---- Override the defaults below (these may be changed at anytime) ----

    config.state_colors = [
        (1,1,1),            # no element/ white background
        (0,1,0),            # forest 
        (0.67,0.85,0.90),   # lake
        (0.70,0.59,0.02),   # chaparral
        (0.0,0.70,0.54),    # canyon
        (1,0.3,0),          # burning state
        (0,0,0)             # burnt state
    ]
    # config.grid_dims = (200,200)

    # ----------------------------------------------------------------------
    config.fill_in_defaults()
    POWER_STATION = "LEFT" # "RIGHT"

    if POWER_STATION == "LEFT":
        config.initial_grid[0,0] = 5
    elif POWER_STATION == "RIGHT":
        config.initial_grid[0,-1] = 5

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
    NO_ELEMENT=0 
    FOREST = 1
    LAKE = 2
    CHAPARRAL = 3
    CANYON = 4
    BURNING = 5
    BURNT = 6

    #Ignite probability
    IGNITE_PROB = {
        NO_ELEMENT: 0.9,
        FOREST: 0.1,
        LAKE: 0.0,
        CHAPARRAL: 0.5,
        CANYON: 0.7
    }

    #Burn Duration
    # 1 iteration = 1/2 day
    BURN_DURATION = {
        NO_ELEMENT:30,
        FOREST: 60,        #30 days
        LAKE: 0,
        CHAPARRAL: 14,     #7 days
        CANYON: 1          #1/2 day
    }
    
    burning_neighbours = neighbourcounts[BURNING]

    #new grid bcz some cells change state, some don't
    current = grid.copy()
    new_grid = grid.copy()

    for terrain in (NO_ELEMENT, FOREST, LAKE, CHAPARRAL, CANYON):

        prob = IGNITE_PROB[terrain]
        if prob == 0:
            continue #skip lake

        # find cells that will burn
        adjacency = (current == terrain) & (burning_neighbours>0)

        # method to decide to burn
        rand = np.random.random(grid.shape)
        ignite = adjacency & (rand <prob)

        # ignite
        new_grid[ignite] = BURNING
        new_grid [grid == BURNING] = BURNING

    return new_grid

def main():
    """ Main function that sets up, runs and saves CA"""
    # Get the config object from set up
    config = setup(sys.argv[1:])

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
