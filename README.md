# COM 3524 Team 14 – System Tools

This repository contains the source code and documentation for the system tools developed by team 14 for the COM3524 assignment. In this project, we adapted Conway's game of Life of cellular Automata to Model a Forest Fire spread. We used moore neighbourhood also multi-state to demonstrate the model of environment of different terrain (chaparral, forest, canyon, lake, town) and other states such as, will burn, burning, burnt and extinguished. The simulation will stop running when the fire reach the town or the are no fire left to be extinguished. The last iteration will either show no fire left or fire have reached one of the edges of the town. Number of hours can be obtain by looking at the most bottom slider. You can move the slider to see how the fire moves water dropped in every iterations.

Also, they are few parameters that can be changes which are wind directions and wind speed to see how it affects the fire spread. We also implemented water drops to help in reducing the fire spread as short term interventions. The water drop can start at a later i

use > 400 generations so the fire can reach town, fewer may make the simulation appear stuck

## Features

- Cross-platform support (Linux, macOS, Windows)
- Modular, extensible design for course assignments

---
## Prerequisites
Before starting, ensure the following softwares and tools are installed on your machine:

- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Python package manager for installing necessary dependencies)
- Git (to clone this repository)


###  Docker Desktop
Download and install Docker Desktop:  
[https://www.docker.com/products/docker-desktop/]

###  X11 Server
| Platform | Tool     | Link                                      |
|----------|----------|-------------------------------------------|
| Windows  | VcXsrv   | [VcXsrv Download](https://sourceforge.net/projects/vcxsrv/) |
| macOS    | XQuartz  | [XQuartz Download](https://www.xquartz.org/) |
| Linux    | Built-in | Usually pre-installed with the system     |

---

## Author 
Ayesha Sana, Sharifah Anisah, Nurul Amilah, William Levine, Szymon emczyk Department of Computer Science  
