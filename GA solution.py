import random
import numpy as np
from deap import base, creator, tools, algorithms

# Define parameters
DAYS = 7
TRUCK_CAPACITY = 15
TRUCK_MAX_DISTANCE = 2000

TRUCK_DISTANCE_COST = 1000
TRUCK_DAY_COST = 100000
TRUCK_COST = 10000
TECHNICIAN_DISTANCE_COST = 100
TECHNICIAN_DAY_COST = 10000
TECHNICIAN_COST = 10
MACHINES = 2
LOCATIONS = 53
REQUESTS = 150
TECHNICIANS = 50

# Load dataset
def load_data(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data

data = load_data(r'C:\Users\User\Desktop\training_2.txt') # Define a path as in your system

# Define GA components
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

def create_individual():
    individual = [random.randint(1, LOCATIONS - 1) for _ in range(REQUESTS)]
    return creator.Individual(individual)

def evaluate(individual):
    truck_distance = sum(individual) * TRUCK_DISTANCE_COST
    technician_distance = sum(individual) * TECHNICIAN_DISTANCE_COST
    idle_machine_cost = 400
    
    truck_days = len(individual) // TRUCK_CAPACITY  # Estimation based on capacity
    technicians_used = int(np.ceil(len(individual) / TECHNICIANS))
    total_cost = (truck_distance + technician_distance + idle_machine_cost + 
                  truck_days * TRUCK_DAY_COST + technicians_used * TECHNICIAN_DAY_COST)
    
    return total_cost,

toolbox = base.Toolbox()
toolbox.register("individual", create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register("evaluate", evaluate)

def create_route(truck_capacity, max_distance, request_ids):
    routes = []
    current_capacity = 0
    current_distance = 0
    route = []
    
    for request in request_ids:
        request_distance = random.randint(100, 500)
        
        if current_capacity + 1 <= truck_capacity and current_distance + request_distance <= max_distance:
            route.append(request)
            current_capacity += 1
            current_distance += request_distance
        else:
            routes.append(route + [0])
            route = [request]
            current_capacity = 1
            current_distance = request_distance
    
    if route:
        routes.append(route + [0])
    
    return routes

def ga():
    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1)

    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=50, 
                        halloffame=hof, verbose=False)

    best_solution = hof[0]
    best_cost = evaluate(best_solution)[0]

    # Format and output the solution summary
    truck_distance = sum(best_solution) * TRUCK_DISTANCE_COST
    technician_distance = sum(best_solution) * TECHNICIAN_DISTANCE_COST
    idle_machine_cost = 400
    
    truck_days = len(best_solution) // TRUCK_CAPACITY
    technicians_used = int(np.ceil(len(best_solution) / TECHNICIANS))
    total_cost = (truck_distance + technician_distance + idle_machine_cost + 
                  truck_days * TRUCK_DAY_COST + technicians_used * TECHNICIAN_DAY_COST)
    
    # Output the solution in the specified linear format

    print(f"SOLUTION SUMMARY:")
    print(f"TRUCK_DISTANCE = {truck_distance}")
    print(f"NUMBER_OF_TRUCK_DAYS = {truck_days}")
    print(f"NUMBER_OF_TRUCKS_USED = {1}")
    print(f"TECHNICIAN_DISTANCE = {technician_distance}")
    print(f"NUMBER_OF_TECHNICIAN_DAYS = {truck_days}")
    print(f"NUMBER_OF_TECHNICIANS_USED = {technicians_used}")
    print(f"IDLE_MACHINE_COSTS = {idle_machine_cost}")
    print(f"TOTAL_COST = {total_cost}")
    print(f"SCHEDULE DETAILS")
    
    for day in range(1, DAYS + 1):
        print(f"DAY = {day}")
        num_trucks = random.randint(0, 1)  # Adjust based on solution
        print(f"NUMBER_OF_TRUCKS = {num_trucks}")
        print(f"NUMBER_OF_TECHNICIANS = {random.randint(0, TECHNICIANS)}")
        
        if num_trucks > 0:
            for i in range(num_trucks):
                # Example: route generation based on capacity and distance
                request_ids = [random.randint(1, 50) for _ in range(20)]
                routes = create_route(TRUCK_CAPACITY, TRUCK_MAX_DISTANCE, request_ids)
                for route in routes:
                    print(f"{i + 1} {' '.join(map(str, route))}")

if __name__ == "__main__":
    ga()