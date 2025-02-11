# VeRoLog_logistic_problem_solution 
This repository contains implementations of three optimization algorithms: Ant Colony Optimization (ACO), Genetic Algorithm (GA), and Particle Swarm Optimization (PSO) for solving logistics scheduling problems. The goal is to optimize the allocation of trucks and technicians to service locations while minimizing costs.
## Overview
The problem scenario is adapted from the VeRoLog Solver Challenge (http://www.verolog.eu/).  This work provides several optimization models capable of optimising the routing of deliveries and technicians, to meet customer availability so as to reduce the costs incurred the organisation. Customers purchase household appliances/machines from a vendor, after which the vendor needs to arrange delivery of the appliance within the delivery window provided by the customer, and schedule a technician to fit/install said appliance.
Algorithms Implemented

1. Ant Colony Optimization (ACO)

ACO is a probabilistic technique inspired by the behavior of ants seeking the shortest path between their colony and a food source. The implementation models the logistics problem by constructing solutions based on pheromone trails and heuristic information.

Pheromone update mechanism

Heuristic-based solution construction

Cost evaluation and minimization

File: ACO solution.py

2. Genetic Algorithm (GA)

GA is an evolutionary algorithm that mimics natural selection. It employs selection, crossover, and mutation to evolve high-quality solutions over multiple generations.

Tournament selection

Two-point crossover

Bit-flip mutation

Fitness function evaluation

File: GA solution.py

3. Particle Swarm Optimization (PSO)

PSO is inspired by swarm intelligence, where particles (solutions) move within a search space to find the optimal configuration based on personal and global best positions.

Velocity and position update mechanism

Inertia weight and acceleration coefficients

Personal and global best tracking

File: PSO solution.py

Problem Description

The problem involves scheduling logistics for multiple locations, considering:

Truck capacity and distance limits

Technician allocation

Minimization of total cost, including truck and technician costs

The algorithms use a cost function that accounts for:

Distance costs

Idle machine costs

Number of trucks and technicians used

Dependencies

Python 3.x

NumPy

DEAP (for Genetic Algorithm)

To install dependencies, run:

``` pip install numpy deap```

Usage

Each algorithm is implemented as a standalone script.
Run any of the algorithms using:

``` python ACO solution.py
``` python GA solution.py
``` python PSO solution.py

Output Format

Each script prints a summary of the optimized logistics schedule:

``` SOLUTION SUMMARY:
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
NUMBER_OF_TECHNICIANS = <value>
