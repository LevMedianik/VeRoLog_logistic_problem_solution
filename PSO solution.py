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

# Define PSO parameters
PARTICLE_COUNT = 50
ITERATIONS = 100
W = 0.5  # Inertia weight
C1 = 0.2  # Personal best weight
C2 = 0.2  # Global best weight

def load_data(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data

data = load_data(r'C:\Users\User\Desktop\training_2.txt') # Define a path as in your system

def create_particle():
    return [random.randint(1, LOCATIONS - 1) for _ in range(REQUESTS)]

def evaluate_solution(solution):
    # Dummy evaluation function
    truck_distance = sum(solution) * TRUCK_DISTANCE_COST
    technician_distance = sum(solution) * TECHNICIAN_DISTANCE_COST
    idle_machine_cost = 400
    
    truck_days = len(solution) // TRUCK_CAPACITY
    technicians_used = int(np.ceil(len(solution) / TECHNICIANS))
    total_cost = (truck_distance + technician_distance + idle_machine_cost + 
                  truck_days * TRUCK_DAY_COST + technicians_used * TECHNICIAN_DAY_COST)
    
    return total_cost,

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

def pso():
    particles = [create_particle() for _ in range(PARTICLE_COUNT)]
    velocities = [np.random.rand(REQUESTS) for _ in range(PARTICLE_COUNT)]
    personal_best_positions = particles[:]
    personal_best_costs = [evaluate_solution(p)[0] for p in particles]
    global_best_position = personal_best_positions[np.argmin(personal_best_costs)]
    global_best_cost = min(personal_best_costs)
    
    for iteration in range(ITERATIONS):
        for i, particle in enumerate(particles):
            cost = evaluate_solution(particle)[0]
            
            if cost < personal_best_costs[i]:
                personal_best_positions[i] = particle
                personal_best_costs[i] = cost
                
            if cost < global_best_cost:
                global_best_position = particle
                global_best_cost = cost
        
        for i, particle in enumerate(particles):
            r1, r2 = np.random.rand(REQUESTS), np.random.rand(REQUESTS)
            velocities[i] = (W * velocities[i] +
                             C1 * r1 * (np.array(personal_best_positions[i]) - np.array(particle)) +
                             C2 * r2 * (np.array(global_best_position) - np.array(particle)))
            particles[i] = np.clip(np.array(particle) + velocities[i], 1, LOCATIONS - 1).astype(int)
    
    # Format and output the best solution
    best_solution = global_best_position
    best_cost = evaluate_solution(best_solution)[0]
    
    truck_distance = sum(best_solution) * TRUCK_DISTANCE_COST
    technician_distance = sum(best_solution) * TECHNICIAN_DISTANCE_COST
    idle_machine_cost = 400
    truck_days = len(best_solution) // TRUCK_CAPACITY
    technicians_used = int(np.ceil(len(best_solution) / TECHNICIANS))
    total_cost = (truck_distance + technician_distance + idle_machine_cost + 
                  truck_days * TRUCK_DAY_COST + technicians_used * TECHNICIAN_DAY_COST)
    
    # Output the solution

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
        num_trucks = random.randint(0, 1)
        print(f"NUMBER_OF_TRUCKS = {num_trucks}")
        print(f"NUMBER_OF_TECHNICIANS = {random.randint(0, TECHNICIANS)}")
        
        if num_trucks > 0:
            for i in range(num_trucks):
                request_ids = [random.randint(1, 50) for _ in range(20)]
                routes = create_route(TRUCK_CAPACITY, TRUCK_MAX_DISTANCE, request_ids)
                for route in routes:
                    print(f"{i + 1} {' '.join(map(str, route))}")

if __name__ == "__main__":
    pso()