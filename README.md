# VeRoLog_logistic_problem_solution 
This repository contains implementations of three optimization algorithms: Ant Colony Optimization (ACO), Genetic Algorithm (GA), and Particle Swarm Optimization (PSO) for solving logistics scheduling problems. The goal is to optimize the allocation of trucks and technicians to service locations while minimizing costs.

## Overview
The problem scenario is adapted from the VeRoLog Solver Challenge (http://www.verolog.eu/).  This work provides several optimization models capable of optimising the routing of deliveries and technicians, to meet customer availability so as to reduce the costs incurred the organisation. Customers purchase household appliances/machines from a vendor, after which the vendor needs to arrange delivery of the appliance within the delivery window provided by the customer, and schedule a technician to fit/install said appliance.

## Dataset
The dataset training_2.txt contains structured sections defining the logistics constraints, such as truck/technician capacities, customer requests, and machine delivery/installation constraints.

1. General Problem Parameters
These are the fundamental constraints governing the optimization problem:

DAYS = N
The number of days in the planning period (e.g., DAYS = 10).

TRUCK_CAPACITY = X
Maximum number of machines a truck can carry (e.g., TRUCK_CAPACITY = 15).

TRUCK_MAX_DISTANCE = Y
Maximum distance a truck can travel in a day (e.g., TRUCK_MAX_DISTANCE = 2000).

Cost parameters:
TRUCK_DISTANCE_COST = A (Cost per unit distance traveled by a truck)
TRUCK_DAY_COST = B (Cost per truck per day)
TRUCK_COST = C (Fixed cost per truck over the planning period)
TECHNICIAN_DISTANCE_COST = D (Cost per unit distance traveled by a technician)
TECHNICIAN_DAY_COST = E (Cost per technician per day)
TECHNICIAN_COST = F (Fixed cost per technician over the planning period)

2. Machines Section
This section provides information about different machine types available for delivery.

Format:
MACHINES = K
Machine_ID  Size  Idle_Cost

Example:
MACHINES = 2
1 6 343
2 5 887

Where:
1: Machine type ID
6: Size of one machine (units)
343: Cost per day if the machine remains idle

3. Locations Section
This section provides coordinate locations for the depot, customers, and technicians' home locations.

Format:
LOCATIONS = M
Location_ID  X_Coordinate  Y_Coordinate
Example:

LOCATIONS = 54
1 699 335  # Depot (always Location ID = 1)
2 473 376  # Customer 1
3 546 621  # Customer 2

Where:
1: Location ID
699 335: (X, Y) coordinates of the location

4. Requests Section
This section lists all customer requests, including machine type, delivery window, and quantity.

Format:
REQUESTS = R
Request_ID  Customer_Location_ID  First_Day  Last_Day  Machine_ID  Quantity

Example:
REQUESTS = 150
1 8 1 6 1 1
2 46 1 2 1 1
3 12 1 3 1 2

Where:
1: Request ID
8: Customer location ID
1: First day of delivery window
6: Last day of delivery window
1: Machine type ID
1: Number of machines requested

5. Technicians Section
This section provides technician details, including location, working limits, and skill sets.

Format:
TECHNICIANS = T
Technician_ID  Home_Location_ID  Max_Distance  Max_Requests  Skill_1  Skill_2 ... Skill_N

Example:
TECHNICIANS = 50
1 40 529 9 0 1
2 1 995 9 0 1
3 1 1280 7 0 1

Where:
1: Technician ID
40: Home location ID
529: Maximum distance they can travel per day

9: Maximum number of requests they can handle per day
0 1: Skills (0 = cannot install, 1 = can install the respective machine type)

## Algorithms Implemented

**1. Ant Colony Optimization (ACO)**

ACO is a probabilistic technique inspired by the behavior of ants seeking the shortest path between their colony and a food source. The implementation models the logistics problem by constructing solutions based on pheromone trails and heuristic information. File: ACO solution.py

Parameters:
Pheromone update mechanism
Heuristic-based solution construction
Cost evaluation and minimization


**2. Genetic Algorithm (GA)**

GA is an evolutionary algorithm that mimics natural selection. It employs selection, crossover, and mutation to evolve high-quality solutions over multiple generations. File: GA solution.py

Parameters:
Tournament selection
Two-point crossover
Bit-flip mutation
Fitness function evaluation



**3. Particle Swarm Optimization (PSO)**

PSO is inspired by swarm intelligence, where particles (solutions) move within a search space to find the optimal configuration based on personal and global best positions. File: PSO solution.py

Parameters:
Velocity and position update mechanism
Inertia weight and acceleration coefficients
Personal and global best tracking

## Problem Description

The problem involves scheduling logistics for multiple locations, considering: truck capacity and distance limits; technician allocation; minimization of total cost, including truck and technician costs

The algorithms use a cost function that accounts for: distance costs; idle machine costs; number of trucks and technicians used

Dependencies:

-Python 3.x
-NumPy
-DEAP (for Genetic Algorithm)

To install dependencies, run:

``` pip install numpy deap```

Usage

Each algorithm is implemented as a standalone script.
Run any of the algorithms using:

```python ACO solution.py```
```python GA solution.py```
```python PSO solution.py```

Output Format

Each script prints a summary of the optimized logistics schedule:

```SOLUTION SUMMARY:
TRUCK_DISTANCE = <value>
NUMBER_OF_TRUCK_DAYS = <value>
NUMBER_OF_TRUCKS_USED = <value>
TECHNICIAN_DISTANCE = <value>
NUMBER_OF_TECHNICIAN_DAYS = <value>
NUMBER_OF_TECHNICIANS_USED = <value>
IDLE_MACHINE_COSTS = <value>
TOTAL_COST = <value>
SCHEDULE DETAILS
DAY = <value>
NUMBER_OF_TRUCKS = <value>
NUMBER_OF_TECHNICIANS = <value>```
