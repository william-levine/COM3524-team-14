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
    config.states = (0,1,2,3,4,5,6,7,8)
    

    # 0 = chapparal
    # 1 = forest 
    # 2 = lake
    # 3 = canyon
    # 4 = town
    # 5 = burning state
    # 6 = burnt state
    # 7 = might burn
    # 8 = extinguished


    config.state_colors = [
        (0.70, 0.59, 0.02),   # chaparral
        (0, 0.5, 0.05),       # forest 
        (0.67, 0.85, 0.90),   # lake
        (0.9, 0.85, 0.00),    # canyon
        (0.0, 0.0, 0.0),      # town 
        (1, 0.3, 0),          # burning state
        (0.3, 0.2, 0),        # burnt state
        (1.0, 0.984, 0),      # burnt state
        (0.612, 0.612, 0.612) # extinguished state


    ]
  
    ####################################################
    # the GUI calls this to pass the user defined config
    # into the main system with an extra argument
    # do not change
    if len(args) == 2:
        config.save()
        sys.exit()
    
    initial_grid = config.initial_grid
    config.water_drop_left = 200

    return config

# printed = False

def transition_function(grid, neighbourstates, neighbourcounts, burnt_decay_grid, config, mightburn_grid, numgen):
    """Function to apply the transition rules
    and return the new grid"""
    # YOUR CODE HERE


    town_burn = False
    # STATES
    CHAPARRAL= 0 
    FOREST = 1
    LAKE = 2
    CANYON = 3
    TOWN = 4
    BURNING = 5
    BURNT = 6
    MIGHT_BURN = 7
    EXTINGUISHED = 8

    #Burn Duration
    # 1 iteration = 1 hour 
    BURN_DURATION = {    
        CHAPARRAL: 30,    # 30 points deducted for each iteration (will last 168 iterations/ 7 days)
        FOREST: 7,        # 7 points deducted for each iteration (will last 720 iterations/ 30 days)
        LAKE: 0,
        CANYON: 420,       # 420 points deducted for each iteration (will last 12 iteration/ 1/2 day) 
        TOWN: 5040
    }

    #Ignite probability
    IGNITE_PROB = {
        CHAPARRAL : 0.6,
        FOREST : 0.1,
        LAKE : 0.0,
        CANYON : 0.9,
        TOWN : 1.0
    }

    MAX_BURN_PROB = 0.9 # not 1 as it will then become deterministic and won't be as realistic

    """ adjacent neighbours have a more intersecting surface points 
    than corner neighbours, so the probability is higher for 
    the adjacent neighbours """

    # NW, N, NE, W, E, SW, S, SE = neighbourstates
    # EXTRA_IGNITION = {
    #     N,W,E,S : 1,
    #     NW,NE,SW,SE : 0.5
    # }

    # 0:NW, 1:N, 2:NE, 3:W, 4:E, 5:SW, 6:S, 7:SE = neighbourstates
    wind_direction = config.wind_direction
    wind_weight = config.wind_weight

    # print(f"Direction: {wind_direction}")

    # neighbourcounts stores the number of neighbour for each state
    chaparral, forest, lake, canyon, town, burning, burnt, might_burn, extinguished = neighbourcounts
    notburning = (chaparral, forest, lake,canyon)

    # cells that will burn in the next iteration will be shown as yellow
    initial_grid = config.initial_grid
    will_burn = (grid == MIGHT_BURN ) & (burning>0)
    mightburn_grid[will_burn] -= 1
    burning_grid = (mightburn_grid == 0)
    grid[burning_grid] = 5
    mightburn_grid[burning_grid] = 1

    # burning logic 
    for terrain in (CHAPARRAL, FOREST, LAKE,  CANYON, TOWN):
        prob = IGNITE_PROB[terrain]
       
        if prob == 0:
            continue #skip lake
        
        # prob = np.where(grid == EXTINGUISHED, IGNITE_PROB[terrain]*0.2, IGNITE_PROB[terrain])

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
        burning_bias = burning * 0.05
        wind_bias = wind_weight / 5

        # probability must account for:
        #   material 'flammability'
        #   number of burning neighbours
        #   wind
        adjusted_prob = np.where(
            wind_increased,
            np.minimum((prob + burning_bias) + wind_bias, MAX_BURN_PROB),
            np.minimum(prob + burning_bias, MAX_BURN_PROB))
        
        final_prob = np.where(
            wind_decreased,
            np.maximum((prob + burning_bias) - wind_bias, 0.1),
            adjusted_prob)

        # method to decide to burn
        rand = np.random.random()
        ignite = adjacency & (rand < final_prob)
        # reignition after cells have been extinguished
        extinguished = (initial_grid == terrain) & (grid == EXTINGUISHED) & (burning>0)
        reignition = extinguished & (rand < (final_prob * 0.1))

    
        # duration of burning 
        burning_duration = BURN_DURATION[terrain]
        post_burning = ( grid == BURNING ) & (initial_grid == terrain)
        burnt_decay_grid[post_burning] -= burning_duration
        decayed_to_zero = (burnt_decay_grid == 0)

        config.gen_town = numgen
        
        # starts the water drop after certain iteration
        if (numgen > config.water_drop) & config.start_drop & (config.water_drop_left > 0): 
            grid = water_intervention(grid, might_burn, burning,config)

        # cells that will turn into burning state
        # ignite = adjacency & (rand < final_prob)
        will_not_burn = (grid == MIGHT_BURN) & (burning < 1) & (initial_grid == terrain)

        grid[will_not_burn] = terrain
        grid[decayed_to_zero] = BURNT
    
        # if water drop has not been enabled burn like before
        if config.start_drop:
            grid[ignite] = MIGHT_BURN
            grid[reignition] = BURNING
        else:
            grid[ignite] = BURNING


        fire_reached_town = (grid == TOWN) & (neighbourcounts[5] > 0)
        no_fire_left = not (grid == 5).any()
        if (fire_reached_town.any() == True) or no_fire_left :
            town_burn = True

        fire_reached_town = (grid == TOWN) & (neighbourcounts[5] > 0)

        if (fire_reached_town.any() == True) or no_fire_left :
            town_burn = True
        
    return grid , town_burn

