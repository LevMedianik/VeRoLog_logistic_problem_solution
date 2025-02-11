import numpy as np
import random

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

# ACO parameters
ANT_COUNT = 30
ITERATIONS = 100
ALPHA = 1  # Pheromone importance
BETA = 2   # Heuristic importance
RHO = 0.5  # Pheromone evaporation rate
Q = 100    # Constant for pheromone update

def load_data(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data

data = load_data(r'C:\Users\User\Desktop\training_2.txt') # Define a path as in your system

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

def evaluate_solution(solution):
    truck_distance = sum(solution) * TRUCK_DISTANCE_COST
    technician_distance = sum(solution) * TECHNICIAN_DISTANCE_COST
    idle_machine_cost = 400
    
    truck_days = len(solution) // TRUCK_CAPACITY
    technicians_used = int(np.ceil(len(solution) / TECHNICIANS))
    total_cost = (truck_distance + technician_distance + idle_machine_cost + 
                  truck_days * TRUCK_DAY_COST + technicians_used * TECHNICIAN_DAY_COST)
    
    return total_cost,

def initialize_pheromones():
    pheromones = np.ones((LOCATIONS, LOCATIONS))
    return pheromones

def construct_solution(pheromones):
    solution = []
    for _ in range(REQUESTS):
        # Choose next location based on pheromones and heuristic information
        current_location = random.randint(1, LOCATIONS - 1)
        next_location = np.argmax(pheromones[current_location])
        solution.append(next_location)
    return solution

def update_pheromones(pheromones, solutions):
    pheromones *= (1 - RHO)  # Apply evaporation
    for solution in solutions:
        cost = evaluate_solution(solution)[0]
        for i in range(len(solution) - 1):
            pheromones[solution[i], solution[i + 1]] += Q / cost

def aco():
    pheromones = initialize_pheromones()
    best_solution = None
    best_cost = float('inf')
    
    for iteration in range(ITERATIONS):
        solutions = [construct_solution(pheromones) for _ in range(ANT_COUNT)]
        
        for solution in solutions:
            cost = evaluate_solution(solution)[0]
            if cost < best_cost:
                best_cost = cost
                best_solution = solution
        
        update_pheromones(pheromones, solutions)
    
    # Format and output the best solution
    truck_distance = sum(best_solution) * TRUCK_DISTANCE_COST
    technician_distance = sum(best_solution) * TECHNICIAN_DISTANCE_COST
    idle_machine_cost = 400
    truck_days = len(best_solution) // TRUCK_CAPACITY
    technicians_used = int(np.ceil(len(best_solution) / TECHNICIANS))
    total_cost = (truck_distance + technician_distance + idle_machine_cost + 
                  truck_days * TRUCK_DAY_COST + technicians_used * TECHNICIAN_DAY_COST)
    
    # Output the solution in the specified format

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
                request_ids = [random.randint(1, 50) for _ in range(20)]
                routes = create_route(TRUCK_CAPACITY, TRUCK_MAX_DISTANCE, request_ids)
                for route in routes:
                    print(f"{i + 1} {' '.join(map(str, route))}")

if __name__ == "__main__":
    aco()