# COM 3524 Team 14 – System Tools

This repository contains the source code and documentation for the system tools developed by team 14 for the COM3524 assignment. In this project, we adapted Conway's game of Life of cellular Automata to Model a Forest Fire spread. We used moore neighbourhood also multi-state to demonstrate the model of environment of different terrain (chaparral, forest, canyon, lake, town) and other states such as, will burn, burning, burnt and extinguished. The simulation will stop running when the fire reach the town or the are no fire left to be extinguished. The last iteration will either show no fire left or fire have reached one of the edges of the town. Number of hours can be obtain by looking at the most bottom slider. You can move the slider to see how the fire moves water dropped in every iterations.

Also, they are few parameters that can be changes which are wind directions and wind speed to see how it affects the fire spread. We also implemented water drops to help in reducing the fire spread as short term interventions. The water drop can start at a later iteration where fire might not be contained and will reach town 

use > 400 generations so the fire can reach town, fewer may make the simulation appear stuck

## Prerequisites
Before starting, follow the steps in this github :

https://github.com/ac1asana/COM3524 


## Running the program 
after you have run run_tool.py, choose option 1. Then a GUI pop up called capyle will appear on your screen (if not, look at the task bar ). Then choose the tab "File" on the upper left corner of the GUI. After that, click the option "Open" where a new pop up will appear. Then, to choose the file to open, click the templates folder, and click on template2d.py and click open.

## Running the simulation 

When the simulation first appear, the default value would be 500 for generations, this means the iteration will be looped for 500 times. This is the optimal number to see how the fire progress and if it reaches town or not without the simulation seemingly stoppped midway. The default value for wind direction will be random but its wind speed will be 0.0 as a de



## Author 
Ayesha Sana, Sharifah Anisah, Nurul Amilah, William Levine, Szymon emczyk Department of Computer Science  