def water_intervention(grid, might_burn, burning, config):
    
    BURNING = 5
    EXTINGUISHED = 8 
    extinguish_grid = grid.copy()
    # fire to be extinguish
    to_extinguish = (grid == BURNING) & (might_burn>0)
    # if no fire to be extinguished
    if not grid[to_extinguish].all():
        return grid
    
    # grid coordinate
    rows, cols = np.indices(grid.shape)
    # town row and location
    trow, tcol = 175, 55
    # calculating the distance of town to each cell
    dist_from_town = np.sqrt((rows-trow)**2 + (cols-tcol)**2)
    # total distance travel for helicopter 
    total_distance_travelled = 0

    # max dist for one iteration/ one hour
    no_load_speed = 257 # km/h
    with_load_speed = 180 # km/h
    distance_to_fire = 50 # km
    # time for helicopter to make a round trip
    round_trip_time =((1/no_load_speed + 1/with_load_speed )*distance_to_fire) 
    # number of trip that can be made in one hour
    roundtrip_per_iter = 1/round_trip_time
    # maximum distance helicopter can cover in one hour
    max_dist = distance_to_fire*2*roundtrip_per_iter*4  #1km = 4 cell


    # keep extinguishing fire while distance is not maxed out
    while total_distance_travelled < max_dist:
        to_extinguish = (grid == BURNING) & (burning>0)
        num_of_cell = np.sum(grid[to_extinguish])
        # more than 1 cell need to be extinguished
        if num_of_cell > 1:
            min_dist = dist_from_town[to_extinguish].min()
        else:
            min_dist = dist_from_town[to_extinguish]
        # the coordinate of the nearest cell to extinguish
        if min_dist.size >0:
            distance_to_fire = min_dist
            coords = np.where(dist_from_town == min_dist)
            # go and return to town distance ( to refill water )
            total_distance_travelled += min_dist*2
            extinguish_grid[coords] = EXTINGUISHED
            # only extinguish cells that are burning and 
            # not every cell that is in a certain radius from town 
            extinguishing = (extinguish_grid == EXTINGUISHED) & (grid == BURNING)
            grid[extinguishing] = EXTINGUISHED
            config.water_drop_left -= 1
        else :
            return grid

    return grid

def main():
    """ Main function that sets up, runs and saves CA"""
    # Get the config object from set up
    config = setup(sys.argv[1:])
    
    #initialise the decay grid 
    burnt_decay_grid = np.zeros(config.grid_dims)
    mightburn_grid = np.zeros(config.grid_dims)

    """420 because it is the least common multiple for 60 and 14.
    the burning duration kinda work like merit point,
    for each iteration, 7 points will be deducted from
    forest element, once it reaches 0 (basically after 60 iteration),
    it will go to burnt state, same for other element"""
    burnt_decay_grid.fill(5040)
    mightburn_grid.fill(1)

    # Create grid object using parameters from config + transition function
    grid = Grid2D(config, (transition_function, burnt_decay_grid, config, mightburn_grid))


    # Run the CA, save grid state every generation to timeline
    timeline = grid.run()

    # Save updated config to file
    config.save()
    # Save timeline to file
    utils.save(timeline, config.timeline_path)
    # print("transition function",transition_function)

if __name__ == "__main__":
    main()
