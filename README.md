# COM 3524 Team 14 – System Tools

This repository contains the source code and documentation for the system tools developed by team 14 for the COM3524 assignment. In this project, we adapted Conway's game of Life of cellular Automata to Model a Forest Fire spread. We used moore neighbourhood also multi-state to demonstrate the model of environment of different terrain (chaparral, forest, canyon, lake, town) and other states such as, will burn, burning, burnt and extinguished. The simulation will stop running when the fire reach the town or the are no fire left to be extinguished. The last iteration will either show no fire left or fire have reached one of the edges of the town. Number of hours can be obtain by looking at the most bottom slider. You can move the slider to see how the fire moves water dropped in every iterations.

Also, they are few parameters that can be changes which are wind directions and wind speed to see how it affects the fire spread. We also implemented water drops to help in reducing the fire spread as short term interventions. 

## Notes
- use > 400 generations so the fire can reach town, fewer may make the simulation appear stuck
- Please refer to the colour section to see what's happening in the simulation!.

## Prerequisites
Before starting, follow the steps in this github :

https://github.com/ac1asana/COM3524 


## Running the program 
- after you have run run_tool.py, choose option 1. 
- Then a GUI pop up called capyle will appear on your screen (if not, look at the task bar ). 
- Then choose the tab "File" on the upper left corner of the GUI. 
- After that, click the option "Open" where a new pop up will appear.
- Then, to choose the file to open, click the templates folder, and click on template2d.py and click open.
- Change the parameter value as you'd like and click on the "Apply configuration & run CA" to run the simulation
- Wait for the progress bar ( it will not reach the end for certain scenario, dont worry about this, the program still works)
- After the landscape have shown, click on the play button to see how the simulation goes

## Default value of the parameter in the simulation 

<img src="init_configuration.png" alt="How the simulation would look when you first open it " width="600"/>

- When the simulation first appear, the default value would be 500 for generations, this means the iteration will be looped for 500 times. This is the optimal number to see how the fire progress and if it reaches town or not without the simulation seemingly stoppped midway. 

- The default value for wind direction will be random but its wind speed will be 0.0 as the default value. 

- Water drop would also be enabled by default and you can choose to disable it and see how the fire would spread to town with no short term prevention. And to show how the water successfully prevented the fire, the default value for when the water will start to drop is after 12 iterations

- All the colour of the state are shown in the left side of the GUI and can be changed according to your preferences. 

 ## Explanation about the simulation
 - The water drop can start at a later iteration where fire might not be contained and will reach town 
 - The water drop is limited to 12.5 km^2 of area. Therefore, if the water dropped after a certain later hours, the fire will not be contained and the extinguished area would be reignited again. 

## Author 
Ayesha Sana, Sharifah Anisah, Nurul Amilah, William Levine, Szymon emczyk Department of Computer Science  
